/**
 * QUEST AI LEARNING PLATFORM
 * Practice box (code checker) and level completion controller.
 *
 * NOTE: the practice box does NOT compile code. It checks that the student's
 * code contains the key ideas the challenge needs (ignoring comments), then
 * shows the output the real program would print. Students are encouraged to
 * run their code in a real compiler as well.
 */
document.addEventListener('DOMContentLoaded', function () {
  'use strict';

  const runCodeBtn = document.getElementById('runCodeBtn');
  const resetCodeBtn = document.getElementById('resetCodeBtn');
  const solutionBtn = document.getElementById('solutionBtn');
  const submitModuleBtn = document.getElementById('submitModuleBtn');
  const editor = document.getElementById('sandboxEditor');
  const terminal = document.getElementById('terminalOutput');
  const quizOptions = document.querySelectorAll('.quiz-option-radio');
  const quizFeedback = document.getElementById('quizFeedback');
  const FINISH_LABEL = 'Finish Level & Unlock Next ➔';

  let levelData = { expected: '', must_contain: [], solution: '', language: 'c' };
  try {
    levelData = JSON.parse(document.getElementById('levelData').textContent);
  } catch (e) { /* page without data: keep defaults */ }

  let checkPassed = false;

  function esc(t) {
    return String(t).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }

  function getCsrfToken() {
    const metaToken = document.querySelector('[name=csrfmiddlewaretoken]');
    if (metaToken) return metaToken.value;
    const cookie = document.cookie.split('; ').find(row => row.startsWith('csrftoken='));
    return cookie ? cookie.split('=')[1] : '';
  }

  function say(text) {
    if (window.QuestVoice) window.QuestVoice.say(text);
  }

  // Remove comments so words inside // notes or /* notes */ do not count
  function stripComments(code) {
    return code.replace(/\/\*[\s\S]*?\*\//g, '').replace(/\/\/.*$/gm, '');
  }

  function bracketsBalanced(code) {
    const pairs = { ')': '(', ']': '[', '}': '{' };
    const stack = [];
    let inStr = false, quote = '';
    for (let i = 0; i < code.length; i++) {
      const ch = code[i];
      if (inStr) {
        if (ch === '\\') { i++; continue; }
        if (ch === quote) inStr = false;
        continue;
      }
      if (ch === '"' || ch === "'") { inStr = true; quote = ch; continue; }
      if ('([{'.includes(ch)) stack.push(ch);
      else if (pairs[ch]) { if (stack.pop() !== pairs[ch]) return false; }
    }
    return stack.length === 0;
  }

  // Quiz option styling
  quizOptions.forEach(radio => {
    radio.addEventListener('change', function () {
      document.querySelectorAll('.quiz-option-label').forEach(lbl => lbl.classList.remove('selected'));
      if (this.checked) this.closest('.quiz-option-label').classList.add('selected');
    });
  });

  // ---------- Check My Code ----------
  if (runCodeBtn && editor && terminal) {
    const defaultStarter = editor.value;

    runCodeBtn.addEventListener('click', function () {
      const raw = editor.value;
      const code = stripComments(raw);
      const flat = code.replace(/\s+/g, '');
      const cmd = levelData.language === 'c'
        ? 'gcc main.c -o solution && ./solution'
        : 'javac Main.java && java Main';

      terminal.innerHTML = '<span style="color:#38bdf8;">Checking your code...</span>';

      setTimeout(function () {
        const lines = ['<span style="color:#94a3b8;">$ ' + cmd + '</span>'];

        if (!flat) {
          lines.push('<span style="color:#f59e0b;">Your code box is empty. Type some code first!</span>');
          checkPassed = false;
        } else if (!bracketsBalanced(code)) {
          lines.push('<span style="color:#ef4444;">Something looks wrong: the brackets ( ) { } [ ] do not match. Check that every opening bracket has a closing one.</span>');
          checkPassed = false;
        } else {
          const missing = (levelData.must_contain || []).filter(function (tok) {
            return !flat.includes(String(tok).replace(/\s+/g, ''));
          });
          if (missing.length === 0) {
            checkPassed = true;
            lines.push('<span style="color:#10b981;">' + esc(levelData.expected).replace(/\n/g, '<br>') + '</span>');
            lines.push('<span style="color:#64748b;">✔ Great job! Your code has everything this challenge needs.</span>');
            say('Great job! Your code has everything this challenge needs.');
          } else {
            checkPassed = false;
            lines.push('<span style="color:#f59e0b;">Not quite yet. Your code is missing something the challenge needs. Read the challenge and the hint again, then try once more. You can do it!</span>');
            say('Not quite yet. Read the challenge and the hint again, then try once more.');
          }
          lines.push('<span style="color:#64748b;font-size:0.8rem;">Tip: this box checks your idea. For the real result, also run your code in a compiler on your computer.</span>');
        }

        terminal.innerHTML = lines.join('<br>');
        terminal.scrollTop = terminal.scrollHeight;
      }, 350);
    });

    if (resetCodeBtn) {
      resetCodeBtn.addEventListener('click', function () {
        editor.value = defaultStarter;
        checkPassed = false;
        terminal.innerHTML = '<span style="color:#64748b;">Code reset to the starter code.</span>';
      });
    }

    if (solutionBtn) {
      solutionBtn.addEventListener('click', function () {
        if (!levelData.solution) return;
        if (!confirm('Try once more on your own first? Looking at the solution is fine if you are really stuck. Show it now?')) return;
        terminal.innerHTML =
          '<span style="color:#f59e0b;">Solution (read it, understand it, then type it yourself):</span>' +
          '<pre class="code-snippet-box" style="margin-top:8px;white-space:pre-wrap;"><code>' +
          esc(levelData.solution) + '</code></pre>';
      });
    }
  }

  // ---------- Finish level ----------
  if (submitModuleBtn) {
    submitModuleBtn.addEventListener('click', async function () {
      const courseSlug = document.body.dataset.courseSlug;
      const levelNumber = document.body.dataset.levelNumber;

      const selectedOption = document.querySelector('input[name="quiz_option"]:checked');
      if (!selectedOption) {
        if (quizFeedback) {
          quizFeedback.className = 'quiz-feedback-box incorrect';
          quizFeedback.textContent = 'Please choose an answer in the Knowledge Check first!';
          quizFeedback.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
        return;
      }

      if (!checkPassed && !confirm('You have not passed the "Check My Code" step yet. Finish this level anyway?')) {
        return;
      }

      const answerIndex = parseInt(selectedOption.value, 10);
      const code = editor ? editor.value : '';

      submitModuleBtn.disabled = true;
      submitModuleBtn.textContent = 'Checking...';

      try {
        const response = await fetch('/api/complete-level/' + courseSlug + '/' + levelNumber + '/', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', 'X-CSRFToken': getCsrfToken() },
          body: JSON.stringify({ quiz_answer: answerIndex, code: code })
        });
        const data = await response.json();

        if (data.success) {
          if (quizFeedback) {
            quizFeedback.className = 'quiz-feedback-box correct';
            quizFeedback.textContent = 'Correct! ' + (data.explanation || '') + ' ' + (data.message || '');
          }
          say('Correct! ' + (data.explanation || ''));
          data.course_slug = courseSlug;
          if (window.showCelebrationModal) window.showCelebrationModal(data);
          submitModuleBtn.textContent = 'Level Completed! ✓';
          submitModuleBtn.style.background = '#10b981';
        } else {
          if (quizFeedback) {
            quizFeedback.className = 'quiz-feedback-box incorrect';
            quizFeedback.textContent = data.message || 'Not correct yet. Read the lesson again and try once more!';
            quizFeedback.scrollIntoView({ behavior: 'smooth', block: 'center' });
          }
          say('Not correct yet. Read the lesson again and try once more.');
          submitModuleBtn.disabled = false;
          submitModuleBtn.textContent = FINISH_LABEL;
        }
      } catch (err) {
        alert('Could not save your progress. Please check your internet connection.');
        submitModuleBtn.disabled = false;
        submitModuleBtn.textContent = FINISH_LABEL;
      }
    });
  }
});
