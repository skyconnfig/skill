# GitHub Search Skill

Search GitHub repositories directly from Claude Code using `/github-search`. Returns structured results with repo names, descriptions, stars, languages, and topics.

## ✨ Features

- ✅ **完全免费** - 使用 GitHub Search API，无需认证（有配额限制）
- ✅ **结构化输出** - 支持 pretty, json, markdown, csv 格式
- ✅ **多种排序** - 按 stars、forks、updated、pushed 排序
- ✅ **过滤搜索** - 按语言、topic、许可证、组织等过滤
- ✅ **轻量级** - 纯Python脚本，无复杂依赖

## 📦 Prerequisites

### 1. 安装 Python 3.8+

**Windows:**
- 下载 https://www.python.org/downloads/
- 安装时勾选 "Add Python to PATH"

**macOS:**
```bash
brew install python3
```

**Linux:**
```bash
sudo apt-get install python3 python3-pip
```

### 2. 安装 GitHub API Token（可选但建议）

虽然 GitHub Search API 可以在无认证情况下使用，但有严格限制：
- 无认证：每分钟 10 次请求，每小时 30 次
- 有认证（$GITHUB_TOKEN）：每分钟 30 次请求

获取 Token：
1. 访问 https://github.com/settings/tokens
2. 点击 "Generate new token"
3. 选择 "Fine-grained tokens" 或 "Classic tokens"
4. 勾选 `public_repo` 权限（只需读取公开仓库）
5. 生成并复制 token

## 🚀 Installation

### 方法1：自动安装（推荐）

运行设置脚本：
```bash
python scripts/setup.py
```

### 方法2：手动安装

1. **创建 Claude Code 命令**

创建文件 `~/.claude/commands/github-search.md`：
```markdown
---
description: "Search GitHub repositories and return structured results"
argument-hint: "<query> [--count N] [--sort stars|forks|updated|pushed] [--language LANG]"
allowed-tools:
  - Bash
---

Run the GitHub search script with the user's arguments and present the results.

Execute this:

```
python ~/.claude/skills/github-search/scripts/search.py $ARGUMENTS
```

Present the output directly to the user. If the script reports an error, explain it and suggest fixes.
```

2. **验证安装**

```bash
python scripts/search.py "claude code" --count 5
```

## 📖 Usage

### 在 Claude Code 中使用

```
/github-search claude code
/github-search machine learning frameworks --count 15 --sort stars
/github-search react components --language typescript --topic "ui"
/github-search "deep learning" --org microsoft --count 10
```

### 命令行参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `<query>` | 搜索关键词（必需） | - |
| `--count N` | 返回结果数量 | 20 |
| `--sort` | 排序方式: stars\|forks\|updated\|pushed | stars |
| `--order` | 排序顺序: asc\|desc | desc |
| `--language LANG` | 按编程语言过滤 | - |
| `--topic TOPIC` | 按topic过滤 | - |
| `--license LICENSE` | 按许可证过滤 (mit\|apache-2.0\|mit) | - |
| `--org ORG` | 按组织过滤 | - |
| `--user USER` | 按用户过滤 | - |
| `--no-auth` | 不使用 $GITHUB_TOKEN 环境变量 | - |
| `--json` | 输出JSON格式 | - |
| `--csv` | 输出CSV格式 | - |
| `--help` | 显示帮助信息 | - |

### 示例

```bash
# 基础搜索（显示20个结果，按stars排序）
python scripts/search.py "claude code"

# 自定义结果数量
python scripts/search.py "AI agents" --count 10

# 按forks排序
python scripts/search.py "web framework" --sort forks --count 15

# 按语言过滤
python scripts/search.py "machine learning" --language python --count 10

# 按topic过滤
python scripts/search.py "react hooks" --topic "react-hooks" --count 10

# 只搜索特定组织
python scripts/search.py "" --org microsoft --count 10

# 组合使用
python scripts/search.py "kubernetes operators" --language go --sort stars --count 5
```

