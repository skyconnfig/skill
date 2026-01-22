# Design Databases

This directory contains design system databases stored according to the ui-ux-pro-max skill specifications.

## Directory Structure

```
design-databases/
├── README.md                    # This file
├── apple-china/                 # Apple China Design System
│   ├── README.md               # Design system overview
│   ├── INDEX.md                # Searchable index
│   ├── DESIGN_SYSTEM.md        # Complete documentation
│   ├── design-tokens.json      # Design tokens (JSON)
│   └── apple-china-vars.css    # CSS variables
└── template/                   # Template for new design databases
    ├── README.md
    ├── INDEX.md
    ├── DESIGN_SYSTEM.md
    ├── design-tokens.json
    └── template-vars.css
```

## Adding a New Design Database

### 1. Create Directory Structure
```bash
mkdir -p design-databases/[design-name]
```

### 2. Copy Template
```bash
cp -r design-databases/template/* design-databases/[design-name]/
```

### 3. Update Files
- Update `README.md` with design system name and overview
- Update `INDEX.md` with relevant keywords and search terms
- Update `DESIGN_SYSTEM.md` with complete design specifications
- Update `design-tokens.json` with design tokens
- Update `template-vars.css` with CSS custom properties

### 4. Add to Search
The design database will be automatically indexed for search if it follows the structure:
- Has a `design-tokens.json` file
- Has a `README.md` file
- Contains appropriate metadata

## Design Database Structure

### Required Files

#### 1. README.md
Contains:
- Design system overview
- Product type and industry
- Design style tags
- Quick reference information
- Integration examples

#### 2. INDEX.md
Contains:
- Searchable index with keywords
- Quick reference table
- File structure documentation
- Usage examples
- Related design systems

#### 3. DESIGN_SYSTEM.md
Contains:
- Complete design specifications
- Color palette
- Typography system
- Spacing system
- Component styles
- Effects and animations
- Accessibility guidelines
- Usage examples for all tech stacks

#### 4. design-tokens.json
Contains:
- Design tokens in JSON format
- Color tokens
- Typography tokens
- Spacing tokens
- Component tokens
- Effect tokens
- Accessibility tokens

#### 5. [name]-vars.css
Contains:
- CSS custom properties
- All design tokens as CSS variables
- Utility classes (optional)
- Media queries (optional)

## Naming Conventions

### Directory Name
- Use kebab-case: `apple-china`, `material-design`, `fluent-design`
- Use lowercase letters only
- Use hyphens to separate words

### File Names
- `README.md` - Required
- `INDEX.md` - Required
- `DESIGN_SYSTEM.md` - Required
- `design-tokens.json` - Required
- `[name]-vars.css` - Required (where [name] matches directory name)

### CSS Variable Names
- Use kebab-case: `--color-primary`, `--font-size-h1`
- Prefix with design system identifier: `--apple-blue`, `--material-shadow`
- Group related variables: `--color-*`, `--font-*`, `--spacing-*`

### JSON Property Names
- Use camelCase: `primaryColor`, `fontSize`
- Group related properties: `colors`, `typography`, `spacing`

## Metadata Requirements

### design-tokens.json
```json
{
  "name": "Design System Name",
  "version": "1.0.0",
  "description": "Brief description",
  "productType": "Technology/SaaS/E-commerce/etc.",
  "industry": "Industry category",
  "styleTags": ["style1", "style2"],
  "colorTags": ["color1", "color2"],
  "fontTags": ["font1", "font2"]
}
```

## Search Optimization

### Keywords to Include
Include relevant keywords in `INDEX.md` for better search results:

- **By Style**: modern, minimal, clean, material, flat, neumorphism, etc.
- **By Color**: primary colors, accent colors, dark mode, light mode
- **By Typography**: serif, sans-serif, monospace, display fonts
- **By Component**: buttons, forms, cards, navigation, modals
- **By Use Case**: landing page, dashboard, e-commerce, blog
- **By Industry**: technology, healthcare, finance, education

### Tag Format
```markdown
## Search Tags

### By Style
- modern, minimal, clean, material, flat

### By Color
- primary blue, dark mode, light mode

### By Industry
- technology, saas, enterprise
```

## Validation Checklist

Before adding a new design database, ensure:

- [ ] All required files are present
- [ ] JSON is valid (no syntax errors)
- [ ] CSS variables follow naming conventions
- [ ] All links in documentation are valid
- [ ] Code examples are accurate
- [ ] Design tokens are complete
- [ ] Accessibility guidelines are included
- [ ] Multiple tech stack examples are provided
- [ ] Search keywords are comprehensive
- [ ] README provides clear overview

## Best Practices

### 1. Design Tokens
- Use meaningful names
- Group related tokens
- Include units where applicable
- Provide default values

### 2. CSS Variables
- Use CSS custom properties
- Group by category
- Include fallback values
- Support dark mode (if applicable)

### 3. Documentation
- Be comprehensive but clear
- Include visual examples
- Provide copy-paste ready code
- Explain design rationale

### 4. Search Optimization
- Use consistent terminology
- Include common search terms
- Cross-reference related systems
- Provide usage examples

## Integration with ui-ux-pro-max

The design databases in this directory are designed to work with the ui-ux-pro-max skill:

### Search
```bash
python3 scripts/search.py "query" --design-system
```

### Design System Output
```bash
python3 scripts/search.py "query" --design-system -f markdown
```

### Domain-Specific Search
```bash
python3 scripts/search.py "query" --domain colors
python3 scripts/search.py "query" --domain typography
python3 scripts/search.py "query" --domain layout
```

## Contributing

To contribute a new design database:

1. Follow the directory structure and naming conventions
2. Complete all required files
3. Validate against the checklist
4. Test integration with ui-ux-pro-max
5. Submit a pull request (if applicable)

## Support

For questions about:
- Adding new design databases: See Contributing section
- Using existing databases: See individual design system README
- ui-ux-pro-max skill: See `../SKILL.md`

---

**Directory Version**: 1.0.0
**Last Updated**: 2026-01-22
**Based On**: ui-ux-pro-max Skill Specifications
