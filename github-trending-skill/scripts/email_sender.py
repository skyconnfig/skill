#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Email Sender
发送 GitHub Trending 项目摘要邮件
"""

import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
import os
import sys
from datetime import datetime


def load_config_from_env():
    """
    从环境变量加载配置
    
    Returns:
        dict: 配置信息
    """
    return {
        'sender_email': os.environ.get('GITHUB_TRENDING_EMAIL'),
        'sender_password': os.environ.get('GITHUB_TRENDING_EMAIL_PASSWORD'),
        'recipient_email': os.environ.get('GITHUB_TRENDING_RECIPIENT'),
        'smtp_server': os.environ.get('GITHUB_TRENDING_SMTP_SERVER', 'smtp.qq.com'),
        'smtp_port': int(os.environ.get('GITHUB_TRENDING_SMTP_PORT', 465)),
        'use_ssl': os.environ.get('GITHUB_TRENDING_USE_SSL', '1') == '1',
        'subject': os.environ.get('GITHUB_TRENDING_EMAIL_SUBJECT')
    }


def load_summary_data(json_file="github_trending_summary.json"):
    """
    加载摘要数据
    
    Args:
        json_file: JSON 文件路径
    
    Returns:
        dict: 摘要数据
    """
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"文件未找到: {json_file}")
        return None
    except json.JSONDecodeError as e:
        print(f"JSON 解析错误: {e}")
        return None


def create_email_content(data):
    """
    创建邮件内容
    
    Args:
        data: 摘要数据
    
    Returns:
        str: HTML 格式的邮件内容
    """
    if not data:
        return ""
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
            }}
            .header {{
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 30px;
                border-radius: 10px;
                margin-bottom: 20px;
            }}
            .header h1 {{
                margin: 0;
                font-size: 28px;
            }}
            .meta {{
                opacity: 0.9;
                margin-top: 10px;
            }}
            .repo-card {{
                border: 1px solid #e1e4e8;
                border-radius: 8px;
                margin: 15px 0;
                padding: 20px;
                transition: box-shadow 0.3s;
            }}
            .repo-card:hover {{
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            }}
            .repo-title {{
                font-size: 20px;
                color: #0366d6;
                margin: 0 0 10px 0;
            }}
            .repo-title a {{
                text-decoration: none;
                color: inherit;
            }}
            .repo-title a:hover {{
                text-decoration: underline;
            }}
            .repo-description {{
                color: #586069;
                margin: 10px 0;
            }}
            .repo-stats {{
                display: flex;
                gap: 20px;
                margin-top: 15px;
                flex-wrap: wrap;
            }}
            .stat {{
                display: flex;
                align-items: center;
                gap: 5px;
                font-size: 14px;
                color: #586069;
            }}
            .stat-icon {{
                width: 16px;
                height: 16px;
            }}
            .tech-stack {{
                margin-top: 10px;
            }}
            .tech-tag {{
                background: #f1f8ff;
                color: #0366d6;
                padding: 3px 8px;
                border-radius: 3px;
                font-size: 12px;
                margin-right: 5px;
                display: inline-block;
            }}
            .rank {{
                background: #ffd700;
                color: #333;
                padding: 5px 10px;
                border-radius: 50%;
                font-weight: bold;
                margin-right: 10px;
            }}
            .summary-text {{
                background: #f6f8fa;
                padding: 15px;
                border-radius: 5px;
                margin-top: 10px;
                font-size: 14px;
            }}
            .footer {{
                text-align: center;
                padding: 20px;
                color: #586069;
                font-size: 12px;
                margin-top: 30px;
            }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>Github 今日热门项目摘要</h1>
            <div class="meta">
                <p>生成时间: {data.get('generated_at', '未知')}</p>
                <p>项目数量: {data.get('total_repos', 0)}</p>
            </div>
        </div>
    """
    
    # 添加每个项目的详细信息
    repos = data.get('repositories', [])
    for i, repo in enumerate(repos, 1):
        tech_stack = repo.get('涉及技术栈', '')
        tech_tags = ''
        if tech_stack:
            for tech in tech_stack.split(', ')[:5]:  # 最多显示 5 个技术标签
                if tech and tech != '未知':
                    tech_tags += f'<span class="tech-tag">{tech}</span>'
        
        summary = repo.get('项目简介', '')
        summary_html = ''
        if summary:
            summary_html = f'<div class="summary-text">{summary[:300]}...</div>'
        
        html_content += f"""
        <div class="repo-card">
            <h3 class="repo-title">
                <span class="rank">{i}</span>
                <a href="{repo.get('项目地址', '#')}" target="_blank">{repo.get('项目名称', '未知项目')}</a>
            </h3>
            <p class="repo-description">{repo.get('描述', '暂无描述')}</p>
            
            {summary_html}
            
            <div class="repo-stats">
                <div class="stat">
                    <span>编程语言:</span>
                    <span>{repo.get('编程语言', '未知')}</span>
                </div>
                <div class="stat">
                    <span>Star:</span>
                    <span>{repo.get('Star数量', '0')}</span>
                </div>
                <div class="stat">
                    <span>今日新增:</span>
                    <span>{repo.get('今日新增Star', '0')}</span>
                </div>
                <div class="stat">
                    <span>类型:</span>
                    <span>{repo.get('项目类型', '未知')}</span>
                </div>
            </div>
            
            <div class="tech-stack">
                {tech_tags}
            </div>
        </div>
        """
    
    html_content += """
        <div class="footer">
            <p>自动生成 by Github Trending Skill</p>
            <p>此邮件由系统自动发送</p>
        </div>
    </body>
    </html>
    """
    
    return html_content


