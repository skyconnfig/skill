---
name: GitHub Trending Analyzer
description: Comprehensive GitHub trending project analysis tool with automated email reporting. Use when user wants to: (1) Get daily GitHub trending projects summary, (2) Analyze popular repositories with Chinese descriptions, (3) Send trending analysis reports via email. This skill fetches top 10 trending repositories from GitHub, extracts and summarizes README content in Chinese, and delivers formatted reports via email.
---

# GitHub Trending Analyzer Skill

This skill provides automated analysis and reporting of GitHub's daily trending repositories with Chinese summaries and email delivery.

## Quick Start

```bash
# 1. Run the trending scraper
python scripts/github_trending_scraper.py

# 2. Send the summary via email
python scripts/email_sender.py <sender_email> <sender_password> <recipient_email>
```

## Scripts Overview

### 1. github_trending_scraper.py

Fetches GitHub's daily trending projects and generates Chinese summaries.

**Features:**
- Scrapes top 10 trending repositories from GitHub
- Extracts README content from each repository
- Generates Chinese summaries including:
  - Project description and purpose
  - Technology stack
  - Star count and growth
  - Project type classification
- Saves results to JSON file for further processing

**Usage:**
```bash
python scripts/github_trending_scraper.py
```

**Output:**
- `github_trending_summary.json` - Detailed project data
- Console output with Chinese summary

### 2. email_sender.py

Sends formatted email reports with trending analysis.

**Features:**
- Reads data from JSON summary file
- Generates HTML email with project cards
- Includes technology tags, stats, and descriptions
- Supports Gmail and other SMTP providers

**Usage:**
```bash
# Method 1: Command line arguments
python scripts/email_sender.py sender@gmail.com app_password recipient@example.com

# Method 2: Environment variables
export GITHUB_TRENDING_EMAIL="sender@gmail.com"
export GITHUB_TRENDING_EMAIL_PASSWORD="app_password"
export GITHUB_TRENDING_RECIPIENT="recipient@example.com"
python scripts/email_sender.py

# Method 3: Configuration file
# Edit config.env and run:
load_config.bat  # Windows
source config.env  # Linux/Mac
python scripts/email_sender.py
```

**Environment Variables:**
- `GITHUB_TRENDING_EMAIL` - Sender email address
- `GITHUB_TRENDING_EMAIL_PASSWORD` - Sender password or app-specific password
- `GITHUB_TRENDING_RECIPIENT` - Recipient email address
- `GITHUB_TRENDING_SMTP_SERVER` - SMTP server address (default: smtp.qq.com)
- `GITHUB_TRENDING_SMTP port (default: 465)
-_PORT` - SMTP `GITHUB_TRENDING_USE_SSL` - Use SSL (default: 1)

## Configuration

### Email Setup (Gmail Example)

1. Enable 2-Step Verification on your Google account
2. Create an App Password:
   - Go to Google Account > Security
   - Enable 2-Step Verification
   - Go to App Passwords
   - Create new app password for "Mail"
3. Use the app password in `email_sender.py`

### Customization Options

**Change Trending Period:**
```python
# In github_trending_scraper.py, modify:
get_github_trending_repos(language="", period="weekly")  # daily, weekly, monthly
```

**Filter by Language:**
```python
# Get Python trending projects
get_github_trending_repos(language="python")
```

**Adjust Output Count:**
```python
# Get top 20 projects
parse_trending_repos(html_content, top_n=20)
```

## Workflow

1. **Fetch Trending**: Scrapes GitHub trending page for today's top repositories
2. **Extract README**: Downloads and parses README files from each repository
3. **Analyze Content**: Identifies technology stack and project purpose
4. **Generate Summary**: Creates Chinese summary with key information
5. **Send Report**: Emails formatted HTML report to specified recipients

## Output Format

### JSON Output Structure

```json
{
  "generated_at": "2024-01-01T12:00:00",
  "total_repos": 10,
  "repositories": [
    {
      "项目名称": "repository-name",
      "项目地址": "https://github.com/owner/repo",
      "描述": "Repository description",
      "编程语言": "Python",
      "Star数量": "1.2k",
      "今日新增Star": "+123 today",
      "项目类型": "开发框架/库/工具",
      "涉及技术栈": "Python, React, Docker",
      "项目简介": "Extracted README summary..."
    }
  ],
  "summary": "Markdown formatted summary..."
}
```

### Email Report Features

- Responsive HTML design with GitHub-style cards
- Technology stack tags
- Star count and growth metrics
- Project type categorization
- Mobile-friendly layout

## Troubleshooting

**Common Issues:**

1. **Email Authentication Failed**
   - Ensure 2-Step Verification is enabled
   - Use App Password instead of regular password
   - Check SMTP settings for your email provider

2. **No Trending Data Retrieved**
   - Check internet connection
   - Verify GitHub trending page is accessible
   - Try different time periods or languages

3. **README Extraction Failed**
   - Some repositories may not have README files
   - Check repository has main/master branch
   - Verify repository is public

4. **Missing Dependencies**
   ```bash
   pip install requests beautifulsoup4
   ```

## Dependencies

- `requests` - HTTP library for fetching web pages
- `beautifulsoup4` - HTML parsing library
- Standard library: `json`, `re`, `os`, `datetime`, `smtplib`, `email`

## Best Practices

1. **Schedule Regular Reports**: Set up cron job for daily execution
2. **Use App Passwords**: Always use app-specific passwords for email
3. **Error Handling**: Check logs for failed fetches or sends
4. **Data Backup**: Keep JSON summaries for historical analysis

## Integration Examples

### Bash Script for Daily Reports

```bash
#!/bin/bash
# daily_github_report.sh

cd /path/to/skill
python scripts/github_trending_scraper.py
python scripts/email_sender.py "$EMAIL" "$PASSWORD" "$RECIPIENT"
```

### Python Wrapper for Automation

```python
import subprocess
import os

def run_daily_report():
    os.chdir('/path/to/skill')
    
    # Run scraper
    subprocess.run(['python', 'scripts/github_trending_scraper.py'])
    
    # Send email
    subprocess.run([
        'python', 'scripts/email_sender.py',
        os.environ['EMAIL'],
        os.environ['PASSWORD'],
        os.environ['RECIPIENT']
    ])
```

## Technical Notes

- **Rate Limiting**: GitHub may rate limit requests; add delays if needed
- **Character Encoding**: All outputs use UTF-8 encoding
- **Time Zones**: Timestamps use local timezone
- **HTML Sanitization**: README content is sanitized for display

## Security Considerations

- Store credentials in environment variables
- Use app-specific passwords for email accounts
- Avoid committing sensitive data to version control
- Consider using secret management services for production

## Performance

- Typical execution time: 30-60 seconds for 10 repos
- Memory usage: ~50MB during execution
- Network requests: ~11 (1 trending page + 10 README fetches)

## Support

For issues with:
- **Script errors**: Check Python dependencies and syntax
- **GitHub access**: Verify network connectivity and rate limits
- **Email delivery**: Validate SMTP settings and credentials

## Additional Documentation

- **[README_BEST_PRACTICE.md](README_BEST_PRACTICE.md)** - Comprehensive best practice guide with troubleshooting
- **[QUICK_START.md](QUICK_START.md)** - Quick reference for common tasks
