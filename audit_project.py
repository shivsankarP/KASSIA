import glob
import os
import re

html_files = glob.glob('d:/KASSIA/*.html')

print("--- AUDITING HTML FILES ---")

broken = []

for filepath in html_files:
    fname = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check img src
    img_srcs = re.findall(r'src=["\']([^"\']+)["\']', content)
    for src in img_srcs:
        if src.startswith('http') or src.startswith('//') or src.startswith('data:'):
            continue
        clean_src = src.split('?')[0]
        full_path = os.path.normpath(os.path.join('d:/KASSIA', clean_src))
        if not os.path.exists(full_path):
            broken.append(f"[BROKEN SRC] {fname} -> {clean_src}")

    # Check hrefs
    hrefs = re.findall(r'href=["\']([^"\']+)["\']', content)
    for href in hrefs:
        if href.startswith('http') or href.startswith('#') or href.startswith('mailto:') or href.startswith('tel:') or href == '':
            continue
        clean_href = href.split('?')[0].split('#')[0]
        full_path = os.path.normpath(os.path.join('d:/KASSIA', clean_href))
        if not os.path.exists(full_path):
            broken.append(f"[BROKEN HREF] {fname} -> {clean_href}")

if not broken:
    print("NO BROKEN LINKS OR IMAGES FOUND!")
else:
    for b in broken:
        print(b.encode('ascii', errors='ignore').decode('ascii'))

print("--- AUDIT COMPLETE ---")
