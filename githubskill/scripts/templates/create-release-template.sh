#!/bin/bash
#===============================================================================
# GitHub Release Creation Template
# 
# Template for automated GitHub release creation with asset upload
# 
# Usage:
#   ./create-release-template.sh <version> [repo-owner] [repo-name] [assets...]
# 
# Examples:
#   ./create-release-template.sh v1.0.0
#   ./create-release-template.sh v1.0.0 myorg myrepo ./dist.zip
#   ./create-release-template.sh v1.0.0 myorg myrepo ./dist.zip ./readme.md
#===============================================================================

set -euo pipefail

# 配置变量
: "${VERSION:?❌ 请指定版本号，例如: v1.0.0}"
: "${REPO_OWNER:=$(gh repo view --json owner -q .owner.login 2>/dev/null || echo "")}"
: "${REPO_NAME:=$(gh repo view --json name -q .name 2>/dev/null || echo "")}"

# 解析参数
VERSION="$1"
REPO_OWNER="${2:-$REPO_OWNER}"
REPO_NAME="${3:-$REPO_NAME}"
shift $(( $# > 3 ? 3 : 0 ))

# 验证必要参数
if [ -z "$REPO_OWNER" ] || [ -z "$REPO_NAME" ]; then
    echo "❌ 错误: 无法自动检测仓库信息"
    echo ""
    echo "使用方法:"
    echo "  $0 <version> [repo-owner] [repo-name] [assets...]"
    echo ""
    echo "示例:"
    echo "  $0 v1.0.0                          # 使用当前仓库，自动上传资源"
    echo "  $0 v1.0.0 myorg myrepo             # 指定仓库"
    echo "  $0 v1.0.0 myorg myrepo ./dist.zip  # 指定仓库和资源"
    exit 1
fi

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 输出函数
log_info() { echo -e "${BLUE}ℹ️  $1${NC}"; }
log_success() { echo -e "${GREEN}✅ $1${NC}"; }
log_warn() { echo -e "${YELLOW}⚠️  $1${NC}"; }
log_error() { echo -e "${RED}❌ $1${NC}"; }

# 横幅
print_banner() {
    echo ""
    echo "🚀 GitHub Release Creator"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "   版本: $VERSION"
    echo "   仓库: $REPO_OWNER/$REPO_NAME"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
}

# 主函数
main() {
    print_banner
    
    local start_time=$(date +%s)
    
    # Step 1: 检查 GitHub CLI
    log_info "检查 GitHub CLI..."
    if ! command -v gh &> /dev/null; then
        log_error "GitHub CLI 未安装"
        log_info "安装方式: https://cli.github.com/manual/installation"
        exit 1
    fi
    log_success "GitHub CLI 已安装 ($(gh --version | head -n1))"
    
    # Step 2: 检查认证
    log_info "检查 GitHub 认证状态..."
    if ! gh auth status &> /dev/null; then
        log_warn "未登录 GitHub，请运行: gh auth login"
        log_info "或者设置 GITHUB_TOKEN 环境变量"
        exit 1
    fi
    log_success "GitHub 认证通过"
    
    # Step 3: 检查仓库是否存在
    log_info "检查仓库 $REPO_OWNER/$REPO_NAME..."
    if ! gh repo view "$REPO_OWNER/$REPO_NAME" &> /dev/null; then
        log_error "仓库不存在: $REPO_OWNER/$REPO_NAME"
        exit 1
    fi
    log_success "仓库存在"
    
    # Step 4: 检查标签是否已存在
    log_info "检查标签 $VERSION 是否已存在..."
    if gh release view "$VERSION" --repo "$REPO_OWNER/$REPO_NAME" &> /dev/null; then
        log_warn "标签 $VERSION 已存在"
        read -p "是否要替换? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            log_info "已取消"
            exit 0
        fi
        # 删除现有标签
        gh release delete "$VERSION" --repo "$REPO_OWNER/$REPO_NAME" -y || true
        git push origin ":refs/tags/$VERSION" 2>/dev/null || true
    fi
    log_success "标签检查完成"
    
    # Step 5: 创建 Release
    log_info "创建 Release $VERSION..."
    local release_url=$(gh release create "$VERSION" \
        --title "$VERSION Release" \
        --generate-notes \
        --repo "$REPO_OWNER/$REPO_NAME" \
        --json url -q .url)
    
    if [ -z "$release_url" ]; then
        log_error "创建 Release 失败"
        exit 1
    fi
    log_success "Release 创建成功: $release_url"
    
    # Step 6: 上传资源
    if [ $# -gt 0 ]; then
        log_info "上传资源文件..."
        for asset in "$@"; do
            if [ -f "$asset" ]; then
                local file_size=$(du -h "$asset" | cut -f1)
                log_info "  📤 上传: $asset ($file_size)"
                gh release upload "$VERSION" "$asset" \
                    --repo "$REPO_OWNER/$REPO_NAME" \
                    --clobber
                log_success "  ✅ 已上传: $asset"
            else
                log_warn "  ⚠️  文件不存在: $asset"
            fi
        done
    else
        log_info "未指定资源文件，跳过上传"
    fi
    
    # Step 7: 显示结果
    local end_time=$(date +%s)
    local duration=$((end_time - start_time))
    
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    log_success "Release 创建完成!"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "📦 Release 信息:"
    echo "   URL: $release_url"
    echo "   标签: $VERSION"
    echo "   用时: ${duration}秒"
    echo ""
    echo "🔗 访问链接:"
    echo "   $release_url"
    echo ""
    
    # Step 8: 提示后续操作
    echo "📝 建议后续操作:"
    echo "   1. 编辑发布说明: gh release edit $VERSION --repo $REPO_OWNER/$REPO_NAME"
    echo "   2. 发布 Release: gh release edit $VERSION --draft=false --repo $REPO_OWNER/$REPO_NAME"
    echo ""
}

# 执行主函数
main "$@"
