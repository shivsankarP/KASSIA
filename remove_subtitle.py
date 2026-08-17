import glob, re

for f in glob.glob('d:/KASSIA/*.html'):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    new = re.sub(r'\s*<p class="hero-subtitle">Traceable to origin\. Tested for purity\. Shipped from Kerala\.</p>', '', c)
    if new != c:
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(new)
        print(f'Updated {f}')
