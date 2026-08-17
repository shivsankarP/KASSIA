import re, glob

font_block = '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n<link href="https://fonts.googleapis.com/css2?family=Anton&display=swap" rel="stylesheet">'

for f in glob.glob('d:/KASSIA/*.html'):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    new = re.sub(
        r'<link rel="preconnect" href="https://fonts\.googleapis\.com">.*?rel="stylesheet">',
        font_block,
        c, flags=re.DOTALL
    )
    with open(f, 'w', encoding='utf-8') as fp:
        fp.write(new)
    print(f'Updated: {f}')

print('Done')
