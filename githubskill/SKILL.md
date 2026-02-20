---
name: githubskill
description: Comprehensive GitHub repository management and git operations skill. Use when user wants to manage GitHub repositories including cloning, initializing local repositories, basic git workflow (status, add, commit, log), branch management (branch, checkout, merge, delete), remote operations (remote, pull, push, fetch), undo/rollback operations (reset, checkout), and advanced git tools (stash, rebase). Handles GitHub URL parsing, repository updates, and all standard git commands.
---

# GitHub Skill

Execute git commands for repository management, version control, and collaboration workflows.

## Core Operations

### Repository Setup

**Initialize local repository:**
```bash
git init
```

**Clone remote repository:**
```bash
git clone <url>
```

**Parse GitHub URL:**
Extract repo info from GitHub URLs (https://github.com/user/repo, git@github.com:user/repo.git)

### Basic Workflow

**Check repository status:**
```bash
git status
```

**Stage files:**
```bash
git add <file>              # Add specific file
git add .                   # Add all files
```

**Commit changes:**
```bash
git commit -m "提交信息"
```

**View commit history:**
```bash
git log --oneline
```

### Branch Management

**View branches:**
```bash
git branch
```

**Create and switch to new branch:**
```bash
git checkout -b <branch-name>
# or
git switch -c <branch-name>
```

**Switch branches:**
```bash
git checkout <branch-name>
# or
git switch <branch-name>
```

**Merge branches:**
```bash
git merge <branch-name>
```

**Delete branch:**
```bash
git branch -d <branch-name>  # Safe delete
git branch -D <branch-name>  # Force delete
```

### Remote Operations

**Add remote repository:**
```bash
git remote add origin <url>
```

**Pull updates:**
```bash
git pull origin <branch>
```

**Push changes:**
```bash
git push origin <branch>
```

**Push to new branch:**
```bash
git push -u origin <branch-name>
```

**Fetch without merge:**
```bash
git fetch
```

**View remote repositories:**
```bash
git remote -v
```

### Undo and Rollback

**Unstage files:**
```bash
git reset HEAD <file>
```

**Discard working directory changes:**
```bash
git checkout -- <file>
```

**Reset to specific commit:**
```bash
git reset --hard <commit-id>  # WARNING: Loses all uncommitted changes
git reset --soft <commit-id>  # Keeps changes in staging area
```

### Advanced Tools

**Stash changes:**
```bash
git stash                    # Save uncommitted changes
git stash pop                # Restore stashed changes
git stash list               # View stash history
```

**Rebase:**
```bash
git rebase <branch>          # Rebase current branch onto target
git rebase -i <commit>       # Interactive rebase
```

## Common Workflows

### Initial Setup for New Repository
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <url>
git push -u origin main
```

### Feature Development Workflow
```bash
git checkout -b feature-name
# Make changes
git add .
git commit -m "Add feature"
git push -u origin feature-name
# After review, merge to main
git checkout main
git pull origin main
git merge feature-name
git push origin main
```

### Sync with Remote
```bash
git fetch
git pull origin main
# Make changes and push
```

## Error Handling

- **Remote already exists**: Use `git remote set-url origin <new-url>` instead
- **Merge conflicts**: Manual resolution required, show conflicts to user
- **Detached HEAD**: Recommend `git checkout <branch>` to recover
- **Permission errors**: Check SSH key or token authentication

## Safety Guidelines

- **NEVER use --force on shared branches** without explicit user confirmation
- **Always confirm before destructive operations** (reset --hard, branch deletion)
- **Warn before operations that may lose data**
- **Validate remote URLs before adding`

## 📝 README Templates

This skill includes a comprehensive README template collection for creating professional GitHub project documentation.

### Quick Start

```bash
# Navigate to templates directory
cd githubskill/readme-templates

# Copy template to your project
cp README.md /path/to/your/project/README.md

# Customize for your project
```

### Available Templates

| Template | Use Case |
|----------|----------|
| `readme-templates/README.md` | Full-featured template for open source projects |
| `readme-templates/README-simple.md` | Minimalist template for small projects |
| `readme-templates/README-cli.md` | CLI tool focused template |
| `readme-templates/README-webapp.md` | Web application template |
| `readme-templates/multilingual/README-multilingual.md` | **Bilingual (EN/CN) template** |
| `readme-templates/multilingual/README_CN-multilingual.md` | **Chinese version of bilingual template** |
| `readme-templates/multilingual/GUIDE.md` | **Implementation guide for bilingual README** |

### Template Features

- **Professional Structure** - Industry-standard README layout
- **Comprehensive Sections** - All essential information included
- **Easy Customization** - Clear placeholders and sections
- **Best Practices** - Based on top open source projects
- **Bilingual Support** - English and Chinese versions included

### Documentation

See `readme-templates/SKILL.md` for detailed usage guide and examples.

### 🇨🇳 Multilingual README Support

This skill now includes comprehensive support for creating bilingual README files in English and Chinese!

#### What's Included

**For English README:**
```
readme-templates/multilingual/README-multilingual.md
```

**For Chinese README:**
```
readme-templates/multilingual/README_CN-multilingual.md
```

**Implementation Guide:**
```
readme-templates/multilingual/GUIDE.md
```

#### Quick Start for Bilingual README

```bash
# Navigate to multilingual templates
cd githubskill/readme-templates/multilingual

# Copy both templates to your project
cp README-multilingual.md /your-project/README.md
cp README_CN-multilingual.md /your-project/README_CN.md

# Customize both files with your project details
```

#### Features

- ✅ Professional bilingual templates (EN/CN)
- ✅ Consistent structure and formatting
- ✅ Cross-links between language versions
- ✅ Detailed implementation guide
- ✅ Best practices and examples
- ✅ SEO optimized for both languages

#### Use Cases

- **Open source projects** targeting global audience
- **Commercial products** in Chinese market
- **Developer tools** with international users
- **Any project** expecting Chinese contributors

#### Documentation

See `readme-templates/SKILL.md` for comprehensive implementation guide including:
- Step-by-step setup instructions
- Best practices
- Common mistakes to avoid
- Advanced techniques
- Real-world examples

## 📦 Releases Management

Create, manage, and publish GitHub Releases with automated packaging and upload capabilities.

### View Releases

**List all releases:**
```bash
gh release list
```

**View specific release details:**
```bash
gh release view <tag>
```

**Download release assets:**
```bash
gh release download <tag> --pattern "*.zip"
```

### Create Releases

**Create a new release:**
```bash
gh release create v1.0.0 --title "Release v1.0.0" --notes "Release notes here"
```

**Create release with automatic generation from commits:**
```bash
gh release create v1.0.0 --generate-notes
```

**Create release with draft mode:**
```bash
gh release create v1.0.0 --draft --title "Draft Release"
```

**Create prerelease:**
```bash
gh release create v1.0.0-beta --prerelease --title "Beta Release"
```

### Upload Assets

**Upload file to release:**
```bash
gh release upload v1.0.0 ./path/to/asset.zip
```

**Upload multiple files:**
```bash
gh release upload v1.0.0 ./file1.zip ./file2.tar.gz
```

**Replace existing asset:**
```bash
gh release upload v1.0.0 ./new-asset.zip --clobber
```

### Delete Releases

**Delete a release (keeps tag):**
```bash
gh release delete v1.0.0
```

**Delete release and tag:**
```bash
gh release delete v1.0.0 --cleanup-tag
```

### Automation Scripts

This skill includes automation scripts for common release workflows:

**`scripts/create-release.sh`** - Automated release creation
```bash
#!/bin/bash
VERSION=$1
ASSETS=("${@:2}")

# Create release with auto-generated notes
gh release create "$VERSION" --generate-notes

# Upload all provided assets
for asset in "${ASSETS[@]}"; do
    gh release upload "$VERSION" "$asset"
done

echo "Release $VERSION created successfully!"
```

**`scripts/package-release.sh`** - Package repository for release
```bash
#!/bin/bash
VERSION=$1
REPO_NAME=${2:-$(basename $(git rev-parse --show-toplevel))}

# Create archive
git archive --format=zip --output="${REPO_NAME}-${VERSION}.zip" HEAD
git archive --format=tar.gz --output="${REPO_NAME}-${VERSION}.tar.gz" HEAD

echo "Packaged ${REPO_NAME}-${VERSION}.zip and .tar.gz"
```

### Release Best Practices

1. **Semantic Versioning**: Use semantic versioning (v1.0.0, v1.0.1, v2.0.0)
2. **Draft First**: Create as draft, review, then publish
3. **Asset Naming**: Use clear, descriptive asset names (e.g., `project-v1.0.0-linux-x64.zip`)
4. **Release Notes**: Include What's Changed, New Features, Bug Fixes, Known Issues
5. **Multiple Assets**: Provide archives for different platforms (zip, tar.gz)
6. **Security**: Sign releases with GPG for verification

### Example Workflow

```bash
# 1. Package the release
./scripts/package-release.sh v1.0.0

# 2. Create release with notes
gh release create v1.0.0 --title "v1.0.0 Release" --notes-file CHANGELOG.md

# 3. Upload packaged assets
gh release upload v1.0.0 project-v1.0.0.zip
gh release upload v1.0.0 project-v1.0.0.tar.gz

# 4. View the release
gh release view v1.0.0

# 5. If satisfied, publish (or use --draft=false initially)
gh release edit v1.0.0 --draft=false
```
