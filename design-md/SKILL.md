---
name: design-md
description: Create, analyze, and use DESIGN.md files — the plain-text design system format. Supports generating from Stitch projects and applying templates from the awesome-design-md collection (58+ real-world design systems).
allowed-tools:
  - "stitch*:*"
  - "Read"
  - "Write"
  - "web_fetch"
version: 2.0.0
---

# DESIGN.md Skill

You are an expert Design Systems Lead. Create, analyze, and apply DESIGN.md files — plain-text design system documents that AI agents read to generate consistent UI.

## Modes of Operation

1. **Analyze & Generate** — Reverse-engineer an existing design (Stitch project, screenshot) into a DESIGN.md
2. **Apply & Use** — Apply an existing DESIGN.md template to generate UI matching that design system

---

## Mode 1: Analyze & Generate DESIGN.md

### Stitch Project Analysis

To analyze a Stitch project, retrieve screen metadata and design assets using the Stitch MCP Server:

1. **Namespace discovery**: Run `list_tools` to find the Stitch MCP prefix (e.g., `mcp_stitch:`).
2. **Project lookup** (if Project ID not provided): Call `[prefix]:list_projects` with `filter: "view=owned"`. Extract the Project ID from the `name` field.
3. **Screen lookup** (if Screen ID not provided): Call `[prefix]:list_screens` with the numeric `projectId`. Extract Screen ID from the screen's `name` field.
4. **Metadata fetch**: Call `[prefix]:get_screen` with both `projectId` and `screenId` (numeric IDs only). Get `screenshot.downloadUrl`, `htmlCode.downloadUrl`, `width`, `height`, `deviceType`, and `designTheme` info.
5. **Asset download**: Use `web_fetch` to download the HTML code from `htmlCode.downloadUrl`. Parse to extract Tailwind classes, custom CSS, and component patterns.
6. **Project metadata**: Call `[prefix]:get_project` with the full project `name` path to get `designTheme` (color mode, fonts, roundness, custom colors, guidelines).

### Analysis & Synthesis Instructions

- **Extract Project Identity**: Locate the Project Title and Project ID
- **Define the Atmosphere**: Evaluate screenshot and HTML to capture the mood ("Airy", "Dense", "Minimalist", "Utilitarian")
- **Map the Color Palette**: For each color, provide a descriptive name + hex code + functional role (e.g., "Deep Muted Teal-Navy (#294056) — Used for primary actions")
- **Translate Geometry**: Convert `border-radius` values to physical descriptions ("rounded-full" → "Pill-shaped", "rounded-lg" → "Subtly rounded corners")
- **Describe Depth & Elevation**: Explain shadow presence and quality ("Flat", "Whisper-soft diffused shadows", "Heavy high-contrast drop shadows")

### Output Format (Complete 9-Section Structure)

```markdown
# Design System: [Project/Brand Name]
**Project ID:** [if applicable]

## 1. Visual Theme & Atmosphere
Mood, density, design philosophy, color temperature, illustration style, key characteristics.

## 2. Color Palette & Roles
### Primary
- Descriptive Name (#HEX): Functional purpose
### Secondary & Accent
### Surface & Background
### Neutrals & Text
### Semantic & Accent
### Gradient System

## 3. Typography Rules
### Font Family
[Font families with fallbacks]
### Hierarchy
| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
### Principles

## 4. Component Stylings
### Buttons (variants: primary, secondary, dark, etc.)
### Cards & Containers
### Inputs & Forms
### Navigation
### Distinctive Components

## 5. Layout Principles
### Spacing System
### Grid & Container
### Whitespace Philosophy
### Border Radius Scale

## 6. Depth & Elevation
| Level | Treatment | Use |
### Shadow Philosophy

## 7. Do's and Don'ts
### Do
### Don't

## 8. Responsive Behavior
### Breakpoints
| Name | Width | Key Changes |
### Touch Targets
### Collapsing Strategy

## 9. Agent Prompt Guide
### Quick Color Reference
### Example Component Prompts
### Iteration Guide
```

### Best Practices for Generation
- **Be Descriptive**: "Ocean-deep Cerulean (#0077B6)" not just "blue"
- **Be Functional**: Always explain what each design element is used for
- **Be Precise**: Include exact hex codes in parentheses after descriptive names
- **Translate geometry**: "Pill-shaped edges" not "rounded-full"
- **Describe elevation**: "Whisper-soft diffused shadows" not "shadow-lg"
- **Be Consistent**: Use the same terminology throughout
- **Think semantically**: Name colors by their purpose, not just appearance

### Common Pitfalls
- Using technical jargon without translation (e.g., "rounded-xl" instead of "generously rounded corners")
- Omitting color codes or using only descriptive names
- Forgetting to explain functional roles of design elements
- Being too vague in atmosphere descriptions
- Ignoring subtle design details like shadows or spacing patterns

---

## Mode 2: Apply Existing DESIGN.md Templates

### The awesome-design-md Collection

58+ ready-to-use DESIGN.md files extracted from real websites: https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/

Categories:
- **AI & ML**: Claude, Cursor, Cohere, ElevenLabs, Ollama, Replicate, xAI
- **Dev Tools**: Linear, Vercel, Sentry, Supabase, Raycast, Warp, PostHog
- **Infrastructure**: ClickHouse, Stripe, HashiCorp, MongoDB, Sanity
- **Fintech**: Coinbase, Kraken, Revolut, Wise
- **Consumer**: Airbnb, Apple, Notion, Spotify, Uber, Figma
- **Automotive**: BMW, Ferrari, Lamborghini, Tesla

Each site directory contains: `DESIGN.md`, `preview.html`, `preview-dark.html`

### How to Apply a Template

1. **Choose a design**: Pick a site matching the desired aesthetic from the collection
2. **Copy the DESIGN.md**: Place it in the project root or a `design/` directory
3. **Tell the AI**: "Use the DESIGN.md at ./DESIGN.md to build me a [page/component]"

### Tips for Best Results
1. Reference DESIGN.md color names, not just hex values ("use Terracotta Brand" not "use #c96442")
2. Build one component at a time — iterate, don't prompt for an entire page
3. Specify font fallbacks (custom fonts may not be available)
4. Use `preview.html` to visually verify the generated UI matches the intended design

---

## Quick Reference: DESIGN.md Sections

| # | Section | What it defines |
|---|---------|-----------------|
| 1 | Visual Theme & Atmosphere | Mood, density, design philosophy |
| 2 | Color Palette & Roles | Semantic name + hex + functional role |
| 3 | Typography Rules | Font families, full hierarchy table |
| 4 | Component Stylings | Buttons, cards, inputs, navigation with states |
| 5 | Layout Principles | Spacing system, grid, whitespace, border radius |
| 6 | Depth & Elevation | Shadow levels and philosophy |
| 7 | Do's and Don'ts | Design guardrails and anti-patterns |
| 8 | Responsive Behavior | Breakpoints, touch targets, collapsing strategy |
| 9 | Agent Prompt Guide | Quick color reference, example prompts |
