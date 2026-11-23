/**
 * QUEST AI LEARNING PLATFORM
 * Core UI interactions, modal controllers, toasts, and animations
 */

document.addEventListener('DOMContentLoaded', function () {
  'use strict';

  // Smooth scroll for nav anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (targetId.length > 1) {
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
          e.preventDefault();
          targetElement.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
          });
          // Update URL without jump
          history.pushState(null, null, targetId);
        }
      }
    });
  });

  // Auto dismiss flash messages after 6 seconds
  const alerts = document.querySelectorAll('.alert');
  alerts.forEach(alert => {
    setTimeout(() => {
      alert.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
      alert.style.opacity = '0';
      alert.style.transform = 'translateY(-10px)';
      setTimeout(() => alert.remove(), 600);
    }, 6000);
  });
});

// Global Celebration Modal Trigger
window.showCelebrationModal = function (data) {
  const modal = document.getElementById('celebrationModal');
  if (!modal) return;

  const titleEl = document.getElementById('modalLevelTitle');
  const xpEl = document.getElementById('modalXpEarned');
  const rankEl = document.getElementById('modalNewRank');
  const nextBtn = document.getElementById('modalNextLevelBtn');

  if (titleEl) titleEl.textContent = data.message || "Quest Module Complete!";
  if (xpEl) xpEl.textContent = `+${data.xp_earned} XP Added to your profile`;
  if (rankEl) rankEl.textContent = `Current Rank: ${data.rank_title} (Tier ${data.rank_tier})`;

  if (nextBtn) {
    if (data.has_next_level && data.next_level_number) {
      nextBtn.style.display = 'inline-flex';
      nextBtn.href = `/course/${data.course_slug || 'c'}/level/${data.next_level_number}/`;
      nextBtn.textContent = `Proceed to Level ${data.next_level_number} ➔`;
    } else {
      nextBtn.style.display = 'inline-flex';
      nextBtn.href = `/course/${data.course_slug || 'c'}/`;
      nextBtn.textContent = "Return to Quest Map 🗺️";
    }
  }

  modal.classList.add('active');

  // Trigger mini canvas confetti if available
  triggerConfetti();
};

window.closeCelebrationModal = function () {
  const modal = document.getElementById('celebrationModal');
  if (modal) modal.classList.remove('active');
};

function triggerConfetti() {
  // Simple CSS / canvas confetti effect
  const container = document.body;
  const colors = ['#00f2fe', '#38bdf8', '#a855f7', '#f59e0b', '#10b981'];

  for (let i = 0; i < 40; i++) {
    const flake = document.createElement('div');
    flake.style.position = 'fixed';
    flake.style.width = `${Math.random() * 8 + 5}px`;
    flake.style.height = `${Math.random() * 8 + 5}px`;
    flake.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
    flake.style.top = '40%';
    flake.style.left = '50%';
    flake.style.borderRadius = Math.random() > 0.5 ? '50%' : '2px';
    flake.style.zIndex = '1001';
    flake.style.pointerEvents = 'none';
    flake.style.transition = 'all 1.2s cubic-bezier(0.25, 1, 0.5, 1)';

    container.appendChild(flake);

    const destX = (Math.random() - 0.5) * window.innerWidth * 0.75;
    const destY = (Math.random() - 0.5) * window.innerHeight * 0.75;
    const rotate = Math.random() * 720;

    requestAnimationFrame(() => {
      flake.style.transform = `translate(${destX}px, ${destY}px) rotate(${rotate}deg)`;
      flake.style.opacity = '0';
    });

    setTimeout(() => flake.remove(), 1200);
  }
}
