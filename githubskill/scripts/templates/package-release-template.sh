#!/bin/bash
#===============================================================================
# Repository Packaging Template
# 
# Template for packaging repository archives with checksums
# 
# Usage:
#   ./package-release-template.sh [version] [output-dir]
# 
# Examples:
#   ./package-release-template.sh                    # 使用自动版本号
#   ./package-release-template.sh v1.0.0             # 指定版本号
#   ./package-release-template.sh v1.0.0 ./artifacts # 指定版本和输出目录
#===============================================================================

set -euo pipefail

# 配置变量
: "${VERSION:=$(date +%Y.%m.%d-%H%M%S)}"
: "${REPO_NAME:=$(basename $(git rev-parse --show-toplevel 2>/dev/null || echo "project"))}"
: "${OUTPUT_DIR:="${2:-./releases}}"

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# 输出函数
log_info() { echo -e "${BLUE}ℹ️  $1${NC}"; }
log_success() { echo -e "${GREEN}✅ $1${NC}"; }
log_warn() { echo -e "${YELLOW}⚠️  $1${NC}"; }
log_error() { echo -e "${RED}❌ $1${NC}"; }
log_header() { echo -e "\n${CYAN}$1${NC}\n"; }

# 横幅
print_banner() {
    echo ""
    echo "📦 Repository Packager"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "   项目: $REPO_NAME"
    echo "   版本: $VERSION"
    echo "   输出: $OUTPUT_DIR"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
}

# 格式化大小
format_size() {
    local size=$1
    if [ $size -ge 1048576 ]; then
        echo "$(echo "scale=2; $size/1048576" | bc)MB"
    elif [ $size -ge 1024 ]; then
        echo "$(echo "scale=2; $size/1024" | bc)KB"
    else
        echo "${size}B"
    fi
}

# 主函数
main() {
    print_banner
    
    local start_time=$(date +%s)
    local files_created=()
    
    # Step 1: 创建输出目录
    log_info "创建输出目录..."
    mkdir -p "$OUTPUT_DIR"
    log_success "目录已创建: $OUTPUT_DIR"
    
    # Step 2: 检查 git 仓库
    log_info "检查 Git 仓库..."
    if ! git rev-parse --git-dir > /dev/null 2>&1; then
        log_error "当前目录不是 Git 仓库"
        exit 1
    fi
    log_success "Git 仓库: $(git rev-parse --show-toplevel)"
    
    # Step 3: 获取仓库信息
    log_info "仓库信息:"
    echo "   名称: $REPO_NAME"
    echo "   分支: $(git branch --show-current)"
    echo "   提交: $(git rev-parse --short HEAD)"
    echo "   提交者: $(git log -1 --format='%an')"
    
    # Step 4: 创建归档文件
    log_header "📦 创建归档文件"
    
    # ZIP 归档
    local zip_file="${OUTPUT_DIR}/${REPO_NAME}-${VERSION}.zip"
    log_info "创建 ZIP 归档..."
    git archive --format zip \
        --output "$zip_file" \
        HEAD \
        --prefix="${REPO_NAME}-${VERSION}/"
    
    if [ -f "$zip_file" ]; then
        local zip_size=$(stat -f%z "$zip_file" 2>/dev/null || stat -c%s "$zip_file" 2>/dev/null)
        log_success "ZIP 已创建: $(basename $zip_file) ($(format_size $zip_size))"
        files_created+=("$zip_file")
    fi
    
    # TAR.GZ 归档
    local tar_file="${OUTPUT_DIR}/${REPO_NAME}-${VERSION}.tar.gz"
    log_info "创建 TAR.GZ 归档..."
    git archive --format tar.gz \
        --output "$tar_file" \
        HEAD \
        --prefix="${REPO_NAME}-${VERSION}/"
    
    if [ -f "$tar_file" ]; then
        local tar_size=$(stat -f%z "$tar_file" 2>/dev/null || stat -c%s "$tar_file" 2>/dev/null)
        log_success "TAR.GZ 已创建: $(basename $tar_file) ($(format_size $tar_size))"
        files_created+=("$tar_file")
    fi
    
    # Step 5: 生成校验和
    log_header "🔐 生成 SHA256 校验和"
    
    for file in "${files_created[@]}"; do
        if [ -f "$file" ]; then
            local checksum_file="${file}.sha256"
            sha256sum "$file" > "$checksum_file"
            local hash=$(head -c 64 "$checksum_file")
            log_success "校验和已生成: $(basename $checksum_file)"
            echo "   Hash: $hash"
        fi
    done
    
    # Step 6: 生成文件列表
    log_header "📁 输出文件列表"
    
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    printf "   %-45s %10s\n" "文件名" "大小"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    
    ls -lh "$OUTPUT_DIR" | tail -n +2 | while read -r line; do
        local name=$(echo "$line" | awk '{print $9}')
        local size=$(echo "$line" | awk '{print $5}')
        printf "   %-45s %10s\n" "$name" "$size"
    done
    
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    
    # Step 7: 生成下载说明
    log_header "📝 下载说明"
    
    cat > "${OUTPUT_DIR}/DOWNLOAD.md" << EOF
# ${REPO_NAME} v${VERSION} 下载说明

## 下载链接

- [${REPO_NAME}-${VERSION}.zip](${REPO_NAME}-${VERSION}.zip)
- [${REPO_NAME}-${VERSION}.tar.gz](${REPO_NAME}-${VERSION}.tar.gz)

## 校验

下载后请验证文件完整性：

\`\`\`bash
# 生成 SHA256 校验和
sha256sum -c ${REPO_NAME}-${VERSION}.zip.sha256
sha256sum -c ${REPO_NAME}-${VERSION}.tar.gz.sha256
\`\`\`

预期输出：
\`\`\`
${REPO_NAME}-${VERSION}.zip: OK
${REPO_NAME}-${VERSION}.tar.gz: OK
\`\`\`

## 安装

\`\`\`bash
# ZIP 解压 (Windows/macOS)
unzip ${REPO_NAME}-${VERSION}.zip

# TAR.GZ 解压 (Linux/macOS)
tar -xzf ${REPO_NAME}-${VERSION}.tar.gz
\`\`\`

## 更多信息

- 完整文档: [README.md](./README.md)
- 更新日志: [CHANGELOG.md](./CHANGELOG.md)
- 问题反馈: https://github.com/{owner}/${REPO_NAME}/issues
EOF
    
    log_success "下载说明已生成: ${OUTPUT_DIR}/DOWNLOAD.md"
    
    # Step 8: 完成
    local end_time=$(date +%s)
    local duration=$((end_time - start_time))
    
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    log_success "打包完成!"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "📊 统计:"
    echo "   文件数: ${#files_created[@]}"
    echo "   用时: ${duration}秒"
    echo ""
    echo "🔗 下一步:"
    echo "   1. 创建 Release:"
    echo "      gh release create $VERSION --generate-notes"
    echo ""
    echo "   2. 上传资源:"
    echo "      gh release upload $VERSION ${REPO_NAME}-${VERSION}.zip"
    echo "      gh release upload $VERSION ${REPO_NAME}-${VERSION}.tar.gz"
    echo ""
    echo "   3. 或使用自动化脚本:"
    echo "      ./scripts/create-release.sh $VERSION ${REPO_NAME}-${VERSION}.zip"
    echo ""
}

# 执行主函数
main "$@"
