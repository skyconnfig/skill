# Apple China Design Database

Design system database for Apple China website clone, stored according to ui-ux-pro-max skill specifications.

## Overview

This design database contains the complete design specifications for the Apple China website clone, including:
- Design tokens in JSON format
- CSS custom properties
- Complete design documentation
- Searchable index

## File Structure

```
apple-china/
├── README.md                  # This file
├── INDEX.md                   # Searchable index with keywords
├── DESIGN_SYSTEM.md           # Complete design system documentation
├── design-tokens.json         # Design tokens (JSON format)
└── apple-china-vars.css       # CSS custom properties
```

## Design System Details

### Product Information
- **Product Type**: Technology / Premium Consumer Electronics
- **Industry**: Consumer Electronics / Tech
- **Design Style**: Minimalism, Clean, Premium
- **Version**: 1.0.1
- **Last Updated**: 2026-01-22

### Design Tags
- **UI Styles**: minimal, clean, premium, professional, sleek, modern, sophisticated
- **Color Tags**: tech-blue, monochrome, premium, professional, sophisticated
- **Font Tags**: sans-serif, geometric, clean, modern, premium

## Usage

### Using CSS Variables

```html
<link rel="stylesheet" href="apple-china-vars.css">

<style>
  .btn-primary {
    background-color: var(--color-apple-blue);
    color: var(--color-white);
    padding: var(--button-padding-y) var(--button-padding-x);
    border-radius: var(--button-border-radius);
    height: var(--button-height);
  }
</style>
```

### Using Design Tokens (JSON)

```json
{
  "designSystem": {
    "name": "Apple China",
    "version": "1.0.1"
  },
  "colors": {
    "primary": {
      "blue": "#007AFF"
    }
  },
  "spacing": {
    "unit": 8
  }
}
```

### Searching the Design System

The design database is structured to work with the ui-ux-pro-max search script:

```bash
# Search by style
python3 ../../scripts/search.py "minimal clean premium" --design-system

# Search by color
python3 ../../scripts/search.py "apple blue" --domain colors

# Search by typography
python3 ../../scripts/search.py "sans-serif geometric" --domain typography

# Get design system info
python3 ../../scripts/search.py "apple china" --design-system -f markdown
```

## Key Specifications

### Colors
- Primary: Apple Blue (`#007AFF`)
- Semantic: Success (`#34C759`), Warning (`#FF9500`), Danger (`#FF3B30`)
- Neutral: White, Black, Gray 1-5 (`#f5f5f7` - `#6e6e73`)

### Typography
- Chinese: SF Pro SC, PingFang SC, 苹方
- English: SF Pro, -apple-system
- Sizes: 12px - 48px (h1)

### Spacing
- Base unit: 8px
- Scale: 4px - 128px (10 levels)

### Components
- Button: 44px height, 980px border radius
- Navigation: 44px height, 20px backdrop blur
- Card: 18px border radius

### Effects
- Shadows: Small to Extra Large
- Transitions: Fast (150ms), Normal (250ms), Slow (350ms)
- Blur: 4px - 20px

### Breakpoints
- Mobile: 734px
- Tablet: 1068px
- Desktop: 1440px
- Wide: 1920px

## Integration Examples

### HTML + Tailwind
```html
<button class="bg-[#007AFF] text-white px-[22px] py-[12px] rounded-[980px] h-[44px]">
  Button Text
</button>
```

### React / Next.js
```jsx
const styles = {
  button: {
    backgroundColor: '#007AFF',
    color: '#ffffff',
    padding: '12px 22px',
    borderRadius: '980px',
    height: '44px'
  }
};
```

### Vue
```vue
<template>
  <button class="btn-primary">Button Text</button>
</template>

<style scoped>
.btn-primary {
  background-color: #007AFF;
  color: #ffffff;
  padding: 12px 22px;
  border-radius: 980px;
  height: 44px;
}
</style>
```

### SwiftUI
```swift
Button(action: {}) {
    Text("Button Text")
        .font(.body)
        .padding(.horizontal, 22)
        .padding(.vertical, 12)
        .background(Color.blue)
        .foregroundColor(.white)
        .clipShape(Capsule())
}
```

### Flutter
```dart
ElevatedButton(
  style: ElevatedButton.styleFrom(
    backgroundColor: Color(0xFF007AFF),
    padding: EdgeInsets.symmetric(horizontal: 22, vertical: 12),
    shape: RoundedRectangleBorder(
      borderRadius: BorderRadius.circular(980),
    ),
  ),
  onPressed: () {},
  child: Text('Button Text'),
)
```

## Validation

This design system has been validated against:
- ✅ No emojis as icons
- ✅ cursor-pointer on clickable elements
- ✅ Hover states with smooth transitions (150-300ms)
- ✅ Contrast ratio requirements (4.5:1 normal, 3:1 large)
- ✅ Focus states for keyboard navigation
- ✅ prefers-reduced-motion support
- ✅ Responsive breakpoints
- ✅ Minimum touch target (44x44px)

## References

- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- [Apple Design Resources](https://developers.apple.com/design/resources/)
- [SF Pro Font](https://developer.apple.com/fonts/)
- [ui-ux-pro-max Skill](../SKILL.md)

## License

Based on Apple Human Interface Guidelines. This is a design system clone for educational purposes.

---

**Created**: 2026-01-22
**Version**: 1.0.1
**Author**: Sisyphus AI Agent
