/**
 * QUEST AI LEARNING PLATFORM
 * AI Assistant / Tutor Interactive Engine
 */

document.addEventListener('DOMContentLoaded', function () {
  'use strict';

  const aiInput = document.getElementById('aiInput');
  const aiSendBtn = document.getElementById('aiSendBtn');
  const aiHistory = document.getElementById('aiChatHistory');
  const chipBtns = document.querySelectorAll('.chip-btn');

  if (!aiInput || !aiSendBtn || !aiHistory) return;

  function getCsrfToken() {
    const metaToken = document.querySelector('[name=csrfmiddlewaretoken]');
    if (metaToken) return metaToken.value;
    const cookie = document.cookie.split('; ').find(row => row.startsWith('csrftoken='));
    return cookie ? cookie.split('=')[1] : '';
  }

  function appendMessage(sender, text) {
    const msgDiv = document.createElement('div');
    msgDiv.className = `ai-msg ${sender === 'user' ? 'ai-msg-user' : 'ai-msg-tutor'}`;

    if (sender === 'user') {
      msgDiv.textContent = text;
    } else {
      // Basic markdown parser for headings, code blocks and bold
      let formatted = text
        .replace(/### (.*?)\n/g, '<strong style="color:#00f2fe;display:block;margin-bottom:4px;">$1</strong>')
        .replace(/```(c|java|cpp)?\n([\s\S]*?)```/g, '<pre class="code-snippet-box" style="margin:8px 0;padding:8px 12px;font-size:0.85rem;"><code>$2</code></pre>')
        .replace(/`([^`]+)`/g, '<code style="background:rgba(255,255,255,0.1);padding:2px 5px;border-radius:4px;color:#38bdf8;">$1</code>')
        .replace(/\*\*([^*]+)\*\*/g, '<strong style="color:#ffffff;">$1</strong>')
        .replace(/\n\n/g, '<br><br>')
        .replace(/\n/g, '<br>');

      msgDiv.innerHTML = formatted;
    }

    aiHistory.appendChild(msgDiv);
    aiHistory.scrollTop = aiHistory.scrollHeight;
  }

  async function sendAiQuery(promptText) {
    const query = promptText || aiInput.value.trim();
    if (!query) return;

    aiInput.value = '';
    appendMessage('user', query);

    // Typing indicator
    const typingId = 'typing-' + Date.now();
    const typingDiv = document.createElement('div');
    typingDiv.id = typingId;
    typingDiv.className = 'ai-msg ai-msg-tutor';
    typingDiv.innerHTML = '<em>Thinking & compiling answer...</em>';
    aiHistory.appendChild(typingDiv);
    aiHistory.scrollTop = aiHistory.scrollHeight;

    const courseSlug = document.body.dataset.courseSlug || 'c';
    const levelNumber = document.body.dataset.levelNumber || 1;
    const codeArea = document.getElementById('sandboxEditor');
    const userCode = codeArea ? codeArea.value : '';

    try {
      const response = await fetch('/api/ai-tutor/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCsrfToken()
        },
        body: JSON.stringify({
          prompt: query,
          course_slug: courseSlug,
          level_number: parseInt(levelNumber, 10),
          code: userCode
        })
      });

      const data = await response.json();
      const indicator = document.getElementById(typingId);
      if (indicator) indicator.remove();

      if (data.reply) {
        appendMessage('tutor', data.reply);
      } else {
        appendMessage('tutor', 'Could not retrieve AI response. Please try asking again.');
      }
    } catch (err) {
      const indicator = document.getElementById(typingId);
      if (indicator) indicator.remove();
      appendMessage('tutor', 'AI Tutor connection interrupted. Please try again.');
    }
  }

  aiSendBtn.addEventListener('click', () => sendAiQuery());
  aiInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      sendAiQuery();
    }
  });

  chipBtns.forEach(btn => {
    btn.addEventListener('click', function () {
      const prompt = this.getAttribute('data-prompt');
      if (prompt) {
        sendAiQuery(prompt);
      }
    });
  });
});
