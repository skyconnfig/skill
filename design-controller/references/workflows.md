# Design Controller Workflow Reference

This document provides detailed workflow patterns for the design controller.

## Sub-Skill Integration Guide

### Frontend Design Skill (`frontend-design`)

**When called from design-controller:**
- **Creative Path**: Full creative freedom, minimal constraints
- **Normative Path**: Pattern replication, must follow reference
- **Hybrid Path**: Standards-based creativity, document all decisions

**Calling convention:**
```bash
python scripts/main.py --project "DESCRIPTION" --style "HINTS" --constraint "PATTERN_FILE"
```

### UI/UX Pro Max (`ui-ux-pro-max`)

**Database Structure (57 styles, 95 palettes, 56 font pairings):**

```json
{
  "styles": [
    {
      "id": "style_001",
      "name": "Stripe-style Clean Dashboard",
      "category": "fintech-clean",
      "colors": {
        "primary": "#635BFF",
        "secondary": "#00D4FF",
        "background": "#F7F9FC",
        "text": "#1A1F36",
        "accent": ["#00C9A7", "#845EC2"]
      },
      "typography": {
        "font_family": "Inter",
        "font_weights": [400, 500, 600, 700],
        "base_size": "16px",
        "line_height": "1.5",
        "scale": "1.25"
      },
      "spacing": {
        "base_unit": "4px",
        "scale": [4, 8, 12, 16, 24, 32, 48, 64]
      },
      "components": {
        "button": {...},
        "card": {...},
        "input": {...},
        "table": {...},
        "chart": {...}
      },
      "layout": {
        "container": "1140px",
        "grid": "12 columns",
        "gap": "24px"
      }
    }
  ],
  "palettes": [...],
  "font_pairings": [...]
}
```

**Query API:**
```python
def query_style(reference: str) -> Dict:
    """Find matching design style."""
    # Searches: name, category, colors, components
    return matched_style or None

def extract_from_url(url: str) -> Dict:
    """Capture and analyze website design."""
    # Uses playwright to capture
    # Analyzes: colors, typography, spacing, components
    # Returns: structured design tokens
```

### Playwright Skill

**For design extraction:**
```bash
python scripts/capture.py --url "https://example.com" --output "design_extract.json"
```

**Capture output structure:**
```json
{
  "screenshot": "path/to/screenshot.png",
  "css_analysis": {
    "colors": ["#333333", "#0071e3", ...],
    "fonts": ["Inter", ...],
    "spacing_patterns": ["4px", "8px", "16px", ...]
  },
  "dom_structure": {
    "elements": [...],
    "components": [...]
  }
}
```

## Design Extraction Workflow (Path 4)

### Step 1: URL Validation
```python
def validate_url(url: str) -> bool:
    """Check if URL is accessible."""
    import requests
    response = requests.head(url)
    return response.status_code < 400
```

### Step 2: Page Capture
```python
def capture_page(url: str, output_dir: str) -> Dict:
    """Capture full page with playwright."""
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        
        # Capture screenshot
        screenshot_path = f"{output_dir}/screenshot.png"
        page.screenshot(path=screenshot_path, full_page=True)
        
        # Extract CSS
        css_rules = page.evaluate("""
            () => {
                const sheets = document.styleSheets;
                let rules = [];
                for (let sheet of sheets) {
                    try {
                        for (let rule of sheet.cssRules) {
                            rules.push(rule.cssText);
                        }
                    } catch(e) {}
                }
                return rules;
            }
        """)
        
        browser.close()
        return {"screenshot": screenshot_path, "css": css_rules}
```

### Step 3: Design Analysis
```python
def analyze_design(screenshot: str, css: List[str]) -> Dict:
    """Extract design tokens from capture."""
    # Extract colors
    colors = extract_colors_from_css(css)
    
    # Extract typography
    typography = extract_typography_from_css(css)
    
    # Extract spacing
    spacing = extract_spacing_from_css(css)
    
    # Identify components
    components = identify_components(screenshot)
    
    return {
        "colors": colors,
        "typography": typography,
        "spacing": spacing,
        "components": components
    }
```

### Step 4: Database Storage
```python
def store_design_tokens(url: str, analysis: Dict) -> str:
    """Store extracted design to ui-ux-pro-max database."""
    import sqlite3
    
    conn = sqlite3.connect('design_database.db')
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO styles 
        (source_url, colors, typography, spacing, components, extracted_at)
        VALUES (?, ?, ?, ?, ?, datetime('now'))
    """, (
        url,
        json.dumps(analysis['colors']),
        json.dumps(analysis['typography']),
        json.dumps(analysis['spacing']),
        json.dumps(analysis['components'])
    ))
    
    style_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return f"style_{style_id}"
```

