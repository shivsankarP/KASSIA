import os
import glob
import re

# 1. Create particles-config.js
config_js = """
document.addEventListener('DOMContentLoaded', () => {
  if (typeof particlesJS !== 'undefined') {
    particlesJS("particles-js", {
      particles: {
        number: { value: 140, density: { enable: true, value_area: 800 } },
        color: { value: "#A8C49E" },
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
        detect_on: "window",
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
  }
});
"""
with open('d:/KASSIA/js/particles-config.js', 'w', encoding='utf-8') as f:
    f.write(config_js)

# 2. Update style.css
css_file = 'd:/KASSIA/css/style.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace body background
css = re.sub(r'body\s*{[^}]*background:\s*radial-gradient[^;]*;[^}]*}', 
             lambda m: m.group(0).replace('background: radial-gradient(circle at center, var(--bg-sand) 0%, var(--bg-cream) 100%) fixed;', 'background: transparent;'), css)
# If it didn't match perfectly, just append
if 'background: transparent;' not in css and 'body { background: transparent !important; }' not in css:
    css += '\nbody { background: transparent !important; }\n'
if '#particles-js' not in css:
    css += '\n#particles-js { background: radial-gradient(circle at center, var(--bg-sand) 0%, var(--bg-cream) 100%); }\n'

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css)

# 3. Update all HTML files
html_files = glob.glob('d:/KASSIA/*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove inline styles from index.html if present
    content = re.sub(r'\s*body \{ background: transparent !important; \}\s*#particles-js \{\s*background: radial-gradient[^\}]+\}\s*', '\n', content)
    
    # Clean up any existing particles block at top
    content = re.sub(r'<body>\s*(?:<div id="particles-js"[^>]*></div>\s*)?(?:<div id="content-wrapper"[^>]*>\s*)?', '<body>\n  <div id="particles-js" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 0;"></div>\n  <div id="content-wrapper" style="position: relative; z-index: 1;">\n', content, count=1)
    
    # Clean up any existing particles block at bottom
    # First remove old particles scripts and content wrapper closing if they exist
    content = re.sub(r'\s*</div> <!-- End content-wrapper -->\s*<!-- Particles\.js -->\s*<script src="[^"]*particles\.min\.js"></script>\s*<script>[\s\S]*?</script>\s*</body>', '\n</body>', content)
    
    # Also remove if they only have the wrapper closing and not scripts (for other files if run multiple times)
    content = re.sub(r'\s*</div> <!-- End content-wrapper -->\s*<script src="[^"]*particles\.min\.js"></script>\s*<script src="[^"]*particles-config\.js[^"]*"></script>\s*</body>', '\n</body>', content)

    # Insert new unified bottom
    bottom_code = """
  </div> <!-- End content-wrapper -->
  <!-- Particles.js -->
  <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
  <script src="js/particles-config.js?v=1"></script>
</body>"""
    content = content.replace('</body>', bottom_code)
    
    # Bump cache
    content = re.sub(r'href="css/style\.css\?v=\d+"', 'href="css/style.css?v=12360"', content)
    content = re.sub(r'src="js/main\.js\?v=\d+"', 'src="js/main.js?v=12360"', content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("All pages updated with particles background.")
