#!/bin/bash
#
# Link Explainer Pink - 一键生成简化解释页面
#
# 用法:
#   ./run.sh <url> [output_file]
#
# 示例:
#   ./run.sh "https://opencode.ai/docs"
#   ./run.sh "https://opencode.ai/docs" "my-output.html"
#

set -e

# 颜色定义
PINK='\033[0;35m'
BLUE='\033[0;34m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 打印带颜色的消息
print_msg() {
    echo -e "${PINK}🌸${NC} $1"
}

print_success() {
    echo -e "${GREEN}✅${NC} $1"
}

print_info() {
    echo -e "${BLUE}ℹ️${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠️${NC} $1"
}

# 检查依赖
check_dependencies() {
    print_msg "检查依赖..."
    
    if ! command -v python3 &> /dev/null; then
        print_warning "Python 3 未安装，将尝试使用 python"
        PYTHON_CMD="python"
    else
        PYTHON_CMD="python3"
    fi
    
    # 检查 Python 包
    if ! $PYTHON_CMD -c "import requests" 2>/dev/null; then
        print_warning "缺少 requests 包，正在安装..."
        pip install requests
    fi
    
    if ! $PYTHON_CMD -c "import bs4" 2>/dev/null; then
        print_warning "缺少 beautifulsoup4 包，正在安装..."
        pip install beautifulsoup4
    fi
    
    print_success "依赖检查完成"
}

# 主函数
main() {
    # 检查参数
    if [ $# -lt 1 ]; then
        echo "用法: $0 <url> [output_file]"
        echo ""
        echo "参数:"
        echo "  url          要解释的网页 URL（必需）"
        echo "  output_file  输出文件名（可选，默认: explanation.html）"
        echo ""
        echo "示例:"
        echo "  $0 \"https://opencode.ai/docs\""
        echo "  $0 \"https://opencode.ai/docs\" \"my-output.html\""
        exit 1
    fi
    
    URL="$1"
    OUTPUT_FILE="${2:-explanation.html}"
    
    # 获取脚本所在目录
    SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
    SCRIPTS_DIR="$SCRIPT_DIR/scripts"
    
    print_msg "Link Explainer Pink - 简化解释生成器"
    echo ""
    
    # 检查依赖
    check_dependencies
    
    echo ""
    print_info "目标 URL: $URL"
    print_info "输出文件: $OUTPUT_FILE"
    echo ""
    
    # Step 1: 获取内容
    print_msg "Step 1/3: 获取网页内容..."
    if $PYTHON_CMD "$SCRIPTS_DIR/fetch_content.py" "$URL" > content.json; then
        print_success "内容获取完成"
    else
        print_warning "内容获取失败，使用备用方法"
        curl -sL "$URL" > temp_page.html
    fi
    
    echo ""
    
    # Step 2: 简化内容
    print_msg "Step 2/3: 简化内容并解释专业术语..."
    if [ -f "content.json" ]; then
        $PYTHON_CMD "$SCRIPTS_DIR/simplify_content.py" content.json > simplified.json
        print_success "内容简化完成"
    else
        print_warning "跳过简化步骤"
    fi
    
    echo ""
    
    # Step 3: 生成 HTML
    print_msg "Step 3/3: 生成动画 HTML 页面..."
    if [ -f "simplified.json" ]; then
        $PYTHON_CMD "$SCRIPTS_DIR/generate_html.py" simplified.json
        print_success "HTML 生成完成"
    else
        print_warning "跳过 HTML 生成"
    fi
    
    echo ""
    
    # 清理临时文件
    rm -f content.json simplified.json temp_page.html
    
    # 检查输出文件
    if [ -f "$OUTPUT_FILE" ]; then
        print_success "🎉 大功告成！"
        echo ""
        echo "📄 生成的文件: $OUTPUT_FILE"
        echo ""
        print_info "你可以用浏览器打开查看效果："
        echo "  open $OUTPUT_FILE    # macOS"
        echo "  xdg-open $OUTPUT_FILE  # Linux"
        echo "  start $OUTPUT_FILE   # Windows"
    else
        print_warning "输出文件未生成，请检查错误信息"
        exit 1
    fi
}

# 运行主函数
main "$@"
