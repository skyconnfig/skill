# Design Database Index - Apple China

This index provides a searchable reference for the Apple China design system.

## Quick Reference

### Product Information
- **Product Type**: Technology / Premium Consumer Electronics
- **Industry**: Consumer Electronics / Tech
- **Design Style**: Minimalism, Clean, Premium
- **Version**: 1.0.1
- **Last Updated**: 2026-01-22

### Key Characteristics
- **UI Style**: Minimalist, Clean, Premium, Professional, Sleek, Modern, Sophisticated
- **Color Palette**: Tech-blue, Monochrome, Premium, Professional, Sophisticated
- **Typography**: Sans-serif, Geometric, Clean, Modern, Premium

## Search Keywords

### By Style
```
minimalism, clean design, premium, professional, sleek, modern, sophisticated,
tech, electronics, apple-style, minimal, uncluttered, whitespace
```

### By Color
```
apple blue #007AFF, tech blue, monochrome, neutral colors, grayscale,
premium colors, professional colors, clean colors
```

### By Typography
```
sans-serif, geometric fonts, clean typography, modern typography,
SF Pro, PingFang,苹方, Chinese fonts, multilingual
```

### By Component
```
buttons, navigation, cards, hero sections, product grid, footer,
mobile-first, responsive, 44px touch target
```

### By Use Case
```
e-commerce, product showcase, premium brand, consumer electronics,
landing page, corporate website, saas (for comparison)
```

### By Industry
```
technology, consumer electronics, premium products, luxury tech,
hardware, software, ios, mac, iphone, apple
```

## File Structure

```
apple-china/
├── DESIGN_SYSTEM.md          # Complete design documentation
├── design-tokens.json        # Design tokens in JSON format
├── apple-china-vars.css      # CSS custom properties
└── INDEX.md                  # This file
```

## Usage Examples

### Finding This Design System
```bash
# Search by style
python3 scripts/search.py "minimal clean premium" --design-system

# Search by color
python3 scripts/search.py "apple blue tech" --domain colors

# Search by industry
python3 scripts/search.py "consumer electronics technology" --design-system
```

### Integration
```html
<!-- Using CSS Variables -->
<link rel="stylesheet" href="apple-china-vars.css">

<!-- Using in code -->
<style>
  .btn {
    background-color: var(--color-apple-blue);
    padding: var(--button-padding-y) var(--button-padding-x);
    border-radius: var(--button-border-radius);
  }
</style>
```

```json
// Using design tokens
{
  "colors": {
    "primary": "#007AFF"
  },
  "spacing": {
    "unit": 8
  }
}
```

## Design Principles

1. **Clarity** - Content is clear and easy to understand
2. **Deference** - UI defers to content, not the other way around
3. **Depth** - Visual hierarchy and subtle depth effects
4. **Consistency** - Consistent patterns across all components
5. **Performance** - Fast, smooth animations and transitions

## Validation Status

- ✅ No emojis as icons (use SVG: Heroicons/Lucide)
- ✅ cursor-pointer on all clickable elements
- ✅ Hover states with smooth transitions (150-300ms)
- ✅ Light mode contrast ratio minimum 4.5:1
- ✅ Dark mode contrast ratio minimum 3:1
- ✅ Focus states visible for keyboard navigation
- ✅ prefers-reduced-motion respected
- ✅ Responsive breakpoints: 734px, 1068px, 1440px, 1920px
- ✅ Minimum touch target: 44x44px

## Related Design Systems

- Apple Human Interface Guidelines (Official)
- iOS Design System
- macOS Design System
- Material Design (for comparison)
- Fluent Design System (for comparison)

## References

- Apple Design Resources: https://developers.apple.com/design/resources/
- SF Pro Font: https://developer.apple.com/fonts/
- SF Symbols: https://developer.apple.com/sf-symbols/
- Human Interface Guidelines: https://developer.apple.com/design/human-interface-guidelines/

---

**Index Version**: 1.0.0
**Created**: 2026-01-22
**Author**: Sisyphus AI Agent
