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
- **Validate remote URLs before adding**

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

### Template Features

- **Professional Structure** - Industry-standard README layout
- **Comprehensive Sections** - All essential information included
- **Easy Customization** - Clear placeholders and sections
- **Best Practices** - Based on top open source projects

### Documentation

See `readme-templates/SKILL.md` for detailed usage guide and examples.
