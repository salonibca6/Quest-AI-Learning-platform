/**
 * QUEST - Voice Teacher
 * Reads a level aloud using the browser's built-in speech engine
 * (Web Speech API). No server, no API key, no cost.
 * The student can switch it ON or OFF at any time. The choice is remembered.
 */
(function () {
  'use strict';

  const panel = document.getElementById('voicePanel');
  if (!panel) return; // not on a level page

  const synth = window.speechSynthesis;
  if (!synth || !window.SpeechSynthesisUtterance) {
    const msg = document.getElementById('voiceUnsupported');
    if (msg) msg.hidden = false;
    return;
  }

  const toggle = document.getElementById('voiceToggle');
  const stateText = document.getElementById('voiceState');
  const hint = document.getElementById('voiceHint');
  const controls = document.getElementById('voiceControls');
  const playBtn = document.getElementById('voicePlay');
  const pauseBtn = document.getElementById('voicePause');
  const stopBtn = document.getElementById('voiceStop');
  const rateSel = document.getElementById('voiceRate');
  const listenBtns = document.querySelectorAll('.listen-btn');

  const KEY_ON = 'questVoiceOn';
  const KEY_RATE = 'questVoiceRate';

  let enabled = false;
  let runId = 0;          // changes every time we start/stop, so old callbacks are ignored
  let paused = false;
  let voice = null;

  function load(key, fallback) {
    try { const v = localStorage.getItem(key); return v === null ? fallback : v; }
    catch (e) { return fallback; }
  }
  function save(key, value) {
    try { localStorage.setItem(key, value); } catch (e) { /* private mode: ignore */ }
  }

  // ---- pick a friendly English voice ----
  function pickVoice() {
    const voices = synth.getVoices();
    if (!voices.length) return;
    voice =
      voices.find(v => /en-(IN|US|GB)/i.test(v.lang) && /(natural|google|samantha|zira|aria|female)/i.test(v.name)) ||
      voices.find(v => /^en/i.test(v.lang)) ||
      null;
  }
  pickVoice();
  if (synth.onvoiceschanged !== undefined) synth.onvoiceschanged = pickVoice;

  // ---- turn page content into clean, speakable text ----
  const SAY = [
    [/&&/g, ' and '], [/\|\|/g, ' or '], [/==/g, ' equals '], [/!=/g, ' is not equal to '],
    [/>=/g, ' is greater than or equal to '], [/<=/g, ' is less than or equal to '],
    [/\+\+/g, ' plus plus '], [/--/g, ' minus minus '], [/\\n/g, ' backslash n '], [/\\0/g, ' backslash zero '],
    [/%%/g, ' percent sign '], [/%d/g, ' percent d '], [/%f/g, ' percent f '], [/%c/g, ' percent c '], [/%s/g, ' percent s '],
    [/[{}<>;*`#]/g, ' '], [/->/g, ' arrow '], [/\s+/g, ' ']
  ];

  function sectionText(el) {
    const clone = el.cloneNode(true);
    clone.querySelectorAll('[data-no-speak], pre, button, script, style, .listen-btn').forEach(n => n.remove());
    // add a pause after headings, paragraphs and list items
    clone.querySelectorAll('h1,h2,h3,h4,p,li').forEach(n => n.appendChild(document.createTextNode('. ')));
    let text = clone.textContent || '';
    SAY.forEach(([re, rep]) => { text = text.replace(re, rep); });
    return text.replace(/\.\s*\./g, '.').trim();
  }

  // short chunks work reliably in all browsers (long ones get cut off in Chrome)
  function chunk(text) {
    const parts = text.match(/[^.!?]+[.!?]*/g) || [text];
    const out = [];
    parts.forEach(p => {
      p = p.trim();
      if (!p) return;
      while (p.length > 180) {
        let cut = p.lastIndexOf(',', 180);
        if (cut < 60) cut = p.lastIndexOf(' ', 180);
        if (cut < 1) cut = 180;
        out.push(p.slice(0, cut + 1).trim());
        p = p.slice(cut + 1).trim();
      }
      if (p) out.push(p);
    });
    return out;
  }

  // ---- speaking ----
  function clearHighlight() {
    document.querySelectorAll('.speak-section.speaking').forEach(n => n.classList.remove('speaking'));
  }

  function speakSections(sections) {
    stop(true);
    const myRun = ++runId;
    const queue = [];
    sections.forEach(sec => {
      chunk(sectionText(sec)).forEach(t => queue.push({ text: t, sec }));
    });
    if (!queue.length) return;
    let i = 0;
    paused = false;
    updatePauseLabel();

    function next() {
      if (myRun !== runId) return;      // cancelled or replaced
      if (i >= queue.length) { clearHighlight(); return; }
      const item = queue[i++];
      clearHighlight();
      item.sec.classList.add('speaking');
      const u = new SpeechSynthesisUtterance(item.text);
      u.rate = parseFloat(rateSel.value) || 0.95;
      u.pitch = 1;
      u.lang = (voice && voice.lang) || 'en-US';
      if (voice) u.voice = voice;
      u.onend = next;
      u.onerror = next;
      synth.speak(u);
    }
    next();
  }

  function stop(silent) {
    runId++;                // invalidates any running queue
    synth.cancel();
    paused = false;
    clearHighlight();
    if (!silent) updatePauseLabel();
  }

  function updatePauseLabel() {
    pauseBtn.innerHTML = paused
      ? '<i class="fa-solid fa-play"></i> Resume'
      : '<i class="fa-solid fa-pause"></i> Pause';
  }

  function allSections() {
    return Array.from(document.querySelectorAll('.speak-section'));
  }

  // ---- ON / OFF ----
  function applyState(on, startReading) {
    enabled = on;
    toggle.checked = on;
    stateText.textContent = on ? 'ON' : 'OFF';
    panel.classList.toggle('voice-on', on);
    controls.hidden = !on;
    listenBtns.forEach(b => { b.hidden = !on; });
    hint.textContent = on
      ? 'Press "Listen to this level" or tap a speaker icon next to a section.'
      : 'Turn it ON to listen to this level.';
    save(KEY_ON, on ? '1' : '0');
    if (on && startReading) speakSections(allSections());
    if (!on) stop();
  }

  toggle.addEventListener('change', () => applyState(toggle.checked, true));
  playBtn.addEventListener('click', () => speakSections(allSections()));
  stopBtn.addEventListener('click', () => stop());
  pauseBtn.addEventListener('click', () => {
    if (paused) { synth.resume(); paused = false; }
    else { synth.pause(); paused = true; }
    updatePauseLabel();
  });
  rateSel.value = load(KEY_RATE, '0.95');
  rateSel.addEventListener('change', () => save(KEY_RATE, rateSel.value));

  listenBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const sec = document.getElementById(btn.dataset.listen);
      if (sec && enabled) speakSections([sec]);
    });
  });

  // stop talking when the student leaves the page
  window.addEventListener('pagehide', () => synth.cancel());
  window.addEventListener('beforeunload', () => synth.cancel());

  // remember the choice, but never auto-play (browsers block that)
  applyState(load(KEY_ON, '0') === '1', false);

  // small helper other scripts can use, e.g. to read quiz feedback aloud
  window.QuestVoice = {
    isOn: () => enabled,
    say: function (text) {
      if (!enabled || !text) return;
      speakSections([Object.assign(document.createElement('div'), { textContent: text })]);
    }
  };
})();
