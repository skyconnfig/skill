---
name: design-controller
description: Master design controller that orchestrates creative and normative design workflows. Use when user needs design work and wants intelligent routing to appropriate design specialists. Supports three paths: (1) Creative direction - calls frontend-design-skill for unique, original designs. (2) Normative replication - calls ui-ux-pro-max to find reference cases and replicate them. (3) Hybrid approach - uses ui-ux-pro-max for standards reference, then frontend-design-skill for creative leadership. Also supports design standard extraction - input a URL, capture via playwright, analyze, and add new standards to ui-ux-pro-max database.
---

# Design Controller

Master orchestration skill for design workflows. Routes requests to appropriate design specialists based on user intent.

## Quick Start

```markdown
/use design-controller --intent creative --project "Create a landing page"
/use design-controller --intent normative --reference "模仿Stripe官网风格"
/use design-controller --intent hybrid --reference "科技感风格，有规范可循"
/use design-controller --intent extract --url "https://example.com"
```

## Decision Tree

### Step 1: Classify User Intent

| Intent | Signal | Action |
|--------|--------|--------|
| **Creative** | "原创", "独特", "自由发挥", "设计师风格" | → Path 1: Creative Designer |
| **Normative** | "复刻", "模仿", "按照某个网站", "规范" | → Path 2: Normative Replication |
| **Hybrid** | "既有风格又有规范", "参考+创意" | → Path 3: Hybrid Approach |
| **Extract** | "提取规范", "分析网站设计" | → Path 4: Design Extraction |

### Step 2: Execute Corresponding Path

## Path 1: Creative Designer

When user wants unique, original design without specific reference:

```markdown
/use design-controller --intent creative --project "PROJECT_DESCRIPTION" --style "optional-style-hints"
```

**Execution:**
1. Call `frontend-design-skill` with project details
2. Pass any style preferences as guidance (not constraints)
3. Let creative skill lead the design language

**Example:**
```
User: "帮我设计一个炫酷的个人作品集页面"

→ Call frontend-design-skill:
   - Project: Personal portfolio page
   - Style hints: Creative, modern, showcase-oriented
   - Freedom: High (no strict reference)
```

## Path 2: Normative Replication

When user wants to replicate an existing design pattern:

```markdown
/use design-controller --intent normative --reference "REFERENCE_DESCRIPTION" --project "PROJECT_DESCRIPTION"
```

**Execution:**
1. Call `ui-ux-pro-max` to find matching design pattern from database
2. Retrieve the 57 styles/95 palettes/56 font pairings database
3. Find closest match to user's reference description
4. Call `frontend-design-skill` to replicate the pattern
5. Output: Replicated design with documented standards

**Example:**
```
User: "我想做一个像Stripe官网那种支付界面"

→ Call ui-ux-pro-max:
   - Search: "Stripe payment dashboard"
   - Get: Color palette, typography, spacing rules, component patterns
   
→ Call frontend-design-skill:
   - Replicate found pattern
   - Apply to new project
   - Maintain consistency with reference
```

## Path 3: Hybrid Approach

When user wants both creative flair and documented standards:

```markdown
/use design-controller --intent hybrid --reference "STYLE_REFERENCE" --project "PROJECT_DESCRIPTION" --balance "creativity=60&standard=40"
```

**Execution:**
1. Call `ui-ux-pro-max` first to establish design standards
   - Extract color palette, typography, spacing, component library
   - Document all design tokens and rules
2. Call `frontend-design-skill` to lead overall design language
   - Use standards as foundation
   - Apply creative interpretation on top
   - Maintain design system consistency
3. Final output: Creative design with full documentation

**Example:**
```
User: "我要一个有苹果官网那种简洁感，但又要我们自己的一套设计规范"

→ Phase 1 (ui-ux-pro-max):
   - Establish design tokens (colors, type, space)
   - Define component patterns
   - Document design system
   
→ Phase 2 (frontend-design-skill):
   - Lead creative direction
   - Apply creative interpretations
   - Deliver design + documentation
```

## Path 4: Design Standard Extraction

Extract and learn design standards from any URL:

```markdown
/use design-controller --intent extract --url "https://example.com" --output "Store to ui-ux-pro-max"
```

**Execution:**

