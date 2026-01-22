@echo off
REM Load GitHub Trending Configuration
REM 加载 GitHub Trending 配置文件

echo 正在加载配置...
echo.

REM 读取配置文件
for /f "usebackq tokens=1,* delims==" %%a in ("config.env") do (
    if not "%%b"=="" (
        set %%a=%%b
        echo 设置: %%a=%%b
    )
)

echo.
echo 配置加载完成！
echo 发件人: %GITHUB_TRENDING_EMAIL%
echo 收件人: %GITHUB_TRENDING_RECIPIENT%
echo.