## 📋 Output Format

每个搜索结果包含：

```
─────────────────────────────────────────────────────────────────────

 1. claude-antrophic/claude-code
    ⭐ 12,345  ·  🍴 2,345 forks  ·  Python (95%) + TypeScript (5%)
    Description: Claude Code skill repository for GitHub integration
    语言: Python 95%, TypeScript 5%  ·  1,234 issues  ·  567 pull requests
    更新: 2025-03-15T10:30:00Z  ·  HTTPS克隆: https://github.com/claude-antrophic/claude-code.git

─────────────────────────────────────────────────────────────────────
```

### 显示信息

- **仓库全名** - organization/repo
- **⭐ stars** - star 数量
- **🍴 forks** - fork 数量
- **语言分布** - 主要语言及百分比
- **描述** - 仓库描述
- **语言组成** - 各语言占比
- **issues** - 开/闭 issues 数量
- **更新** - 最后更新时间
- **克隆URL** - HTTPS和SSH克隆地址

## 🔧 Configuration

创建 `.env` 文件自定义配置（可选）：

```bash
# 复制示例配置
cp .env.example .env
```

可配置项：
```bash
# GitHub API token (从环境变量读取)
GITHUB_TOKEN=${GITHUB_TOKEN}

# 默认搜索参数
DEFAULT_COUNT=20
DEFAULT_SORT=stars
DEFAULT_ORDER=desc

# API请求配置
API_TIMEOUT=30
API_PER_PAGE=100
```

## 🔍 高级用法

### JSON 输出（用于程序处理）

```bash
python scripts/search.py "claude code" --json --count 5
```

输出示例：
```json
{
  "query": "claude code",
  "total_count": 1234,
  "items": [
    {
      "full_name": "claude-antrophic/claude-code",
      "description": "Claude Code skill repository",
      "language": "Python",
      "languages": {"Python": 95, "TypeScript": 5},
      "stargazers_count": 12345,
      "forks_count": 2345,
      "open_issues_count": 1234,
      "created_at": "2025-01-01T00:00:00Z",
      "updated_at": "2025-03-15T10:30:00Z",
      "pushed_at": "2025-03-15T10:30:00Z",
      "html_url": "https://github.com/claude-antrophic/claude-code",
      "ssh_url": "git@github.com:claude-antrophic/claude-code.git",
      "topics": ["claude", "ai", "skills"],
      "license": "MIT",
      "owner": {
        "login": "claude-antrophic",
        "type": "Organization",
        "avatar_url": "https://..."
      }
    }
  ]
}
```

### CSV 导出

```bash
python scripts/search.py "deep learning" --csv --count 50 > results.csv
```

### 批量搜索

```bash
# 循环读取关键词文件
while read query; do
  python scripts/search.py "$query" --count 5 --sort stars
done < queries.txt
```

### 监控仓库更新

```bash
# 搜索特定组织的最新仓库
python scripts/search.py "" --org your-org --sort updated --count 20
```

## 🛠️ Development

### 项目结构

```
github-search/
├── SKILL.md              # Skill 详细文档（中文）
├── README.md             # 本文件 - 用户指南
├── CHANGELOG.md          # 版本历史
├── LICENSE               # MIT 许可证
├── .env.example          # 环境变量示例
├── .gitignore            # Git 忽略文件
├── requirements.txt      # Python 依赖
├── scripts/
│   ├── search.py        # 主搜索脚本
│   └── setup.py         # 安装向导
├── lib/                 # 库目录（可选扩展）
│   ├── formatter.py    # 输出格式化
│   ├── github_api.py   # GitHub API 封装
│   └── cache.py        # 缓存功能
├── cache/              # 缓存目录（自动生成）
├── logs/               # 日志目录（自动生成）
└── test_skill.py       # 测试脚本
```

### 本地开发

