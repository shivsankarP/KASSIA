import re

html_file = 'd:/KASSIA/index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove old SVG particles container
content = re.sub(r'<div class="hero-particles-container"[^>]*></div>', '', content)

# Insert #particles-js into hero section
if '<div class="hero-background"></div>' in content:
    particles_div = '<div id="particles-js" style="position: absolute; inset: 0; z-index: 0;"></div>\n      <div class="hero-background"></div>'
    content = content.replace('<div class="hero-background"></div>', particles_div)

# Add particles.min.js and initialization logic before </body>
particles_script = """
  <!-- Particles.js -->
  <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', () => {
      // Initialize particles.js using the config provided by the user, adapted to the Kassia green theme
      particlesJS("particles-js", {
        particles: {
          number: { value: 140, density: { enable: true, value_area: 800 } },
          color: { value: "#A8C49E" }, // Cardamom accent
          shape: { type: "circle", stroke: { width: 0.5, color: "#E8C163" } },
          opacity: {
            value: 0.7,
            random: true,
            anim: { enable: true, speed: 1, opacity_min: 0.3 },
          },
          size: {
            value: 3,
            random: true,
            anim: { enable: true, speed: 2, size_min: 1 },
          },
          line_linked: {
            enable: true,
            distance: 160,
            color: "#A8C49E",
            opacity: 0.4,
            width: 1.2,
          },
          move: { enable: true, speed: 2, random: true, out_mode: "bounce" },
        },
        interactivity: {
          detect_on: "canvas",
          events: {
            onhover: { enable: true, mode: "grab" },
            onclick: { enable: true, mode: "push" },
            resize: true,
          },
          modes: {
            grab: { distance: 220, line_linked: { opacity: 0.8 } },
            push: { particles_nb: 4 },
            repulse: { distance: 180, duration: 0.4 },
          },
        },
        retina_detect: true,
      });
    });
  </script>
"""

# replace </body>
content = content.replace('</body>', particles_script + '\n</body>')

# Cache bust
content = re.sub(r'href="css/style\.css\?v=\d+"', 'href="css/style.css?v=12351"', content)
content = re.sub(r'src="js/main\.js\?v=\d+"', 'src="js/main.js?v=12351"', content)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Particles added.")
