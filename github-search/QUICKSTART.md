# GitHub Search Skill - Quick Start Guide

快速开始指南 - 5分钟上手 GitHub Search Skill

## 📦 安装步骤

### 1. 自动安装（推荐）

```bash
cd ~/.claude/skills/github-search
python scripts/setup.py
```

安装脚本会自动：
- ✓ 检查 Python 版本（需要 3.8+）
- ✓ 安装依赖包（requests, pyyaml, python-dotenv）
- ✓ 创建 Claude Code 命令配置
- ✓ 生成配置文件
- ✓ 验证安装

### 2. 手动安装

如果自动安装失败，手动执行以下步骤：

```bash
# 安装依赖
pip install requests pyyaml python-dotenv

# 创建命令文件
mkdir -p ~/.claude/commands
# 将 github-search.md 内容复制到 ~/.claude/commands/github-search.md

# 创建配置文件
cp config.yaml.example config.yaml
```

## 🔑 配置 GitHub Token（强烈推荐）

虽然不使用 Token 也可以搜索，但配额非常有限（每小时30次）。使用 Token 可以获得：
- ✓ 每小时 5000 次请求（vs 30次）
- ✓ 每分钟 30 次请求（相同）
- ✓ 更稳定的服务

### 获取 Token

1. 访问 https://github.com/settings/tokens
2. 点击 "Generate new token" → "Fine-grained tokens"
3. 选择 "Only select repositories" → "Public repositories"
4. 勾选权限：
   - ✅ `Public repo access (read-only)`
5. 点击 "Generate token"
6. 复制生成的 token

### 设置 Token

**方法1：环境变量**
```bash
# 临时设置（当前终端有效）
export GITHUB_TOKEN="your_token_here"

# 永久设置（添加到 ~/.bashrc 或 ~/.zshrc）
echo 'export GITHUB_TOKEN="your_token_here"' >> ~/.bashrc
source ~/.bashrc
```

**Windows PowerShell:**
```powershell
$env:GITHUB_TOKEN="your_token_here"
# 永久：添加到 $PROFILE
notepad $PROFILE
# 添加：$env:GITHUB_TOKEN="your_token_here"
```

**方法2：.env 文件**
```bash
cd ~/.claude/skills/github-search
cp .env.example .env
# 编辑 .env 文件，填入：
GITHUB_TOKEN=your_token_here
```

## 🚀 快速使用

### 基础搜索

```bash
# 在 Claude Code 中使用
/github-search "claude code"

# 或直接运行脚本
python scripts/search.py "claude code"
```

### 常用场景

```bash
# 搜索最热门的 AI 仓库（按 stars 排序）
/github-search "artificial intelligence" --count 10

# 搜索 Python 机器学习库
/github-search "machine learning" --language python --count 15

# 搜索特定组织的仓库
/github-search "" --org microsoft --sort stars

# 按 forks 排序（找活跃项目）
/github-search "web framework" --sort forks --count 10

# 查看最新更新的仓库
/github-search "" --sort updated --count 20

# 获取 JSON 格式（适合程序处理）
/github-search "react components" --json --count 5

# 导出 CSV
/github-search "deep learning" --csv --count 50 > results.csv
```

### 组合搜索示例

```bash
# TypeScript 写的 UI 库，MIT 许可证
/github-search "ui components" --language typescript --license mit --count 10

# Google 的 Go 语言项目，最近更新
/github-search "" --org google --language go --sort updated --count 15

# 搜索带有特定 topic 的仓库
/github-search "" --topic "react-hooks" --topic "typescript" --count 10
```

## 📊 输出说明

### Pretty 格式（默认）

```
─────────────────────────────────────────────────────────────────────

 1. claude-antrophic/claude-code
     ⭐ 12,345  ·  🍴 2,345 forks  ·  Python (95%) + TypeScript (5%)
     Description: Claude Code skill repository
     Issues: 1,234  ·  Size: 5.2 MB
     Updated: 2d ago
     URL: https://github.com/claude-antrophic/claude-code.git
     Topics: claude, ai, skills, github
     License: MIT

─────────────────────────────────────────────────────────────────────
```

