import os
from skimage import io
import numpy as np
 
input_dir = "stable\output\inference_patches"
output_dir = "\stable\output/inference_png"
os.makedirs(output_dir, exist_ok=True)
 
for f in os.listdir(input_dir):
    if f.endswith(".tif"):
        img = io.imread(os.path.join(input_dir, f))
        img = (img - img.min()) / (img.max() - img.min() + 1e-7)
        img = (img * 255).astype(np.uint8)
        io.imsave(os.path.join(output_dir, f.replace(".tif", ".png")), img)
        print(f"Converted {f}")
