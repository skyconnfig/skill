---
name: github-search
description: GitHub仓库搜索和分析技能 - 搜索仓库、获取元数据、分析趋势
version: 1.0.0
author: Claude Code
source: user-created
tags:
  - github
  - search
  - repositories
  - code
  - api
---

# GitHub Search Skill

## 概述

本 skill 提供强大的 GitHub 仓库搜索、元数据提取和趋势分析能力。支持关键词搜索、按 stars/forks/updated 排序，以及按语言、topic、许可证、组织等多种过滤条件。

## 核心功能

### 1. 仓库搜索

**基础搜索：**
- ✅ 关键词搜索仓库
- ✅ 按 stars、forks、updated、pushed 排序
- ✅ 分页获取结果（每次最多100个）
- ✅ 多种过滤条件（语言、topic、许可证、组织、用户）

**高级搜索：**
- ✅ 精确匹配搜索（引号包裹）
- ✅ 多条件组合（AND 逻辑）
- ✅ 排除关键词（使用 - 前缀）
- ✅ Topic 多选（多个 --topic 参数）

### 2. 元数据获取

**仓库信息：**
- ✅ 名称、描述、URL
- ✅ stars、forks、issues 数量
- ✅ 主要编程语言及占比
- ✅ 创建时间、更新时间、最后推送时间
- ✅ 许可证类型
- ✅ Topics 标签
- ✅ 所有者信息（个人/组织）
- ✅ 克隆地址（HTTPS/SSH）

**批量获取：**
- ✅ 一次获取多个仓库的详细元数据
- ✅ 支持分页自动处理
- ✅ 自动重试失败请求

### 3. 输出格式

**支持格式：**
- ✅ Pretty（美观的表格格式）- 默认
- ✅ JSON（结构化数据）
- ✅ CSV（表格数据）
- ✅ Markdown（文档格式）

**格式化功能：**
- ✅ 数字格式化（1.2K, 3.4M）
- ✅ 日期格式化（相对时间，精确时间）
- ✅ 语言百分比显示
- ✅ 多列布局优化

### 4. 缓存和性能

- ✅ 内存缓存（可配置 TTL）
- ✅ 请求去重
- ✅ 速率限制处理
- ✅ 自动重试机制
- ✅ 分页自动合并

## 使用方法

### 基本搜索

```
用户: 搜索"claude code"仓库
Skill: 执行GitHub搜索，返回前10个结果，包含：
  - 仓库名称和URL
  - stars数
  - 编程语言
  - 描述
  - 更新时间
```

### 按stars排序搜索

```
用户: 搜索"AI agents"按stars排序，返回前15个
Skill: 执行GitHub搜索，按stars降序排列，返回前15个最热门仓库
```

### 按语言过滤

```
用户: 搜索"machine learning"且语言为Python的仓库
Skill: 返回语言为Python的机器学习相关仓库
```

### 组织搜索

```
用户: 显示microsoft组织的最新仓库
Skill: 搜索 org:microsoft，按updated排序，返回最新更新的仓库
```

## 技术实现

### API选择

**方案1: GitHub Search API（官方，推荐）**
```python
# 无需API密钥（但有严格限制）
# 或使用token获得更高配额
import requests

headers = {}
if os.getenv("GITHUB_TOKEN"):
    headers["Authorization"] = f"token {os.getenv('GITHUB_TOKEN')}"

response = requests.get(
    "https://api.github.com/search/repositories",
    params={
        "q": query,
        "sort": sort,
        "order": order,
        "per_page": per_page,
        "language": language,
        "topic": topic,
    },
    headers=headers
)
```

**方案2: GitHub GraphQL API（高级）**
- 更灵活的查询
- 更少的数据传输
- 更高的配额
- 适合复杂查询

**方案3: 模拟数据（无配额担忧）**
- 仅用于演示和测试
- 不需要网络连接
- 可快速原型开发

### 配置要求

```bash
# .env 或配置文件
GITHUB_TOKEN=your_github_token_here  # 可选但强烈推荐
DEFAULT_COUNT=20
DEFAULT_SORT=stars
DEFAULT_ORDER=desc
```

## 返回格式

### 搜索结果（Pretty格式）

```
┌─────────────────────────────────────────────────────────────────────┐
│ 1. claude-antrophic/claude-code                                    │
│ ⭐ 12,345  ·  🍴 2,345 forks  ·  Python (95%) + TypeScript (5%)   │
│ Description: Claude Code skill repository for GitHub integration  │
│ 语言: Python 95%, TypeScript 5%  ·  1,234 issues  ·  567 PRs     │
│ 更新: 2025-03-15 10:30 (15天前)  ·  HTTPS: https://github.com/... │
└─────────────────────────────────────────────────────────────────────┘
```

