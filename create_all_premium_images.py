#!/usr/bin/env python3
"""
Create ALL premium professional images for the book
Complete recreation with world-class quality
"""

from image_generator import GeminiImageGenerator, ImageValidator
from pathlib import Path
import time

API_KEY = "AIzaSyC15ewbSpMcboNAmMJhsj1dZmXA8l8yeGQ"

def create_all_premium_images():
    """Generate complete set of premium images"""

    generator = GeminiImageGenerator(API_KEY)
    validator = ImageValidator(API_KEY)

    Path("images/premium").mkdir(parents=True, exist_ok=True)

    all_images = []

    # All image specifications with PREMIUM prompts
    image_specs = [
        # Chapter 1 remaining image
        {
            "name": "Ch1: Program Flow",
            "prompt": """Professional flowchart: Python executes print("Hello World").

FLOW: [Code Written] → [Python Interprets] → [Recognizes print()] → [Executes] → [Output to Screen]

STYLE: Clean process diagram, IBM quality, blue gradient boxes, numbered steps, professional arrows, clear labels.
NO cluttered elements. Publication-grade quality like System Design Interview book.""",
            "file": "images/premium/ch1_program_flow.png",
            "aspect": "16:9"
        },

        # Chapter 2 images
        {
            "name": "Ch2: Variables as References",
            "prompt": """Professional technical diagram: Variables are References, NOT Containers.

DIAGRAM:
LEFT: Variable name "x" (label/pointer)
CENTER: Arrow pointing to →
RIGHT: Value "42" (object in memory)

Show: Variable is a LABEL pointing to value, not a box containing it.

STYLE: Clean, minimal, IBM/Google quality. Blue/cyan colors. Clear labels. Memory address notation. Professional typography. Like AWS architecture diagrams.""",
            "file": "images/premium/ch2_variables_references.png",
            "aspect": "16:9"
        },
        {
            "name": "Ch2: Data Types",
            "prompt": """Professional comparison chart: Python Data Types Overview.

SHOW 5 TYPES IN GRID:
1. int (42) - whole numbers
2. float (3.14) - decimals
3. str ("hello") - text
4. bool (True/False) - logical
5. None - null/nothing

Each with: Icon, Name, Example, Description

STYLE: Clean table/grid layout, color-coded by type, professional icons, clear typography. Google Material Design quality. Enterprise documentation level.""",
            "file": "images/premium/ch2_data_types.png",
            "aspect": "16:9"
        },
        {
            "name": "Ch2: Type Conversion",
            "prompt": """Professional flow diagram: Type Conversion between Python types.

SHOW CONVERSIONS:
str "5" → int() → int 5 → float() → float 5.0
With arrows and transformation boxes

Include: int(), float(), str(), bool() functions
Show: When and why conversions are needed

STYLE: Process flow quality, clean arrows, color progression (blue→green), professional boxes. System Design Interview book quality. Clear, educational.""",
            "file": "images/premium/ch2_type_conversion.png",
            "aspect": "16:9"
        },

        # Chapter 3 images
        {
            "name": "Ch3: Collections",
            "prompt": """Professional comparison diagram: Python's 4 Collection Types.

SHOW IN GRID:
1. List [1,2,3] - ordered, mutable
2. Tuple (1,2,3) - ordered, immutable
3. Dict {'key':'val'} - key-value pairs
4. Set {1,2,3} - unique values only

Each with: Visual, Properties, Use Cases

STYLE: Clean 2x2 or 1x4 layout, color-coded, professional icons, clear labels. IBM Design Language quality. Enterprise technical doc level.""",
            "file": "images/premium/ch3_collections.png",
            "aspect": "16:9"
        },
        {
            "name": "Ch3: List Operations",
            "prompt": """Professional reference diagram: Common List Operations in Python.

SHOW OPERATIONS WITH BEFORE/AFTER:
- append() - adds to end
- insert() - adds at index
- remove() - deletes value
- [index] - access element
- [start:end] - slicing

Each operation shown with example and visual

STYLE: Clean reference card, blue theme, monospace for code, clear arrows, professional layout. Google technical docs quality.""",
            "file": "images/premium/ch3_list_operations.png",
            "aspect": "16:9"
        },

        # End page
        {
            "name": "End Page",
            "prompt": """Professional book END PAGE design.

TEXT CONTENT:
"Thank you for reading!"
"The Ultimate Guide to AI Development"
Author: Shriyavallabh Pethkar
"in collaboration with Claude"

DESIGN: Minimalist, elegant, professional. Subtle tech theme. Clean typography. Matching book cover style (navy blue, cyan accents).

STYLE: Premium closing page worthy of $60 technical book. O'Reilly/No Starch quality.""",
            "file": "images/premium/end_page.png",
            "aspect": "3:4"
        }
    ]

    print("\n" + "="*80)
    print("🎨 CREATING COMPLETE SET OF PREMIUM IMAGES")
    print("="*80)

    for spec in image_specs:
        print(f"\n📊 Generating: {spec['name']}")

        path = generator.generate_image(
            prompt=spec['prompt'],
            output_path=spec['file'],
            aspect_ratio=spec['aspect'],
            style="technical" if "Ch" in spec['name'] else "professional"
        )

        if path:
            validation = validator.validate_image(path, spec['name'])
            all_images.append((spec['name'], path, validation['score']))
            print(f"   ✅ Score: {validation['score']}/10")
        else:
            print(f"   ❌ Failed")

        time.sleep(2)  # Rate limiting

    print("\n" + "="*80)
    print("📊 GENERATION COMPLETE")
    print("="*80)
    print(f"\n✅ Total images: {len(all_images)}")
    for name, path, score in all_images:
        print(f"   • {name}: {Path(path).name} (score: {score}/10)")

    return all_images


if __name__ == "__main__":
    results = create_all_premium_images()
    print(f"\n🎉 Complete! Generated {len(results)} premium images")
