# Design Pattern Database

## Overview

This document defines the schema and examples for the design pattern database, which stores design style specifications extracted from real-world examples.

## Database Schema

### Pattern Entry Structure

```json
{
  "id": "pattern_001",
  "name": "Minimalist Tech",
  "category": "style",
  "style": "minimalism",
  "colors": {
    "primary": "#2563eb",
    "secondary": "#64748b",
    "background": "#ffffff",
    "surface": "#f8fafc",
    "text": "#1e293b",
    "accent": "#3b82f6"
  },
  "typography": {
    "fontFamily": "Inter, system-ui, sans-serif",
    "headingWeight": "700",
    "bodyWeight": "400",
    "headingSize": "2.5rem",
    "bodySize": "1rem",
    "lineHeight": "1.6"
  },
  "spacing": {
    "base": "1rem",
    "scale": "1.25",
    "container": "1200px",
    "gridGap": "2rem"
  },
  "components": {
    "button": {
      "borderRadius": "0.5rem",
      "padding": "0.75rem 1.5rem",
      "fontWeight": "600",
      "transition": "all 0.2s ease"
    },
    "card": {
      "borderRadius": "1rem",
      "shadow": "0 4px 6px -1px rgba(0, 0, 0, 0.1)",
      "padding": "1.5rem"
    },
    "input": {
      "borderRadius": "0.375rem",
      "border": "1px solid #e2e8f0",
      "padding": "0.625rem 0.875rem"
    }
  },
  "layout": {
    "type": "grid",
    "columns": 12,
    "breakpoints": {
      "mobile": "640px",
      "tablet": "768px",
      "desktop": "1024px",
      "wide": "1280px"
    }
  },
  "responsive": {
    "mobile": "single column",
    "tablet": "two columns",
    "desktop": "three columns",
    "wide": "four columns"
  },
  "visualEffects": {
    "borderRadius": "0.5rem",
    "shadows": "md",
    "transitions": "all 0.2s ease",
    "animations": "fade-in, slide-up"
  },
  "accessibility": {
    "contrast": "AA compliant",
    "focus": "visible focus states",
    "motion": "prefers-reduced-motion support"
  },
  "examples": [
    "https://vercel.com",
    "https://linear.app"
  ],
  "tags": ["minimal", "tech", "clean", "modern"]
}
```

## Design Styles

### 1. Minimalist Tech (极简科技)
- **Style**: Minimalism
- **Characteristics**: Clean lines, generous whitespace, blue accents
- **Use Case**: SaaS products, developer tools

### 2. Dark Mode Focus (深色模式)
- **Style**: Dark UI
- **Characteristics**: Dark backgrounds, high contrast text, subtle accents
- **Use Case**: Gaming platforms, developer tools, media apps

### 3. Material Design (谷歌材质设计)
- **Style**: Material
- **Characteristics**: Cards, elevation, ripple effects, bold colors
- **Use Case**: Android apps, Google products

### 4. Apple Human Interface (苹果界面)
- **Style**: Apple HIG
- **Characteristics**: Translucency, blur effects, smooth animations
- **Use Case**: iOS/macOS apps, Apple ecosystem

### 5. Brutalist Raw (原始粗野主义)
- **Style**: Brutalism
- **Characteristics**: Bold typography, high contrast, raw aesthetics
- **Use Case**: Art portfolios, experimental projects

### 6. Glassmorphism (玻璃拟态)
- **Style**: Glassmorphism
- **Characteristics**: Frosted glass effect, vivid backgrounds, soft shadows
- **Use Case**: Mobile apps, modern dashboards

### 7. Neumorphism (新拟态)
- **Style**: Neumorphism
- **Characteristics**: Soft shadows, subtle highlights, low contrast
- **Use Case**: Smart device interfaces, widgets

### 8. Flat Design (扁平设计)
- **Style**: Flat
- **Characteristics**: No shadows, bold colors, simple shapes
- **Use Case**: Corporate websites, mobile apps

### 9. Skeuomorphic (拟物设计)
- **Style**: Skeuomorphic
- **Characteristics**: Realistic textures, shadows, depth
- **Use Case**: Games, creative tools

### 10. Bento Grid (便当网格)
- **Style**: Bento
- **Characteristics**: Grid layout, card-based, modular design
- **Use Case**: Dashboards, feature showcases

## Color Palette Categories

### Light Themes
- **Clean Light**: White backgrounds, blue accents
- **Warm Light**: Cream backgrounds, orange accents
- **Cool Light**: Gray backgrounds, green accents

### Dark Themes
- **Pure Dark**: Black backgrounds, white text
- **Soft Dark**: Dark gray backgrounds, light gray text
- **Colored Dark**: Dark backgrounds with color accents

### Brand-Specific
- **Tech Blue**: Various blue shades
- **Nature Green**: Forest and mint greens
- **Passion Red**: Crimson and rose reds
- **Royal Purple**: Deep purple tones

## Typography Systems

### Sans-Serif Systems
- **Inter System**: Inter, system-ui
- **SF Pro System**: SF Pro, -apple-system
- **Roboto System**: Roboto, sans-serif

### Serif Systems
- **Editorial**: Merriweather, Georgia
- **Elegant**: Playfair Display, Didot

### Monospace Systems
- **Code**: JetBrains Mono, Fira Code
- **Technical**: IBM Plex Mono, Roboto Mono

## Component Pattern Library

### Buttons
- **Primary**: Solid color, rounded corners
- **Secondary**: Outline style, subtle
- **Ghost**: No background, text only
- **Icon**: Icon-only for toolbar

### Cards
- **Basic**: Simple container with shadow
- **Elevated**: Higher elevation for importance
- **Outlined**: Border only, no shadow
- **Interactive**: Hover effects, clickable

### Forms
- **Input**: Standard text input
- **Select**: Dropdown selection
- **Checkbox**: Binary selection
- **Radio**: Single selection from options
- **Toggle**: On/off switch

### Navigation
- **Top Bar**: Horizontal navigation
- **Sidebar**: Vertical navigation
- **Tab Bar**: Tab-based navigation
- **Breadcrumb**: Hierarchical navigation
