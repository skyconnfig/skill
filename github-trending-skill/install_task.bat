@echo off
echo 正在创建定时任务...
schtasks /create /tn "GitHub Trending Daily" /tr "C:\Users\lixin\.config\opencode\skill\github-trending-skill\daily_github_trending.bat" /sc daily /st 20:00:00 /rl HIGHEST
if %errorlevel% equ 0 (
    echo ✓ 定时任务创建成功！
    echo 任务名称: GitHub Trending Daily
    echo 执行时间: 每天晚上 20:00
    echo 执行脚本: daily_github_trending.bat
) else (
    echo ✗ 定时任务创建失败
    echo 请尝试以管理员身份运行此脚本
)
pause
