import re

# Update index.html
html_file = 'd:/KASSIA/index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Update container height
content = content.replace('height: 500px;', 'height: 650px;')
# Update card dimensions
content = content.replace('width: 300px; height: 380px;', 'width: 440px; height: 580px;')

# Bust cache for CSS/JS
content = re.sub(r'href="css/style\.css\?v=\d+"', 'href="css/style.css?v=12347"', content)
content = re.sub(r'src="js/main\.js\?v=\d+"', 'src="js/main.js?v=12347"', content)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

# Update main.js
js_file = 'd:/KASSIA/js/main.js'
with open(js_file, 'r', encoding='utf-8') as f:
    js_content = f.read()

js_content = js_content.replace('cardWidth: 300,', 'cardWidth: 440,')

with open(js_file, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Sizes updated and cache busted.")
