#!/usr/bin/env python3
"""
Simple prompt generator for cute glossy iOS-style app icons.
Run this script, describe your icon, and get a ready-to-use prompt.
"""

def generate_prompt(subject: str, color: str = "vibrant purple to pink") -> str:
    template = (
        "A cute glossy 3D app icon in modern iOS style, "
        f"{subject}, "
        "soft plastic/clay material with subtle specular highlights and soft shadows, "
        f"vibrant {color} gradient background filling the entire rounded square, "
        "soft studio lighting from the top-left, centered composition, "
        "playful and minimal, high quality, no text, no border, no frame"
    )
    return template

def main():
    print("=== Cute Glossy iOS App Icon Prompt Generator ===\n")
    subject = input("Describe your icon subject (e.g. 'a black cat with big white eyes and a smile'): ").strip()
    if not subject:
        subject = "a cute character with big eyes and a smile"
    
    color = input("Color/gradient (press Enter for default purple-pink): ").strip()
    if not color:
        color = "vibrant purple to pink"
    
    prompt = generate_prompt(subject, color)
    print("\n" + "="*60)
    print("YOUR PROMPT:")
    print("="*60)
    print(prompt)
    print("="*60)
    print("\nCopy the above into Grok, ChatGPT, Midjourney, or any AI image generator!")
    print("For Midjourney, you can add: --ar 1:1 --s 250 --no text")

if __name__ == "__main__":
    main()
