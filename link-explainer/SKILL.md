---
name: link-explainer
description: Transforms complex web articles into simple, animated HTML explanations for beginners. Use when user provides a URL and wants it explained in plain language with analogies, step-by-step breakdowns, and visual animations.
---

# Link Explainer Skill

This skill takes a web article URL, extracts its core content, simplifies it for beginners, and generates a beautiful animated HTML page with smooth transitions and card-based layouts.

## When to Use

- User provides a URL and asks to "explain this", "simplify this", "make this easy to understand"
- Content involves technical topics that need analogies and simple language
- User wants the explanation in a visual, animated format
- Target audience is a "beginner", "newbie", or "non-expert"

## Workflow

### Step 1: Extract Content from URL
Use `fetch_content.py` script to extract the main content from the provided URL.

```bash
python scripts/fetch_content.py <url>
```

This will output the article title, main sections, and key points.

### Step 2: Simplify Content
Use `simplify_content.py` script to transform the extracted content into beginner-friendly format.

```bash
python scripts/simplify_content.py <extracted_content.json>
```

This script:
- Identifies technical jargon and explains it in simple terms
- Generates real-life analogies for complex concepts
- Breaks down complex ideas into step-by-step explanations
- Creates summary cards for key concepts

### Step 3: Generate Animated HTML
Use `generate_html.py` script to create the final animated HTML page.

```bash
python scripts/generate_html.py <simplified_content.json>
```

This generates a self-contained HTML file with:
- Fade-in animations on scroll
- Card-based layout for concepts
- Smooth transitions between sections
- Responsive design for all devices

## Required Scripts

All scripts must be in the `scripts/` directory:

- `fetch_content.py` - Extract main content from web pages
- `simplify_content.py` - Simplify and explain content for beginners
- `generate_html.py` - Generate animated HTML output

## Required Assets

All assets must be in the `assets/` directory:

- `template.html` - Base HTML template with animation styles
- `styles.css` - CSS animations and visual styles (or inline in template)

## Output

The skill produces a single HTML file (`explanation.html`) containing:
1. Simplified title and summary
2. Key concepts as animated cards
3. Step-by-step explanations
4. Real-life analogies
5. Smooth scroll-triggered animations

## Example Usage

```
User: Can you explain this article to me? https://example.com/blockchain-guide

Assistant: I'll simplify that article and create an animated HTML page for you.
[Calls fetch_content.py, simplify_content.py, generate_html.py]
Here you go! I've created a simplified, animated explanation:
explanation.html
```

## Content Simplification Guidelines

When simplifying content:

1. **Identify jargon**: Mark technical terms that need explanation
2. **Create analogies**: Use everyday examples (e.g., "blockchain is like a shared diary that everyone can read but no one can erase")
3. **Step breakdown**: For processes, break into numbered steps
4. **Concept cards**: Each major concept gets a visual card
5. **Progressive detail**: Start simple, add complexity gradually
6. **Summary**: End with key takeaways in simple terms

## Animation Specifications

Animations should be subtle and enhance readability:

- **Fade-in**: Elements appear smoothly as user scrolls
- **Card reveal**: Cards slide up and fade in
- **Hover effects**: Subtle scale and shadow changes
- **Progress indicator**: Show reading progress
- **Mobile responsive**: Animations respect reduced motion preferences

All CSS animations must be in the HTML template or external CSS file.
