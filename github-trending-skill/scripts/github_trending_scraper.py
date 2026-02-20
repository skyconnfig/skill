#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GitHub Trending Scraper
爬取 GitHub 今日热门项目前 10 个，获取 README，总结成中文摘要
"""

import requests
from bs4 import BeautifulSoup
import json
import re
import os
from datetime import datetime


def get_github_trending_repos(language="", period="daily"):
    """
    获取 GitHub 今日热门项目
    
    Args:
        language: 编程语言
        period: 时间范围 (daily, weekly, monthly)
    
    Returns:
        list: 热门项目列表
    """
    base_url = "https://github.com/trending"
    params = {
        "spoken_language_code": "zh"  # 中文项目
    }
    
    if language:
        params["language"] = language
    
    url = f"{base_url}/{language}" if language else base_url
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching trending page: {e}")
        return None


def parse_trending_repos(html_content, top_n=10):
    """
    解析 GitHub Trending 页面，提取项目信息
    
    Args:
        html_content: HTML 内容
        top_n: 获取前 N 个项目
    
    Returns:
        list: 项目列表
    """
    if not html_content:
        return []
    
    soup = BeautifulSoup(html_content, 'html.parser')
    repos = []
    
    # 查找所有仓库条目 - 使用正确的选择器
    repo_items = soup.select('.Box-row')[:top_n]
    
    for item in repo_items:
        try:
            # 获取仓库名称和链接
            title_elem = item.select_one('h2 a')
            if not title_elem:
                continue
            
            repo_full_name = (title_elem.get('href', '') or '').strip('/')
            repo_url = f"https://github.com/{repo_full_name}"
            
            # 获取描述
            desc_elem = item.select_one('p')
            description = desc_elem.get_text(strip=True) if desc_elem else ""
            
            # 获取编程语言
            lang_elem = item.select_one('[itemprop="programmingLanguage"]')
            language = lang_elem.get_text(strip=True) if lang_elem else ""
            
            # 获取 star 数量
            star_elem = item.select_one('a[href$="/stargazers"]')
            if star_elem:
                stars = star_elem.get_text(strip=True)
            else:
                stars = "0"
            
            # 获取今日新增 star
            today_elem = item.select_one('span.d-inline-block')
            today_stars = today_elem.get_text(strip=True) if today_elem else ""
            
            repo_info = {
                "full_name": repo_full_name,
                "url": repo_url,
                "description": description,
                "language": language,
                "stars": stars,
                "today_stars": today_stars,
                "fetched_at": datetime.now().isoformat()
            }
            
            repos.append(repo_info)
            
        except Exception as e:
            print(f"Error parsing repo: {e}")
            continue
    
    return repos


def get_repo_readme(repo_full_name, branch="main"):
    """
    获取仓库的 README 文件
    
    Args:
        repo_full_name: 仓库完整名称 (owner/repo)
        branch: 分支名称
    
    Returns:
        str: README 内容
    """
    # 首先尝试 main 分支，然后是 master 分支
    branches = [branch, "master", "main"]
    
    for branch_name in branches:
        # 尝试获取 README
        readme_urls = [
            f"https://raw.githubusercontent.com/{repo_full_name}/{branch_name}/README.md",
            f"https://raw.githubusercontent.com/{repo_full_name}/{branch_name}/readme.md",
            f"https://raw.githubusercontent.com/{repo_full_name}/{branch_name}/README.rst",
            f"https://raw.githubusercontent.com/{repo_full_name}/{branch_name}/README",
            f"https://raw.githubusercontent.com/{repo_full_name}/{branch_name}/docs/README.md",
        ]
        
        for url in readme_urls:
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    return response.text
            except:
                continue
    
    return None


def extract_repo_info_from_readme(readme_content):
    """
    从 README 中提取关键信息
    
    Args:
        readme_content: README 内容
    
    Returns:
        dict: 提取的信息
    """
    if not readme_content:
        return {}
    
    # 移除 markdown 格式，提取纯文本
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', readme_content)  # 移除链接
    text = re.sub(r'#{1,6}\s*', '', text)  # 移除标题符号
    text = re.sub(r'`{1,3}[^`]*`{1,3}', '', text)  # 移除代码块
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)  # 移除粗体
    text = re.sub(r'\*([^*]+)\*', r'\1', text)  # 移除斜体
    text = re.sub(r'\n{3,}', '\n\n', text)  # 规范化换行
    
    # 提取前 2000 字符作为摘要
    summary = text[:2000].strip() if len(text) > 2000 else text.strip()
    
    # 提取技术栈信息
    tech_stack = []
    
    # 常见技术关键词
    tech_keywords = [
        'React', 'Vue', 'Angular', 'Node.js', 'Python', 'Java', 'Go', 'Rust',
        'TypeScript', 'JavaScript', 'Docker', 'Kubernetes', 'AWS', 'TensorFlow',
        'PyTorch', 'Machine Learning', 'AI', 'API', 'GraphQL', 'REST',
        'MongoDB', 'PostgreSQL', 'MySQL', 'Redis', 'Flask', 'Django',
        'Spring', 'Express', 'FastAPI', 'Next.js', 'Nuxt', 'Svelte'
    ]
    
    for keyword in tech_keywords:
        if keyword.lower() in text.lower():
            tech_stack.append(keyword)
    
    return {
        "summary": summary,
        "tech_stack": tech_stack[:10]  # 最多保留 10 个技术栈
    }


def analyze_repo_with_llm(repo_info, readme_content):
    """
    使用 LLM 分析项目信息（模拟）
    实际使用时可以接入 API 进行更智能的分析
    
    Args:
        repo_info: 仓库基本信息
        readme_content: README 内容
    
    Returns:
        dict: 分析结果
    """
    # 基础信息
    analysis = {
        "项目名称": repo_info['full_name'].split('/')[-1],
        "项目地址": repo_info['url'],
        "描述": repo_info['description'],
        "编程语言": repo_info['language'],
        "Star数量": repo_info['stars'],
        "今日新增Star": repo_info['today_stars']
    }
    
    # 从 README 提取信息
    if readme_content:
        readme_info = extract_repo_info_from_readme(readme_content)
        analysis['项目简介'] = readme_info['summary']
        analysis['涉及技术栈'] = ', '.join(readme_info['tech_stack']) if readme_info['tech_stack'] else '未知'
    
    # 推断项目类型和用途
    analysis['项目类型'] = infer_project_type(repo_info, readme_content)
    
    return analysis


def infer_project_type(repo_info, readme_content):
    """
    推断项目类型和用途
    
    Args:
        repo_info: 仓库信息
        readme_content: README 内容
    
    Returns:
        str: 项目类型描述
    """
    text = f"{repo_info['description']} {readme_content or ''}".lower()
    
    # 根据关键词推断
    if any(kw in text for kw in ['framework', 'library', 'sdk', 'tool']):
        return "开发框架/库/工具"
    elif any(kw in text for kw in ['app', 'application', 'web', 'site']):
        return "Web应用/网站"
    elif any(kw in text for kw in ['machine learning', 'ml', 'ai', 'deep learning', 'neural']):
        return "机器学习/AI项目"
    elif any(kw in text for kw in ['docker', 'kubernetes', 'devops', 'cloud']):
        return "DevOps/云原生项目"
    elif any(kw in text for kw in ['database', 'db', 'storage']):
        return "数据库/存储项目"
    elif any(kw in text for kw in ['api', 'server', 'service', 'backend']):
        return "API/后端服务"
    else:
        return "其他类型项目"


def generate_chinese_summary(repos_data):
    """
    生成中文摘要
    
    Args:
        repos_data: 项目数据列表
    
    Returns:
        str: 中文摘要
    """
    summary_lines = []
    summary_lines.append("GitHub 今日热门项目摘要")
    summary_lines.append("=" * 50)
    summary_lines.append(f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    summary_lines.append(f"项目数量: {len(repos_data)}")
    summary_lines.append("")
    
    for i, repo in enumerate(repos_data, 1):
        summary_lines.append(f"第 {i} 名: {repo['项目名称']}")
        summary_lines.append(f"   地址: {repo['项目地址']}")
        summary_lines.append(f"   描述: {repo['描述']}")
        summary_lines.append(f"   语言: {repo['编程语言']}")
        summary_lines.append(f"   Star: {repo['Star数量']}")
        summary_lines.append(f"   今日新增: {repo['今日新增Star']}")
        summary_lines.append(f"   技术栈: {repo['涉及技术栈']}")
        summary_lines.append(f"   类型: {repo['项目类型']}")
        
        # 添加项目简介（如果有）
        if '项目简介' in repo and repo['项目简介']:
            summary_lines.append(f"   简介: {repo['项目简介'][:200]}...")
        
        summary_lines.append("")
    
    return '\n'.join(summary_lines)


def main():
    """
    主函数：执行完整的爬取和分析流程
    """
    # 设置控制台编码
    import sys
    import io
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
    
    print("开始爬取 GitHub 今日热门项目...")
    
    # 获取 GitHub Trending 页面
    html_content = get_github_trending_repos()
    
    if not html_content:
        print("获取 trending 页面失败")
        return
    
    # 解析项目列表
    repos = parse_trending_repos(html_content, top_n=10)
    print(f"获取到 {len(repos)} 个热门项目")
    
    # 获取每个项目的 README 并分析
    analyzed_repos = []
    for i, repo in enumerate(repos, 1):
        print(f"处理第 {i}/{len(repos)} 个项目: {repo['full_name']}")
        
        # 获取 README
        readme_content = get_repo_readme(repo['full_name'])
        
        # 分析项目
        analysis = analyze_repo_with_llm(repo, readme_content)
        analyzed_repos.append(analysis)
    
    # 生成中文摘要
    summary = generate_chinese_summary(analyzed_repos)
    print(f"\n分析完成，共 {len(analyzed_repos)} 个项目")
    
    # 保存结果到 JSON 文件
    output_data = {
        "generated_at": datetime.now().isoformat(),
        "total_repos": len(analyzed_repos),
        "repositories": analyzed_repos,
        "summary": summary
    }
    
    output_file = "github_trending_summary.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
    
    print(f"结果已保存到: {output_file}")
    
    # 打印摘要
    print("\n" + "="*60)
    print("GitHub 今日热门项目摘要")
    print("="*60)
    print(summary)
    
    return output_file


if __name__ == "__main__":
    main()