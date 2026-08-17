
document.addEventListener('DOMContentLoaded', () => {
  if (typeof particlesJS !== 'undefined') {
    particlesJS("particles-js", {
      particles: {
        number: { value: 140, density: { enable: true, value_area: 800 } },
        color: { value: ["#ffffff", "#E8F5E5", "#B8E0B2", "#FFEC80"] },
        shape: { type: "circle", stroke: { width: 1, color: "#ffffff" } },
        opacity: {
          value: 1.0,
          random: true,
          anim: { enable: true, speed: 1.2, opacity_min: 0.6 },
        },
        size: {
          value: 4,
          random: true,
          anim: { enable: true, speed: 2, size_min: 1.5 },
        },
        line_linked: {
          enable: true,
          distance: 160,
          color: "#ffffff",
          opacity: 0.7,
          width: 1.5,
        },
        move: { enable: true, speed: 2, random: true, out_mode: "bounce" },
      },
      interactivity: {
        detect_on: "window",
        events: {
          onhover: { enable: true, mode: "grab" },
          onclick: { enable: true, mode: "push" },
          resize: true,
        },
        modes: {
          grab: { distance: 220, line_linked: { opacity: 1.0 } },
          push: { particles_nb: 4 },
          repulse: { distance: 180, duration: 0.4 },
        },
      },
      retina_detect: true,
    });
  }
});
