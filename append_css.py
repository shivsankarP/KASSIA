css_code = """
/* ── Depth Carousel ─────────────────────────────── */
.depth-carousel {
  position: relative;
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  perspective: var(--dc-perspective, 1400px);
  user-select: none;
  touch-action: pan-y;
}

.depth-carousel__stage {
  position: absolute;
  inset: 0;
  transform-style: preserve-3d;
}

.depth-carousel__card {
  position: absolute;
  top: 50%;
  left: 50%;
  overflow: hidden;
  will-change: transform, opacity, filter, z-index;
  box-shadow: 0 20px 40px rgba(0,0,0,0.4), 0 5px 15px rgba(0,0,0,0.2);
  cursor: pointer;
}

.depth-carousel__img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.depth-carousel__tint {
  position: absolute;
  inset: 0;
  pointer-events: none;
  z-index: 1;
}

.process-card-content {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  padding: 2rem;
  background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0) 100%);
  color: #fff;
  z-index: 2;
  text-align: left;
}

.process-card-content span {
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--accent-cardamom, #A8C49E);
  margin-bottom: 0.5rem;
  display: block;
}

.process-card-content h3 {
  font-size: 1.8rem;
  margin-bottom: 0.5rem;
  font-family: var(--font-serif, 'Cormorant Garamond', serif);
}

.process-card-content p {
  font-size: 0.95rem;
  opacity: 0.9;
  line-height: 1.4;
  margin: 0;
  font-family: var(--font-sans, sans-serif);
}

.depth-carousel__arrow {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(255,255,255,0.1);
  backdrop-filter: blur(5px);
  border: 1px solid rgba(255,255,255,0.2);
  color: #fff;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  z-index: 3000;
  transition: background 0.3s ease, border-color 0.3s ease;
}

.depth-carousel__arrow:hover {
  background: rgba(255,255,255,0.2);
  border-color: rgba(255,255,255,0.4);
}

.depth-carousel__arrow--prev {
  left: 2rem;
}

.depth-carousel__arrow--next {
  right: 2rem;
}

.depth-carousel__dots {
  position: absolute;
  bottom: -40px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 12px;
  z-index: 3000;
}

.depth-carousel__dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: rgba(255,255,255,0.3);
  border: none;
  cursor: pointer;
  padding: 0;
  transition: background 0.3s ease, transform 0.3s ease;
}

.depth-carousel__dot.is-active {
  background: #fff;
  transform: scale(1.4);
}

@media (max-width: 768px) {
  .depth-carousel__arrow {
    display: none;
  }
}
"""

with open('d:/KASSIA/css/style.css', 'a', encoding='utf-8') as f:
    f.write(css_code)

print("CSS appended to style.css")
