@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

REM ========================================
REM GitHub Trending 一键配置脚本
REM ========================================

echo.
echo ============================================
echo   GitHub Trending 自动推送配置向导
echo ============================================
echo.

REM 获取当前路径
set "SCRIPT_DIR=%~dp0"
set "CONFIG_FILE=%SCRIPT_DIR%config.env"

echo [1/5] 检查环境...
echo.

REM 检查 Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 未找到 Python，请先安装 Python 3.x
    echo    下载地址: https://www.python.org/downloads/
    pause
    exit /b 1
)
echo ✅ Python 环境正常

REM 检查依赖
pip show requests >nul 2>&1
if errorlevel 1 (
    echo 📦 安装依赖包...
    pip install requests beautifulsoup4
    if errorlevel 1 (
        echo ❌ 依赖安装失败
        pause
        exit /b 1
    )
)
echo ✅ 依赖包正常

echo.
echo [2/5] 邮箱配置
echo.

set /p SENDER_EMAIL="请输入发件人邮箱 (例如: 564884588@qq.com): "
if "!SENDER_EMAIL!"=="" (
    echo ❌ 邮箱地址不能为空
    pause
    exit /b 1
)

set /p SENDER_PASSWORD="请输入授权码 (非登录密码): "
if "!SENDER_PASSWORD!"=="" (
    echo ❌ 授权码不能为空
    pause
    exit /b 1
)

set /p RECIPIENT_EMAIL="请输入收件人邮箱 (例如: 564884588@qq.com): "
if "!RECIPIENT_EMAIL!"=="" (
    echo ❌ 收件人邮箱不能为空
    pause
    exit /b 1
)

echo.
echo [3/5] 生成配置文件...
echo.

REM 生成配置文件
(
    echo # GitHub Trending Email Configuration
    echo # GitHub 热门项目邮件推送配置
    echo.
    echo # 邮箱配置（必填）
    echo GITHUB_TRENDING_EMAIL=!SENDER_EMAIL!
    echo GITHUB_TRENDING_EMAIL_PASSWORD=!SENDER_PASSWORD!
    echo GITHUB_TRENDING_RECIPIENT=!RECIPIENT_EMAIL!
    echo.
    echo # SMTP 服务器配置
    echo GITHUB_TRENDING_SMTP_SERVER=smtp.qq.com
    echo GITHUB_TRENDING_SMTP_PORT=465
    echo GITHUB_TRENDING_USE_SSL=1
) > "!CONFIG_FILE!"

echo ✅ 配置文件已生成: !CONFIG_FILE!

echo.
echo [4/5] 测试发送邮件...
echo.

REM 爬取数据
echo 📊 正在爬取 GitHub 热门项目...
python "!SCRIPT_DIR!scripts\github_trending_scraper.py"
if errorlevel 1 (
    echo ❌ 爬取数据失败
    pause
    exit /b 1
)

REM 发送测试邮件
echo 📧 正在发送测试邮件...
python "!SCRIPT_DIR!scripts\email_sender.py" !SENDER_EMAIL! !SENDER_PASSWORD! !RECIPIENT_EMAIL!
if errorlevel 1 (
    echo ❌ 邮件发送失败，请检查配置
    echo.
    echo 常见问题:
    echo 1. 确保已开启 SMTP 服务
    echo 2. 确保使用的是授权码而非登录密码
    echo 3. 检查邮箱地址是否正确
    pause
    exit /b 1
)

echo.
echo [5/5] 设置定时任务
echo.

echo 是否设置每日自动推送定时任务?
echo   1) 设置每天晚上 8:00 执行
echo   2) 暂不设置
echo.
set /p TASK_CHOICE="请选择 (1/2): "

if "!TASK_CHOICE!"=="1" (
    echo.
    echo ⚠️  需要管理员权限创建定时任务
    echo    请在弹出的对话框中确认
    echo.
    
    REM 创建定时任务
    schtasks /create /tn "GitHub Trending Daily" /tr "\"!SCRIPT_DIR!daily_github_trending.bat\"" /sc daily /st 20:00:00 /rl HIGHEST /f
    
    if errorlevel 1 (
        echo ❌ 定时任务创建失败
        echo    请尝试手动以管理员身份运行 install_task.bat
    ) else (
        echo ✅ 定时任务创建成功！
        echo    任务名称: GitHub Trending Daily
        echo    执行时间: 每天晚上 20:00
    )
)

echo.
echo ============================================
echo   配置完成！
echo ============================================
echo.
echo 📁 配置文件: !CONFIG_FILE!
echo 📋 每日脚本: !SCRIPT_DIR!daily_github_trending.bat
echo.
echo 常用命令:
echo   - 手动执行: daily_github_trending.bat
echo   - 查看任务: schtasks /query ^| findstr "GitHub"
echo   - 删除任务: schtasks /delete /tn "GitHub Trending Daily" /f
echo.
echo 📖 详细文档: README_BEST_PRACTICE.md
echo.

pause
endlocal
