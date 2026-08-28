import glob

html_files = glob.glob('d:/KASSIA/*.html')

replacements = {
    'Card amom': 'Cardamom',
    'Clo ves': 'Cloves',
    'Cinn amon': 'Cinnamon',
    'Trace able': 'Traceable',
}

for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Card titles cleaned up.")