def send_email(
    sender_email,
    sender_password,
    recipient_email,
    subject=None,
    json_file="github_trending_summary.json",
    smtp_server="smtp.qq.com",
    smtp_port=465,
    use_ssl=True
):
    """
    发送邮件
    
    Args:
        sender_email: 发件人邮箱
        sender_password: 发件人密码或应用专用密码
        recipient_email: 收件人邮箱
        subject: 邮件主题 (默认自动生成)
        json_file: JSON 文件路径
        smtp_server: SMTP 服务器地址
        smtp_port: SMTP 端口
    
    Returns:
        bool: 是否发送成功
    """
    # 加载数据
    data = load_summary_data(json_file)
    if not data:
        print("无法加载数据")
        return False
    
    # 生成邮件主题
    if not subject:
        date_str = datetime.now().strftime("%Y-%m-%d")
        subject = f"Github 今日热门项目摘要 ({date_str})"
    
    # 创建邮件内容
    html_content = create_email_content(data)
    plain_text = data.get('summary', '无法生成纯文本摘要')
    
    # 创建邮件对象
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Date'] = formatdate()
    
    # 添加 HTML 和纯文本版本
    html_part = MIMEText(html_content, 'html', 'utf-8')
    text_part = MIMEText(plain_text, 'plain', 'utf-8')
    
    msg.attach(text_part)
    msg.attach(html_part)
    
    try:
        print(f"正在发送邮件到 {recipient_email}...")
        
        # 根据是否使用SSL选择不同的连接方式
        if use_ssl:
            with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
                server.login(sender_email, sender_password)
                server.send_message(msg)
        else:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()  # 启用 TLS 加密
                server.login(sender_email, sender_password)
                server.send_message(msg)
        
        print(f"邮件发送成功!")
        return True
        
    except smtplib.SMTPAuthenticationError:
        print("认证失败，请检查邮箱和密码")
        print("提示: 如果使用 Gmail，请启用两步验证并使用应用专用密码")
        print("提示: 如果使用 QQ邮箱，请确保已开启SMTP服务并使用授权码")
        return False
    except smtplib.SMTPException as e:
        print(f"邮件发送失败: {e}")
        return False
    except Exception as e:
        print(f"发生错误: {e}")
        return False


def main():
    """
    主函数：发送 GitHub Trending 摘要邮件
    """
    print("Github Trending 邮件发送工具")
    print("="*40)
    
    # 从环境变量获取配置
    config = load_config_from_env()
    sender_email = config['sender_email']
    sender_password = config['sender_password']
    recipient_email = config['recipient_email']
    
    # 检查环境变量
    if not all([sender_email, sender_password, recipient_email]):
        print("未找到完整的邮箱配置")
        print("请设置以下环境变量:")
        print("  GITHUB_TRENDING_EMAIL - 发件人邮箱")
        print("  GITHUB_TRENDING_EMAIL_PASSWORD - 发件人密码或应用专用密码")
        print("  GITHUB_TRENDING_RECIPIENT - 收件人邮箱")
        print("\n或者在命令行参数中提供:")
        print("python email_sender.py <sender_email> <sender_password> <recipient_email>")
        
        # 尝试从命令行参数获取
        if len(sys.argv) >= 4:
            sender_email = sys.argv[1]
            sender_password = sys.argv[2]
            recipient_email = sys.argv[3]
        else:
            return False
    
    # 获取 SMTP 配置
    smtp_server = config['smtp_server']
    smtp_port = config['smtp_port']
    use_ssl = config['use_ssl']
    subject = config['subject']
    
    # 发送邮件
    return send_email(
        sender_email=sender_email,
        sender_password=sender_password,
        recipient_email=recipient_email,
        subject=subject,
        smtp_server=smtp_server,
        smtp_port=smtp_port,
        use_ssl=use_ssl
    )


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)