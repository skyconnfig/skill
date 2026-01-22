# Apple China Website Implementation - Quick Reference Card

## Implementation Summary

| Field | Value |
|-------|------|
| **Project** | Apple China Website Clone |
| **Date** | 2026-01-22 |
| **Design Controller Path** | Path 4: Design Standard Extraction |
| **Status** | ✅ Complete - Production Ready |
| **Style** | Minimalism, Clean, Premium |
| **Industry** | Consumer Electronics / Tech |

## Key Metrics

| Metric | Value |
|--------|-------|
| Design Tokens | 50+ |
| Code Examples | 15+ |
| Search Keywords | 100+ |
| Documentation | 798 lines |
| File Size | 22 KB |

## Design System at a Glance

### Colors
- **Primary**: Apple Blue (`#007AFF`)
- **Semantic**: Success (`#34C759`), Warning (`#FF9500`), Danger (`#FF3B30`)
- **Neutral**: White, Black, Gray 1-5 (`#f5f5f7` - `#6e6e73`)

### Typography
- **Fonts**: SF Pro (English), PingFang SC (Chinese)
- **Base Size**: 17px
- **Heading Range**: 48px (h1) - 24px (h4)

### Spacing
- **Base Unit**: 8px
- **Scale**: 10 levels (4px - 128px)

### Components
- **Buttons**: 44px height, 980px radius, 12px 22px padding
- **Navigation**: 44px height, 20px blur, dark theme
- **Cards**: 18px radius, large shadow on hover

### Effects
- **Shadows**: Small (0 2px 8px) → Large (0 16px 48px)
- **Transitions**: Fast (150ms), Normal (250ms), Slow (350ms)
- **Blur**: 4px - 20px

## Quick Start

### 1. View Documentation
```bash
cat references/BEST_PRACTICE-APPLE-CHINA-IMPLEMENTATION.md
```

### 2. Use Design Database
```bash
# Search for Apple China design
python3 scripts/search.py "apple china minimal" --design-system

# Get design tokens
python3 scripts/search.py "apple" --design-system -f json
```

### 3. Apply to Project
```html
<!-- Add CSS variables -->
<link rel="stylesheet" href="apple-china-vars.css">

<!-- Use in your code -->
<style>
  .btn {
    background-color: var(--color-apple-blue);
    padding: var(--button-padding-y) var(--button-padding-x);
    border-radius: var(--button-border-radius);
  }
</style>
```

### 4. View Website Clone
```
C:\Users\lixin\Desktop\web-page-skill\index.html
```

## File Locations

### Implementation Files
- **Website Clone**: `C:\Users\lixin\Desktop\web-page-skill\`
- **Design Database**: `ui-ux-pro-max\design-databases\apple-china\`
- **Best Practice Archive**: `design-controller\references\BEST_PRACTICE-APPLE-CHINA-IMPLEMENTATION.md`

### Key Files
```
apple-china/
├── README.md                  # Overview & usage
├── INDEX.md                   # Searchable index
├── DESIGN_SYSTEM.md           # Complete documentation
├── design-tokens.json         # JSON tokens
└── apple-china-vars.css       # CSS variables
```

## Search Keywords

### By Style
```
minimal, clean, premium, professional, sleek, modern, sophisticated
```

### By Color
```
apple blue, tech blue, monochrome, premium colors, professional colors
```

### By Typography
```
sans-serif, geometric, clean typography, modern typography, SF Pro
```

### By Industry
```
technology, consumer electronics, premium tech, hardware, apple-style
```

## Multi-Stack Examples

### HTML + Tailwind
```html
<button class="bg-[#007AFF] text-white px-[22px] py-[12px] rounded-[980px] h-[44px]">
  Button Text
</button>
```

### React / Next.js
```jsx
<button style={{
  backgroundColor: '#007AFF',
  padding: '12px 22px',
  borderRadius: '980px',
  height: '44px'
}}>
  Button Text
</button>
```

### Vue
```vue
<button class="btn-primary">Button Text</button>

<style scoped>
.btn-primary {
  background-color: #007AFF;
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
        .padding(.horizontal, 22)
        .padding(.vertical, 12)
        .background(Color.blue)
        .foregroundColor(.white)
        .clipShape(Capsule())
        .frame(height: 44)
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

## Validation Checklist

- ✅ No emojis as icons (use SVG: Heroicons/Lucide)
- ✅ cursor-pointer on all clickable elements
- ✅ Hover states with smooth transitions (150-300ms)
- ✅ Light mode contrast ratio minimum 4.5:1
- ✅ Dark mode contrast ratio minimum 3:1
- ✅ Focus states visible for keyboard navigation
- ✅ prefers-reduced-motion respected
- ✅ Responsive breakpoints: 734px, 1068px, 1440px, 1920px
- ✅ Minimum touch target: 44x44px

## Design Controller Workflow

### This Implementation Used: Path 4

```
Path 4: Design Standard Extraction
├─ Step 4A: Capture Target URL (Research & Analysis)
│   └─ Used librarian agent to analyze Apple China website
│
├─ Step 4B: Analyze Design System (Extract Tokens)
│   └─ Extracted colors, typography, spacing, components
│
└─ Step 4C: Store to Database (Persist to ui-ux-pro-max)
    └─ Created apple-china design database
```

## Best For Replicating

- Premium technology websites
- Consumer electronics e-commerce
- Minimalist brand sites
- Clean, content-focused layouts
- High-end product showcases

## Related Resources

### Design Resources
- **Apple Human Interface Guidelines**: https://developer.apple.com/design/human-interface-guidelines/
- **Apple Design Resources**: https://developers.apple.com/design/resources/
- **SF Pro Font**: https://developer.apple.com/fonts/

### Implementation Files
- **Website Clone**: `C:\Users\lixin\Desktop\web-page-skill\index.html`
- **Design Database**: `C:\Users\lixin\.config\opencode\skill\ui-ux-pro-max\design-databases\apple-china\`
- **Best Practice Archive**: `C:\Users\lixin\.config\opencode\skill\design-controller\references\BEST_PRACTICE-APPLE-CHINA-IMPLEMENTATION.md`

### Design Controller Resources
- **Skill Documentation**: `design-controller\SKILL.md`
- **Workflows**: `design-controller\references\workflows.md`

---

## Quick Command Reference

```bash
# Search this design system
python3 scripts/search.py "apple china minimal clean" --design-system

# Get design tokens as JSON
python3 scripts/search.py "apple" --design-system -f json

# View full documentation
cat design-controller/references/BEST_PRACTICE-APPLE-CHINA-IMPLEMENTATION.md

# View quick reference
cat design-controller/references/QUICK_REFERENCE-APPLE-CHINA.md
```

---

**Card Version**: 1.0.0  
**Created**: 2026-01-22  
**Archive**: BEST_PRACTICE-APPLE-CHINA-IMPLEMENTATION.md  
**Status**: ✅ Ready for Replication

*Use this card for quick lookup during design implementation projects.*
