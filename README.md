# Cute Glossy iOS-Style App Icons

Easily generate any app icon you can imagine in the same playful, glossy, modern vibe as the reference images (cute characters, soft gradients, rounded squares, soft lighting).

These icons feature:
- Rounded square / squircle shape (iOS-style)
- Soft 3D / glossy plastic or claymorphism look
- Vibrant color gradients
- Cute, simple characters or faces (cats, ghosts, blobs, objects with expressions)
- Soft studio lighting with highlights
- Clean, readable at small sizes, no text

## Quick Start (Recommended)

### 1. Use Grok, ChatGPT, or any AI image generator
Copy a prompt from `prompts.md` or generate one with the script below, then paste it into:
- Grok (xAI) image generation
- ChatGPT with DALL-E / GPT-Image
- Midjourney, Flux, Recraft, etc.

### 2. Master Prompt Template
```
A cute glossy 3D app icon in modern iOS style, [YOUR SUBJECT HERE, e.g. a black cat face with big white eyes and a small smile], soft plastic/clay material with subtle specular highlights and soft shadows, vibrant [COLOR e.g. purple to pink] gradient background filling the entire rounded square, soft studio lighting from the top-left, centered composition, playful and minimal, high quality, no text, no border, no frame
```

Replace the parts in [brackets].

### 3. Python Prompt Generator
```bash
python generate_prompt.py
```
It will ask for your idea and print a ready-to-use prompt.

## Style Tips for Best Results
- Keep the subject simple and centered (one main character or object).
- Specify "soft plastic", "claymorphism", or "glossy 3D" for the material.
- Always mention "rounded square" or "iOS app icon style" and "no text".
- Use vibrant but soft gradients (purple, pink, orange, blue, etc.).
- Add "soft lighting", "specular highlights", "subtle shadows".
- Generate at high resolution (1024x1024 or higher), then crop/round if needed.

## Post-Processing (Optional)
If the AI generates a square image without rounded corners:
- Use any image editor or the simple Pillow script ideas in the code comments.
- Or just let the OS apply the mask on the home screen.

## Examples Matching the Vibe
See `prompts.md` for ready prompts inspired by the reference icons (black cat, ghost, chef face, rabbit, star, lock, etc.).

## Free Tools That Work Well
- Grok / xAI image gen
- ChatGPT
- Recraft.ai
- Superapp icon generators
- IconikAI
- Midjourney (use --ar 1:1 --s 200-400)

Enjoy creating endless icons in this style! Just describe what you want.