## Quality Scoring for Extracted Designs

```python
def calculate_quality_score(analysis: Dict) -> float:
    """Score extracted design quality (0.0 - 1.0)."""
    score = 0.0
    
    # Color completeness (max 0.3)
    color_count = len(analysis.get('colors', []))
    score += min(color_count / 10, 1.0) * 0.3
    
    # Typography completeness (max 0.3)
    has_font = bool(analysis.get('typography', {}).get('font_family'))
    has_size = bool(analysis.get('typography', {}).get('base_size'))
    score += (0.15 if has_font else 0) + (0.15 if has_size else 0)
    
    # Spacing scale (max 0.2)
    spacing_complete = bool(analysis.get('spacing', {}).get('scale'))
    score += 0.2 if spacing_complete else 0
    
    # Component identification (max 0.2)
    component_count = len(analysis.get('components', []))
    score += min(component_count / 5, 1.0) * 0.2
    
    return round(score, 2)
```

## Common Design References

| Reference | Category | Key Characteristics |
|-----------|----------|---------------------|
| Stripe | Fintech Clean | Vibrant gradients, clean cards, subtle shadows |
| Apple | Minimal Premium | Heavy whitespace, large typography, smooth animations |
| Linear | Dark Minimal | Dark theme, compact spacing, purple accents |
| Notion | Content-First | Document-based, collapsible nav, clean typography |
| Vercel | Developer | Black/white, grid layouts, mono fonts |
| Shopify | E-commerce | Bold CTAs, product grids, card layouts |

## Best Practice Archives

### Apple China Website Implementation (2026-01-22)

**Archive Location**: `references/BEST_PRACTICE-APPLE-CHINA-IMPLEMENTATION.md`

**Implementation Overview**:
- Complete Path 4: Design Standard Extraction workflow
- Premium consumer electronics website clone
- Minimalist, clean, premium design style
- Full design token extraction and database storage

**Design System Extracted**:
- Colors: 10 colors (Primary Blue, Semantic, Neutral grays)
- Typography: SF Pro + PingFang SC, 7 sizes
- Spacing: 10-level scale (4px - 128px)
- Components: Buttons, Navigation, Cards, Inputs
- Effects: Shadows, Transitions, Blur effects
- Accessibility: WCAG 2.1 AA compliant

**Implementation Artifacts**:
1. **Website Clone**: `C:\Users\lixin\Desktop\web-page-skill\`
   - index.html (15 KB)
   - styles.css (14 KB)
   - design-tokens.json (3.5 KB)
   - DESIGN_SYSTEM.md (6.4 KB)

2. **Design Database**: `ui-ux-pro-max/design-databases/apple-china/`
   - README.md (5.0 KB) - Overview & usage
   - INDEX.md (3.9 KB) - Searchable index
   - DESIGN_SYSTEM.md (5.0 KB) - Complete documentation
   - design-tokens.json (3.4 KB) - JSON tokens
   - apple-china-vars.css (8.4 KB) - CSS variables

**Key Features**:
- ✅ Complete design token extraction
- ✅ Multi-stack integration examples (HTML, React, Vue, SwiftUI, Flutter)
- ✅ Search-optimized keywords
- ✅ Validation checklist compliance
- ✅ Accessibility documentation
- ✅ 798-line comprehensive archive documentation

**Usage**:
```bash
# Search for this design system
python3 scripts/search.py "apple china minimal clean premium" --design-system

# Retrieve design tokens
python3 scripts/search.py "apple china" --design-system -f json

# Apply to new project
<link rel="stylesheet" href="apple-china-vars.css">
```

**Related Resources**:
- **Original Website**: https://www.apple.com.cn/
- **Design Guidelines**: Apple Human Interface Guidelines
- **Archive Document**: `references/BEST_PRACTICE-APPLE-CHINA-IMPLEMENTATION.md`

---

## Error Recovery Patterns

### When Sub-skill Fails
```python
def handle_skill_failure(skill_name: str, error: Exception) -> Dict:
    """Handle sub-skill failure with fallback."""
    fallback_strategies = {
        'frontend-design': 'Use template-based design',
        'ui-ux-pro-max': 'Use generic design system',
        'playwright': 'Manual CSS analysis'
    }
    
    strategy = fallback_strategies.get(skill_name, 'Report error')
    return {
        'failed_skill': skill_name,
        'fallback': strategy,
        'error': str(error)
    }
```
