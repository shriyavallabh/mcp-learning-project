#!/usr/bin/env python3
"""
Generate ALL premium images sequentially - DO NOT STOP until complete
With retries, proper waiting, and error handling
"""

from image_generator import GeminiImageGenerator, ImageValidator
from pathlib import Path
import time
import sys

API_KEY = "AIzaSyC15ewbSpMcboNAmMJhsj1dZmXA8l8yeGQ"

def generate_with_retry(generator, prompt, path, aspect, max_retries=5):
    """Generate image with retry logic"""

    for attempt in range(max_retries):
        try:
            print(f"      Attempt {attempt + 1}/{max_retries}...")
            result = generator.generate_image(prompt, path, aspect, "technical")

            if result:
                print(f"      ✅ SUCCESS on attempt {attempt + 1}")
                return result
            else:
                print(f"      ⚠️  No result on attempt {attempt + 1}")

        except Exception as e:
            print(f"      ❌ Error on attempt {attempt + 1}: {e}")

        if attempt < max_retries - 1:
            wait_time = (attempt + 1) * 5  # Increasing wait time
            print(f"      ⏳ Waiting {wait_time} seconds before retry...")
            time.sleep(wait_time)

    print(f"      ❌ FAILED after {max_retries} attempts")
    return None


def main():
    print("\n" + "="*80)
    print("🎨 GENERATING ALL PREMIUM IMAGES SEQUENTIALLY")
    print("   DO NOT STOP UNTIL COMPLETE!")
    print("="*80)

    generator = GeminiImageGenerator(API_KEY)
    validator = ImageValidator(API_KEY)

    Path("images/premium").mkdir(parents=True, exist_ok=True)

    # Complete list of ALL images needed
    all_images = [
        {
            "num": 1,
            "name": "Premium Cover Page",
            "prompt": """WORLD-CLASS professional book cover - FAANG interview guide quality.

TITLE: "The Ultimate Guide to MCP, AI Agents, and Modern AI Development"
SUBTITLE: "From Zero to OpenAI-Level Expertise"
AUTHOR: Shriyavallabh Pethkar
COLLABORATION: "in collaboration with Claude"

DESIGN: Minimalist premium, dark blue to cyan gradient, geometric AI patterns, bold modern typography, perfect alignment. IBM/Google/Apple level quality. NO cartoons.

Make it scream "$200K career inside" - Like O'Reilly modern covers, worth $60-80 retail.""",
            "file": "images/premium/cover_final.png",
            "aspect": "3:4"
        },
        {
            "num": 2,
            "name": "Ch1: What is Programming",
            "prompt": """Professional IBM-quality diagram: What is Programming

FLOW: [Human with idea] → [Writes Code: print("Hello")] → [Computer executes] → [Output: Hello]

STYLE: Clean horizontal flow, numbered steps (1→2→3→4), professional arrows, blue/cyan theme, minimal icons, perfect typography. IBM Design Language quality. NO clutter.""",
            "file": "images/premium/ch1_programming.png",
            "aspect": "16:9"
        },
        {
            "num": 3,
            "name": "Ch1: Python Ecosystem",
            "prompt": """Professional architecture diagram: Python's AI/ML Dominance

CENTER: Python (large circle)
CONNECTED: TensorFlow, PyTorch, scikit-learn, LangChain, Pandas, NumPy, Keras (8 nodes around center)

STYLE: Network/radial diagram, color-coded by category (DL/ML/Data), clean lines, professional labels, subtle arrows. AWS/Google Cloud architecture diagram quality.""",
            "file": "images/premium/ch1_ecosystem.png",
            "aspect": "16:9"
        },
        {
            "num": 4,
            "name": "Ch1: Program Execution Flow",
            "prompt": """Professional process flow: How Python executes print("Hello World")

STEPS (vertical or horizontal):
1. Code Written → 2. Python Interprets → 3. Recognizes print() → 4. Executes → 5. Output to Screen

STYLE: Clean flowchart, numbered boxes, professional arrows, blue gradient (light→dark→green), rounded corners, subtle shadows. System Design Interview book quality.""",
            "file": "images/premium/ch1_execution.png",
            "aspect": "16:9"
        },
        {
            "num": 5,
            "name": "Ch2: Variables as References",
            "prompt": """Professional technical diagram: Variables Are References NOT Containers

SHOW: Variable name "age" (label) → ARROW → Value 25 (object in memory box)
LABELS: "Variable (pointer)", "Memory address: 0x1234", "Value object"

STYLE: Clean, minimal, IBM quality, blue/cyan, clear typography, memory diagram style. Google technical docs level.""",
            "file": "images/premium/ch2_variables.png",
            "aspect": "16:9"
        },
        {
            "num": 6,
            "name": "Ch2: Python Data Types",
            "prompt": """Professional comparison grid: Python's 5 Basic Data Types

GRID (5 boxes):
1. int (42) - whole numbers - blue icon
2. float (3.14) - decimals - cyan icon
3. str ("text") - strings - green icon
4. bool (True) - logical - purple icon
5. None - null - gray icon

Each: Icon, Type Name, Example, One-line description

STYLE: Clean grid/table, color-coded, professional icons, excellent typography. Enterprise documentation quality.""",
            "file": "images/premium/ch2_types.png",
            "aspect": "16:9"
        },
        {
            "num": 7,
            "name": "Ch2: Type Conversion",
            "prompt": """Professional flow diagram: Type Conversion in Python

CONVERSIONS FLOW:
str "5" → int() → int 5 → float() → float 5.0 → str() → back to str "5.0"

Show transformation boxes with function names, arrows showing direction, color progression

STYLE: Process flow, professional boxes, clear arrows, color transitions (blue→green), clean labels. Alex Xu System Design quality.""",
            "file": "images/premium/ch2_conversion.png",
            "aspect": "16:9"
        },
        {
            "num": 8,
            "name": "Ch3: Python Collections",
            "prompt": """Professional comparison diagram: Python's 4 Collection Types

GRID (2x2 or horizontal 4):
1. LIST [1,2,3] - ordered, mutable, allows duplicates
2. TUPLE (1,2,3) - ordered, immutable, allows duplicates
3. DICT {'k':'v'} - key-value, mutable, unique keys
4. SET {1,2,3} - unordered, mutable, unique values only

Each: Visual example, Properties, When to use

STYLE: Professional grid, color-coded (blue/green/purple/orange), clear typography, visual examples. IBM Design quality.""",
            "file": "images/premium/ch3_collections.png",
            "aspect": "16:9"
        },
        {
            "num": 9,
            "name": "Ch3: List Operations",
            "prompt": """Professional reference card: Common List Operations

OPERATIONS (with before/after visuals):
- list.append(x) - adds to end
- list.insert(i, x) - inserts at index
- list.remove(x) - removes value
- list[i] - access by index
- list[a:b] - slicing

Show each with example: [1,2,3] → operation → result

STYLE: Clean reference layout, monospace for code, professional arrows, blue theme, clear labels. Google developer docs quality.""",
            "file": "images/premium/ch3_lists.png",
            "aspect": "16:9"
        },
        {
            "num": 10,
            "name": "Premium End Page",
            "prompt": """Professional book END PAGE - elegant conclusion

TEXT:
"Thank you for reading!"
"The Ultimate Guide to AI Development"
Author: Shriyavallabh Pethkar
"in collaboration with Claude"

DESIGN: Minimal, elegant, professional. Subtle tech elements (light circuit pattern). Clean typography. Navy blue background with cyan accents. Warm, professional, concluding tone.

QUALITY: Matches premium cover, belongs in $60 technical book, O'Reilly/No Starch level.""",
            "file": "images/premium/end_page_final.png",
            "aspect": "3:4"
        }
    ]

    successful = []
    failed = []

    total = len(all_images)

    for img_spec in all_images:
        num = img_spec['num']
        name = img_spec['name']

        print(f"\n{'='*80}")
        print(f"📊 IMAGE {num}/{total}: {name}")
        print(f"{'='*80}")

        # Check if already exists
        if Path(img_spec['file']).exists():
            file_size = Path(img_spec['file']).stat().st_size / 1024
            print(f"   ℹ️  File already exists ({file_size:.0f} KB)")
            print(f"   🔄 Regenerating to ensure quality...")

        print(f"   📝 Generating...")

        result = generate_with_retry(
            generator,
            img_spec['prompt'],
            img_spec['file'],
            img_spec['aspect'],
            max_retries=5
        )

        if result:
            # Validate
            print(f"   🔍 Validating...")
            validation = validator.validate_image(result, name)
            score = validation['score']

            print(f"   ✅ COMPLETE! Score: {score}/10")
            successful.append((num, name, result, score))

            # Wait between images
            print(f"   ⏳ Waiting 5 seconds before next image...")
            time.sleep(5)
        else:
            print(f"   ❌ FAILED after all retries")
            failed.append((num, name))
            # Even on failure, wait before next
            print(f"   ⏳ Waiting 10 seconds before next image...")
            time.sleep(10)

    # Final report
    print("\n\n" + "="*80)
    print("📊 FINAL GENERATION REPORT")
    print("="*80)

    print(f"\n✅ SUCCESSFUL: {len(successful)}/{total} images")
    for num, name, path, score in successful:
        print(f"   {num}. {name}")
        print(f"      File: {Path(path).name}")
        print(f"      Score: {score}/10")

    if failed:
        print(f"\n❌ FAILED: {len(failed)}/{total} images")
        for num, name in failed:
            print(f"   {num}. {name}")
    else:
        print(f"\n🎉 ALL IMAGES GENERATED SUCCESSFULLY!")

    print("\n" + "="*80)

    if len(successful) == total:
        print("✅ ✅ ✅  100% COMPLETE!  ✅ ✅ ✅")
        print("="*80)
        return True
    else:
        print(f"⚠️  {len(successful)}/{total} completed ({len(failed)} failed)")
        print("   You may need to regenerate failed images manually")
        print("="*80)
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
