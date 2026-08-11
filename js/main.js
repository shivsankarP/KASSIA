document.addEventListener('DOMContentLoaded', () => {
  // Register GSAP ScrollTrigger if GSAP is available
  if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
    gsap.registerPlugin(ScrollTrigger);
    initGSAPAnimations();
  } else {
    // Fallback simple scroll reveals if GSAP is blocked or fails to load
    initFallbackAnimations();
  }

  initHeader();
  initMobileMenu();
  initCardTilt();
});

/* --- Header Sticky & Scroll Interactions --- */
function initHeader() {
  const header = document.querySelector('header');
  if (!header) return;

  const checkScroll = () => {
    if (window.scrollY > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  };

  window.addEventListener('scroll', checkScroll);
  checkScroll(); // Run once in case page loads scrolled down
}

/* --- Mobile Navigation Menu --- */
function initMobileMenu() {
  const hamburger = document.querySelector('.hamburger');
  const navMenu = document.querySelector('.nav-menu');

  if (!hamburger || !navMenu) return;

  hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    navMenu.classList.toggle('active');
  });

  // Close menu when clicking nav link
  document.querySelectorAll('.nav-menu a').forEach(link => {
    link.addEventListener('click', () => {
      hamburger.classList.remove('active');
      navMenu.classList.remove('active');
    });
  });
}

