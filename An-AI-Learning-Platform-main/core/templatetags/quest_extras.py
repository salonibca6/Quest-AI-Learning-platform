import re
from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe

register = template.Library()


def _inline(text):
    """Turn **bold** and `code` into HTML (text must already be escaped)."""
    text = re.sub(r'`([^`]+)`', r'<code class="inline-code">\1</code>', text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    return text


@register.filter(name='simple_md')
def simple_md(value):
    """
    Very small, safe Markdown: ### headings, **bold**, `code`, - bullets,
    ``` code blocks and normal paragraphs. Everything is escaped first.
    """
    lines = str(value or '').splitlines()
    out, para, bullets, code = [], [], [], None

    def flush_para():
        if para:
            out.append('<p>' + _inline(escape(' '.join(para))) + '</p>')
            para.clear()

    def flush_bullets():
        if bullets:
            out.append('<ul>' + ''.join('<li>%s</li>' % _inline(escape(b)) for b in bullets) + '</ul>')
            bullets.clear()

    for line in lines:
        if line.strip().startswith('```'):
            if code is None:
                flush_para(); flush_bullets(); code = []
            else:
                out.append('<pre class="code-snippet-box" data-no-speak="1"><code>%s</code></pre>' % escape('\n'.join(code)))
                code = None
            continue
        if code is not None:
            code.append(line)
            continue
        stripped = line.strip()
        if not stripped:
            flush_para(); flush_bullets()
        elif stripped.startswith('### '):
            flush_para(); flush_bullets()
            out.append('<h4 class="concept-heading">%s</h4>' % _inline(escape(stripped[4:])))
        elif stripped.startswith('- '):
            flush_para()
            bullets.append(stripped[2:])
        else:
            flush_bullets()
            para.append(stripped)
    flush_para(); flush_bullets()
    if code is not None:
        out.append('<pre class="code-snippet-box" data-no-speak="1"><code>%s</code></pre>' % escape('\n'.join(code)))
    return mark_safe('\n'.join(out))
