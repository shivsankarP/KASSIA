import os
import glob
from PIL import Image, ImageFilter
import numpy as np

def inpaint_wood_grain(img_arr, cx=1160, cy=599):
    h, w, c = img_arr.shape
    r = 30
    x1, y1 = max(0, cx - r - 10), max(0, cy - r - 10)
    x2, y2 = min(w, cx + r + 10), min(h, cy + r + 10)
    
    patch = img_arr[y1:y2, x1:x2].astype(float)
    ph, pw, _ = patch.shape
    pcx, pcy = cx - x1, cy - y1
    
    Y, X = np.ogrid[:ph, :pw]
    dist = np.abs(X - pcx) / 25.0 + np.abs(Y - pcy) / 25.0
    mask = np.clip((1.15 - dist) / 0.35, 0.0, 1.0)
    
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
            noise_sample = (patch[max(0, y-3), x] + patch[min(ph-1, y+3), x]) / 2.0
            noise_blur = (patch[max(0, y-3), x_start] + patch[min(ph-1, y+3), x_end]) / 2.0
            texture_detail = (noise_sample - noise_blur) * 0.3
            reconstructed[y, x] = interp_color + texture_detail
            
    recon_img = Image.fromarray(np.clip(reconstructed, 0, 255).astype(np.uint8))
    recon_smooth = np.array(recon_img.filter(ImageFilter.GaussianBlur(radius=0.8))).astype(float)
    
    mask_3d = mask[:, :, np.newaxis]
    final_patch = patch * (1.0 - mask_3d) + recon_smooth * mask_3d
    
    out = img_arr.copy()
    out[y1:y2, x1:x2] = np.clip(final_patch, 0, 255).astype(np.uint8)
    return out

def process_all_destop_frames():
    destop_dir = r"d:\KASSIA\DESTOP"
    pattern = os.path.join(destop_dir, "ezgif-frame-*.png")
    frame_files = sorted(glob.glob(pattern))
    print(f"Found {len(frame_files)} frames in {destop_dir}")
    
    cx, cy = 1160, 599
    modified_count = 0
    
    for fpath in frame_files:
        img = Image.open(fpath)
        arr = np.array(img)
        
        # Check if watermark is present at (cx, cy)
        # Compare center patch brightness with border
        crop_test = arr[cy-35:cy+35, cx-35:cx+35].mean(axis=2)
        c_val = crop_test[25:45, 25:45].mean()
        b_val = (crop_test[:10, :].mean() + crop_test[-10:, :].mean() + crop_test[:, :10].mean() + crop_test[:, -10:].mean()) / 4.0
        diff = c_val - b_val
        
        if diff > 10.0: # Watermark is present
            cleaned_arr = inpaint_wood_grain(arr, cx=cx, cy=cy)
            cleaned_img = Image.fromarray(cleaned_arr)
            cleaned_img.save(fpath, "PNG")
            modified_count += 1
            if modified_count % 20 == 0 or modified_count == 1:
                print(f"Cleaned {os.path.basename(fpath)} (diff={diff:.1f})")
                
    print(f"\nProcessing complete: Successfully removed diamond artifact from {modified_count} frames.")

if __name__ == "__main__":
    process_all_destop_frames()
