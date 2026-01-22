# Design Workflow Guides

## Table of Contents

1. [Requirement Analysis](#requirement-analysis)
2. [Approach Classification](#approach-classification)
3. [Workflow Execution](#workflow-execution)
4. [Database Operations](#database-operations)
5. [Quality Standards](#quality-standards)

## Requirement Analysis

### Key Questions to Ask

When receiving a design request, determine:

1. **Design Goals**
   - What is the purpose of this design?
   - What problem does it solve?
   - Who is the target audience?

2. **Constraints**
   - Are there brand guidelines to follow?
   - Are there existing design patterns to maintain?
   - Are there technical limitations?

3. **Success Criteria**
   - What does a successful design look like?
   - What metrics will measure success?
   - Who will approve the design?

### Requirement Checklist

- [ ] Design type (landing page, dashboard, mobile app, etc.)
- [ ] Target platform (web, mobile, tablet)
- [ ] Brand identity requirements
- [ ] Accessibility requirements
- [ ] Performance constraints
- [ ] Timeline and deliverables

## Approach Classification

### Classification Criteria

| Criteria | Creative | Standardized | Hybrid |
|----------|----------|--------------|--------|
| Uniqueness priority | High | Low | Medium |
| Standards priority | Low | High | Medium |
| Reference availability | None | Required | Preferred |
| Brand customization | Extensive | Minimal | Moderate |
| Time investment | Variable | Predictable | Moderate |

### Classification Triggers

**Creative Direction Triggers**:
- "unique", "creative", "innovative", "stand out"
- "distinctive", "memorable", "eye-catching"
- No specific reference sites mentioned

**Standardized Direction Triggers**:
- "follow guidelines", "consistent with"
- "like [specific company/framework]"
- "standard", "规范", "规范"
- Reference to Material Design, Apple HIG, etc.

**Hybrid Direction Triggers**:
- "professional yet unique"
- "standard base with creative touch"
- "brand identity within guidelines"
- Combines both creativity and standards language

## Workflow Execution

### Creative Workflow

```
1. Collect design requirements
2. Brainstorm design concepts (3-5 directions)
3. Select best concept direction
4. Develop design with frontend-design
5. Iterate based on feedback
6. Finalize and deliver
```

### Standardized Workflow

```
1. Collect design requirements
2. Query ui-ux-pro-max database
3. Find matching design patterns
4. Select best pattern match
5. Replicate pattern with adjustments
6. Verify consistency
7. Deliver design solution
```

### Hybrid Workflow

```
1. Collect design requirements
2. Establish design standards (ui-ux-pro-max)
3. Identify customization opportunities
4. Apply creative enhancements (frontend-design)
5. Balance standards and creativity
6. Finalize and deliver
```

## Database Operations

### Adding a New Design Pattern

**Input**: URL of a design to analyze

**Process**:
1. Call Playwright to capture page screenshot
2. Extract CSS and design tokens
3. Identify color palette
4. Document typography system
5. Map component patterns
6. Store in database

**Output**: Complete design pattern entry

### Searching Design Patterns

**Query types**:
- By design style (minimalist, brutalist, etc.)
- By component type (buttons, forms, cards)
- By color scheme (dark, light, colorful)
- By industry (SaaS, e-commerce, portfolio)

### Pattern Matching

Match user requirements to database patterns using:
1. Style similarity scoring
2. Component type matching
3. Color scheme comparison
4. Layout pattern recognition

## Quality Standards

### Creative Design Quality

- **Originality**: Design should be distinctive
- **Visual impact**: Strong visual hierarchy
- **User engagement**: Encourages interaction
- **Brand alignment**: Reflects brand personality

### Standardized Design Quality

- **Consistency**: Follows established patterns
- **Usability**: Meets usability standards
- **Accessibility**: WCAG compliant
- **Maintainability**: Easy to update and scale

### Hybrid Design Quality

- **Balance**: Harmonizes standards with creativity
- **Professionalism**: Maintains credibility
- **Innovation**: Adds unique value
- **Adaptability**: Works across contexts

## Common Patterns

### Landing Page Patterns
- Hero section with CTA
- Feature grid layout
- Testimonial slider
- Pricing table
- Footer with navigation

### Dashboard Patterns
- Sidebar navigation
- Header with user menu
- Data visualization cards
- Table with sorting/filtering
- Form layout patterns

### Mobile App Patterns
- Bottom navigation bar
- Card-based content
- Swipeable carousels
- Form input patterns
- Modal dialogs