/* --- GSAP Animations (Premium Effects) --- */
function initGSAPAnimations() {
  // Page entry reveal for header & hero content
  const heroTl = gsap.timeline({ defaults: { ease: 'power3.out', duration: 1 } });
  
  if (document.querySelector('.hero-title')) {
    heroTl.fromTo('.hero-title', 
      { opacity: 0, y: 40 },
      { opacity: 1, y: 0, delay: 0.2 }
    );
    heroTl.fromTo('.hero-subtitle', 
      { opacity: 0, y: 20 },
      { opacity: 1, y: 0 },
      '-=0.7'
    );
    heroTl.fromTo('.hero .btn', 
      { opacity: 0, y: 15 },
      { opacity: 1, y: 0 },
      '-=0.7'
    );
  }

  // Floating Spice Particles in Hero
  const particleContainer = document.querySelector('.hero-particles-container');
  if (particleContainer) {
    const particleTypes = [
      // Cardamom pod path SVG outline
      `<svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M12 2C8 6 6 10 6 14C6 18 9 21 12 21C15 21 18 18 18 14C18 10 16 6 12 2Z" stroke="#6D8262" stroke-width="1.5" fill="none" opacity="0.6"/></svg>`,
      // Pepper grain filled dot
      `<svg width="10" height="10" viewBox="0 0 12 12" fill="none"><circle cx="6" cy="6" r="4" fill="#1C2B21" opacity="0.4"/></svg>`,
      // Cinnamon bark rect line
      `<svg width="12" height="28" viewBox="0 0 12 28" fill="none"><rect x="2" y="2" width="8" height="24" rx="3" stroke="#B26A43" stroke-width="1.5" fill="none" opacity="0.5"/></svg>`,
      // Small gold leaf outline
      `<svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M2 22C6 18 10 16 14 16C18 16 22 20 22 22M22 2C18 6 16 10 16 14C16 18 20 22 22 22" stroke="#D39B31" stroke-width="1.2" fill="none" opacity="0.4"/></svg>`
    ];

    const particleCount = window.innerWidth < 768 ? 10 : 20;

    for (let i = 0; i < particleCount; i++) {
      const particle = document.createElement('div');
      particle.className = 'floating-particle';
      particle.innerHTML = particleTypes[Math.floor(Math.random() * particleTypes.length)];
      
      // Random coordinates
      particle.style.left = Math.random() * 100 + '%';
      particle.style.top = Math.random() * 90 + 5 + '%';
      
      particleContainer.appendChild(particle);

      // Random slow drifting movement
      gsap.to(particle, {
        y: '-=' + (Math.random() * 200 + 100),
        x: '+=' + (Math.random() * 80 - 40),
        rotation: Math.random() * 360,
        duration: Math.random() * 10 + 10,
        opacity: 0,
        repeat: -1,
        ease: 'power1.out',
        delay: Math.random() * 5
      });
    }
  }

  // Scroll Reveal Elements
  const revealElements = document.querySelectorAll('.reveal-up');
  revealElements.forEach(element => {
    gsap.fromTo(element, 
      { opacity: 0, y: 40 },
      {
        opacity: 1,
        y: 0,
        duration: 1.2,
        ease: 'power2.out',
        scrollTrigger: {
          trigger: element,
          start: 'top 85%',
          toggleActions: 'play none none none'
        }
      }
    );
  });

  // --- Radial Scroll Gallery ---
  const radialPin = document.getElementById('radial-pin');
  const radialWheel = document.getElementById('radial-wheel');
  const radialItems = document.querySelectorAll('.radial-item');

  if (radialPin && radialWheel && radialItems.length > 0) {
    const isMobile = window.innerWidth < 768;
    const radius = isMobile ? 220 : 600;
    const circleDiameter = radius * 2;
    const scrollDuration = 3000;
    const visiblePercentage = 45; 
    const visibleDecimal = visiblePercentage / 100;
    const hiddenDecimal = 1 - visibleDecimal;

    radialWheel.style.width = circleDiameter + 'px';
    radialWheel.style.height = circleDiameter + 'px';
    radialWheel.style.bottom = -(circleDiameter * hiddenDecimal) + 'px';

    const childrenCount = radialItems.length;
    
    radialItems.forEach((item, index) => {
      // Place items counter-clockwise so that clockwise rotation (360) brings them in order (1 -> 2 -> 3)
      const angle = (-index / childrenCount) * 2 * Math.PI - Math.PI / 2;
      const x = radius * Math.cos(angle);
      const y = radius * Math.sin(angle);
      const rotationAngle = (angle * 180) / Math.PI;
      
      item.style.transform = `translate(-50%, -50%) translate3d(${x}px, ${y}px, 0) rotate(${rotationAngle + 90}deg)`;
    });

    const cardHeight = isMobile ? 380 : 480;
    const visibleAreaHeight = (circleDiameter * visibleDecimal) + (cardHeight / 2) + 150;
    document.getElementById('radial-mask').style.height = visibleAreaHeight + 'px';
    radialPin.style.minHeight = (visibleAreaHeight + 50) + 'px';

    // Set GSAP internal transforms so it doesn't wipe out CSS translations during rotation
    gsap.set(radialWheel, { xPercent: -50 });

    // Animate the inner cards, so we don't overwrite the positioning transforms on the list items
    const cards = Array.from(radialWheel.children).map(li => li.querySelector('.radial-card'));
    
    gsap.fromTo(cards, 
      { scale: 0, autoAlpha: 0 },
      {
        scale: 1,
        autoAlpha: 1,
        duration: 1.2,
        ease: 'back.out(1.2)',
        stagger: 0.1,
        scrollTrigger: {
          trigger: radialPin,
          start: 'top 80%',
        }
      }
    );

    gsap.to(radialWheel, {
      rotation: 360,
      ease: 'none',
      scrollTrigger: {
        trigger: radialPin,
        pin: true,
        start: 'center center',
        end: `+=${scrollDuration}`,
        scrub: 1,
        invalidateOnRefresh: true,
      }
    });

    radialItems.forEach(item => {
      const card = item.querySelector('.radial-card');
      if (card) {
        card.addEventListener('mouseenter', () => radialWheel.classList.add('has-hover'));
        card.addEventListener('mouseleave', () => radialWheel.classList.remove('has-hover'));
      }
    });
  }

  // Stats Counters
  document.querySelectorAll('.stat-counter').forEach(counter => {
    const target = parseInt(counter.getAttribute('data-target'), 10);
    ScrollTrigger.create({
      trigger: counter,
      start: 'top 85%',
      onEnter: () => {
        let count = 0;
        const duration = 1500; // ms
        const steps = 60;
        const increment = target / steps;
        const stepTime = duration / steps;

        const updateCount = () => {
          count += increment;
          if (count < target) {
            counter.innerText = Math.ceil(count);
            setTimeout(updateCount, stepTime);
          } else {
            counter.innerText = target;
          }
        };
        updateCount();
      },
      once: true
    });
  });
}

/* --- Fallback Scroll Animation if GSAP is absent --- */
function initFallbackAnimations() {
  const revealOnScroll = () => {
    const elements = document.querySelectorAll('.reveal-up');
    const windowHeight = window.innerHeight;

    elements.forEach(element => {
      const position = element.getBoundingClientRect().top;
      if (position < windowHeight - 100) {
        element.style.opacity = '1';
        element.style.transform = 'translateY(0)';
        element.style.transition = 'opacity 1s ease, transform 1s ease';
      }
    });
  };

  window.addEventListener('scroll', revealOnScroll);
  revealOnScroll(); // Trigger once on load
}

