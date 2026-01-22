@echo off
REM Link Explainer Pink - Windows 批处理脚本
REM 用法: run.bat <url> [output_file]

setlocal enabledelayedexpansion

set "PINK=[93m"
set "BLUE=[94m"
set "GREEN=[92m"
set "YELLOW=[93m"
set "NC=[0m"

set "URL=%~1"
set "OUTPUT_FILE=%~2"
if "%OUTPUT_FILE%"=="" set "OUTPUT_FILE=explanation.html"

set "SCRIPT_DIR=%~dp0"
set "SCRIPTS_DIR=%SCRIPT_DIR%scripts"

echo.
echo [93m🌸[0m Link Explainer Pink - 简化解释生成器
echo.

REM 检查 Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [93m⚠️[0m 未找到 Python，请确保已安装 Python 3
    exit /b 1
)

REM Step 1: 获取内容
echo [93m📥[0m Step 1/3: 获取网页内容...
python "%SCRIPTS_DIR%\fetch_content.py" "%URL%" > content.json
if errorlevel 1 (
    echo [93m⚠️[0m 内容获取失败
    exit /b 1
)
echo [92m✅[0m 内容获取完成

REM Step 2: 简化内容
echo.
echo [93m🔍[0m Step 2/3: 简化内容并解释专业术语...
python "%SCRIPTS_DIR%\simplify_content.py" content.json > simplified.json
echo [92m✅[0m 内容简化完成

REM Step 3: 生成 HTML
echo.
echo [93m🎨[0m Step 3/3: 生成动画 HTML 页面...
python "%SCRIPTS_DIR%\generate_html.py" simplified.json
echo [92m✅[0m HTML 生成完成

REM 清理临时文件
del content.json simplified.json >nul 2>&1

echo.
echo [92m🎉[0m 大功告成！
echo.
echo 📄 生成的文件: %OUTPUT_FILE%
echo.
echo [94mℹ️[0m 你可以双击 %OUTPUT_FILE% 用浏览器打开查看效果

endlocal
