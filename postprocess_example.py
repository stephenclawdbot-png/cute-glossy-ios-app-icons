#!/usr/bin/env python3
"""
Optional: Simple post-processing example using Pillow.
Takes a square image and adds rounded corners + a subtle gloss overlay.
Requires: pip install pillow
"""

from PIL import Image, ImageDraw, ImageFilter
import sys

def add_rounded_corners(im, radius=180):
    # Create mask for rounded corners
    mask = Image.new('L', im.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0, im.size[0], im.size[1]), radius=radius, fill=255)
    output = Image.new('RGBA', im.size)
    output.paste(im, (0, 0))
    output.putalpha(mask)
    return output

def add_subtle_gloss(im):
    # Very simple highlight overlay
    gloss = Image.new('RGBA', im.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(gloss)
    # Soft elliptical highlight at top
    draw.ellipse([im.size[0]*0.2, -im.size[1]*0.1, im.size[0]*0.8, im.size[1]*0.4], fill=(255, 255, 255, 40))
    gloss = gloss.filter(ImageFilter.GaussianBlur(radius=20))
    return Image.alpha_composite(im.convert('RGBA'), gloss)

def main(input_path, output_path):
    im = Image.open(input_path).convert('RGBA')
    # Resize to 1024 if needed
    if im.size != (1024, 1024):
        im = im.resize((1024, 1024), Image.Resampling.LANCZOS)
    rounded = add_rounded_corners(im, radius=220)
    final = add_subtle_gloss(rounded)
    final.save(output_path, 'PNG')
    print(f"Saved processed icon to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python postprocess_example.py input.png output.png")
    else:
        main(sys.argv[1], sys.argv[2])