```bash
# 克隆或进入项目目录
cd ~/.claude/skills/github-search

# 安装依赖（如果使用虚拟环境）
pip install -r requirements.txt

# 运行测试
python test_skill.py

# 或直接搜索
python scripts/search.py "test query" --count 3
```

### 扩展开发

计划中的模块化结构：

```python
# Python API（未来版本）
from github_search import GitHubSearcher

searcher = GitHubSearcher(
    token=os.getenv("GITHUB_TOKEN"),
    count=20,
    sort="stars"
)

results = searcher.search("claude code")
formatted = searcher.format("pretty", results)
print(formatted)
```

## ❓ FAQ

### Q: GitHub API 配额是什么？

A: GitHub Search API 有速率限制：
- 无认证：每分钟 10 次请求，每小时 30 次（非常严格）
- 有认证：每分钟 30 次请求
- 每个请求最多返回 100 条结果（分页）

### Q: 为什么推荐使用 GitHub Token？

A:
- **更高配额** - 无 token 限制极严，很容易触发限流
- **更快搜索** - 认证请求优先级更高
- **无成本** - Token 完全免费
- **隐私** - 仅需 public_repo 只读权限

### Q: 如何设置 $GITHUB_TOKEN 环境变量？

**Windows (PowerShell):**
```powershell
$env:GITHUB_TOKEN="your_token_here"
```

持久化（加入 $PROFILE）：
```powershell
# 编辑 profile
notepad $PROFILE
# 添加: $env:GITHUB_TOKEN="your_token_here"
```

**macOS/Linux:**
```bash
export GITHUB_TOKEN="your_token_here"
# 持久化：添加到 ~/.bashrc 或 ~/.zshrc
```

### Q: 搜索速度如何？

A: 通常单次搜索在 1-5 秒内完成，取决于：
- 网络速度
- 返回结果数量
- GitHub API 响应时间

### Q: 可以搜索代码内容吗？

A: 当前实现搜索仓库（repositories）。GitHub API 支持代码搜索，但限制更严格：
- 每分钟 30 次（已认证）
- 每次搜索最多返回 100 个结果

如需代码搜索功能，可在后续版本添加。

## 🐛 故障排除

### 错误: `API rate limit exceeded`

**原因:** 无认证或请求过于频繁，触发了 GitHub 限流

**解决:**
```bash
# 1. 设置 GitHub Token
export GITHUB_TOKEN="your_token_here"

# 2. 或减少请求频率，等待限流恢复
# 无认证：每小时限制30次，需等待1小时
# 有认证：每分钟限制30次，需等待1分钟

# 3. 检查当前限流状态
python -c "import requests; r=requests.get('https://api.github.com/rate_limit', headers={'Authorization': 'token $GITHUB_TOKEN'}); print(r.json())"
```

### 错误: `403 Client Error: Forbidden`

**原因:**
- GitHub API 不可用
- IP 被限制
- Token 无效

**解决:**
1. 检查网络连接
2. 验证 Token 是否有效
3. 尝试使用 `--no-auth` 绕过认证

### 搜索结果为空

**原因:**
- 关键词太具体
- 无匹配仓库
- 过滤条件太严格

**解决:**
- 尝试更通用的关键词
- 移除部分过滤条件（如 language 或 topic）
- 使用英文搜索测试

## 🤝 Contributing

欢迎提交 Issue 和 Pull Request！

## 📄 License

MIT License - 详见 LICENSE 文件

## 🔗 Related

- [GitHub Search API](https://docs.github.com/en/rest/search/search)
- [GitHub API Rate Limits](https://docs.github.com/en/rest/overview/resources-in-the-rest-api#rate-limiting)
- [GitHub Authentication](https://docs.github.com/en/rest/overview/resources-in-the-rest-api#authentication)

---

**提示:** 本 skill 使用 GitHub Search API，适合个人和研究使用。生产环境建议实现更完善的缓存和重试机制。
