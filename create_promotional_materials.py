#!/usr/bin/env python3
"""
Create promotional materials for the book:
- Social media graphics
- Book preview images
- Marketing materials
"""

from image_generator import GeminiImageGenerator
from pathlib import Path
import time

API_KEY = "AIzaSyC15ewbSpMcboNAmMJhsj1dZmXA8l8yeGQ"

def create_promotional_materials():
    """Generate promotional graphics for the book"""

    print("\n" + "="*80)
    print("📣 CREATING PROMOTIONAL MATERIALS")
    print("="*80)

    generator = GeminiImageGenerator(API_KEY)

    # Create promotional directory
    Path("images/promotional").mkdir(parents=True, exist_ok=True)

    promotional_images = []

    # ========================================================================
    # 1. SOCIAL MEDIA COVER (Square - for Instagram/Facebook)
    # ========================================================================
    print("\n📱 Generating social media cover (square)...")

    social_square = generator.generate_image(
        prompt="""
Create a STUNNING social media post graphic for a new programming book launch:

BOOK: "The Ultimate Guide to MCP, AI Agents, and Modern AI Development"
AUTHOR: Shriyavallabh Pethkar
TAGLINE: "From Zero to OpenAI-Level Expertise"

DESIGN FOR: Instagram/Facebook square post (1:1)

ELEMENTS TO INCLUDE:
- Eye-catching "NEW BOOK LAUNCH!" text at top
- Book title (bold, prominent)
- Author name
- Tagline
- Visual elements: AI/tech themed (circuits, code, neural networks)
- "Available Now!" badge
- Professional yet exciting design
- Color scheme: Blues, purples, cyan (tech colors)
- Modern, clean, shareable

Style: Exciting book launch announcement that makes people want to learn more!
Make it pop on social media feeds!
""",
        output_path="images/promotional/social_media_square.png",
        aspect_ratio="1:1",
        style="professional"
    )

    if social_square:
        promotional_images.append(("Social Media Square", social_square))
        print("✅ Social media square created!")

    time.sleep(2)

    # ========================================================================
    # 2. TWITTER/X HEADER (Wide banner)
    # ========================================================================
    print("\n🐦 Generating Twitter/X header...")

    twitter_header = generator.generate_image(
        prompt="""
Create a professional Twitter/X header banner for a technical book author:

AUTHOR: Shriyavallabh Pethkar
BOOK: "The Ultimate Guide to MCP, AI Agents, and Modern AI Development"
TAGLINE: "Teaching AI Development | Author | Python Expert"

DESIGN FOR: Twitter/X header (3:1 wide banner)

ELEMENTS:
- Professional, tech-themed background
- Author name (Shriyavallabh Pethkar) prominently displayed
- Book title or subtle book cover mockup
- Tagline about AI/Python expertise
- Modern, professional aesthetic
- Tech motifs: circuits, code snippets, AI symbols
- Color scheme: Professional blues and purples
- Clean, minimalist but impressive

Style: Professional author branding that establishes expertise and credibility.
""",
        output_path="images/promotional/twitter_header.png",
        aspect_ratio="3:1",
        style="professional"
    )

    if twitter_header:
        promotional_images.append(("Twitter Header", twitter_header))
        print("✅ Twitter header created!")

    time.sleep(2)

    # ========================================================================
    # 3. BOOK PREVIEW TEASER
    # ========================================================================
    print("\n👀 Generating book preview teaser...")

    preview_teaser = generator.generate_image(
        prompt="""
Create an exciting BOOK PREVIEW teaser graphic:

Show an open book with sample content visible, creating curiosity:

BOOK: "The Ultimate Guide to AI Development"
AUTHOR: Shriyavallabh Pethkar

DESIGN ELEMENTS:
- 3D or illustrated open book showing pages
- Visible content on pages: code snippets, diagrams, text (readable but artistic)
- "PREVIEW" or "SNEAK PEEK" text overlay
- Professional yet intriguing design
- Tech theme: AI, programming, Python
- Lighting effects to make it pop
- Color scheme: Blues, purples, white pages
- Portrait or square orientation

Make people CURIOUS about the book content!
Show quality and professionalism.
""",
        output_path="images/promotional/book_preview_teaser.png",
        aspect_ratio="3:4",
        style="professional"
    )

    if preview_teaser:
        promotional_images.append(("Book Preview Teaser", preview_teaser))
        print("✅ Book preview teaser created!")

    time.sleep(2)

    # ========================================================================
    # 4. TESTIMONIAL TEMPLATE
    # ========================================================================
    print("\n💬 Generating testimonial template...")

    testimonial_template = generator.generate_image(
        prompt="""
Create a TESTIMONIAL graphic template for book reviews:

BOOK: "The Ultimate Guide to AI Development"
AUTHOR: Shriyavallabh Pethkar

DESIGN FOR: Sharing positive reviews and testimonials

ELEMENTS:
- Space for a quote/testimonial text (center focus)
- Quotation marks (large, stylish)
- Book title at top or bottom
- Author name
- "Reader Review" or "What Readers Say" heading
- Professional background
- Tech-themed but clean design
- Color scheme: Professional blues with white text area
- Room for 2-3 sentences of testimonial text

Style: Professional testimonial card that looks shareable and credible.
Make it easy to add text over later.
""",
        output_path="images/promotional/testimonial_template.png",
        aspect_ratio="1:1",
        style="professional"
    )

    if testimonial_template:
        promotional_images.append(("Testimonial Template", testimonial_template))
        print("✅ Testimonial template created!")

    time.sleep(2)

    # ========================================================================
    # 5. "WHAT YOU'LL LEARN" INFOGRAPHIC
    # ========================================================================
    print("\n📚 Generating 'What You'll Learn' infographic...")

    learning_outcomes = generator.generate_image(
        prompt="""
Create an educational "WHAT YOU'LL LEARN" infographic for book marketing:

BOOK: "The Ultimate Guide to AI Development"

SHOW LEARNING OUTCOMES:
- Python Programming from Scratch
- AI & Machine Learning Fundamentals
- MCP Protocol Mastery
- Building AI Agents
- LangChain & LangGraph
- Production Deployment
- Real-World Projects

DESIGN:
- Title: "What You'll Learn"
- 6-8 key learning outcomes as visual list
- Icons or symbols for each topic
- Checkmarks or progress indicators
- Professional, exciting design
- Tech color scheme (blues, purples, greens)
- Vertical or square layout
- Clear, readable typography

Make it showcase the VALUE of the book!
Show the transformation: "Zero to Expert"
""",
        output_path="images/promotional/what_you_will_learn.png",
        aspect_ratio="3:4",
        style="professional"
    )

    if learning_outcomes:
        promotional_images.append(("What You'll Learn", learning_outcomes))
        print("✅ Learning outcomes infographic created!")

    time.sleep(2)

    # ========================================================================
    # 6. AUTHOR PROFILE IMAGE
    # ========================================================================
    print("\n👤 Generating author branding graphic...")

    author_profile = generator.generate_image(
        prompt="""
Create a professional AUTHOR BRANDING graphic:

AUTHOR: Shriyavallabh Pethkar
TITLE: "AI Development Expert & Technical Author"
BOOK: "The Ultimate Guide to AI Development"

DESIGN ELEMENTS:
- Professional tech-themed background
- Author name (large, prominent): "Shriyavallabh Pethkar"
- Title/credentials below name
- "Author of [book title]" text
- Tech motifs: AI symbols, code elements, circuit patterns
- Professional color scheme: Blues, purples, white text
- Modern, clean design
- Square or portrait orientation
- Could include silhouette or abstract representation

Style: Establishes authority and expertise in AI/tech space.
Professional branding for author platforms (LinkedIn, website, etc.)
""",
        output_path="images/promotional/author_branding.png",
        aspect_ratio="1:1",
        style="professional"
    )

    if author_profile:
        promotional_images.append(("Author Branding", author_profile))
        print("✅ Author branding graphic created!")

    time.sleep(2)

    # ========================================================================
    # 7. BOOK LAUNCH ANNOUNCEMENT
    # ========================================================================
    print("\n🚀 Generating launch announcement...")

    launch_announcement = generator.generate_image(
        prompt="""
Create an EXCITING book launch announcement graphic:

"NOW AVAILABLE!"

BOOK: "The Ultimate Guide to MCP, AI Agents, and Modern AI Development"
AUTHOR: Shriyavallabh Pethkar
SUBTITLE: "From Zero to OpenAI-Level Expertise"

DESIGN:
- Bold "NOW AVAILABLE!" or "JUST LAUNCHED!" text
- Book title (large, impactful)
- Author name
- Subtitle
- "Get Your Copy Today!" call-to-action
- Celebratory elements: burst rays, sparkles, excitement
- Professional but energetic design
- Tech-themed colors: blues, purples, cyan
- Modern typography
- Portrait or square orientation

Make it EXCITING and shareable!
This is the BIG announcement!
Create FOMO and excitement!
""",
        output_path="images/promotional/launch_announcement.png",
        aspect_ratio="3:4",
        style="professional"
    )

    if launch_announcement:
        promotional_images.append(("Launch Announcement", launch_announcement))
        print("✅ Launch announcement created!")

    time.sleep(2)

    # ========================================================================
    # 8. CHAPTER HIGHLIGHT TEASER
    # ========================================================================
    print("\n📖 Generating chapter highlight teaser...")

    chapter_highlight = generator.generate_image(
        prompt="""
Create a CHAPTER HIGHLIGHT teaser graphic for social media:

FROM: "The Ultimate Guide to AI Development"
CHAPTER: "Chapter 2: Variables and Data Types"
KEY CONCEPT: "Variables are References, Not Boxes"

DESIGN:
- "Inside the Book" or "Chapter Highlight" header
- Chapter number and title
- Key concept or learning point
- Small code snippet or diagram snippet (artistic, not fully detailed)
- "Learn more in the book" call-to-action
- Book title at bottom
- Tech-themed design
- Professional colors
- Square or portrait layout

Purpose: Give a taste of the book content to create interest!
Show the quality and depth of teaching.
""",
        output_path="images/promotional/chapter_highlight.png",
        aspect_ratio="1:1",
        style="professional"
    )

    if chapter_highlight:
        promotional_images.append(("Chapter Highlight", chapter_highlight))
        print("✅ Chapter highlight created!")

    # ========================================================================
    # FINAL REPORT
    # ========================================================================
    print("\n\n" + "="*80)
    print("📊 PROMOTIONAL MATERIALS REPORT")
    print("="*80)

    print(f"\n✅ Created {len(promotional_images)} promotional graphics:")
    for name, path in promotional_images:
        print(f"   • {name}: {path}")

    print(f"\n📁 All promotional materials in: images/promotional/")
    print(f"\n💡 USE THESE FOR:")
    print(f"   • Social media posts (Instagram, Facebook, Twitter)")
    print(f"   • Book launch announcements")
    print(f"   • Author branding (LinkedIn, website)")
    print(f"   • Marketing campaigns")
    print(f"   • Email newsletters")
    print(f"   • Blog posts")
    print(f"   • Amazon KDP promotional graphics")

    print("\n" + "="*80)
    print("🎉 PROMOTIONAL MATERIALS COMPLETE!")
    print("="*80)


if __name__ == "__main__":
    create_promotional_materials()
