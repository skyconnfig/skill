# Apple China Design System - Design Database

## Overview
- **Product Type**: Technology / Premium Consumer Electronics
- **Industry**: Consumer Electronics / Tech
- **Design Style**: Minimalism, Clean, Premium
- **Style Tags**: minimal, clean, premium, professional, sleek, modern, sophisticated
- **Color Tags**: tech-blue, monochrome, premium, professional, sophisticated
- **Font Tags**: sans-serif, geometric, clean, modern, premium

## Design System Components

### 1. Color Palette
**Primary Colors**
- Apple Blue: `#007AFF`
- Apple Blue Hover: `#338BFF`
- Apple Blue Active: `#0062CC`

**Semantic Colors**
- Success: `#34C759`
- Warning: `#FF9500`
- Danger: `#FF3B30`

**Neutral Colors**
- White: `#ffffff`
- Black: `#1d1d1f`
- Gray 1: `#f5f5f7`
- Gray 2: `#e8e8ed`
- Gray 3: `#d2d2d7`
- Gray 4: `#86868b`
- Gray 5: `#6e6e73`

### 2. Typography
**Font Families**
- Chinese: 'SF Pro SC', 'PingFang SC', '苹方-简', -apple-system, 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif
- English: 'SF Pro', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif
- Mono: 'SF Mono', 'Menlo', 'Monaco', 'Consolas', monospace

**Font Sizes**
- h1: 48px (Semibold)
- h2: 40px (Semibold)
- h3: 32px (Semibold)
- h4: 24px (Semibold)
- Body: 17px (Regular)
- Body Small: 14px (Regular)
- Caption: 12px (Regular)

### 3. Spacing System
- xxs: 4px
- xs: 8px
- sm: 12px
- md: 16px
- lg: 24px
- xl: 32px
- xxl: 48px
- xxxl: 64px
- xxxxl: 96px
- Jumbo: 128px

### 4. Components
**Buttons**
- Height: 44px
- Padding: 12px 22px
- Border Radius: 980px
- Font Size: 17px

**Navigation**
- Height: 44px
- Background: rgba(0, 0, 0, 0.8)
- Backdrop Blur: 20px

**Cards**
- Border Radius: 18px
- Padding: 24px

### 5. Effects
**Shadows**
- Small: 0 2px 8px rgba(0, 0, 0, 0.04)
- Medium: 0 8px 16px rgba(0, 0, 0, 0.08)
- Large: 0 16px 48px rgba(0, 0, 0, 0.12)
- Extra Large: 0 32px 64px rgba(0, 0, 0, 0.16)

**Transitions**
- Fast: 150ms ease
- Normal: 250ms ease
- Slow: 350ms ease

**Blur**
- Small: 4px
- Medium: 8px
- Large: 16px
- Navigation: 20px

### 6. Breakpoints
- Mobile: 734px
- Tablet: 1068px
- Desktop: 1440px
- Wide: 1920px

## Usage Guidelines

### Do's
- Use generous whitespace
- Maintain visual hierarchy
- Use subtle shadows and blurs
- Implement smooth transitions (150-300ms)
- Ensure high contrast for accessibility
- Use consistent border radius (18px for cards, 980px for buttons)

### Don'ts
- Use excessive colors (stick to monochrome + Apple Blue)
- Use heavy shadows or borders
- Create cluttered layouts
- Use more than 2-3 font sizes in a component
- Use bright, flashy animations

### Accessibility
- Minimum contrast ratio: 4.5:1 for normal text
- Minimum contrast ratio: 3:1 for large text
- Minimum touch target: 44x44px
- Respect prefers-reduced-motion

### Responsive Behavior
- Mobile first approach
- Grid collapses to single column on mobile
- Navigation simplifies on smaller screens
- Typography scales appropriately

## Stack-Specific Guidelines

### HTML + Tailwind
```html
<button class="bg-[#007AFF] text-white px-[22px] py-[12px] rounded-[980px] h-[44px] text-[17px]">
  Button Text
</button>
```

### React / Next.js
```jsx
<button className="bg-blue-500 text-white px-6 py-3 rounded-full h-11 text-lg">
  Button Text
</button>
```

### Vue
```vue
<button class="bg-blue-500 text-white px-6 py-3 rounded-full h-11 text-lg">
  Button Text
</button>
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

## Validation Checklist
- [x] No emojis as icons (use SVG: Heroicons/Lucide)
- [x] cursor-pointer on all clickable elements
- [x] Hover states with smooth transitions (150-300ms)
- [x] Light mode contrast ratio minimum 4.5:1
- [x] Dark mode contrast ratio minimum 3:1
- [x] Focus states visible for keyboard navigation
- [x] prefers-reduced-motion respected
- [x] Responsive breakpoints: 734px, 1068px, 1440px, 1920px
- [x] Minimum touch target: 44x44px

## Related Design Systems
- Apple Human Interface Guidelines
- iOS Design System
- macOS Design System
- Material Design (for comparison)

## References
- Apple Design Resources: https://developers.apple.com/design/resources/
- SF Pro Font: https://developer.apple.com/fonts/
- SF Symbols: https://developer.apple.com/sf-symbols/
- Human Interface Guidelines: https://developer.apple.com/design/human-interface-guidelines/

---
**Created**: 2026-01-22
**Version**: 1.0.1
**Last Updated**: 2026-01-22
**Author**: Sisyphus AI Agent
**Based On**: Apple Human Interface Guidelines & Apple China Website Analysis
