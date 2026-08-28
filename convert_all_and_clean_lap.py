import os
import glob
from PIL import Image, ImageFilter
import numpy as np

def convert_destop_to_webp():
    destop_dir = r"d:\KASSIA\DESTOP"
    png_files = sorted(glob.glob(os.path.join(destop_dir, "ezgif-frame-*.png")))
    print(f"Converting {len(png_files)} frames in DESTOP to .webp...")
    
    for i, png_path in enumerate(png_files):
        webp_path = os.path.splitext(png_path)[0] + ".webp"
        img = Image.open(png_path)
        img.save(webp_path, "WEBP", quality=92)
        if (i + 1) % 50 == 0 or i == 0:
            print(f"Converted {os.path.basename(webp_path)}")
    print("DESTOP WebP conversion complete!")

def inpaint_lap_frames():
    lap_dir = r"d:\KASSIA\lap"
    lap_files = sorted(glob.glob(os.path.join(lap_dir, "ezgif-frame-*.webp")))
    print(f"Cleaning {len(lap_files)} frames in lap...")
    
    # In lap (1920x1080), center is at cx=1740, cy=898
    cx, cy = 1740, 898
    r = 45 # radius in 1080p
    
    modified = 0
    for fpath in lap_files:
        img = Image.open(fpath)
        arr = np.array(img)
        h, w, _ = arr.shape
        
        x1, y1 = max(0, cx - r - 15), max(0, cy - r - 15)
        x2, y2 = min(w, cx + r + 15), min(h, cy + r + 15)
        
        patch = arr[y1:y2, x1:x2].astype(float)
        ph, pw, _ = patch.shape
        pcx, pcy = cx - x1, cy - y1
        
        Y, X = np.ogrid[:ph, :pw]
        dist = np.abs(X - pcx) / 38.0 + np.abs(Y - pcy) / 38.0
        mask = np.clip((1.2 - dist) / 0.35, 0.0, 1.0)
        
        reconstructed = patch.copy()
        for y in range(ph):
            row_mask = mask[y] > 0
            if not np.any(row_mask):
                continue
                
            x_indices = np.where(row_mask)[0]
            x_start = max(0, x_indices[0] - 1)
            x_end = min(pw - 1, x_indices[-1] + 1)
            
            val_start = patch[y, x_start]
            val_end = patch[y, x_end]
            span = max(1, x_end - x_start)
            
            for x in x_indices:
                t = (x - x_start) / span
                interp_color = (1.0 - t) * val_start + t * val_end
                noise_sample = (patch[max(0, y-4), x] + patch[min(ph-1, y+4), x]) / 2.0
                noise_blur = (patch[max(0, y-4), x_start] + patch[min(ph-1, y+4), x_end]) / 2.0
                texture_detail = (noise_sample - noise_blur) * 0.3
                reconstructed[y, x] = interp_color + texture_detail
                
        recon_img = Image.fromarray(np.clip(reconstructed, 0, 255).astype(np.uint8))
        recon_smooth = np.array(recon_img.filter(ImageFilter.GaussianBlur(radius=1.0))).astype(float)
        
        mask_3d = mask[:, :, np.newaxis]
        final_patch = patch * (1.0 - mask_3d) + recon_smooth * mask_3d
        
        out = arr.copy()
        out[y1:y2, x1:x2] = np.clip(final_patch, 0, 255).astype(np.uint8)
        
        Image.fromarray(out).save(fpath, "WEBP", quality=92)
        modified += 1
        
    print(f"lap cleaning complete: {modified} frames processed.")

if __name__ == "__main__":
    convert_destop_to_webp()
    inpaint_lap_frames()
