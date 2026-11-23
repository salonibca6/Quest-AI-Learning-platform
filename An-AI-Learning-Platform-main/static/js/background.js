/**
 * QUEST AI LEARNING PLATFORM
 * Animated Developer Background Canvas
 * Renders glowing floating syntax tokens, interactive constellation network nodes,
 * and developer code ambient particles.
 */

(function () {
  'use strict';

  const canvas = document.getElementById('developer-canvas');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');
  let width, height;
  let animationFrameId;

  // Developer Syntax Tokens
  const CODE_TOKENS = [
    'int main()',
    '#include <stdio.h>',
    'printf("Quest AI");',
    'malloc(sizeof(Node))',
    '*ptr = &memory',
    'public static void main',
    'System.out.println()',
    'new ArrayList<>()',
    'struct Hero',
    'free(memory)',
    'class QuestEngine',
    'return 0;',
    '0x7FFF8A',
    'try { } catch()',
    '->next = NULL',
    'implements Serializable',
    'while (1)',
    'boolean isSolved = true;'
  ];

  let particles = [];
  let codeLabels = [];
  const particleCount = 45;
  const maxDistance = 140;

  // Mouse interaction
  const mouse = {
    x: null,
    y: null,
    radius: 130
  };

  window.addEventListener('mousemove', function (e) {
    mouse.x = e.clientX;
    mouse.y = e.clientY;
  });

  window.addEventListener('mouseout', function () {
    mouse.x = null;
    mouse.y = null;
  });

  function resizeCanvas() {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
    initElements();
  }

  // Network Node Particle Class
  class Particle {
    constructor() {
      this.reset();
    }

    reset() {
      this.x = Math.random() * width;
      this.y = Math.random() * height;
      this.vx = (Math.random() - 0.5) * 0.75;
      this.vy = (Math.random() - 0.5) * 0.75;
      this.radius = Math.random() * 2 + 1.2;
      this.alpha = Math.random() * 0.5 + 0.2;
      this.color = Math.random() > 0.4 ? 'rgba(0, 242, 254, ' : 'rgba(168, 85, 247, ';
    }

    update() {
      this.x += this.vx;
      this.y += this.vy;

      // Bounce at screen edges
      if (this.x < 0 || this.x > width) this.vx *= -1;
      if (this.y < 0 || this.y > height) this.vy *= -1;

      // Mouse repulsion/interaction
      if (mouse.x !== null && mouse.y !== null) {
        const dx = mouse.x - this.x;
        const dy = mouse.y - this.y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < mouse.radius) {
          const force = (mouse.radius - dist) / mouse.radius;
          const angle = Math.atan2(dy, dx);
          this.x -= Math.cos(angle) * force * 3;
          this.y -= Math.sin(angle) * force * 3;
        }
      }
    }

    draw() {
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
      ctx.fillStyle = this.color + this.alpha + ')';
      ctx.shadowBlur = 8;
      ctx.shadowColor = 'rgba(0, 242, 254, 0.4)';
      ctx.fill();
      ctx.shadowBlur = 0;
    }
  }

  // Floating Syntax Code Label Class
  class CodeLabel {
    constructor() {
      this.reset(true);
    }

    reset(initial = false) {
      this.text = CODE_TOKENS[Math.floor(Math.random() * CODE_TOKENS.length)];
      this.x = Math.random() * (width - 150);
      this.y = initial ? Math.random() * height : height + 30;
      this.vy = -(Math.random() * 0.35 + 0.2); // Slowly floats upward
      this.alpha = Math.random() * 0.18 + 0.08;
      this.fontSize = Math.floor(Math.random() * 3 + 11);
      this.color = Math.random() > 0.5 ? '#38bdf8' : '#a855f7';
    }

    update() {
      this.y += this.vy;
      if (this.y < -30) {
        this.reset(false);
      }
    }

    draw() {
      ctx.font = `${this.fontSize}px "Fira Code", monospace`;
      ctx.fillStyle = this.color;
      ctx.globalAlpha = this.alpha;
      ctx.fillText(this.text, this.x, this.y);
      ctx.globalAlpha = 1.0;
    }
  }

  function initElements() {
    particles = [];
    for (let i = 0; i < particleCount; i++) {
      particles.push(new Particle());
    }

    codeLabels = [];
    const labelCount = Math.min(18, Math.floor(width / 90));
    for (let i = 0; i < labelCount; i++) {
      codeLabels.push(new CodeLabel());
    }
  }

  function connectParticles() {
    for (let a = 0; a < particles.length; a++) {
      for (let b = a + 1; b < particles.length; b++) {
        const dx = particles[a].x - particles[b].x;
        const dy = particles[a].y - particles[b].y;
        const dist = Math.sqrt(dx * dx + dy * dy);

        if (dist < maxDistance) {
          const lineAlpha = (1 - dist / maxDistance) * 0.15;
          ctx.beginPath();
          ctx.moveTo(particles[a].x, particles[a].y);
          ctx.lineTo(particles[b].x, particles[b].y);
          ctx.strokeStyle = `rgba(56, 189, 248, ${lineAlpha})`;
          ctx.lineWidth = 0.9;
          ctx.stroke();
        }
      }

      // Connect to mouse if close
      if (mouse.x !== null && mouse.y !== null) {
        const dx = particles[a].x - mouse.x;
        const dy = particles[a].y - mouse.y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < mouse.radius) {
          const mouseAlpha = (1 - dist / mouse.radius) * 0.25;
          ctx.beginPath();
          ctx.moveTo(particles[a].x, particles[a].y);
          ctx.lineTo(mouse.x, mouse.y);
          ctx.strokeStyle = `rgba(0, 242, 254, ${mouseAlpha})`;
          ctx.lineWidth = 1;
          ctx.stroke();
        }
      }
    }
  }

  function render() {
    ctx.clearRect(0, 0, width, height);

    // Draw floating code tokens
    for (let i = 0; i < codeLabels.length; i++) {
      codeLabels[i].update();
      codeLabels[i].draw();
    }

    // Draw connection lines
    connectParticles();

    // Draw nodes
    for (let i = 0; i < particles.length; i++) {
      particles[i].update();
      particles[i].draw();
    }

    animationFrameId = requestAnimationFrame(render);
  }

  window.addEventListener('resize', resizeCanvas);
  resizeCanvas();
  render();
})();
