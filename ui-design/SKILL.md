---
name: ui-design
description: HTML and Tailwind CSS coding standards for UI development
version: 1.0.0
source: manual-definition

---

# UI HTML/Tailwind Standards

## Core Principles

### Code Output Requirements

- **Single Code Block**: Output all HTML/Tailwind code in ONE code block
- **Complete Document**: Always include `<html>`, `<head>`, and `<body>` tags
- **No Tool Mentioning**: Never mention tokens, Tailwind, or HTML in conversational text
- **Response Structure**: Start with response → Include code → End with response

### Styling Approach

- **Style Attributes**: Use inline CSS styles in the `style` attribute for custom styling
- **Direct Tailwind**: Apply Tailwind classes directly in HTML tags
- **No Config Files**: Never add tailwind config or CSS files
- **Body-level Classes**: Put Tailwind classes in body tags, not html tag

### Design Aesthetic

- **Default Style**: Linear, Stripe, Vercel, TailwindUI inspired (don't mention these names)
- **Theme Selection**:
  - **Dark Mode**: For tech, cool, futuristic designs (default unless specified)
  - **Light Mode**: For modern, traditional, professional, business designs
- **Subtle Contrast**: Use subtle contrast in design

### Typography Standards

- **Font Weight**: Use one level thinner (e.g., Bold → Semibold)
- **Tracking**: Titles above 20px should use `tracking-tight`
- **Logos**: Use letters only with `tracking-tight`
- **Creative Fonts**: Be creative with fonts and layouts

### Component Details

#### Interactive Elements (Custom Built)

- Checkboxes
- Sliders
- Dropdowns
- Toggles

**Important**: Only include if part of the UI design

#### Icons

- Use Lucide icons
- Stroke width: **1.5**
- Avoid gradient containers for icons
- Be extremely detailed and creative

### Visual Design

#### Layout & Spacing

- **Responsive**: Make it responsive
- **Dividers**: Add subtle dividers where appropriate
- **Outlines**: Add subtle outlines where appropriate
- **Accuracy**: Be extremely accurate with all design details

#### Images

- **Unsplash**: Use Unsplash images when no images are specified
- **Image Types**: faces, 3d, renders, etc.

### Interactions & Animations

- **Tailwind Only**: Use Tailwind for animations, NOT JavaScript
- **Hover Effects**: Add hover color and outline interactions
- **Download Button**: Avoid bottom right floating download button

### Charts & Technical Elements

- **Chart.js**: Use Chart.js for charts
- **Canvas Bug Fix**: If canvas is on same level as other nodes (`h2 p canvas div`), it causes infinite growth
- **Correct Structure**: Use `h2 p div>canvas div` pattern to prevent layout issues

### Code Examples

#### Basic Document Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body class="bg-white text-gray-900">
  <!-- Content here -->
</body>
</html>
```

#### Custom Interactive Components

```html
<!-- Checkbox -->
<div class="flex items-center gap-2">
  <input type="checkbox" class="w-5 h-5 rounded border-gray-300 text-blue-600 focus:ring-blue-500">
  <span class="text-sm font-medium">Label</span>
</div>

<!-- Toggle -->
<button class="relative inline-flex h-6 w-11 items-center rounded-full transition-colors">
  <span class="sr-only">Toggle</span>
  <span class="transform rounded-full bg-gray-200 transition-transform inline-block w-4 h-4"></span>
</button>

<!-- Slider -->
<input type="range" class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer">
```

#### Icons Usage

```html
<!-- Lucide icon with 1.5 stroke width -->
<svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24">
  <path stroke-linecap="round" stroke-linejoin="round" d="M..."/>
</svg>
```

#### Chart.js Canvas

```html
<!-- Correct structure to avoid infinite growth -->
<div>
  <h2>Title</h2>
  <p>Description</p>
  <div>
    <canvas id="chart"></canvas>
  </div>
</div>
```

### Dark Mode Example

```html
<body class="bg-gray-950 text-white antialiased">
  <header class="border-b border-gray-800">
    <h1 class="text-2xl font-semibold tracking-tight">Dashboard</h1>
  </header>
  <main class="p-6">
    <!-- Content with subtle outlines -->
    <div class="rounded-xl border border-gray-800 bg-gray-900/50 p-6">
      <!-- Custom components -->
    </div>
  </main>
</body>
```

### Light Mode Example

```html
<body class="bg-white text-gray-900 antialiased">
  <header class="border-b border-gray-100">
    <h1 class="text-2xl font-semibold tracking-tight">Dashboard</h1>
  </header>
  <main class="p-6">
    <div class="rounded-xl border border-gray-200 bg-white p-6 shadow-sm">
      <!-- Professional components -->
    </div>
  </main>
</body>
```

## Design Guidelines

### Do's

- Be creative with fonts, layouts, and details
- Make components functional
- Add subtle dividers and outlines
- Use 1.5 stroke width for all Lucide icons
- Use subtle contrast in designs
- Be extremely detailed in implementation
- Respect original designs, fonts, colors, and styles when provided

### Don'ts

- Don't mention Tailwind, HTML, or tokens in responses
- Don't use JavaScript for animations (use Tailwind only)
- Don't add tailwind config or CSS files
- Don't put Tailwind classes in html tag
- Don't use gradient containers for icons
- Don't create bottom right floating download buttons
- Don't include interactive components unless part of the UI

## Summary

This skill ensures high-quality, professional UI implementations following industry-standard design patterns. The focus is on creating visually appealing, functional, and responsive interfaces with precise attention to typography, spacing, and interaction design.