### JSON 格式

```json
{
  "query": "claude code",
  "total_count": 1234,
  "returned_count": 20,
  "items": [
    {
      "full_name": "claude-antrophic/claude-code",
      "stargazers_count": 12345,
      "language": "Python",
      "html_url": "https://github.com/...",
      ...
    }
  ]
}
```

## 🔧 配置说明

编辑 `config.yaml` 调整默认行为：

```yaml
github:
  default_sort: "stars"      # 默认排序
  default_order: "desc"      # 排序顺序
  per_page: 100              # 每页结果数

search:
  default_page_size: 20      # 默认返回条数
  max_page_size: 100         # 最大返回条数

cache:
  enabled: true              # 启用缓存
  ttl: 1800                  # 缓存时间（秒，30分钟）

output:
  format: "pretty"          # 默认输出格式
  truncate_description: 200 # 描述截断长度
```

## 🐛 常见问题

### Q: API rate limit exceeded 错误？

**原因：** 配额用尽

**解决：**
```bash
# 设置 Token（一劳永逸）
export GITHUB_TOKEN="your_token"

# 或等待配额恢复
# 无认证：等待1小时（每小时30次限制）
# 有认证：等待1分钟（每分钟30次）
```

### Q: 搜索结果为空？

**原因：** 关键词太具体或过滤条件太严格

**解决：**
- 尝试更通用的关键词
- 移除部分过滤条件
- 使用英文搜索测试

### Q: 如何查看剩余配额？

```bash
python -c "import requests; import os; token=os.getenv('GITHUB_TOKEN'); headers={'Authorization': f'token {token}'} if token else {}; r=requests.get('https://api.github.com/rate_limit', headers=headers); print(r.json())"
```

### Q: 支持搜索代码内容吗？

当前版本只支持仓库搜索。代码搜索（`search/code` API）配额更严格，将在未来版本支持。

## 🎯 使用技巧

### 1. 精准搜索

使用引号包裹多词查询：
```bash
/github-search '"deep learning"'  # 搜索完整短语 "deep learning"
```

### 2. 排除 unwanted 结果

在查询中使用减号排除：
```bash
/github-search "react -example -demo"  # 排除包含 example 或 demo 的仓库
```

### 3. 批量搜索

从文件读取查询：
```bash
while read query; do
  /github-search "$query" --count 5 --format json
done < queries.txt
```

### 4. 监控活跃仓库

```bash
# 查找过去24小时内更新的仓库
/github-search "" --sort updated --count 50

# 查找特定语言的新项目
/github-search "" --language rust --sort created --count 20
```

## 🆘 获取帮助

- **详细文档：** 查看 `README.md` 和 `SKILL.md`
- **问题反馈：** 在项目仓库提交 Issue
- **GitHub API 文档：** https://docs.github.com/en/rest/search/search

## ✅ 验证安装

运行测试确保一切正常：

```bash
python test_skill.py
```

预期输出：
```
✓ All argument parsing tests passed
✓ All query building tests passed
✓ All cache tests passed
✓ All formatting tests passed
✓ Integration tests passed

All Tests Passed!
```

## 🎉 下一步

安装完成后，你还可以：

1. **自定义配置** - 编辑 `config.yaml` 调整默认行为
2. **查看高级功能** - 阅读 `SKILL.md` 了解技术细节
3. **运行 setup 脚本** - 自动创建命令和验证环境
4. **探索扩展** - 查看 `lib/` 目录了解模块化设计

---

**提示：** 如果不确定如何搜索，试试这些热门查询：

```bash
/github-search "claude code"
/github-search "machine learning" --language python
/github-search "react" --topic "ui"
/github-search "" --org openai --sort stars
```

祝探索愉快！🚀
