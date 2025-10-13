#!/usr/bin/env python3
"""
Generate ALL images for the complete book:
- Cover page
- Chapter infographics
- End page
"""

from image_generator import GeminiImageGenerator, ImageValidator
from pathlib import Path
import time

API_KEY = "AIzaSyC15ewbSpMcboNAmMJhsj1dZmXA8l8yeGQ"

def main():
    print("\n" + "="*80)
    print("📚 GENERATING ALL BOOK IMAGES")
    print("="*80)

    generator = GeminiImageGenerator(API_KEY)
    validator = ImageValidator(API_KEY)

    images_generated = []
    images_failed = []

    # Create images directory
    Path("images/book").mkdir(parents=True, exist_ok=True)

    # ========================================================================
    # 1. COVER PAGE
    # ========================================================================
    print("\n\n" + "="*80)
    print("📖 GENERATING COVER PAGE")
    print("="*80)

    cover_path = generator.generate_cover_page(
        title="The Ultimate Guide to MCP, AI Agents, and Modern AI Development",
        subtitle="From Zero to OpenAI-Level Expertise",
        author="Shriyavallabh Pethkar",
        collaboration="in collaboration with Claude",
        output_path="images/book/cover.png"
    )

    if cover_path:
        validation = validator.validate_image(cover_path, "Professional book cover")
        if validation['valid']:
            images_generated.append(("Cover Page", cover_path, validation['score']))
            print(f"✅ Cover page generated successfully!")
        else:
            print(f"⚠️  Cover generated but validation failed (score: {validation['score']})")
            images_generated.append(("Cover Page", cover_path, validation['score']))
    else:
        images_failed.append("Cover Page")
        print(f"❌ Cover generation FAILED")

    time.sleep(2)  # Rate limiting

    # ========================================================================
    # 2. CHAPTER 1 INFOGRAPHICS
    # ========================================================================
    print("\n\n" + "="*80)
    print("📊 CHAPTER 1: Introduction to Programming and Python")
    print("="*80)

    chapter1_images = [
        {
            "concept": "What is Programming?",
            "description": "Programming is giving explicit step-by-step instructions to a computer. Like a recipe for a robot. Show: Human writes code → Computer executes → Output produced. Visual: flowchart style.",
            "filename": "ch1_what_is_programming.png"
        },
        {
            "concept": "Python Ecosystem",
            "description": "Python's role in AI: Shows Python at center, connected to TensorFlow, PyTorch, LangChain, scikit-learn, and other AI libraries. Demonstrates why Python dominates AI development.",
            "filename": "ch1_python_ecosystem.png"
        },
        {
            "concept": "Your First Program Flow",
            "description": "Step-by-step flow of print('Hello World'): 1. Python reads code 2. Recognizes print function 3. Executes with argument 4. Outputs to screen. Show each step visually with arrows.",
            "filename": "ch1_first_program_flow.png"
        }
    ]

    for img_spec in chapter1_images:
        print(f"\n🎨 Generating: {img_spec['concept']}")

        path = generator.generate_chapter_infographic(
            chapter_number=1,
            chapter_title="Introduction to Programming and Python",
            concept=img_spec['concept'],
            description=img_spec['description'],
            output_path=f"images/book/{img_spec['filename']}"
        )

        if path:
            validation = validator.validate_image(path, img_spec['concept'])
            images_generated.append((f"Ch1: {img_spec['concept']}", path, validation['score']))
            print(f"✅ Generated: {img_spec['concept']}")
        else:
            images_failed.append(f"Ch1: {img_spec['concept']}")
            print(f"❌ Failed: {img_spec['concept']}")

        time.sleep(2)  # Rate limiting

    # ========================================================================
    # 3. CHAPTER 2 INFOGRAPHICS
    # ========================================================================
    print("\n\n" + "="*80)
    print("📊 CHAPTER 2: Variables and Data Types")
    print("="*80)

    chapter2_images = [
        {
            "concept": "Variables as References",
            "description": "Visual showing: Variable (label) → Arrow → Object in memory. NOT a box containing value. Show x = 5 as: 'x' label pointing to '5' object. Demonstrate that variables are pointers/references.",
            "filename": "ch2_variables_references.png"
        },
        {
            "concept": "Python Data Types Overview",
            "description": "Show all Python basic types in a visual chart: int (42), float (3.14), str ('hello'), bool (True/False), None. Use icons and examples for each. Color-coded by type category.",
            "filename": "ch2_data_types.png"
        },
        {
            "concept": "Type Conversion Flow",
            "description": "Show conversion between types: str '5' → int(5) → float 5.0. Display with arrows and transformation boxes. Include common conversions and when they're needed (e.g., input() returns string).",
            "filename": "ch2_type_conversion.png"
        }
    ]

    for img_spec in chapter2_images:
        print(f"\n🎨 Generating: {img_spec['concept']}")

        path = generator.generate_chapter_infographic(
            chapter_number=2,
            chapter_title="Variables and Data Types",
            concept=img_spec['concept'],
            description=img_spec['description'],
            output_path=f"images/book/{img_spec['filename']}"
        )

        if path:
            validation = validator.validate_image(path, img_spec['concept'])
            images_generated.append((f"Ch2: {img_spec['concept']}", path, validation['score']))
            print(f"✅ Generated: {img_spec['concept']}")
        else:
            images_failed.append(f"Ch2: {img_spec['concept']}")
            print(f"❌ Failed: {img_spec['concept']}")

        time.sleep(2)

    # ========================================================================
    # 4. CHAPTER 3 INFOGRAPHIC
    # ========================================================================
    print("\n\n" + "="*80)
    print("📊 CHAPTER 3: Data Structures")
    print("="*80)

    chapter3_images = [
        {
            "concept": "Python Collections Overview",
            "description": "Show 4 main collection types: List [1,2,3] - ordered, mutable; Tuple (1,2,3) - ordered, immutable; Dict {'key':'value'} - key-value pairs; Set {1,2,3} - unique values. Visual comparison chart.",
            "filename": "ch3_collections_overview.png"
        },
        {
            "concept": "List Operations Visual",
            "description": "Show common list operations: append(), insert(), remove(), indexing [0], slicing [1:3]. Display with before/after states and visual arrows showing what each operation does.",
            "filename": "ch3_list_operations.png"
        }
    ]

    for img_spec in chapter3_images:
        print(f"\n🎨 Generating: {img_spec['concept']}")

        path = generator.generate_chapter_infographic(
            chapter_number=3,
            chapter_title="Data Structures",
            concept=img_spec['concept'],
            description=img_spec['description'],
            output_path=f"images/book/{img_spec['filename']}"
        )

        if path:
            validation = validator.validate_image(path, img_spec['concept'])
            images_generated.append((f"Ch3: {img_spec['concept']}", path, validation['score']))
            print(f"✅ Generated: {img_spec['concept']}")
        else:
            images_failed.append(f"Ch3: {img_spec['concept']}")
            print(f"❌ Failed: {img_spec['concept']}")

        time.sleep(2)

    # ========================================================================
    # 5. END PAGE
    # ========================================================================
    print("\n\n" + "="*80)
    print("📄 GENERATING END PAGE")
    print("="*80)

    end_path = generator.generate_end_page(
        author="Shriyavallabh Pethkar",
        collaboration="in collaboration with Claude",
        output_path="images/book/end_page.png"
    )

    if end_path:
        validation = validator.validate_image(end_path, "Professional end page with credits")
        images_generated.append(("End Page", end_path, validation['score']))
        print(f"✅ End page generated!")
    else:
        images_failed.append("End Page")
        print(f"❌ End page generation FAILED")

    # ========================================================================
    # FINAL REPORT
    # ========================================================================
    print("\n\n" + "="*80)
    print("📊 FINAL REPORT")
    print("="*80)

    print(f"\n✅ Successfully generated: {len(images_generated)} images")
    for name, path, score in images_generated:
        print(f"   • {name}: {path} (score: {score}/10)")

    if images_failed:
        print(f"\n❌ Failed to generate: {len(images_failed)} images")
        for name in images_failed:
            print(f"   • {name}")

    print(f"\n📁 All images saved in: images/book/")
    print(f"🎉 Image generation complete!")
    print("="*80)


if __name__ == "__main__":
    main()
