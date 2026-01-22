@echo off
cd /d %%~dp0
python scripts/github_trending_scraper.py
python scripts/email_sender.py 564884588@qq.com ynyfdzlfboklbdaf 564884588@qq.com
echo 任务完成
pause