### Step 4A: Capture Target URL
1. Call `playwright` skill to navigate to URL
2. Capture full-page screenshot
3. Extract all CSS/styling information
4. Get HTML structure and DOM hierarchy

### Step 4B: Analyze Design System
Extract from captured data:
- **Colors**: Primary, secondary, accent, background, text colors
- **Typography**: Font families, sizes, weights, line heights
- **Spacing**: Scale, base unit, responsive breakpoints
- **Components**: Buttons, cards, inputs, navigation patterns
- **Layout**: Grid system, container widths, flex/grid patterns

### Step 4C: Store to Database
Add new standard entry to `ui-ux-pro-max` database:
```json
{
  "source_url": "https://example.com",
  "extracted_date": "2026-01-22",
  "colors": [...],
  "typography": {...},
  "spacing": {...},
  "components": [...],
  "style_category": "detected_category",
  "quality_score": 0.95
}
```

**Example:**
```
User: "帮我分析这个网站的设计规范并存入数据库: https://linear.app"

→ Step 4A: playwright captures:
   - Screenshot: linear-screenshot.png
   - CSS: extracted-styles.json
   - HTML: page-structure.html

→ Step 4B: Analyze extracts:
   - Colors: Dark theme, purple accents (#5E6AD2)
   - Typography: Inter, 14px base, tight tracking
   - Components: Minimal buttons, borderless inputs
   
→ Step 4C: Store to ui-ux-pro-max:
   - New entry: "Linear-style-dark-minimal"
   - All parameters documented
   - Ready for future replication
```

## Workflow Integration

### Context-Aware Routing

The controller maintains context across interactions:

```
Session Start:
  - User: "帮我设计一个SaaS仪表盘" (creative)
  → Path 1: Call frontend-design-skill
  
  - User: "我要像Notion那种简洁风格" (normative)
  → Path 2: Call ui-ux-pro-max → frontend-design-skill
  
  - User: "分析这个网站并存入规范" (extract)
  → Path 4: playwright → analyze → ui-ux-pro-max
```

### Intent Detection Examples

| User Input | Detected Intent | Reasoning |
|------------|-----------------|-----------|
| "随便发挥，设计一个炫酷的页面" | Creative | "随便发挥" = freedom |
| "模仿Airbnb的搜索组件" | Normative | "模仿" = replication |
| "我要独特的风格但要有规范文档" | Hybrid | Both creativity + standards |
| "把这个网站的设计规范提取出来" | Extract | "提取规范" = extraction |

## Output Formats

### Creative Path Output
```markdown
## Creative Design

[Design generated by frontend-design-skill]
- Original concept
- Unique visual language
- No strict reference constraints

Next: Refine based on feedback
```

### Normative Path Output
```markdown
## Normative Replication

Reference: [Source case from ui-ux-pro-max]
- Colors: [...]
- Typography: [...]
- Components: [...]

Design: [Replicated by frontend-design-skill]
- Pattern matched
- Standards documented

Ready for: Implementation
```

### Hybrid Path Output
```markdown
## Hybrid Design

### Design Standards (from ui-ux-pro-max)
- Color palette: [...]
- Typography system: [...]
- Spacing scale: [...]
- Component library: [...]

### Creative Interpretation (from frontend-design-skill)
- Unique design language
- Design system applied
- Full documentation included

Deliverables:
- Design files
- Design tokens (JSON)
- Component specifications
```

### Extract Path Output
```markdown
## Design Standard Extracted

Source: https://example.com
Captured: [screenshot.png]

### Analysis Results
- Colors: [...]
- Typography: [...]
- Components: [...]

### Stored in Database
Entry ID: [new_entry_id]
Category: [style_category]
Quality Score: 0.95

Ready for: Replication via Path 2
```

## Error Handling

| Scenario | Handling |
|----------|----------|
| Sub-skill unavailable | Fallback to alternative path or report error |
| Extraction failed (URL invalid) | Suggest checking URL and retry |
| Pattern not found in database | Offer to extract from URL instead |
| Creative skill needs clarification | Ask user for more details |

## Best Practices

1. **Always clarify intent** before routing
2. **Document decisions** in hybrid workflows
3. **Extract standards** when encountering quality designs
4. **Build the database** over time for better matching
5. **Preserve attribution** when replicating designs