### 结构化数据（JSON格式）

```json
{
  "success": true,
  "query": "claude code",
  "total_count": 1234,
  "page": 1,
  "per_page": 20,
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
      "size": 5000,
      "fork": false,
      "archived": false,
      "disabled": false,
      "html_url": "https://github.com/claude-antrophic/claude-code",
      "ssh_url": "git@github.com:claude-antrophic/claude-code.git",
      "clone_url": "https://github.com/claude-antrophic/claude-code.git",
      "topics": ["claude", "ai", "skills", "github"],
      "license": {"name": "MIT", "spdx_id": "MIT", "url": "..."},
      "owner": {
        "login": "claude-antrophic",
        "type": "Organization",
        "avatar_url": "https://avatars.githubusercontent.com/u/...",
        "url": "https://api.github.com/users/claude-antrophic"
      }
    }
  ]
}
```

## 使用限制与最佳实践

### GitHub API 限制

**无认证：**
- 每小时 30 次请求（非常严格）
- 每分钟 10 次请求

**有认证（$GITHUB_TOKEN）：**
- 每小时 5000 次请求
- 每分钟 30 次请求

**优化策略：**
- ⚠️ 强烈建议使用 GitHub Token
- 缓存常用搜索结果
- 合理设置 per_page（最大100）
- 避免频繁重复搜索
- 使用条件过滤减少结果集

### 配额管理

```python
# 检查剩余配额
import requests

def check_rate_limit():
    headers = {}
    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"token {token}"

    r = requests.get("https://api.github.com/rate_limit", headers=headers)
    data = r.json()["resources"]["core"]
    return {
        "limit": data["limit"],
        "remaining": data["remaining"],
        "reset": data["reset"],
    }
```

### 错误处理

**常见错误：**
- `rateLimitExceeded` - 配额耗尽
- `403 Forbidden` - 被限制或IP被封
- `422 Validation Failed` - 查询参数错误
- `503 Service Unavailable` - GitHub服务暂时不可用

**应对措施：**
```python
try:
    result = search_repositories(query)
    return result
except requests.exceptions.HTTPError as e:
    if e.response.status_code == 403:
        # 配额不足，等待重置
        reset_time = e.response.headers.get('X-RateLimit-Reset')
        wait_seconds = int(reset_time) - time.time()
        time.sleep(max(0, wait_seconds))
        return search_repositories(query)
    if e.response.status_code == 422:
        # 参数错误，提示用户
        return {"error": "搜索参数无效，请检查输入"}
    raise
```

## 示例工作流

### 场景1: 搜索热门AI框架

```
用户: 找10个最流行的机器学习Python库
Skill执行:
1. 搜索 "machine learning"
2. 添加过滤: language:python
3. 按stars排序，取前10
4. 返回：
   - TensorFlow (95.2K ⭐)
   - PyTorch (71.3K ⭐)
   - scikit-learn (58.1K ⭐)
   ...
```

### 场景2: 搜索特定组织的仓库

```
用户: 显示google组织的前20个热门仓库
Skill执行:
1. 搜索 org:google
2. 按stars排序
3. 过滤掉forks（只显示原仓库）
4. 返回仓库列表及star数
```

### 场景3: 多条件组合搜索

```
用户: 搜索TypeScript写的UI组件库，支持MIT许可证
Skill执行:
1. 搜索 "react components"
2. 过滤: language:typescript license:mit
3. 按stars排序
4. 返回符合条件的仓库
   - 显示license、language、stars
   - 提供详细URL
```

### 场景4: 监控仓库趋势

```
用户: 监控"kubernetes"相关仓库过去一周的更新
Skill执行:
1. 搜索 "kubernetes"
2. 按pushed时间排序
3. 过滤掉超过1年未更新的仓库
4. 返回近期活跃的仓库清单
5. （可选）生成趋势报告
```

## 安全性考虑

