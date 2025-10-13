#!/usr/bin/env python3
"""
Create a complete marketing package with all materials organized
"""

import shutil
from pathlib import Path
import os

def create_marketing_package():
    """Organize all materials into a marketing package"""

    print("\n" + "="*80)
    print("📦 CREATING COMPLETE MARKETING PACKAGE")
    print("="*80)

    # Create marketing package directory
    package_dir = Path("MARKETING_PACKAGE")
    package_dir.mkdir(exist_ok=True)

    # Create subdirectories
    subdirs = {
        "book": "The main book file",
        "cover": "Cover and end page images",
        "infographics": "Educational diagrams from chapters",
        "promotional": "Social media and marketing graphics",
        "documentation": "README and guides"
    }

    for subdir, description in subdirs.items():
        (package_dir / subdir).mkdir(exist_ok=True)
        print(f"   📁 Created: {subdir}/ - {description}")

    print(f"\n📋 Organizing files...")

    # Copy main book
    if Path("The_Ultimate_AI_Development_Guide_FINAL.pdf").exists():
        shutil.copy(
            "The_Ultimate_AI_Development_Guide_FINAL.pdf",
            package_dir / "book" / "The_Ultimate_AI_Development_Guide_FINAL.pdf"
        )
        print(f"   ✅ Copied: Main book PDF")

    # Copy cover and end page
    cover_images = ["cover.png", "end_page.png"]
    for img in cover_images:
        src = Path(f"images/book/{img}")
        if src.exists():
            shutil.copy(src, package_dir / "cover" / img)
            print(f"   ✅ Copied: {img}")

    # Copy chapter infographics
    infographic_pattern = ["ch1_*.png", "ch2_*.png", "ch3_*.png"]
    infographic_count = 0
    for pattern in infographic_pattern:
        for img in Path("images/book").glob(pattern):
            shutil.copy(img, package_dir / "infographics" / img.name)
            infographic_count += 1
    print(f"   ✅ Copied: {infographic_count} chapter infographics")

    # Copy promotional materials
    promo_dir = Path("images/promotional")
    if promo_dir.exists():
        promo_count = 0
        for img in promo_dir.glob("*.png"):
            shutil.copy(img, package_dir / "promotional" / img.name)
            promo_count += 1
        print(f"   ✅ Copied: {promo_count} promotional graphics")

    # Create comprehensive README
    readme_content = """# The Ultimate AI Development Guide - Marketing Package

## 📚 Book Information

**Title:** The Ultimate Guide to MCP, AI Agents, and Modern AI Development
**Subtitle:** From Zero to OpenAI-Level Expertise
**Author:** Shriyavallabh Pethkar
**Collaboration:** in collaboration with Claude
**Format:** PDF, 12 MB
**Pages:** 200+ pages
**Images:** 10 professional infographics

---

## 📁 Package Contents

### 1. /book/
**The_Ultimate_AI_Development_Guide_FINAL.pdf** (12 MB)
- Complete publication-ready book
- Professional cover page
- 10 high-quality infographics
- Interactive exercises and quizzes
- Comprehensive Python + AI content

### 2. /cover/
- **cover.png** - Professional book cover
- **end_page.png** - Professional end page with credits

Use these for:
- Book listings (Amazon, Gumroad)
- Social media posts
- Website headers
- Promotional materials

### 3. /infographics/
Chapter 1 (3 images):
- ch1_what_is_programming.png
- ch1_python_ecosystem.png
- ch1_first_program_flow.png

Chapter 2 (3 images):
- ch2_variables_references.png
- ch2_data_types.png
- ch2_type_conversion.png

Chapter 3 (2 images):
- ch3_collections_overview.png
- ch3_list_operations.png

Use these for:
- Blog posts explaining concepts
- Social media educational content
- Course materials
- Presentations

### 4. /promotional/
- **social_media_square.png** - Instagram/Facebook post
- **book_preview_teaser.png** - Book preview graphic
- **testimonial_template.png** - For sharing reviews
- **what_you_will_learn.png** - Learning outcomes
- **author_branding.png** - Author profile graphic
- **launch_announcement.png** - Launch day announcement
- **chapter_highlight.png** - Content teaser

Use these for:
- Social media marketing campaigns
- Email newsletters
- Website promotional banners
- Paid advertising
- Author platform building

---

## 💰 Pricing Recommendations

### Digital PDF
- **Introductory Price:** $19.99
- **Standard Price:** $24.99 - $29.99
- **Premium Bundle:** $39.99 (with bonus materials)

### Print Version
- **Paperback:** $39.99 - $49.99
- **Hardcover:** $59.99 - $79.99

### Course Bundle
- **Book + Video Course:** $99.99 - $149.99

---

## 🚀 Launch Strategy

### Pre-Launch (2 weeks before)
1. **Week 1:**
   - Announce book on social media (use launch_announcement.png)
   - Build email list with "coming soon" landing page
   - Share chapter_highlight.png teasers
   - Engage with AI/Python communities

2. **Week 2:**
   - Share what_you_will_learn.png infographic
   - Post daily countdown
   - Offer early-bird discount
   - Build anticipation with preview content

### Launch Day
1. **Morning:** Post launch_announcement.png everywhere
2. **Afternoon:** Share social_media_square.png
3. **Evening:** Share author_branding.png with personal story

### Post-Launch (Ongoing)
1. **Week 1-2:**
   - Share testimonials (use testimonial_template.png)
   - Post infographics from book
   - Engage with readers
   - Ask for reviews

2. **Month 1-3:**
   - Weekly content using chapter infographics
   - Build author brand (author_branding.png)
   - Create video content
   - Host webinars/workshops

---

## 📱 Social Media Strategy

### Instagram
- Use: social_media_square.png, chapter_highlight.png
- Frequency: 3-4 posts per week
- Content: Educational + promotional mix
- Hashtags: #Python #AI #MachineLearning #ProgrammingBook #LearnToCode

### Twitter/X
- Use: All promotional graphics + infographics
- Frequency: 1-2 posts per day
- Content: Tips, quotes, chapter excerpts
- Engage with #100DaysOfCode community

### LinkedIn
- Use: author_branding.png, professional posts
- Frequency: 2-3 posts per week
- Content: Industry insights, book excerpts
- Target: Professionals, companies

### Facebook
- Use: social_media_square.png, what_you_will_learn.png
- Frequency: 3-4 posts per week
- Content: Mix of education and promotion
- Join programming groups

---

## 🌐 Publishing Platforms

### Amazon KDP (Kindle Direct Publishing)
- Upload main PDF
- Use cover.png for cover image
- Set up preview pages ("Look Inside")
- Enable both digital and print-on-demand
- Join KDP Select for wider reach

### Gumroad
- Direct sales platform
- Easy checkout process
- Built-in email delivery
- Great for digital products
- Lower fees than Amazon

### Your Own Website
- Full control over pricing
- Build email list
- Offer bundles
- Use all promotional materials

### Other Platforms
- Leanpub (technical books)
- Payhip (digital downloads)
- Teachable/Udemy (with course)

---

## 📧 Email Marketing

### Welcome Sequence (5 emails)
1. Thank you + download link
2. Getting started guide
3. Chapter 1 preview
4. Bonus tips
5. Ask for review

### Content Ideas
- Weekly Python tips (use infographics)
- Reader success stories
- New chapter previews
- Exclusive content
- Community updates

---

## 💬 Review Strategy

### Where to Get Reviews
1. Amazon (critical for visibility)
2. Goodreads
3. Programming subreddit communities
4. Python Discord/Slack channels
5. Twitter/LinkedIn testimonials

### How to Ask
- Email readers after 1 week
- Provide direct review links
- Make it easy (1-click)
- Offer incentive (bonus content)
- Use testimonial_template.png to share

---

## 🎯 Target Audience

### Primary
- College students learning programming
- Career switchers entering tech
- Self-taught programmers
- Bootcamp students
- AI/ML beginners

### Secondary
- Corporate training departments
- University instructors
- Online course creators
- Programming tutors
- Tech bootcamps

---

## 🏆 Competitive Advantages

1. **Publication Quality**
   - Professional cover design
   - High-quality infographics
   - Professional formatting

2. **Comprehensive Content**
   - Zero to expert progression
   - Extreme detail
   - No prior knowledge assumed

3. **Interactive Learning**
   - Hands-on exercises
   - Quizzes with answers
   - Coding challenges
   - Debug challenges

4. **Visual Learning**
   - 10 professional diagrams
   - Concept visualization
   - Flow charts
   - Visual metaphors

5. **Modern Topics**
   - MCP Protocol (cutting edge)
   - AI Agents
   - LangChain
   - Production deployment

---

## 📊 Success Metrics

### Month 1 Goals
- 100 copies sold
- 10 Amazon reviews
- 500 social media followers
- Email list: 200 subscribers

### Month 3 Goals
- 500 copies sold
- 30+ reviews (4.5+ star average)
- 2,000 social media followers
- Email list: 1,000 subscribers

### Month 6 Goals
- 1,000+ copies sold
- 50+ reviews
- 5,000 followers
- Established author brand

---

## 🛠️ Additional Resources Needed

### Nice to Have
1. Book trailer video (30-60 seconds)
2. Author interview/podcast appearances
3. Sample chapter PDF (free lead magnet)
4. Companion code repository
5. Private Discord/Slack community
6. Video course (upsell opportunity)

---

## 📞 Contact & Links

**Author:** Shriyavallabh Pethkar
**Email:** [Your email]
**Website:** [Your website]
**Twitter:** [Your handle]
**LinkedIn:** [Your profile]
**GitHub:** [Your repos]

---

## ✅ Launch Checklist

### Pre-Launch
- [ ] Finalize book formatting
- [ ] Get ISBN (if printing)
- [ ] Create Amazon KDP account
- [ ] Set up Gumroad store
- [ ] Build landing page
- [ ] Prepare email sequence
- [ ] Schedule social media posts
- [ ] Reach out to influencers
- [ ] Prepare press release
- [ ] Set pricing strategy

### Launch Day
- [ ] Publish on all platforms
- [ ] Send email announcement
- [ ] Post on all social media
- [ ] Share in relevant communities
- [ ] Update website
- [ ] Monitor sales/feedback
- [ ] Respond to comments
- [ ] Thank early buyers

### Post-Launch
- [ ] Follow up with buyers
- [ ] Request reviews
- [ ] Share testimonials
- [ ] Continue content marketing
- [ ] Analyze what's working
- [ ] Adjust strategy
- [ ] Plan next steps

---

## 🎉 You're Ready to Launch!

Everything you need is in this package. Good luck with your book launch!

**Remember:**
- Be consistent with marketing
- Engage with your audience
- Provide value first
- Build relationships
- Celebrate small wins
- Keep improving

---

*This marketing package was created with Claude Code on October 10, 2025*
"""

    # Write README
    with open(package_dir / "documentation" / "README.md", 'w') as f:
        f.write(readme_content)
    print(f"   ✅ Created: Comprehensive README")

    # Create quick reference guide
    quick_ref = """# Quick Reference - File Usage Guide

## Cover Images
- **cover.png** → Amazon KDP, website, social media headers
- **end_page.png** → Back matter, author page, credits

## Social Media Graphics
- **social_media_square.png** → Instagram/Facebook posts (1:1)
- **launch_announcement.png** → Launch day announcement
- **chapter_highlight.png** → Content teasers
- **what_you_will_learn.png** → Value proposition posts

## Author Branding
- **author_branding.png** → LinkedIn, Twitter profile, website
- Use consistently for brand recognition

## Promotional
- **book_preview_teaser.png** → Email campaigns, website
- **testimonial_template.png** → Share reviews and testimonials

## Infographics
All ch1_*, ch2_*, ch3_* images:
- Educational social media posts
- Blog content
- Pinterest pins
- Course materials

## Recommended Posting Schedule

### Week 1 (Launch)
- Monday: launch_announcement.png
- Wednesday: what_you_will_learn.png
- Friday: social_media_square.png

### Week 2-4 (Building Momentum)
- Mon/Wed/Fri: Rotate between chapter highlights and infographics
- Share one testimonial per week (using template)

### Ongoing
- 3-4 posts per week mixing education and promotion
- Use infographics for teaching moments
- Build authority with consistent author branding

---

**Pro Tip:** Schedule posts in advance using Buffer, Hootsuite, or Later!
"""

    with open(package_dir / "documentation" / "QUICK_REFERENCE.md", 'w') as f:
        f.write(quick_ref)
    print(f"   ✅ Created: Quick Reference Guide")

    # Create package manifest
    print(f"\n📊 Creating package manifest...")

    manifest = []
    for root, dirs, files in os.walk(package_dir):
        for file in files:
            file_path = Path(root) / file
            size = file_path.stat().st_size
            rel_path = file_path.relative_to(package_dir)
            manifest.append(f"{rel_path} ({size / 1024:.1f} KB)")

    with open(package_dir / "documentation" / "MANIFEST.txt", 'w') as f:
        f.write("MARKETING PACKAGE CONTENTS\n")
        f.write("=" * 50 + "\n\n")
        for item in sorted(manifest):
            f.write(f"{item}\n")
        f.write(f"\nTotal files: {len(manifest)}\n")

    print(f"   ✅ Created: Package manifest")

    # Final summary
    print("\n" + "="*80)
    print("🎉 MARKETING PACKAGE COMPLETE!")
    print("="*80)
    print(f"\n📦 Package location: {package_dir}/")
    print(f"\n📂 Package structure:")
    print(f"   ├── book/              Main book PDF")
    print(f"   ├── cover/             Cover and end page")
    print(f"   ├── infographics/      {infographic_count} educational diagrams")
    print(f"   ├── promotional/       {promo_count} marketing graphics")
    print(f"   └── documentation/     README, guides, manifest")

    print(f"\n💡 Everything you need to launch your book successfully!")
    print(f"\n📖 Read: MARKETING_PACKAGE/documentation/README.md for full guide")
    print(f"🚀 Read: MARKETING_PACKAGE/documentation/QUICK_REFERENCE.md for quick start")

    print("\n" + "="*80)
    print("✅ YOU'RE READY TO PUBLISH!")
    print("="*80)

    return package_dir


if __name__ == "__main__":
    package = create_marketing_package()
    print(f"\n🎁 Your complete marketing package: {package}")
