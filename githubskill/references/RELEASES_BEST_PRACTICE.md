# GitHub Releases Management Best Practice Guide

**归档日期**: 2026-01-22  
**版本**: 1.0.0  
**作者**: Sisyphus AI Agent

---

## 📋 目录

1. [概述](#概述)
2. [实现步骤](#实现步骤)
3. [脚本使用指南](#脚本使用指南)
4. [完整工作流程](#完整工作流程)
5. [最佳实践](#最佳实践)
6. [故障排除](#故障排除)
7. [模板集合](#模板集合)

---

## 概述

本文档记录了为 `githubskill` 添加 GitHub Releases 管理功能的完整实现过程，包括：

- ✅ 查看、创建、上传、删除 Releases
- ✅ 自动化打包脚本（ZIP、TAR.GZ）
- ✅ SHA256 校验和生成
- ✅ 发布说明模板
- ✅ 多平台支持

### 核心功能

| 功能 | 命令/脚本 | 位置 |
|------|-----------|------|
| 查看 Releases | `gh release list` | 内置 |
| 创建 Release | `gh release create` | 内置 |
| 上传资源 | `gh release upload` | 内置 |
| 自动化创建 | `scripts/create-release.sh` | 自定义 |
| 打包仓库 | `scripts/package-release.sh` | 自定义 |

---

## 实现步骤

### 步骤 1: 更新 SKILL.md

在 `githubskill/SKILL.md` 中添加 **## 📦 Releases Management** 章节：

```markdown
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

### Create Releases

**Create a new release:**
```bash
gh release create v1.0.0 --title "Release v1.0.0" --notes "Release notes here"
```

**Create release with automatic generation:**
```bash
gh release create v1.0.0 --generate-notes
```
```

### 步骤 2: 创建自动化脚本

#### 脚本 1: `scripts/create-release.sh`

**功能**: 自动创建 Release 并上传资源

```bash
#!/bin/bash
# Automated GitHub Release Creation Script
# Usage: ./create-release.sh <version> [assets...]

set -e

VERSION=$1
REPO_OWNER=${2:-$(gh repo view --json owner -q .owner.login)}
REPO_NAME=${3:-$(gh repo view --json name -q .name)}

if [ -z "$VERSION" ]; then
    echo "Usage: $0 <version> [assets...]"
    echo "Example: $0 v1.0.0 ./dist.zip"
    exit 1
fi

shift

echo "🚀 Creating release $VERSION for $REPO_OWNER/$REPO_NAME..."

# Create release with auto-generated notes
gh release create "$VERSION" --generate-notes --repo "$REPO_OWNER/$REPO_NAME"

# Upload assets if provided
for asset in "$@"; do
    if [ -f "$asset" ]; then
        gh release upload "$VERSION" "$asset" --repo "$REPO_OWNER/$REPO_NAME"
    fi
done

gh release view "$VERSION" --repo "$REPO_OWNER/$REPO_NAME"
```

#### 脚本 2: `scripts/package-release.sh`

**功能**: 打包仓库为 ZIP 和 TAR.GZ 格式

```bash
#!/bin/bash
# Repository Packaging Script for GitHub Releases
# Usage: ./package-release.sh [version] [output-dir]

set -e

VERSION=${1:-$(date +%Y.%m.%d-%H%M%S)}
REPO_NAME=$(basename $(git rev-parse --show-toplevel 2>/dev/null || echo "project"))
OUTPUT_DIR=${2:-./releases}

mkdir -p "$OUTPUT_DIR"

# Create ZIP
git archive --format zip --output "$OUTPUT_DIR/${REPO_NAME}-${VERSION}.zip" HEAD

# Create TAR.GZ
git archive --format tar.gz --output "$OUTPUT_DIR/${REPO_NAME}-${VERSION}.tar.gz" HEAD

# Generate SHA256 checksums
cd "$OUTPUT_DIR"
for file in *.zip *.tar.gz; do
    [ -f "$file" ] && sha256sum "$file" > "${file}.sha256"
done
```

### 步骤 3: 执行打包和发布

```bash
# 1. 打包仓库
cd /path/to/repo
bash githubskill/scripts/package-release.sh v1.0.0 ./releases

# 2. 创建 Release
gh release create v1.0.0 --title "v1.0.0 Release" --notes "## 🎉 Release Notes"

# 3. 上传资源
gh release upload v1.0.0 ./releases/repo-v1.0.0.zip
gh release upload v1.0.0 ./releases/repo-v1.0.0.tar.gz

# 4. 验证
gh release view v1.0.0
```

---

## 脚本使用指南

### 使用 create-release.sh

```bash
# 基本用法
./githubskill/scripts/create-release.sh v1.0.0

# 带资源上传
./githubskill/scripts/create-release.sh v1.0.0 ./dist.zip ./readme.md

# 指定仓库
./githubskill/scripts/create-release.sh v1.0.0 ./dist.zip owner repo-name
```

### 使用 package-release.sh

```bash
# 使用默认版本（日期时间）
./githubskill/scripts/package-release.sh

# 使用指定版本
./githubskill/scripts/package-release.sh v1.0.0

# 指定输出目录
./githubskill/scripts/package-release.sh v1.0.0 ./artifacts
```

### 输出示例

```
📦 Packaging repository for release...
   Repository: myrepo
   Version: v1.0.0
   Output: ./releases
   Creating archives...
   ✅ myrepo-v1.0.0.zip
   ✅ myrepo-v1.0.0.tar.gz
   Creating clean archives (without .git)...
   ✅ myrepo-v1.0.0-clean.zip
   ✅ myrepo-v1.0.0-clean.tar.gz

📁 Created files in ./releases:
-rw-r--r-- 1 user  3.5M myrepo-v1.0.0.tar.gz
-rw-r--r-- 1 user  3.6M myrepo-v1.0.0.zip

🔐 Generating SHA256 checksums...
   ✅ myrepo-v1.0.0.zip.sha256
   ✅ myrepo-v1.0.0.tar.gz.sha256
```

---

## 完整工作流程

### 自动化完整流程

```bash
#!/bin/bash
# Complete Release Workflow

REPO_NAME="my-project"
VERSION=$1
OUTPUT_DIR="./releases"

echo "🚀 Starting release workflow for $REPO_NAME v$VERSION"

# Step 1: 打包
echo "📦 Step 1: Packaging repository..."
bash githubskill/scripts/package-release.sh $VERSION $OUTPUT_DIR

# Step 2: 创建 Release
echo "📝 Step 2: Creating GitHub Release..."
gh release create "$VERSION" \
    --title "$REPO_NAME v$VERSION" \
    --notes-file CHANGELOG.md \
    --repo owner/repo

# Step 3: 上传资源
echo "📤 Step 3: Uploading assets..."
gh release upload "$VERSION" "$OUTPUT_DIR/$REPO_NAME-$VERSION.zip" --repo owner/repo
gh release upload "$VERSION" "$OUTPUT_DIR/$REPO_NAME-$VERSION.tar.gz" --repo owner/repo

# Step 4: 验证
echo "✅ Step 4: Verifying release..."
gh release view "$VERSION" --repo owner/repo

echo "🎉 Release $VERSION completed successfully!"
```

### 手动完整流程

```bash
# 1. 确保代码已提交
git add .
git commit -m "Prepare for release v1.0.0"
git push origin main

# 2. 标签
git tag v1.0.0
git push origin v1.0.0

# 3. 打包
./githubskill/scripts/package-release.sh v1.0.0 ./releases

# 4. 创建 Release v1.0.0 \
    --title "v1.0.0 Release" \
    --generate-notes \
    --draft
gh release create

# 5. 编辑发布说明（可选）
gh release edit v1.0.0 --notes-file RELEASE_NOTES.md

# 6. 上传资源
gh release upload v1.0.0 ./releases/project-v1.0.0.zip
gh release upload v1.0.0 ./releases/project-v1.0.0.tar.gz

# 7. 发布
gh release edit v1.0.0 --draft=false
```

---

## 最佳实践

### 1. 版本命名规范

```
主版本.次版本.修订版本
v1.0.0  - 首次发布
v1.0.1  - 修订版（Bug修复）
v1.1.0  - 次版本（新功能，向后兼容）
v2.0.0  - 主版本（重大变更，不向后兼容）
```

### 2. 发布说明结构

```markdown
## 🎉 Release v1.0.0

### ✨ New Features
- Feature A description
- Feature B description

### 🐛 Bug Fixes
- Fixed issue #123
- Fixed issue #456

### 📦 Included Skills
- Skill 1 description
- Skill 2 description

### 🚀 Quick Start
```bash
git clone https://github.com/user/repo.git
```

### 🔗 Links
- [Documentation](./README.md)
- [Changelog](./CHANGELOG.md)
```

### 3. 资产命名规范

```
{project}-{version}-{platform}.{extension}

示例:
project-v1.0.0-linux-x64.zip
project-v1.0.0-macos-arm64.tar.gz
project-v1.0.0-windows-x64.exe
```

### 4. 必备资源

| 格式 | 用途 | 大小 |
|------|------|------|
| `.zip` | Windows/macOS 用户 | 中 |
| `.tar.gz` | Linux/开发者 | 小 |
| `.sha256` | 完整性验证 | 极小 |

### 5. 发布前检查清单

- [ ] 所有代码已提交并推送
- [ ] 标签已创建并推送
- [ ] 发布说明已编写
- [ ] 资源文件已生成
- [ ] SHA256 校验和已生成
- [ ] 测试通过
- [ ] 文档已更新
- [ ] 发布说明链接正确

---

## 故障排除

### 问题 1: gh 命令未找到

**错误**:
```
gh: command not found
```

**解决方案**:
```bash
# 安装 GitHub CLI
# macOS
brew install gh

# Linux
sudo apt install gh

# Windows
winget install GitHub.cli
```

### 问题 2: 未认证

**错误**:
```
Authentication required
```

**解决方案**:
```bash
# 登录 GitHub
gh auth login

# 检查认证状态
gh auth status
```

### 问题 3: 仓库不存在

**错误**:
```
HTTP 404: Not Found
```

**解决方案**:
```bash
# 检查仓库地址
gh repo view owner/repo

# 如果是私有仓库，确保有访问权限
gh repo view owner/repo --json visibility
```

### 问题 4: 标签已存在

**错误**:
```
a tag with name v1.0.0 already exists
```

**解决方案**:
```bash
# 删除本地标签
git tag -d v1.0.0

# 删除远程标签
git push origin :refs/tags/v1.0.0

# 或者使用新版本号
gh release create v1.0.1 ...
```

### 问题 5: 资源上传失败

**错误**:
```
release asset upload failed
```

**解决方案**:
```bash
# 检查文件是否存在
ls -la ./releases/project-v1.0.0.zip

# 检查文件大小（限制 2GB）
du -h ./releases/project-v1.0.0.zip

# 重新上传
gh release upload v1.0.0 ./releases/project-v1.0.0.zip --clobber
```

### 问题 6: git archive 失败

**错误**:
```
fatal: pathspec '.gitignore' did not match any files
```

**解决方案**:
修改脚本，移除 `.gitignore` 检查：

```bash
# 不使用排除模式，直接创建完整归档
git archive --format zip --output "$OUTPUT_DIR/${REPO_NAME}-${VERSION}.zip" HEAD
```

---

## 模板集合

### 发布说明模板

详见: [templates/release-notes-template.md](templates/release-notes-template.md)

### 自动化脚本模板

详见:
- [scripts/templates/create-release-template.sh](scripts/templates/create-release-template.sh)
- [scripts/templates/package-release-template.sh](scripts/templates/package-release-template.sh)

---

## 相关资源

- [GitHub CLI 文档](https://cli.github.com/manual/)
- [创建 Releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)
- [自动化发布](https://docs.github.com/en/actions/deployment/about-deployments/deploying-with-github-actions)

---

## 更新日志

| 版本 | 日期 | 描述 |
|------|------|------|
| 1.0.0 | 2026-01-22 | 初始版本，记录完整实现过程 |

---

**文档结束** 🎉
