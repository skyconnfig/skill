---
name: design-workflow
description: Intelligent design workflow management system that routes design requests to appropriate design strategies based on project requirements. Supports three design approaches: Creative (frontend-design for unique designs), Standardized (ui-ux-pro-max database for case replication), and Hybrid (combining standards with creative direction). Includes a design pattern database that captures and stores design specifications from URLs using Playwright.
---

# Design Workflow Management System

## Quick Start

1. **Understand user requirements** - Determine design goals and constraints
2. **Classify design approach** - Creative, Standardized, or Hybrid
3. **Execute appropriate workflow** - Route to corresponding design strategy
4. **Deliver design solution** - Complete the design task

## Design Approach Classification

### Creative Direction (创意方向)

**When to use**:
- User wants unique, distinctive design
- No specific design constraints or reference sites
- Phrases like "creative", "unique", "innovative", "make it stand out"

**Workflow**:
1. Call `frontend-design` skill
2. Provide design requirements and goals
3. Allow creative freedom within project scope

### Standardized Direction (规范方向)

**When to use**:
- User emphasizes consistency and standards
- Needs to replicate existing design patterns
- Phrases like "standard", "consistent", "follow guidelines", "like [site]"

**Workflow**:
1. Call `ui-ux-pro-max` skill
2. Query design pattern database for matching cases
3. Replicate the selected design pattern

### Hybrid Direction (混合方向)

**When to use**:
- User wants both creativity and standardization
- Needs foundational standards with creative enhancements
- Phrases like "professional yet unique", "standard base with creative touch"

**Workflow**:
1. Call `ui-ux-pro-max` to establish design standards
2. Use `frontend-design` to enhance and customize the standards
3. Deliver refined design solution

## Design Pattern Database

### Adding New Patterns

To capture and store a new design pattern:

1. **Input**: Provide a URL to analyze
2. **Capture**: Use Playwright to screenshot the page
3. **Extract**: Analyze CSS and design tokens
4. **Store**: Save to the design pattern database

### Database Structure

Each design pattern includes:
- **Visual reference**: Screenshot of the design
- **Color palette**: Primary, secondary, accent colors
- **Typography**: Font families, sizes, weights
- **Spacing system**: Margins, padding, grid gaps
- **Component patterns**: Button styles, form inputs, cards
- **Responsive behavior**: Breakpoints and adaptations

## Usage Examples

### Example 1: Creative Request

User says: "Create a landing page that stands out with unique visuals"

```
→ Classify as Creative Direction
→ Call frontend-design with requirements
→ Deliver distinctive, creative design solution
```

### Example 2: Standardized Request

User says: "Make our dashboard follow Material Design guidelines"

```
→ Classify as Standardized Direction
→ Call ui-ux-pro-max to find Material Design pattern
→ Replicate the standardized pattern
→ Deliver consistent, guideline-compliant design
```

### Example 3: Hybrid Request

User says: "Create a professional design that follows Apple HIG but has our brand identity"

```
→ Classify as Hybrid Direction
→ Call ui-ux-pro-max to establish Apple HIG standards
→ Call frontend-design to incorporate brand identity
→ Deliver professional design with unique brand elements
```

## Integration with Other Skills

This skill coordinates with:

- **frontend-design**: For creative design execution
- **ui-ux-pro-max**: For standardized design patterns and replication
- **playwright**: For capturing and analyzing design patterns from URLs

## Workflow Scripts

### database_manager.py

Manages the design pattern database:
- Add new design patterns
- Search and retrieve patterns
- Query patterns by category

### page_analyzer.py

Analyzes web pages to extract design specifications:
- Captures screenshots
- Extracts CSS variables and design tokens
- Identifies component patterns

See [WORKFLOW_GUIDES.md](references/WORKFLOW_GUIDES.md) for detailed workflow documentation.
See [DESIGN_PATTERNS.md](references/DESIGN_PATTERNS.md) for design pattern database schema and examples.