- ✅ 不要在前端暴露 API tokens
- ✅ 使用只读权限的 GitHub Token（public_repo）
- ✅ 验证用户输入，防止注入攻击
- ✅ 限制搜索频率，遵守 GitHub 服务条款
- ✅ 日志记录（仅用于调试，不存储敏感数据）
- ⚠️ 遵守 [GitHub API 服务条款](https://docs.github.com/en/rest/overview/terms-of-service)

## 扩展功能（可选）

### 1. 代码搜索

```python
def search_code(query, language=None):
    """搜索代码内容（配额更严格）"""
    url = "https://api.github.com/search/code"
    params = {"q": query, "per_page": 100}
    if language:
        params["q"] += f" language:{language}"
    # 需处理更严格的速率限制
```

### 2. Issue搜索

```python
def search_issues(query, state="open"):
    """搜索issues和PR"""
    url = "https://api.github.com/search/issues"
    params = {"q": query, "state": state, "per_page": 100}
```

### 3. 用户搜索

```python
def search_users(query, type="user"):
    """搜索GitHub用户或组织"""
    url = "https://api.github.com/search/users"
    params = {"q": query, "type": type, "per_page": 100}
```

### 4. 趋势分析

```python
def analyze_trends(repos):
    """分析仓库趋势"""
    trends = {
        "avg_stars_per_day": calculate_growth_rate(repos),
        "most_active_languages": get_active_languages(repos),
        "licenses_distribution": get_licenses(repos),
        "top_contributors": get_top_orgs(repos),
    }
    return trends
```

### 5. 数据导出

- JSON 格式（API响应）
- CSV 导出（Excel可读）
- Markdown报告（可直接发布）
- HTML可视化（需要前端支持）

## 配置文件示例

```yaml
# github-search.config.yaml
api:
  base_url: "https://api.github.com"
  token: "${GITHUB_TOKEN}"  # 从环境变量读取
  timeout: 30
  per_page: 100
  max_pages: 5  # 最多获取5页（500条）

search:
  default_count: 20
  default_sort: stars  # stars|forks|updated|pushed
  default_order: desc  # asc|desc
  default_language: null
  safe_search: false

cache:
  enabled: true
  ttl: 1800  # 30分钟
  backend: memory  # memory|file|redis
  max_size: 1000

rate_limit:
  requests_per_minute: 30  # 认证用户限额
  warn_at_usage: 0.8  # 80%时警告
  auto_wait: true  # 自动等待配额恢复

output:
  format: pretty  # pretty|json|csv|markdown
  include_languages: true
  include_topics: true
  include_license: true
  show_owner_avatar: false
  truncate_description: 200  # 描述截断长度

features:
  auto_suggest: true  # 自动建议关键词
  trending: true  # 显示热门话题
  language_detection: false  # 自动检测查询语言
  advanced_filters: true  # 启用高级过滤
```

## 限制与注意事项

### GitHub API 限制

1. **认证配额**
   - 无认证：每小时 30 次请求（极低，强烈不推荐）
   - 有认证：每小时 5000 次请求
   - Search API 每分钟最多 30 次请求（无论总配额）

2. **结果数量**
   - 单次请求最多 100 条
   - 通过分页最多获取 1000 条（10页）
   - 排序方式影响分页（stars 排序不能分页超过前几页）

3. **搜索复杂度**
   - 复杂查询可能消耗更多配额
   - 某些搜索词会返回"无结果"（太具体）
   - Topic 搜索需要仓库显式标注

### 法律与合规

- ⚠️ 遵守 [GitHub API 服务条款](https://docs.github.com/terms)
- ⚠️ 不得用于自动化数据挖掘或商业爬取
- ⚠️ 尊重仓库许可证
- ✅ 仅用于合法的搜索、分析、研究目的
- ✅ 不要禁用或绕过 rate limits

## 调试与日志

启用调试模式：

```bash
GITHUB_SEARCH_DEBUG=true /github-search "React"
```

会输出：
- API请求详情（URL、参数）
- 配额使用情况
- 响应时间
- 缓存命中率
- 错误详情

## 替代方案

如果GitHub API配额不足，可以考虑：

1. **GitHub GraphQL API**
   - 优点：更灵活，配额更高
   - 缺点：学习曲线较陡

2. **GitHub CLI (gh)**
   ```bash
   gh search repos "query" --limit 20 --json name,stargazersCount
   ```
   - 优点：已安装gh则无需额外依赖
   - 缺点：输出格式化较复杂

3. **自建爬虫**
   - 优点：完全可控，无配额限制
   - 缺点：违反ToS风险，需要维护

## 版本历史

- **1.0.0** (2026-04-01): 初始版本，支持基础搜索和元数据获取

## 获取帮助

- 📖 [GitHub Search API 文档](https://docs.github.com/en/rest/search/search)
- 🔧 [GitHub API 配额计算器](https://docs.github.com/en/rest/overview/resources-in-the-rest-api#rate-limiting)
- 💬 问题反馈：在项目仓库提交Issue

---

**提示：** 使用此 skill 时，强烈建议设置 $GITHUB_TOKEN 环境变量以获得更好的配额和稳定体验。对于生产环境，务必实现配额监控和优雅降级机制。
