#!/usr/bin/env python3
"""Quick generation of remaining premium images"""

from image_generator import GeminiImageGenerator
from pathlib import Path
import time

API_KEY = "AIzaSyC15ewbSpMcboNAmMJhsj1dZmXA8l8yeGQ"

def main():
    gen = GeminiImageGenerator(API_KEY)
    Path("images/premium").mkdir(parents=True, exist_ok=True)

    # Remaining images with concise prompts
    remaining = [
        ("Ch2 Variables", "Professional diagram: Variable 'x' → arrow → value 5 in memory. Show variables as pointers. Clean IBM style, blue theme.", "images/premium/ch2_variables.png", "16:9"),
        ("Ch2 Types", "Grid showing Python types: int/float/str/bool/None with icons and examples. Professional, color-coded, clean layout.", "images/premium/ch2_types.png", "16:9"),
        ("Ch2 Conversion", "Flow: str→int→float with transformation boxes and arrows. Professional process diagram, blue gradient.", "images/premium/ch2_conversion.png", "16:9"),
        ("Ch3 Collections", "Grid: List/Tuple/Dict/Set with properties. Professional comparison chart, enterprise quality.", "images/premium/ch3_collections.png", "16:9"),
        ("Ch3 Lists", "Reference card: append/insert/remove/slice operations. Before/after examples, clean professional layout.", "images/premium/ch3_lists.png", "16:9"),
        ("End Page", "Elegant end page: 'Thank you!' Author: Shriyavallabh Pethkar, in collaboration with Claude. Minimal, professional.", "images/premium/end.png", "3:4"),
    ]

    for name, prompt, path, aspect in remaining:
        print(f"\n🎨 {name}...")
        result = gen.generate_image(prompt, path, aspect, "technical")
        print(f"   {'✅' if result else '❌'} {Path(path).name if result else 'Failed'}")
        time.sleep(2)

    print("\n✅ Done!")

if __name__ == "__main__":
    main()
