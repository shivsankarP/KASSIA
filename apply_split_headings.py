import glob
import re

# First clean out old split spans from ALL html files to get clean text
html_files = glob.glob('d:/KASSIA/*.html')

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Clean out heading-first-half and heading-second-half spans
    content = re.sub(r'<span class="heading-first-half">(.*?)</span>\s*<span class="heading-second-half">(.*?)</span>', r'\1 \2', content)
    content = re.sub(r'<span class="heading-first-half">(.*?)</span><span class="heading-second-half">(.*?)</span>', r'\1\2', content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Cleaned up previous heading spans.")

# Now split ONLY section-level headings (excluding cards/containers)
def split_section_heading(match):
    tag = match.group(1)
    attrs = match.group(2)
    text = match.group(3).strip()
    
    # Check if inside container or card
    # If tag or parent attributes indicate a card title, skip!
    if 'why-title' in attrs or 'spice-card' in attrs or 'bento-title' in attrs or 'stack-carousel' in attrs:
        return match.group(0)
    
    # Skip if contains interactive elements
    if '<' in text:
        return match.group(0)
    
    words = text.split()
    if len(words) > 1:
        mid = (len(words) + 1) // 2
        h1 = " ".join(words[:mid])
        h2 = " ".join(words[mid:])
        return f'<{tag}{attrs}><span class="heading-first-half">{h1}</span> <span class="heading-second-half">{h2}</span></{tag}>'
    elif len(text) > 3:
        mid = (len(text) + 1) // 2
        h1 = text[:mid]
        h2 = text[mid:]
        return f'<{tag}{attrs}><span class="heading-first-half">{h1}</span><span class="heading-second-half">{h2}</span></{tag}>'
    
    return match.group(0)

pattern = re.compile(r'<(h[1-3])([^>]*)>(.*?)</\1>', re.DOTALL)

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We will split section-level h1, h2, h3
    lines = []
    # Process file line by line or section by section
    new_content = pattern.sub(split_section_heading, content)
    
    # Extra check: remove split spans from inside spice-card, why-card, bento-grid, stack-carousel
    # Using regex to clean card containers
    card_container_pattern = re.compile(r'(<div[^>]*class="[^"]*(?:spice-card|why-card|bento-grid|bento-item|stack-carousel)[^"]*"[^>]*>.*?</div>)', re.DOTALL)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Processed section headings in: {file_path}")

print("Section heading split complete.")
