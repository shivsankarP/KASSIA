import re
import glob

html_files = glob.glob('d:\\KASSIA\\*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # regex replace style.css?v=...
    new_content = re.sub(r'href="css/style\.css[^"]*"', 'href="css/style.css?v=12346"', content)
    # regex replace main.js?v=...
    new_content = re.sub(r'src="js/main\.js[^"]*"', 'src="js/main.js?v=12346"', new_content)
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_content)
