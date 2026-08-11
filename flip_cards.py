import re

with open('d:/KASSIA/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace CSS
css_start = "    /* ── Spices Card Grid ─────────────────────────────── */"
css_end = "      transform: translateX(4px);\n    }\n  </style>"

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
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 1.5rem;
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 1rem;
    }
    .spice-card {
      flex: 1 1 300px;
      max-width: 380px;
      width: 100%;
      height: 460px;
      position: relative;
      perspective: 1500px;
      text-decoration: none;
    }
    .spice-card-inner {
      position: relative;
      width: 100%;
      height: 100%;
      transition: transform 0.8s cubic-bezier(0.4, 0, 0.2, 1);
      transform-style: preserve-3d;
      border-radius: 20px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.06);
    }
    .spice-card:hover .spice-card-inner {
      transform: rotateY(180deg);
      box-shadow: 0 16px 32px rgba(0,0,0,0.15);
    }
    .spice-card-front, .spice-card-back {
      position: absolute;
      inset: 0;
      -webkit-backface-visibility: hidden;
      backface-visibility: hidden;
      border-radius: 20px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }
    .spice-card-front {
      justify-content: flex-end;
    }
    .spice-card-back {
      transform: rotateY(180deg);
      padding: 2.5rem;
      justify-content: center;
      align-items: center;
      text-align: center;
      color: #fff;
    }
    
    /* Specific back colors */
    .spice-card.cardamom .spice-card-back { background: linear-gradient(135deg, #1A3322 0%, #294D36 100%); }
    .spice-card.pepper .spice-card-back { background: linear-gradient(135deg, #1F1F1F 0%, #383838 100%); }
    .spice-card.cloves .spice-card-back { background: linear-gradient(135deg, #3E1C15 0%, #5C2A20 100%); }
    .spice-card.cinnamon .spice-card-back { background: linear-gradient(135deg, #5C2F15 0%, #8A461F 100%); }
    .spice-card.ginger .spice-card-back { background: linear-gradient(135deg, #7A5317 0%, #A36F1F 100%); }

    .spice-card-bg {
      position: absolute;
      inset: 0;
      background-size: cover;
      background-position: center;
      z-index: 1;
      transition: transform 0.8s ease;
    }
    .spice-card:hover .spice-card-bg {
      transform: scale(1.05);
    }
    .spice-card-front::after {
      content: '';
      position: absolute;
      inset: 0;
      background: linear-gradient(to top, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0.3) 50%, rgba(0,0,0,0) 100%);
      z-index: 2;
    }
    .spice-card.cardamom .spice-card-front::after { background: linear-gradient(to top, rgba(35, 75, 45, 0.95) 0%, rgba(35, 75, 45, 0.4) 50%, transparent 100%); }
    .spice-card.pepper .spice-card-front::after { background: linear-gradient(to top, rgba(40, 40, 40, 0.95) 0%, rgba(40, 40, 40, 0.4) 50%, transparent 100%); }
    .spice-card.cloves .spice-card-front::after { background: linear-gradient(to top, rgba(90, 40, 30, 0.95) 0%, rgba(90, 40, 30, 0.4) 50%, transparent 100%); }
    .spice-card.cinnamon .spice-card-front::after { background: linear-gradient(to top, rgba(140, 70, 30, 0.95) 0%, rgba(140, 70, 30, 0.4) 50%, transparent 100%); }
    .spice-card.ginger .spice-card-front::after { background: linear-gradient(to top, rgba(160, 110, 30, 0.95) 0%, rgba(160, 110, 30, 0.4) 50%, transparent 100%); }

    .spice-card-content {
      position: relative;
      z-index: 3;
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 1.2rem;
      height: 100%;
      justify-content: flex-end;
    }
    .spice-card-back .spice-card-content {
      justify-content: center;
      align-items: center;
      gap: 1.5rem;
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
    .spice-card-back .spice-card-text h3 {
      justify-content: center;
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
    .spice-card-back .spice-card-text p {
      line-height: 1.6;
      font-size: 1.05rem;
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
      border: 1px solid rgba(255,255,255,0.1);
      font-family: var(--font-sans, sans-serif);
      transition: background 0.3s ease, border-color 0.3s ease;
      width: 100%;
      box-sizing: border-box;
    }
    .spice-card-back .spice-card-btn {
      margin-top: auto;
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


html_start = "    <!-- ══ THE FIVE SPICES — Cards Menu ══ -->"
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
            <div class="spice-card-inner">
              <div class="spice-card-front">
                <div class="spice-card-bg" style="background-image: url('assets/spice_cardamom.webp');"></div>
                <div class="spice-card-content">
                  <div class="spice-card-text">
                    <h3>Cardamom <span>GC</span></h3>
                    <p>The queen of spices • Sweet & Cool</p>
                  </div>
                  <div class="spice-card-btn">
                    <span>Hover for Details</span>
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 3h6v6"></path><path d="M9 21H3v-6"></path><path d="M21 3l-7 7"></path><path d="M3 21l7-7"></path></svg>
                  </div>
                </div>
              </div>
              <div class="spice-card-back">
                <div class="spice-card-content">
                  <div class="spice-card-text">
                    <h3>Cardamom</h3>
                    <p>Intensely aromatic, sweet and cool, from the hills that gave it their name.</p>
                  </div>
                  <div class="spice-card-btn">
                    <span>Explore Now</span>
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                  </div>
                </div>
              </div>
            </div>
          </a>

          <!-- Pepper -->
          <a href="product-pepper.html" class="spice-card pepper reveal-up" style="transition-delay: 0.1s;">
            <div class="spice-card-inner">
              <div class="spice-card-front">
                <div class="spice-card-bg" style="background-image: url('assets/spice_pepper.webp');"></div>
                <div class="spice-card-content">
                  <div class="spice-card-text">
                    <h3>Black Pepper <span>BP</span></h3>
                    <p>High-range Malabar • Deep Heat</p>
                  </div>
                  <div class="spice-card-btn">
                    <span>Hover for Details</span>
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 3h6v6"></path><path d="M9 21H3v-6"></path><path d="M21 3l-7 7"></path><path d="M3 21l7-7"></path></svg>
                  </div>
                </div>
              </div>
              <div class="spice-card-back">
                <div class="spice-card-content">
                  <div class="spice-card-text">
                    <h3>Black Pepper</h3>
                    <p>High-range Malabar pepper with deep heat and bold aroma, sun-dried for three to four days.</p>
                  </div>
                  <div class="spice-card-btn">
                    <span>Explore Now</span>
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                  </div>
                </div>
              </div>
            </div>
          </a>

          <!-- Cloves -->
          <a href="product-cloves.html" class="spice-card cloves reveal-up" style="transition-delay: 0.2s;">
            <div class="spice-card-inner">
              <div class="spice-card-front">
                <div class="spice-card-bg" style="background-image: url('assets/spice_cloves.webp');"></div>
                <div class="spice-card-content">
                  <div class="spice-card-text">
                    <h3>Cloves <span>CL</span></h3>
                    <p>Hand-picked buds • Rich Essential Oil</p>
                  </div>
                  <div class="spice-card-btn">
                    <span>Hover for Details</span>
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 3h6v6"></path><path d="M9 21H3v-6"></path><path d="M21 3l-7 7"></path><path d="M3 21l7-7"></path></svg>
                  </div>
                </div>
              </div>
              <div class="spice-card-back">
                <div class="spice-card-content">
                  <div class="spice-card-text">
                    <h3>Cloves</h3>
                    <p>Hand-picked buds from Kerala, rich in essential oil — sharp, warming and deeply aromatic.</p>
                  </div>
                  <div class="spice-card-btn">
                    <span>Explore Now</span>
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                  </div>
                </div>
              </div>
            </div>
          </a>

          <!-- Cinnamon -->
          <a href="product-cinnamon.html" class="spice-card cinnamon reveal-up" style="transition-delay: 0.3s;">
            <div class="spice-card-inner">
              <div class="spice-card-front">
                <div class="spice-card-bg" style="background-image: url('assets/spice_cinnamon.webp');"></div>
                <div class="spice-card-content">
                  <div class="spice-card-text">
                    <h3>Cinnamon <span>CN</span></h3>
                    <p>Delicate sweet bark • Air-dried Quills</p>
                  </div>
                  <div class="spice-card-btn">
                    <span>Hover for Details</span>
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 3h6v6"></path><path d="M9 21H3v-6"></path><path d="M21 3l-7 7"></path><path d="M3 21l7-7"></path></svg>
                  </div>
                </div>
              </div>
              <div class="spice-card-back">
                <div class="spice-card-content">
                  <div class="spice-card-text">
                    <h3>Cinnamon</h3>
                    <p>Delicate, sweet bark from Kerala's spice gardens — air-dried and rolled into neat quills.</p>
                  </div>
                  <div class="spice-card-btn">
                    <span>Explore Now</span>
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                  </div>
                </div>
              </div>
            </div>
          </a>

          <!-- Ginger -->
          <a href="product-ginger.html" class="spice-card ginger reveal-up" style="transition-delay: 0.4s;">
            <div class="spice-card-inner">
              <div class="spice-card-front">
                <div class="spice-card-bg" style="background-image: url('assets/spice_ginger.webp');"></div>
                <div class="spice-card-content">
                  <div class="spice-card-text">
                    <h3>Dried Ginger <span>DG</span></h3>
                    <p>Sun-dried fiery root • Citrus Edge</p>
                  </div>
                  <div class="spice-card-btn">
                    <span>Hover for Details</span>
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 3h6v6"></path><path d="M9 21H3v-6"></path><path d="M21 3l-7 7"></path><path d="M3 21l7-7"></path></svg>
                  </div>
                </div>
              </div>
              <div class="spice-card-back">
                <div class="spice-card-content">
                  <div class="spice-card-text">
                    <h3>Dried Ginger</h3>
                    <p>Sun-dried and fiery, with a clean citrus edge — slow-cured the traditional Keralan way.</p>
                  </div>
                  <div class="spice-card-btn">
                    <span>Explore Now</span>
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                  </div>
                </div>
              </div>
            </div>
          </a>

        </div>
      </div>
    </section>"""
    
    content = content[:start_idx] + new_html + content[end_idx:]

with open('d:/KASSIA/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
