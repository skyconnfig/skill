---
name: ui-ux-pro-max
description: AI skill for building professional UI/UX across multiple platforms - 57 UI styles, 95 color palettes, 56 font pairings, and 100 reasoning rules
license: MIT
compatibility: opencode
metadata:
  audience: frontend-developers
  use-case: ui-ux-design
  platforms: react vue svelte swift flutter html-tailwind
---

# UI/UX Pro Max

AI skill that provides design intelligence for building professional UI/UX across multiple platforms and frameworks. Features intelligent design system generation based on industry-specific reasoning rules.

## What It Does

1. **Analyzes your request** - Understands product type and requirements
2. **Generates complete design system** - Pattern + Style + Colors + Typography + Effects
3. **Provides smart recommendations** - Best matching styles, colors, and typography for your industry
4. **Implements UI** - Code generation with proper colors, fonts, spacing, and best practices
5. **Validates against anti-patterns** - Pre-delivery checks for common UI/UX issues

## Features

| Category | Count | Examples |
|----------|-------|----------|
| UI Styles | 57 | Glassmorphism, Claymorphism, Minimalism, Brutalism, Neumorphism, Bento Grid, Dark Mode, AI-Native UI |
| Color Palettes | 95 | Industry-specific palettes for SaaS, E-commerce, Healthcare, Fintech, Beauty |
| Font Pairings | 56 | Curated typography combinations with Google Fonts imports |
| Chart Types | 24 | Recommendations for dashboards and analytics |
| Tech Stacks | 11 | React, Next.js, Vue, Nuxt.js, Nuxt UI, Svelte, SwiftUI, React Native, Flutter, HTML+Tailwind, shadcn/ui |
| UX Guidelines | 98 | Best practices, anti-patterns, accessibility rules |
| Reasoning Rules | 100 | Industry-specific design system generation |

## 100 Industry-Specific Reasoning Rules

The reasoning engine includes specialized rules for:

### Tech & SaaS
SaaS, Micro SaaS, B2B Enterprise, Developer Tools, AI/Chatbot Platform

### Finance
Fintech, Banking, Crypto, Insurance, Trading Dashboard

### Healthcare
Medical Clinic, Pharmacy, Dental, Veterinary, Mental Health

### E-commerce
General, Luxury, Marketplace, Subscription Box

### Services
Beauty/Spa, Restaurant, Hotel, Legal, Consulting

### Creative
Portfolio, Agency, Photography, Gaming, Music Streaming

### Emerging Tech
Web3/NFT, Spatial Computing, Quantum Computing, Autonomous Systems

## Usage

Simply describe what you want to build:

```
Build a landing page for my SaaS product
Create a dashboard for healthcare analytics
Design a portfolio website with dark mode
Make a mobile app UI for e-commerce
Build a fintech banking app with dark theme
```

## Supported Stacks

The skill provides stack-specific guidelines for:
- **HTML + Tailwind** (default)
- **React** / **Next.js** / **shadcn/ui**
- **Vue** / **Nuxt.js** / **Nuxt UI** / **Svelte**
- **SwiftUI** / **React Native** / **Flutter**

Just mention your preferred stack in the prompt, or let it default to HTML + Tailwind.

## Design System Command (Advanced)

```bash
# Generate design system with ASCII output
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "beauty spa wellness" --design-system -p "Serenity Spa"

# Generate with Markdown output
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "fintech banking" --design-system -f markdown

# Domain-specific search
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "glassmorphism" --domain style
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "elegant serif" --domain typography
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "dashboard" --domain chart

# Stack-specific guidelines
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "form validation" --stack react
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "responsive layout" --stack html-tailwind
```

## When to Use

**MANDATORY** for:
- Any frontend visual/styling changes (colors, spacing, layout, typography, animation)
- Building landing pages, dashboards, mobile apps
- Creating new UI components or pages
- Any UI/UX design decisions

**Logic-only changes** (data fetching, API calls, state management) can be handled directly without this skill.

## Pre-Delivery Checklist

The skill validates:
- No emojis as icons (use SVG: Heroicons/Lucide)
- cursor-pointer on all clickable elements
- Hover states with smooth transitions (150-300ms)
- Light mode:.5:1 minimum
- Focus states visible for keyboard text contrast 4 nav
- prefers-reduced-motion respected
- Responsive breakpoints: 375px, 768px, 1024px, 1440px

## Prerequisites

Python 3.x is required for the search script.

```bash
# Check if Python is installed
python3 --version

# macOS
brew install python3

# Ubuntu/Debian
sudo apt update && sudo apt install python3

# Windows
winget install Python.Python.3.12
```

## References

- Source: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- Documentation: https://ui-ux-pro-max-skill.nextlevelbuilder.io
- NPM Package: https://www.npmjs.com/package/uipro-cli
