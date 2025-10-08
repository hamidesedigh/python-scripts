# -*- coding: utf-8 -*-
"""
@author: Hamideh
@created: Wed Jul 2 06:28:53 2025

Program Description:
-------------------------
Demonstration of Basic Image Processing with Pillow (PIL)
--------------------------------------------------------------
Covers:
✔ Open, show, and inspect image attributes
✔ Rotate, crop, paste, and save images
✔ Pixel manipulation with getpixel() and putpixel()
✔ Add transparency (alpha channel)
✔ Simple steganography-like pixel encoding demo

Requirements:
-------------
pip install pillow
"""

from PIL import Image

# ============================================================
# --- Step 1: Load and Inspect Image ---
# ============================================================

img = Image.open("test.png")
print("✅ Image loaded successfully.")
print("Format:", img.format)
print("Size:", img.size)
print("Mode:", img.mode)
print("Filename:", img.filename)
print("Info:", img.info)

# Show image (uncomment if running locally)
# img.show()

# ============================================================
# --- Step 2: Rotate, Crop, Paste, and Save ---
# ============================================================

# Rotate the image 90° counter-clockwise (use negative for clockwise)
rotated = img.rotate(-90)
print("\nRotated image size:", rotated.size)

# Crop region: (left, top, right, bottom)
crop_box = (100, 0, 200, 100)
tile = rotated.crop(crop_box)

# Paste the cropped region into the top-left corner
rotated.paste(tile, (0, 0))
rotated.save("modified_test.png")
print("✅ Rotated and cropped image saved as 'modified_test.png'")

# ============================================================
# --- Step 3: Manipulate Pixels ---
# ============================================================

img_stra = Image.open("strawberry.jpg")
print("\nLoaded image:", img_stra.filename)
print("Pixel at (100,100):", img_stra.getpixel((100, 100)))

# Change one pixel (R, G, B)
img_stra.putpixel((100, 100), (255, 0, 0))  # red pixel
print("Modified pixel at (100,100):", img_stra.getpixel((100, 100)))

# Draw a small blue square (10×10) starting from (100,100)
for i in range(10):
    for j in range(10):
        img_stra.putpixel((100 + i, 100 + j), (0, 0, 255))

img_stra.show()

# ============================================================
# --- Step 4: Add Alpha Channel (Transparency) ---
# ============================================================

img_stra = img_stra.convert("RGBA")  # Ensure has alpha channel
img_stra.putalpha(255)  # Fully opaque
print("✅ Alpha channel added.")

# ============================================================
# --- Step 5: Simple Pixel Encoding (Character-to-Pixel Demo) ---
# ============================================================

msg = "Hamideh is cool!"

# Encode message letters into pixel blue channel (ASCII)
for i in range(0, img_stra.size[0], 10):
    for j in range(0, img_stra.size[1], 10):
        char_index = (i + j) // 10 % len(msg)
        img_stra.putpixel((i, j), (0, 0, ord(msg[char_index])))

# Save result
img_stra.save("encoded_strawberry.png")
print("✅ Encoded message saved in 'encoded_strawberry.png'.")

# ============================================================
# --- Quick Summary ---
# ============================================================
"""
Quick Summary:
--------------
✔ Image.open(path) → Load an image.
✔ img.format, img.size, img.mode → Inspect metadata.
✔ img.rotate(angle) → Rotate image.
✔ img.crop(box) → Extract region (left, top, right, bottom).
✔ img.paste(region, position) → Paste one image into another.
✔ img.getpixel(xy) / img.putpixel(xy, color) → Read/write pixels.
✔ img.convert("RGBA") / putalpha() → Add transparency.
✔ img.save(path) → Save image to file.

Bonus:
- You can use pixel operations for artistic effects or basic steganography.
"""

print("\n✅ Image processing demonstration completed successfully.")
