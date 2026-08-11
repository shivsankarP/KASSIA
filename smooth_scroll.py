import re

js_file = 'd:/KASSIA/js/main.js'
with open(js_file, 'r', encoding='utf-8') as f:
    js_content = f.read()

# Comment out wheel event
wheel_code = """    // Wheel
    this.root.addEventListener('wheel', e => {
      if (this.cfg.count < 2) return;
      e.preventDefault();
      if (this.tween) this.tween.kill();
      const raw = Math.abs(e.deltaX) > Math.abs(e.deltaY) ? e.deltaX : e.deltaY;
      const delta = e.deltaMode === 1 ? raw * 24 : raw;
      const step = this.clamp(delta / (this.cfg.cardWidth * 0.9), -0.6, 0.6);
      this.pos += step;
      this.layout(this.pos);
      if (this.wheelTimer) clearTimeout(this.wheelTimer);
      this.wheelTimer = setTimeout(() => this.setFocus(Math.round(this.pos), true), 130);
    }, { passive: false });"""

new_wheel_code = """    // Wheel disabled - using GSAP ScrollTrigger for smooth scroll integration instead
    /*
    this.root.addEventListener('wheel', e => {
      //...
    }, { passive: false });
    */"""

if wheel_code in js_content:
    js_content = js_content.replace(wheel_code, new_wheel_code)
else:
    # Use regex if exact match fails
    js_content = re.sub(r'// Wheel\s+this\.root\.addEventListener\(\'wheel\', e => \{.*?(?=// Pointer)', new_wheel_code + "\n\n    ", js_content, flags=re.DOTALL)


# Update initialization block
init_code = """document.addEventListener('DOMContentLoaded', () => {
  const el = document.getElementById('process-carousel');
  if (el) {
    new DepthCarousel(el);
  }
});"""

new_init_code = """document.addEventListener('DOMContentLoaded', () => {
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
});"""

js_content = js_content.replace(init_code, new_init_code)

with open(js_file, 'w', encoding='utf-8') as f:
    f.write(js_content)


# Bust cache in html files
import glob
html_files = glob.glob('d:/KASSIA/*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = re.sub(r'href="css/style\.css\?v=\d+"', 'href="css/style.css?v=12348"', content)
    content = re.sub(r'src="js/main\.js\?v=\d+"', 'src="js/main.js?v=12348"', content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Smooth scroll added and cache busted.")
