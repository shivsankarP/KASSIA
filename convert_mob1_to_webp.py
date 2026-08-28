import os
import glob
from PIL import Image

mob1_dir = r"d:\KASSIA\MOB1"
png_files = sorted(glob.glob(os.path.join(mob1_dir, "ezgif-frame-*.png")))
print(f"Found {len(png_files)} frames in MOB1. Converting to .webp...")

for i, png_path in enumerate(png_files):
    webp_path = os.path.splitext(png_path)[0] + ".webp"
    img = Image.open(png_path)
    img.save(webp_path, "WEBP", quality=90)
    if (i + 1) % 50 == 0 or i == 0:
        print(f"Converted {os.path.basename(webp_path)}")

print("MOB1 conversion complete!")