/* --- Card Hover Tilt Effect --- */
function initCardTilt() {
  // Only apply tilt on wider viewports with hover support
  if (window.innerWidth < 992) return;

  document.querySelectorAll('.product-card').forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;

      const centerX = rect.width / 2;
      const centerY = rect.height / 2;

      // Restrict rotation to max 8 degrees
      const rotateX = ((centerY - y) / centerY) * 8;
      const rotateY = ((x - centerX) / centerX) * 8;

      card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-8px)`;
      card.style.transition = 'transform 0.1s ease';
    });

    card.addEventListener('mouseleave', () => {
      card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translateY(0px)';
      card.style.transition = 'transform 0.5s ease';
    });
  });
}

// ── Depth Carousel (Vanilla JS) ──
class DepthCarousel {
  constructor(element, options = {}) {
    this.root = element;
    this.stage = this.root.querySelector('.depth-carousel__stage');
    this.cards = Array.from(this.stage.querySelectorAll('.depth-carousel__card'));
    this.overlays = Array.from(this.stage.querySelectorAll('.depth-carousel__tint'));
    this.dots = Array.from(this.root.querySelectorAll('.depth-carousel__dot'));
    this.prevBtn = this.root.querySelector('.depth-carousel__arrow--prev');
    this.nextBtn = this.root.querySelector('.depth-carousel__arrow--next');

    const clamp = (v, min, max) => Math.min(Math.max(v, min), max);

    this.cfg = {
      count: this.cards.length,
      depth: 220,
      spread: 90,
      tilt: 22,
      tiltDirection: 'right',
      visibleCards: 4,
      falloff: 0.2,
      blur: 6,
      duration: 700,
      ease: 'power3.out',
      loop: true,
      cardWidth: 440,
      autoplayDelay: 3200,
      autoplay: false,
      ...options
    };

    this.pos = 0;
    this.focus = 0;
    this.scale = 1;
    this.active = 0;
    this.clamp = clamp;

    this.tween = null;
    this.wheelTimer = null;
    this.autoTimer = null;
    this.drag = null;
    this.reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    this.init();
  }

  init() {
    this.setupEvents();
    this.handleResize();
    this.layout(this.pos);
  }

  layout(pos) {
    const cfg = this.cfg;
    const n = cfg.count;
    if (!n) return;
    const dir = cfg.tiltDirection === 'left' ? -1 : 1;
    const sc = this.scale;

    for (let i = 0; i < n; i++) {
      const el = this.cards[i];
      let d = i - pos;
      if (cfg.loop && n > 1) {
        d = ((d % n) + n) % n;
        if (d > n / 2) d -= n;
      }

      const back = Math.max(0, d);
      const az = Math.abs(d);
      const shown = az <= cfg.visibleCards + 0.5;

      const tz = -cfg.depth * d;
      const tx = dir * cfg.spread * d;
      const ry = dir * cfg.tilt * this.clamp(d, 0, 1);

      let opacity = d < 0 ? Math.max(0, 1 + d) : 1;
      if (!shown) opacity = 0;

      const brightness = Math.max(0.15, 1 - back * cfg.falloff);
      const blurPx = cfg.blur > 0 ? Math.min(cfg.blur, (back / Math.max(1, cfg.visibleCards)) * cfg.blur) : 0;
      const zi = Math.round(2000 - d * 20);

      el.style.transform = `translate(-50%, -50%) scale(${sc}) translateX(${tx.toFixed(2)}px) translateZ(${tz.toFixed(2)}px) rotateY(${ry.toFixed(3)}deg)`;
      el.style.opacity = opacity.toFixed(3);
      el.style.filter = `brightness(${brightness.toFixed(3)}) blur(${blurPx.toFixed(2)}px)`;
      el.style.zIndex = String(zi);
      el.style.pointerEvents = shown && opacity > 0.05 ? 'auto' : 'none';

      const ov = this.overlays[i];
      if (ov) ov.style.opacity = this.clamp(back * cfg.falloff * 1.25, 0, 0.86).toFixed(3);
    }
  }

  notify(idx) {
    this.active = idx;
    this.dots.forEach((d, i) => {
      if (d) d.classList.toggle('is-active', i === idx);
    });
    this.cards.forEach((c, i) => {
      c.setAttribute('aria-hidden', i !== idx);
    });
  }

  tweenTo(target, animate) {
    if (this.tween) this.tween.kill();
    const cfg = this.cfg;
    const dur = animate && !this.reducedMotion ? cfg.duration / 1000 : 0;
    const proxy = { p: this.pos };

    this.tween = gsap.to(proxy, {
      p: target,
      duration: dur,
      ease: cfg.ease,
      onUpdate: () => {
        this.pos = proxy.p;
        this.layout(proxy.p);
      },
      onComplete: () => {
        const n = cfg.count;
        if (n > 0) this.pos = ((this.pos % n) + n) % n;
        this.layout(this.pos);
      }
    });
  }

  setFocus(rawIndex, animate = true) {
    const cfg = this.cfg;
    const n = cfg.count;
    if (!n) return;
    const idx = cfg.loop ? ((rawIndex % n) + n) % n : this.clamp(rawIndex, 0, n - 1);
    let delta = idx - this.pos;
    if (cfg.loop && n > 1) {
      delta = ((delta % n) + n) % n;
      if (delta > n / 2) delta -= n;
    }
    this.tweenTo(this.pos + delta, animate);
    if (idx !== this.focus) {
      this.focus = idx;
      this.notify(idx);
    }
  }

  navigateBy(step) {
    this.setFocus(this.focus + step, true);
  }

  setupEvents() {
    // Resize
    const ro = new ResizeObserver(entries => {
      this.handleResize(entries[0].contentRect.width);
    });
    ro.observe(this.root);

    // Wheel disabled - using GSAP ScrollTrigger for smooth scroll integration instead
    /*
    this.root.addEventListener('wheel', e => {
      //...
    }, { passive: false });
    */

    // Pointer
    this.root.addEventListener('pointerdown', e => {
      if (this.cfg.count < 2) return;
      if (this.tween) this.tween.kill();
      this.drag = {
        x: e.clientX,
        startPos: this.pos,
        lastX: e.clientX,
        lastT: performance.now(),
        v: 0,
        moved: false,
        id: e.pointerId
      };
    });

    this.root.addEventListener('pointermove', e => {
      if (!this.drag) return;
      const stepPx = Math.max(this.cfg.cardWidth * 0.55 * this.scale, 40);
      const dx = e.clientX - this.drag.x;
      if (!this.drag.moved && Math.abs(dx) > 4) {
        this.drag.moved = true;
        this.root.setPointerCapture(this.drag.id);
      }
      if (!this.drag.moved) return;
      const now = performance.now();
      const dt = Math.max(now - this.drag.lastT, 1);
      this.drag.v = (e.clientX - this.drag.lastX) / dt;
      this.drag.lastX = e.clientX;
      this.drag.lastT = now;
      this.pos = this.drag.startPos - dx / stepPx;
      this.layout(this.pos);
    });

    const onPointerEnd = () => {
      if (!this.drag) return;
      const drag = this.drag;
      this.drag = null;
      if (!drag.moved) return;
      const stepPx = Math.max(this.cfg.cardWidth * 0.55 * this.scale, 40);
      const projected = this.pos - (drag.v * 180) / stepPx;
      this.setFocus(Math.round(projected), true);
    };
    this.root.addEventListener('pointerup', onPointerEnd);
    this.root.addEventListener('pointercancel', onPointerEnd);

    // Keyboard
    this.root.addEventListener('keydown', e => {
      if (e.key === 'ArrowLeft') {
        e.preventDefault();
        this.navigateBy(-1);
      } else if (e.key === 'ArrowRight') {
        e.preventDefault();
        this.navigateBy(1);
      }
    });

    // Clicks
    this.cards.forEach((card, i) => {
      card.addEventListener('click', () => {
        if (this.drag && this.drag.moved) return;
        this.setFocus(i, true);
      });
    });

    this.dots.forEach((dot, i) => {
      dot.addEventListener('click', () => this.setFocus(i, true));
    });

    if (this.prevBtn) this.prevBtn.addEventListener('click', () => this.navigateBy(-1));
    if (this.nextBtn) this.nextBtn.addEventListener('click', () => this.navigateBy(1));
  }

  handleResize(w) {
    if (!w) w = this.root.clientWidth;
    const needed = this.cfg.cardWidth + Math.abs(this.cfg.spread) * 2 + 120;
    this.scale = this.clamp(w / needed, 0.4, 1);
    this.layout(this.pos);
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const el = document.getElementById('process-carousel');
  if (el) {
    const carousel = new DepthCarousel(el);
    
    // Smooth GSAP ScrollTrigger integration
    if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
      const section = document.getElementById('process-section');
      if (section) {
        gsap.to(carousel, {
          pos: carousel.cfg.count - 1, // animate to last card
          ease: 'none',
          scrollTrigger: {
            trigger: section,
            pin: true,
            start: 'center center',
            end: '+=2000', // Scroll distance to scrub through
            scrub: 1,      // Smooth scrubbing (1 second delay)
            onUpdate: () => {
              carousel.layout(carousel.pos);
              carousel.notify(Math.round(carousel.pos));
            }
          }
        });
      }
    }
  }
});
