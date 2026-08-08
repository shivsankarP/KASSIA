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
