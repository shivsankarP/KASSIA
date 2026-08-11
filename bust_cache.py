import os
import glob

html_files = glob.glob('d:\\KASSIA\\*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update css version to bust cache
    for v in range(1, 10):
        old_css = f'<link rel="stylesheet" href="css/style.css?v={v}">'
        if old_css in content:
            content = content.replace(old_css, '<link rel="stylesheet" href="css/style.css?v=999">')
            
    old_css_base = '<link rel="stylesheet" href="css/style.css">'
    if old_css_base in content:
        content = content.replace(old_css_base, '<link rel="stylesheet" href="css/style.css?v=999">')
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
