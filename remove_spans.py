import os

filepath = 'd:/KASSIA/index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the spans
for span in [' <span>GC</span>', ' <span>BP</span>', ' <span>CL</span>', ' <span>CN</span>', ' <span>DG</span>']:
    content = content.replace(span, '')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Spans removed.")
