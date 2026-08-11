import re

with open('d:/KASSIA/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace CSS
css_start = "    /* ── Serpentine Vine Menu ─────────────────────────────── */"
css_end = "      }\n    }\n  </style>"

if css_start in content:
    start_idx = content.find(css_start)
    end_idx = content.find(css_end, start_idx) + len(css_end) - 10 # Keep </style>
    
    new_css = """    /* ── Spices Card Grid ─────────────────────────────── */
    .spices-card-section {
      padding: 5rem 0 7rem;
      background-color: #F7F3EE;
      position: relative;
    }
    .spices-header {
      text-align: center;
      margin-bottom: 3.5rem;
    }
    .spices-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 1.5rem;
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 1rem;
    }
    .spice-card {
      position: relative;
      height: 460px;
      border-radius: 20px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      text-decoration: none;
      box-shadow: 0 8px 24px rgba(0,0,0,0.06);
      transition: transform 0.4s ease, box-shadow 0.4s ease;
    }
    .spice-card:hover {
      transform: translateY(-8px);
      box-shadow: 0 16px 32px rgba(0,0,0,0.12);
    }
    .spice-card-bg {
      position: absolute;
      inset: 0;
      background-size: cover;
      background-position: center;
      transition: transform 0.8s cubic-bezier(0.25, 1, 0.5, 1);
      z-index: 1;
    }
    .spice-card:hover .spice-card-bg {
      transform: scale(1.05);
    }
    .spice-card::after {
      content: '';
      position: absolute;
      inset: 0;
      background: linear-gradient(to top, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0.3) 50%, rgba(0,0,0,0) 100%);
      z-index: 2;
      transition: background 0.4s ease;
    }
    .spice-card.cardamom::after { background: linear-gradient(to top, rgba(35, 75, 45, 0.95) 0%, rgba(35, 75, 45, 0.4) 50%, transparent 100%); }
    .spice-card.pepper::after { background: linear-gradient(to top, rgba(40, 40, 40, 0.95) 0%, rgba(40, 40, 40, 0.4) 50%, transparent 100%); }
    .spice-card.cloves::after { background: linear-gradient(to top, rgba(90, 40, 30, 0.95) 0%, rgba(90, 40, 30, 0.4) 50%, transparent 100%); }
    .spice-card.cinnamon::after { background: linear-gradient(to top, rgba(140, 70, 30, 0.95) 0%, rgba(140, 70, 30, 0.4) 50%, transparent 100%); }
    .spice-card.ginger::after { background: linear-gradient(to top, rgba(160, 110, 30, 0.95) 0%, rgba(160, 110, 30, 0.4) 50%, transparent 100%); }

    .spice-card-content {
      position: relative;
      z-index: 3;
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 1.2rem;
    }
    .spice-card-text {
      color: #fff;
    }
    .spice-card-text h3 {
      font-family: var(--font-sans, sans-serif);
      font-size: 2.2rem;
      font-weight: 700;
      margin-bottom: 0.3rem;
      display: flex;
      align-items: baseline;
      gap: 0.6rem;
      line-height: 1.1;
    }
    .spice-card-text h3 span {
      font-size: 1.1rem;
      font-weight: 700;
      opacity: 0.8;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .spice-card-text p {
      font-size: 0.95rem;
      opacity: 0.9;
      font-weight: 500;
      margin: 0;
      font-family: var(--font-sans, sans-serif);
    }
    .spice-card-btn {
      background: rgba(255, 255, 255, 0.1);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      border-radius: 12px;
      padding: 1rem 1.2rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      color: #fff;
      font-weight: 600;
      font-size: 1.05rem;
      transition: background 0.3s ease, border-color 0.3s ease;
      border: 1px solid rgba(255,255,255,0.1);
      font-family: var(--font-sans, sans-serif);
    }
    .spice-card:hover .spice-card-btn {
      background: rgba(255, 255, 255, 0.2);
      border-color: rgba(255,255,255,0.3);
    }
    .spice-card-btn svg {
      transition: transform 0.3s ease;
    }
    .spice-card:hover .spice-card-btn svg {
      transform: translateX(4px);
    }
"""
    
    content = content[:start_idx] + new_css + content[end_idx:]


html_start = "    <!-- ══ THE FIVE SPICES — Serpentine Vine Menu ══ -->"
html_end = "    </section>"

if html_start in content:
    start_idx = content.find(html_start)
    end_idx = content.find(html_end, start_idx) + len(html_end)
    
    new_html = """    <!-- ══ THE FIVE SPICES — Cards Menu ══ -->
    <section id="spices" class="spices-card-section">
      <div class="container">
        <div class="spices-header reveal-up">
          <span class="eyebrow">OUR SPICES</span>
          <h2>Five spices. One origin.</h2>
          <p style="max-width:520px;margin:1rem auto 0;font-size:1.05rem;">Sourced lot by lot from Kerala's spice belt — each one singular in origin, graded by hand, and traceable to where it grew.</p>
        </div>

        <div class="spices-grid">
          <!-- Cardamom -->
          <a href="product-cardamom.html" class="spice-card cardamom reveal-up">
            <div class="spice-card-bg" style="background-image: url('assets/spice_cardamom.webp');"></div>
            <div class="spice-card-content">
              <div class="spice-card-text">
                <h3>Cardamom <span>GC</span></h3>
                <p>The queen of spices • Sweet & Cool</p>
              </div>
              <div class="spice-card-btn">
                <span>Explore Now</span>
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
              </div>
            </div>
          </a>

          <!-- Pepper -->
          <a href="product-pepper.html" class="spice-card pepper reveal-up" style="transition-delay: 0.1s;">
            <div class="spice-card-bg" style="background-image: url('assets/spice_pepper.webp');"></div>
            <div class="spice-card-content">
              <div class="spice-card-text">
                <h3>Black Pepper <span>BP</span></h3>
                <p>High-range Malabar • Deep Heat</p>
              </div>
              <div class="spice-card-btn">
                <span>Explore Now</span>
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
              </div>
            </div>
          </a>

          <!-- Cloves -->
          <a href="product-cloves.html" class="spice-card cloves reveal-up" style="transition-delay: 0.2s;">
            <div class="spice-card-bg" style="background-image: url('assets/spice_cloves.webp');"></div>
            <div class="spice-card-content">
              <div class="spice-card-text">
                <h3>Cloves <span>CL</span></h3>
                <p>Hand-picked buds • Rich Essential Oil</p>
              </div>
              <div class="spice-card-btn">
                <span>Explore Now</span>
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
              </div>
            </div>
          </a>

          <!-- Cinnamon -->
          <a href="product-cinnamon.html" class="spice-card cinnamon reveal-up" style="transition-delay: 0.3s;">
            <div class="spice-card-bg" style="background-image: url('assets/spice_cinnamon.webp');"></div>
            <div class="spice-card-content">
              <div class="spice-card-text">
                <h3>Cinnamon <span>CN</span></h3>
                <p>Delicate sweet bark • Air-dried Quills</p>
              </div>
              <div class="spice-card-btn">
                <span>Explore Now</span>
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
              </div>
            </div>
          </a>

          <!-- Ginger -->
          <a href="product-ginger.html" class="spice-card ginger reveal-up" style="transition-delay: 0.4s;">
            <div class="spice-card-bg" style="background-image: url('assets/spice_ginger.webp');"></div>
            <div class="spice-card-content">
              <div class="spice-card-text">
                <h3>Dried Ginger <span>DG</span></h3>
                <p>Sun-dried fiery root • Citrus Edge</p>
              </div>
              <div class="spice-card-btn">
                <span>Explore Now</span>
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
              </div>
            </div>
          </a>

        </div>
      </div>
    </section>"""
    
    content = content[:start_idx] + new_html + content[end_idx:]

with open('d:/KASSIA/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
