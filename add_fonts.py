import re
import glob

html_files = glob.glob('d:/KASSIA/*.html')

font_link = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Abril+Fatface&family=Bungee&family=Changa+One:ital@0;1&family=Cinzel:wght@400..900&family=Lobster+Two:ital,wght@0,400;0,700;1,400;1,700&family=Slabo+27px&display=swap" rel="stylesheet">"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Skip if already has Cinzel
    if 'Cinzel' in content:
        print(f'Already has Cinzel: {file}')
        continue

    # Replace the existing Google Fonts link or insert before </head>
    if 'fonts.googleapis.com' in content:
        # Replace the existing fonts link block
        content = re.sub(
            r'<link rel="preconnect" href="https://fonts\.googleapis\.com">.*?<link href="https://fonts\.googleapis\.com[^"]*" rel="stylesheet">',
            font_link,
            content,
            flags=re.DOTALL
        )
    else:
        content = content.replace('</head>', font_link + '\n</head>')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated: {file}')

print('Done')
