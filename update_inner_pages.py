import os

files = [
    'contact.html',
    'product-cardamom.html',
    'product-cinnamon.html',
    'product-cloves.html',
    'product-ginger.html',
    'product-pepper.html',
    'story.html'
]

for file in files:
    filepath = os.path.join('d:\\KASSIA', file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Add class="inner-page" to body
    if '<body>' in content:
        content = content.replace('<body>', '<body class="inner-page">')
        print(f'Added body class to {file}')
        
    # 2. Update css version to bust cache
    for v in range(1, 10):
        old_css = f'<link rel="stylesheet" href="css/style.css?v={v}">'
        if old_css in content:
            content = content.replace(old_css, '<link rel="stylesheet" href="css/style.css?v=5">')
            
    old_css_base = '<link rel="stylesheet" href="css/style.css">'
    if old_css_base in content:
        content = content.replace(old_css_base, '<link rel="stylesheet" href="css/style.css?v=5">')
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
