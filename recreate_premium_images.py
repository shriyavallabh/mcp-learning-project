#!/usr/bin/env python3
"""
Recreate ALL images with PREMIUM PROFESSIONAL quality
Based on IBM Design Language, Google Material Design, and top tech book standards
"""

from image_generator import GeminiImageGenerator, ImageValidator
from pathlib import Path
import time

API_KEY = "AIzaSyC15ewbSpMcboNAmMJhsj1dZmXA8l8yeGQ"

def recreate_premium_images():
    """Recreate all images with million-dollar job quality"""

    print("\n" + "="*80)
    print("🎨 RECREATING ALL IMAGES - PREMIUM PROFESSIONAL QUALITY")
    print("="*80)
    print("\nBased on:")
    print("  • IBM Design Language technical diagrams")
    print("  • Google Material Design principles")
    print("  • Top tech company (FAANG) book standards")
    print("  • Alex Xu 'System Design Interview' quality")
    print("  • Martin Kleppmann 'Designing Data-Intensive Applications' quality")
    print("="*80)

    generator = GeminiImageGenerator(API_KEY)
    validator = ImageValidator(API_KEY)

    # Create new images directory
    Path("images/premium").mkdir(parents=True, exist_ok=True)

    images_generated = []

    # ========================================================================
    # 1. PROFESSIONAL COVER PAGE - MILLION DOLLAR QUALITY
    # ========================================================================
    print("\n\n📖 COVER PAGE - Premium Professional Quality")
    print("-"*80)

    cover_prompt = """
Create an EXCEPTIONAL, WORLD-CLASS professional book cover worthy of a $200K+ tech job interview guide.

BOOK TITLE: "The Ultimate Guide to MCP, AI Agents, and Modern AI Development"
SUBTITLE: "From Zero to OpenAI-Level Expertise"
AUTHOR: Shriyavallabh Pethkar
COLLABORATION: "in collaboration with Claude"

DESIGN REQUIREMENTS (FOLLOW EXACTLY):

1. LAYOUT & COMPOSITION:
   - Clean, sophisticated, premium design
   - Title at top 1/3, large and bold
   - Subtitle below title, smaller but visible
   - Author name at bottom 1/4, prominent
   - "in collaboration with Claude" subtly placed near author

2. VISUAL STYLE (IBM/Google/Apple level):
   - Minimalist but powerful
   - Professional gradient background (dark blue to cyan)
   - Geometric patterns suggesting AI/neural networks (subtle, not cluttered)
   - Clean lines, modern aesthetic
   - NO cartoon elements, NO clipart

3. COLOR PALETTE (Premium tech):
   - Primary: Deep navy blue (#0A1929)
   - Secondary: Vibrant cyan (#00E5FF)
   - Accent: Electric purple (#7C4DFF)
   - Text: White on dark, perfect contrast
   - Gradient overlay for depth

4. TYPOGRAPHY (Critical):
   - Title: Ultra-bold, sans-serif, modern (like SF Pro Display or Inter)
   - Perfect kerning and spacing
   - Subtitle: Medium weight, clean
   - Author: Bold, professional
   - ALL text must be CRYSTAL CLEAR and readable

5. TECHNICAL ELEMENTS:
   - Abstract neural network nodes (clean dots connected by lines)
   - Code bracket symbols { } subtly integrated
   - Circuit board pattern (minimal, tasteful)
   - Data flow arrows (subtle, directional)
   - Layered depth with subtle shadows

6. QUALITY MARKERS:
   - Publication-ready, print quality
   - Similar to: O'Reilly's modern covers, No Starch Press, Packt Publishing premium editions
   - Looks like it costs $60-80 retail
   - Would impress FAANG hiring managers
   - Cover that says "million dollar career inside"

7. PROFESSIONAL STANDARDS:
   - No amateur elements
   - Perfect alignment
   - Balanced composition
   - Premium feel
   - Belongs on a bookshelf next to "Designing Data-Intensive Applications"

INSPIRATION: Think Google's technical documentation, Apple's developer guides, Microsoft's Azure architecture books.

Create a cover that makes people think: "This person knows their stuff. This book can change my career."
"""

    cover_path = generator.generate_image(
        prompt=cover_prompt,
        output_path="images/premium/cover.png",
        aspect_ratio="3:4",
        style="cover"
    )

    if cover_path:
        validation = validator.validate_image(cover_path, "Premium professional book cover - world-class quality")
        images_generated.append(("Premium Cover", cover_path, validation['score']))
        print(f"✅ Premium cover created! (Score: {validation['score']}/10)")
        time.sleep(3)

    # ========================================================================
    # 2. CHAPTER 1 - PREMIUM INFOGRAPHICS
    # ========================================================================
    print("\n\n📊 CHAPTER 1 INFOGRAPHICS - IBM Design Language Quality")
    print("-"*80)

    ch1_images = [
        {
            "concept": "What is Programming",
            "prompt": """
Create a PROFESSIONAL TECHNICAL DIAGRAM explaining "What is Programming" - IBM Design Language quality.

CONCEPT: Programming as giving step-by-step instructions to computers

DIAGRAM STRUCTURE (Clean & Professional):

1. LEFT SIDE - Human Intent:
   - Icon: Human figure (minimal, line art)
   - Label: "HUMAN" (clean sans-serif)
   - Text below: "Has an idea/problem to solve"

2. CENTER - The Code:
   - Icon: Code window with sample code snippet
   - Show: print("Hello World") or similar simple code
   - Label: "PROGRAMMING"
   - Subtext: "Translation to computer instructions"
   - Use monospace font for code

3. RIGHT SIDE - Computer Execution:
   - Icon: Computer/processor (geometric, clean)
   - Label: "COMPUTER"
   - Text: "Executes instructions precisely"

4. FLOW:
   - Professional arrows connecting stages (→)
   - Numbered steps (1, 2, 3)
   - Clean bezier curves or straight lines
   - Consistent arrow style

DESIGN SPECIFICATIONS:
- Style: IBM Design Language / Google Material Design
- Colors: Navy blue (#1565C0), cyan (#00BCD4), white/gray text
- Background: Subtle gradient (light to lighter)
- Fonts: Inter, SF Pro, or Roboto
- Icons: Minimal, geometric, professional
- Layout: Horizontal flow, left to right
- Spacing: Generous, not cramped
- Borders: Subtle, rounded corners
- NO: Cartoons, clipart, amateur graphics

QUALITY MARKERS:
- Could be in Google's technical documentation
- Clean enough for IBM whitepaper
- Professional enough for Microsoft Azure docs
- Clear, educational, sophisticated

OUTPUT: Horizontal infographic, landscape orientation, publication quality
""",
            "filename": "ch1_what_is_programming_PREMIUM.png"
        },
        {
            "concept": "Python Ecosystem",
            "prompt": """
Create a PROFESSIONAL ARCHITECTURE DIAGRAM showing Python's dominance in AI/ML - Enterprise quality.

CONCEPT: Python at the center connected to major AI/ML frameworks

DIAGRAM STRUCTURE:

1. CENTER - Python:
   - Large circle or hexagon
   - "PYTHON" text (bold)
   - Python logo if appropriate (or abstract representation)
   - Primary focal point

2. CONNECTED FRAMEWORKS (8-10 surrounding nodes):
   - TensorFlow (Google colors: orange/red)
   - PyTorch (Facebook/Meta: blue)
   - scikit-learn (yellow/orange)
   - LangChain (green)
   - LlamaIndex (purple)
   - Pandas (blue)
   - NumPy (blue)
   - Keras (red)

3. CONNECTIONS:
   - Clean lines from Python to each framework
   - Consistent line weight
   - Subtle directional arrows
   - Color-coded by category (ML/DL/NLP/Data)

4. CATEGORIES (Legend):
   - Deep Learning: One color group
   - Machine Learning: Another color
   - Data Processing: Third color
   - LLM/AI Agents: Fourth color

DESIGN SPECIFICATIONS:
- Style: Network diagram / Ecosystem visualization
- Colors: Professional tech palette (blues, greens, purples, subtle reds)
- Background: Clean white or very subtle gradient
- Fonts: Clean sans-serif throughout
- Icons: Framework logos OR clean geometric shapes
- Layout: Radial from center
- Lines: Subtle, professional
- Labels: Clear, readable

QUALITY MARKERS:
- Looks like AWS architecture diagrams
- Quality of Google Cloud Platform documentation
- Similar to Martin Kleppmann's book diagrams
- Could be in a $50,000 enterprise presentation

AVOID:
- Cluttered connections
- Too many colors
- Amateur spacing
- Unclear labels

OUTPUT: Square or landscape, professional architecture diagram quality
""",
            "filename": "ch1_python_ecosystem_PREMIUM.png"
        },
        {
            "concept": "First Program Execution Flow",
            "prompt": """
Create a PROFESSIONAL PROCESS FLOW DIAGRAM showing how Python executes print("Hello World") - Alex Xu quality.

CONCEPT: Step-by-step execution of your first Python program

DIAGRAM STRUCTURE (Vertical or Horizontal Flow):

STEP 1: Code Written
- Box: "CODE WRITTEN"
- Visual: print("Hello, World!") in code font
- Icon: Text editor symbol
- Color: Light blue

STEP 2: Python Interprets
- Box: "PYTHON INTERPRETER"
- Visual: Python parsing/reading
- Icon: Python logo or parser symbol
- Process: Lexical analysis, parsing
- Color: Medium blue

STEP 3: Recognizes Function
- Box: "FUNCTION RECOGNITION"
- Visual: Highlight print() function
- Icon: Function symbol f(x)
- Process: "Identifies built-in function"
- Color: Cyan

STEP 4: Executes
- Box: "EXECUTION"
- Visual: Function call with argument
- Icon: Gear/process icon
- Process: "Calls print with argument"
- Color: Green

STEP 5: Output
- Box: "OUTPUT"
- Visual: Terminal window showing: Hello, World!
- Icon: Terminal/console symbol
- Result: Display to screen
- Color: Success green

FLOW DESIGN:
- Arrows between each step (professional style)
- Numbered steps (1→2→3→4→5)
- Clean, consistent box styling
- Subtle shadows for depth
- Professional color progression

DESIGN SPECIFICATIONS:
- Style: Process flow / Sequence diagram quality
- Colors: Blue gradient (light to dark) then green for output
- Background: Clean white or subtle gray
- Fonts: Inter or SF Pro for text, Mono for code
- Icons: Minimal, line-style, professional
- Boxes: Rounded corners, subtle borders
- Layout: Top to bottom OR left to right
- Spacing: Generous, clear

QUALITY MARKERS:
- Level of "System Design Interview" book diagrams
- Professional flowchart quality
- Could be in Software Engineering textbook
- Clear enough for complete beginners
- Professional enough for advanced developers

OUTPUT: Professional process flow diagram, publication quality
""",
            "filename": "ch1_first_program_flow_PREMIUM.png"
        }
    ]

    for img_spec in ch1_images:
        print(f"\n🎨 Creating: {img_spec['concept']}")

        path = generator.generate_image(
            prompt=img_spec['prompt'],
            output_path=f"images/premium/{img_spec['filename']}",
            aspect_ratio="16:9",
            style="technical"
        )

        if path:
            validation = validator.validate_image(path, img_spec['concept'])
            images_generated.append((f"Ch1: {img_spec['concept']}", path, validation['score']))
            print(f"✅ Created: {img_spec['concept']} (Score: {validation['score']}/10)")
        else:
            print(f"❌ Failed: {img_spec['concept']}")

        time.sleep(3)

    # Continue with remaining chapters...
    print("\n" + "="*80)
    print(f"✅ PHASE 1 COMPLETE: {len(images_generated)} premium images created")
    print("="*80)

    return images_generated


if __name__ == "__main__":
    results = recreate_premium_images()
    print(f"\n🎉 Premium image recreation started!")
    print(f"📊 Images created so far: {len(results)}")
