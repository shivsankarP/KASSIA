import os

css_code = """
/* ==========================================================================
   BENTO BOX PRODUCT PAGE OVERHAUL
   ========================================================================== */

.bento-hero {
  padding-top: calc(var(--header-height) + 2rem);
  padding-bottom: 2rem;
  background-color: transparent;
  min-height: auto;
  position: relative;
  z-index: 5;
}

.bento-hero-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  align-items: stretch;
}

.bento-hero-details {
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 4rem 2rem 4rem 0;
}

.bento-hero-details .eyebrow {
  margin-bottom: 1rem;
}

.bento-hero-title {
  font-family: var(--font-sans);
  font-size: clamp(3rem, 6vw, 4.5rem);
  font-weight: 700;
  line-height: 1.1;
  text-transform: uppercase;
  color: var(--color-forest);
  margin-bottom: 2rem;
}

.bento-hero-actions {
  display: flex;
  gap: 1rem;
  margin-top: 1rem;
}

.bento-hero-image-wrap {
  position: relative;
  border-radius: 40px;
  overflow: hidden;
  min-height: 400px;
  background-color: var(--bg-sand);
}

.bento-hero-image-wrap img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  position: absolute;
  inset: 0;
}

@media (max-width: 991px) {
  .bento-hero-grid {
    grid-template-columns: 1fr;
  }
  .bento-hero-image-wrap {
    min-height: 300px;
  }
  .bento-hero-details {
    padding: 2rem 0;
    text-align: center;
    align-items: center;
  }
}

/* Horizontal Bento Switcher */
.bento-switcher-section {
  padding: 1rem 0;
  position: relative;
  z-index: 5;
}

.bento-switcher {
  background: linear-gradient(to right, #1c1c1e, #2c2c2e, #ff8c6b);
  border-radius: 100px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.5rem;
  overflow-x: auto;
  gap: 0.5rem;
}

.bento-switcher::-webkit-scrollbar {
  display: none;
}

.bento-switcher-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 0.5rem 1.5rem 0.5rem 0.5rem;
  border-radius: 100px;
  text-decoration: none;
  color: #fff;
  transition: background 0.3s ease;
  white-space: nowrap;
}

.bento-switcher-item:hover, .bento-switcher-item.active {
  background: rgba(255,255,255,0.1);
}

.bento-switcher-item.active {
  background: rgba(255, 255, 255, 0.15);
}

.bento-switcher-img {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  object-fit: cover;
}

.bento-switcher-text {
  display: flex;
  flex-direction: column;
}

.bento-switcher-title {
  font-family: var(--font-sans);
  font-size: 0.9rem;
  font-weight: 700;
  line-height: 1.2;
}

.bento-switcher-subtitle {
  font-size: 0.75rem;
  opacity: 0.7;
}

/* Bento Grid */
.bento-grid-section {
  padding: 4rem 0 8rem;
  position: relative;
  z-index: 5;
}

.bento-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-auto-rows: 250px;
  gap: 1.5rem;
}

@media (max-width: 991px) {
  .bento-grid {
    grid-template-columns: 1fr;
    grid-auto-rows: auto;
  }
}

.bento-item {
  border-radius: 32px;
  overflow: hidden;
  position: relative;
  display: flex;
  flex-direction: column;
  padding: 2.5rem;
}

/* Grid Spans */
.bento-row-2 {
  grid-row: span 2;
}

.bento-col-2 {
  grid-column: span 2;
}

@media (max-width: 991px) {
  .bento-row-2, .bento-col-2 {
    grid-row: span 1;
    grid-column: span 1;
    min-height: 300px;
  }
}

/* Item Variations */
.bento-image-only {
  padding: 0;
}
.bento-image-only img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.bento-dark {
  background-color: #212124;
  color: #fff;
}
.bento-dark h3, .bento-dark p {
  color: #fff;
}

.bento-red {
  background: linear-gradient(135deg, #32252a 0%, #d8695d 100%);
  color: #fff;
}
.bento-red h3, .bento-red p {
  color: #fff;
}

.bento-yellow {
  background-color: #f7b759;
  color: #1a1a1a;
}
.bento-yellow h3, .bento-yellow p {
  color: #1a1a1a;
}

.bento-content {
  position: relative;
  z-index: 2;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: flex-end; /* Push text down like the template */
}

.bento-content.align-top {
  justify-content: flex-start;
}

.bento-title {
  font-family: var(--font-sans);
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  line-height: 1.2;
}

.bento-text {
  font-family: var(--font-sans);
  font-size: 0.95rem;
  line-height: 1.5;
  opacity: 0.9;
}

.bento-btn {
  margin-top: auto;
  align-self: flex-start;
  padding: 0.8rem 1.5rem;
  border-radius: 100px;
  background: rgba(0,0,0,0.1);
  color: inherit;
  text-decoration: none;
  font-weight: 600;
  font-size: 0.9rem;
  transition: background 0.3s;
}

.bento-dark .bento-btn, .bento-red .bento-btn {
  background: rgba(255,255,255,0.15);
}

.bento-btn:hover {
  background: rgba(0,0,0,0.2);
}
.bento-dark .bento-btn:hover, .bento-red .bento-btn:hover {
  background: rgba(255,255,255,0.25);
}
"""

with open('d:/KASSIA/css/style.css', 'a', encoding='utf-8') as f:
    f.write(css_code)

print("Bento CSS added.")
