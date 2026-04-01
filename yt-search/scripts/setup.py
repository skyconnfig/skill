#!/usr/bin/env python3
"""YouTube Search Skill - 安装和配置脚本"""

import io
import os
import sys
import subprocess
from pathlib import Path

# Force UTF-8 output on Windows to handle emoji
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")


def log(message):
    print(f"{message}")


def check_python():
    """检查Python版本"""
    log("\n📦 步骤 1/5: 检查Python环境...")
    try:
        version = sys.version_info
        if version.major >= 3 and version.minor >= 8:
            log(f"✅ Python {version.major}.{version.minor}.{version.micro} 已安装")
            return True
        else:
            print(f"❌ Python版本过低 (3.8+ required): {version.major}.{version.minor}")
            return False
    except Exception as e:
        print(f"❌ Python检查失败: {e}")
        return False


def check_yt_dlp():
    """检查yt-dlp是否已安装"""
    log("\n🔍 步骤 2/5: 检查 yt-dlp...")
    try:
        result = subprocess.run(
            ["yt-dlp", "--version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            version = result.stdout.strip()
            log(f"✅ yt-dlp 已安装: {version}")
            return True
    except (subprocess.TimeoutExpired, FileNotFoundError):
        log("⚠️  yt-dlp 未安装")
        return False
    except Exception as e:
        log(f"⚠️  检查yt-dlp时出错: {e}")
        return False


def install_yt_dlp():
    """安装yt-dlp"""
    log("\n📦 正在安装 yt-dlp...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-U", "yt-dlp"])
        log("✅ yt-dlp 安装成功！")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ yt-dlp 安装失败: {e}")
        log("请手动安装: pip install yt-dlp")
        return False


def create_directories():
    """创建必要的目录"""
    log("\n📁 步骤 3/5: 创建目录结构...")
    script_dir = Path(__file__).parent.parent
    dirs = [
        script_dir / "scripts",
        script_dir / "lib",
        script_dir / "cache",
        script_dir / "logs",
    ]

    for dir_path in dirs:
        dir_path.mkdir(parents=True, exist_ok=True)
        log(f"✅ 创建目录: {dir_path}")

    return True


def check_config():
    """检查配置文件"""
    log("\n📝 步骤 4/5: 检查配置文件...")
    script_dir = Path(__file__).parent.parent
    env_example = script_dir / ".env.example"
    env_file = script_dir / ".env"

    if env_file.exists():
        log(f"✅ 找到配置文件: {env_file}")
        return True

    if env_example.exists():
        log(f"⚠️  未找到 .env 配置文件")
        log(f"   请复制 {env_example} 为 .env 并编辑")
        # 自动复制
        try:
            import shutil
            shutil.copy(env_example, env_file)
            log(f"✅ 已创建默认配置文件: {env_file}")
            return True
        except Exception as e:
            print(f"❌ 复制配置文件失败: {e}")
            return False
    else:
        log("⚠️  未找到 .env.example 配置文件")
        return True  # 不是严重错误


def print_usage():
    """打印使用说明"""
    log("\n" + "="*60)
    log("✅ YouTube Search Skill 设置完成!")
    log("="*60)

    log("\n📖 使用方法:")
    log("1. 在 Claude Code 中使用: /yt-search <查询关键词> [选项]")
    log("2. 直接运行: python scripts/search.py \"查询关键词\" --count 20 --months 6")
    log("3. 查看帮助: python scripts/search.py --help")

    log("\n🔧 常用选项:")
    log("  --count N     结果数量 (默认: 20)")
    log("  --months N    只显示最近N个月的视频 (默认: 6)")
    log("  --no-date-filter  显示所有结果，不限制日期")
    log("  --help        显示帮助信息")

    log("\n💡 提示:")
    log("• 首次使用前建议运行测试: python scripts/search.py \"claude code\" --count 5")
    log("• 如需修改配置，编辑 .env 文件")
    log("• 更多信息请查看 README.md 或 SKILL.md")

    log("\n🔗 相关链接:")
    log("• yt-dlp: https://github.com/yt-dlp/yt-dlp")
    log("• 问题反馈: 请提交 Issue")


def main():
    log("🎬 YouTube Search Skill - 设置向导")
    log("="*60)

    log("\n📦 依赖检查...")

    # 1. 检查Python
    if not check_python():
        log("\n❌ Python检查失败，请安装 Python 3.8+ 后重试")
        sys.exit(1)

    # 2. 检查yt-dlp
    yt_dlp_ok = check_yt_dlp()
    if not yt_dlp_ok:
        log("\n是否自动安装 yt-dlp? (y/n): ")
        # 非交互模式，直接安装
        log("自动安装 yt-dlp...")
        if not install_yt_dlp():
            sys.exit(1)

    # 3. 创建目录
    if not create_directories():
        log("\n❌ 目录创建失败")
        sys.exit(1)

    # 4. 检查配置
    check_config()

    # 5. 完成
    print_usage()


if __name__ == "__main__":
    main()
