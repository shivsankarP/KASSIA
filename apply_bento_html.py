import os
import glob
import re

files = [
    'product-cardamom.html',
    'product-pepper.html',
    'product-cloves.html',
    'product-cinnamon.html',
    'product-ginger.html'
]

switcher_html = """
    <!-- Horizontal Bento Switcher -->
    <section class="bento-switcher-section">
      <div class="container">
        <nav class="bento-switcher" aria-label="Spice Navigator">
          <a href="product-cardamom.html" class="bento-switcher-item {cardamom_active}">
            <img src="assets/spice_cardamom.webp" alt="Cardamom" class="bento-switcher-img">
            <div class="bento-switcher-text">
              <span class="bento-switcher-title">Cardamom</span>
              <span class="bento-switcher-subtitle">Queen of spices</span>
            </div>
          </a>
          <a href="product-pepper.html" class="bento-switcher-item {pepper_active}">
            <img src="assets/spice_pepper.webp" alt="Black Pepper" class="bento-switcher-img">
            <div class="bento-switcher-text">
              <span class="bento-switcher-title">Black Pepper</span>
              <span class="bento-switcher-subtitle">Malabar gold</span>
            </div>
          </a>
          <a href="product-cloves.html" class="bento-switcher-item {cloves_active}">
            <img src="assets/spice_cloves.webp" alt="Cloves" class="bento-switcher-img">
            <div class="bento-switcher-text">
              <span class="bento-switcher-title">Cloves</span>
              <span class="bento-switcher-subtitle">Intense aroma</span>
            </div>
          </a>
          <a href="product-cinnamon.html" class="bento-switcher-item {cinnamon_active}">
            <img src="assets/spice_cinnamon.webp" alt="Cinnamon" class="bento-switcher-img">
            <div class="bento-switcher-text">
              <span class="bento-switcher-title">Cinnamon</span>
              <span class="bento-switcher-subtitle">True Ceylon</span>
            </div>
          </a>
          <a href="product-ginger.html" class="bento-switcher-item {ginger_active}">
            <img src="assets/spice_ginger.webp" alt="Dried Ginger" class="bento-switcher-img">
            <div class="bento-switcher-text">
              <span class="bento-switcher-title">Dried Ginger</span>
              <span class="bento-switcher-subtitle">Sun-dried Chukku</span>
            </div>
          </a>
        </nav>
      </div>
    </section>
"""

for file in files:
    file_path = os.path.join('d:/KASSIA', file)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract eyebrow
    eyebrow = re.search(r'<span class="eyebrow">(.*?)</span>', content).group(1)
    # Extract title
    title = re.search(r'<h1 class="product-hero-title">(.*?)</h1>', content).group(1)
    
    # Extract flavor
    flavor = re.search(r'Flavor Profile.*?</h3>\s*<p>(.*?)</p>', content, re.DOTALL).group(1)
    
    # Extract grown
    grown = re.search(r'How It\'s Grown.*?</h3>\s*<p>(.*?)</p>', content, re.DOTALL).group(1)
    
    # Extract uses
    uses = re.search(r'Traditional Uses.*?</h3>\s*<p>(.*?)</p>', content, re.DOTALL).group(1)
    
    # Extract image src
    img_src = re.search(r'<div class="product-hero-image-col[^>]*>.*?<img src="(.*?)"', content, re.DOTALL).group(1)
    
    # Determine active state for switcher
    actives = {
        'cardamom_active': 'active' if 'cardamom' in file else '',
        'pepper_active': 'active' if 'pepper' in file else '',
        'cloves_active': 'active' if 'cloves' in file else '',
        'cinnamon_active': 'active' if 'cinnamon' in file else '',
        'ginger_active': 'active' if 'ginger' in file else ''
    }
    
    current_switcher = switcher_html.format(**actives)

    new_main = f"""  <main>
    <!-- Product Detail Hero -->
    <section class="bento-hero">
      <div class="container bento-hero-grid">
        
        <!-- Details Column -->
        <div class="bento-hero-details reveal-up">
          <span class="eyebrow">{eyebrow}</span>
          <h1 class="bento-hero-title">{title}</h1>
          <p class="hero-subtitle">Traceable to origin. Tested for purity. Shipped from Kerala.</p>
          <div class="bento-hero-actions">
            <a href="#" class="btn btn-secondary">Add to cart</a>
            <a href="story.html" class="btn btn-secondary">Trace Origin</a>
          </div>
        </div>

        <!-- Image Column -->
        <div class="bento-hero-image-wrap reveal-up">
          <img src="{img_src}" alt="{title}">
        </div>
        
      </div>
    </section>

{current_switcher}
    <!-- Bento Grid Section -->
    <section class="bento-grid-section">
      <div class="container">
        <div class="bento-grid">
          <!-- Row 1, Col 1 (spans 2 rows) -->
          <div class="bento-item bento-image-large bento-row-2 bento-image-only reveal-up">
            <img src="{img_src}" alt="Harvesting {title}">
          </div>

          <!-- Row 1, Col 2 -->
          <div class="bento-item bento-image-only reveal-up">
            <img src="{img_src}" alt="Processing {title}">
          </div>

          <!-- Row 1, Col 3 -->
          <div class="bento-item bento-yellow reveal-up">
            <div class="bento-content">
              <h3 class="bento-title">Traditional Uses</h3>
              <p class="bento-text">{uses}</p>
              <a href="#" class="bento-btn">View recipes</a>
            </div>
          </div>

          <!-- Row 2, Col 2 -->
          <div class="bento-item bento-dark reveal-up">
            <div class="bento-content">
              <h3 class="bento-title">Flavor Profile</h3>
              <p class="bento-text">{flavor}</p>
              <a href="#" class="bento-btn">Discover notes</a>
            </div>
          </div>

          <!-- Row 2, Col 3 (spans 2 rows) -->
          <div class="bento-item bento-image-only bento-row-2 reveal-up">
            <img src="{img_src}" alt="{title} in dish">
          </div>

          <!-- Row 3, Col 1 & 2 (spans 2 cols) -->
          <div class="bento-item bento-red bento-col-2 reveal-up">
            <div class="bento-content align-top">
              <h3 class="bento-title">How It's Grown</h3>
              <p class="bento-text">{grown}</p>
              <a href="story.html" class="bento-btn">Read the story</a>
            </div>
          </div>
          
        </div>
      </div>
    </section>
  </main>"""

    # Replace <main>...</main>
    new_content = re.sub(r'<main>.*?</main>', new_main, content, flags=re.DOTALL)
    
    # Bump CSS version
    new_content = re.sub(r'href="css/style\.css\?v=\d+"', 'href="css/style.css?v=12372"', new_content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Bento HTML applied to all product pages.")
