# 快速开始 - GitHub Trending Email

> 5 分钟完成配置

## 一、安装依赖

```bash
pip install requests beautifulsoup4
```

## 二、配置邮箱

### QQ 邮箱

1. **开启 SMTP 服务**
   - 登录 [QQ 邮箱](https://mail.qq.com)
   - 设置 → 账户 → 开启 SMTP 服务

2. **获取授权码**
   - 设置 → 账户 → 生成授权码
   - 记录 16 位授权码

3. **设置环境变量**
   ```bash
   set GITHUB_TRENDING_EMAIL=564884588@qq.com
   set GITHUB_TRENDING_EMAIL_PASSWORD=ynyfdzlfboklbdaf
   set GITHUB_TRENDING_RECIPIENT=564884588@qq.com
   ```

### Gmail

```bash
set GITHUB_TRENDING_EMAIL=your-email@gmail.com
set GITHUB_TRENDING_EMAIL_PASSWORD=your-app-password
set GITHUB_TRENDING_RECIPIENT=recipient@gmail.com
set GITHUB_TRENDING_SMTP_SERVER=smtp.gmail.com
set GITHUB_TRENDING_SMTP_PORT=587
set GITHUB_TRENDING_USE_SSL=0
```

## 三、测试发送

```bash
# 1. 爬取数据
python scripts/github_trending_scraper.py

# 2. 发送邮件
python scripts/email_sender.py
```

## 四、定时任务

### Windows

```bash
# 创建每日任务（管理员运行）
schtasks /create /tn "GitHub Trending Daily" /tr "C:\path\to\daily_github_trending.bat" /sc daily /st 20:00:00 /rl HIGHEST
```

### 使用安装脚本

```bash
# 交互式配置
setup.bat

# 或直接安装任务（管理员）
install_task.bat
```

## 五、文件说明

```
github-trending-skill/
├── scripts/
│   ├── github_trending_scraper.py  # 爬虫脚本
│   └── email_sender.py             # 邮件发送
├── config.env                      # 配置模板
├── daily_github_trending.bat       # 每日执行
├── install_task.bat                # 任务安装
├── setup.bat                       # 一键配置
├── README_BEST_PRACTICE.md         # 完整文档
└── QUICK_START.md                  # 本文件
```

## 六、常用命令

```bash
# 手动执行
daily_github_trending.bat

# 查看任务状态
schtasks /query | findstr "GitHub"

# 手动运行任务
schtasks /run /tn "GitHub Trending Daily"

# 删除任务
schtasks /delete /tn "GitHub Trending Daily" /f
```

## 七、问题排查

| 问题 | 解决方案 |
|------|----------|
| 认证失败 | 使用授权码，非登录密码 |
| 收不到邮件 | 检查垃圾邮件箱 |
| 定时不执行 | 以管理员身份运行 install_task.bat |
| SMTP 错误 | 确认 SMTP 服务已开启 |

**详细文档**: [README_BEST_PRACTICE.md](./README_BEST_PRACTICE.md)
