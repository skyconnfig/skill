@echo off
schtasks /create /tn "GitHub Trending Daily" /tr "C:\Users\lixin\.config\opencode\skill\github-trending-skill\daily_github_trending.bat" /sc daily /st 20:00:00 /rl HIGHEST
pause
