# YouTube Search Skill

Search YouTube directly from Claude Code using `/yt-search`. Returns structured results with titles, channels, view counts, duration, and dates — filtered to the last 6 months by default.

## ✨ Features

- ✅ **完全免费** - 使用 yt-dlp，无需 YouTube API 密钥
- ✅ **无配额限制** - 不消耗每日 API 配额
- ✅ **结构化输出** - 支持 pretty, json, markdown, csv 格式
- ✅ **日期过滤** - 默认只显示最近6个月的视频
- ✅ **格式化显示** - 观看数、订阅数自动格式化（K/M）
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

### 2. 安装 yt-dlp

```bash
pip install yt-dlp
```

或使用升级命令确保最新版本：
```bash
pip install -U yt-dlp
```

## 🚀 Installation

### 方法1：自动安装（推荐）

运行设置脚本：
```bash
python scripts/setup.py
```

### 方法2：手动安装

1. **创建 Claude Code 命令**

创建文件 `~/.claude/commands/yt-search.md`：
```markdown
---
description: "Search YouTube and return structured video results"
argument-hint: "<query> [--count N] [--months N]"
allowed-tools:
  - Bash
---

Run the YouTube search script with the user's arguments and present the results.

Execute this command:

```
python ~/.claude/skills/yt-search/scripts/search.py $ARGUMENTS
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
/yt-search claude code skills
/yt-search AI agents --count 10
/yt-search react tutorials --months 3
/yt-search machine learning --no-date-filter
```

### 命令行参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `<query>` | 搜索关键词（必需） | - |
| `--count N` | 返回结果数量 | 20 |
| `--months N` | 只显示最近N个月的视频 | 6 |
| `--top-views N` | 按播放量排序，返回前N个结果 | 未启用 |
| `--no-date-filter` | 不限制日期范围 | - |
| `--excel <filename>` | 导出到Excel文件 | - |
| `--help` | 显示帮助信息 | - |

### 示例

```bash
# 基础搜索（显示20个结果，最近6个月）
python scripts/search.py "claude code"

# 自定义结果数量
python scripts/search.py "React Hooks" --count 10

# 搜索最近3个月的视频
python scripts/search.py "AI tutorial" --months 3

# 显示所有时间段的视频
python scripts/search.py "linux commands" --no-date-filter

# 组合使用
python scripts/search.py "python asyncio" --count 5 --months 1
```

## 📋 Output Format

每个搜索结果包含：

```
─────────────────────────────────────────────────────────────────────

 1. Claude Code Complete Tutorial - Build AI Assistant in 25 Min
     频道: Traversy Media (1.5M subs)  ·  2,456,789 views  ·  25:30  ·  Mar 15, 2025
     链接: https://youtube.com/watch?v=abc123

─────────────────────────────────────────────────────────────────────
```

### 显示信息

- **标题** - 视频标题
- **频道** - 频道名称 + 订阅数（自动格式化：1.5M, 45.2K）
- **观看数** - 观看次数（带千位分隔符）
- **时长** - 视频时长（MM:SS 或 HH:MM:SS）
- **日期** - 上传日期（自动格式化）
- **链接** - YouTube 视频链接

## 🔧 Configuration

创建 `.env` 文件自定义配置（可选）：

```bash
# 复制示例配置
cp .env.example .env
```

可配置项：
```bash
# yt-dlp 可执行文件路径（默认从PATH查找）
YT_DLP_PATH=yt-dlp

# 默认搜索参数
DEFAULT_COUNT=20
DEFAULT_MONTHS=6
```

## 🔍 高级用法

### 输出为 JSON 格式（用于程序处理）

虽然脚本主要输出美观的文本格式，但可以通过脚本重构来输出 JSON。如需 JSON 输出，可以：

1. 修改 `scripts/search.py` 的 `main()` 函数，在最后添加 `--json` 参数支持
2. 或使用后续计划中的 `lib/` 模块化版本

### 批量搜索

```bash
# 循环读取关键词文件
while read query; do
  python scripts/search.py "$query" --count 5 --months 3
done < queries.txt
```

### 导出为 Markdown 报告

```bash
python scripts/search.py "TypeScript 2025" --count 10 > report.md
```

### 导入到 Excel/CSV

```bash
# 重构脚本后支持CSV输出（计划功能）
python scripts/search.py "data science" --count 50 --csv > results.csv
```

## 🛠️ Development

### 项目结构

```
yt-search/
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
│   └── cache.py        # 缓存功能
├── cache/              # 缓存目录（自动生成）
├── logs/               # 日志目录（自动生成）
└── test.py             # 测试脚本
```

### 本地开发

```bash
# 克隆或进入项目目录
cd ~/.claude/skills/yt-search

# 安装依赖（如果使用虚拟环境）
pip install -r requirements.txt

# 运行测试
python test.py

# 或直接搜索
python scripts/search.py "test query" --count 3
```

### 扩展开发

计划中的模块化结构（未来版本）：

```javascript
// JavaScript API（计划中）
import { YouTubeSearcher } from '~/.claude/skills/yt-search/lib/index.js';

const searcher = new YouTubeSearcher({
  count: 20,
  months: 6,
  format: 'pretty',
});

const results = await searcher.search('claude code');
console.log(results);
```

## ❓ FAQ

### Q: yt-dlp 是什么？

A: yt-dlp 是 YouTube-DL 的一个分支，是一个命令行工具，可以搜索和下载YouTube视频。它不需要API密钥，通过解析YouTube页面实现搜索功能。

### Q: 为什么选择 yt-dlp 而不是 YouTube API？

A:
- **免费** - 不需要支付 API 配额费用
- **无限制** - 没有每日10000 units的限制
- **简单** - 无需申请 Google Cloud 项目
- **快速** - 直接搜索，无需认证流程

### Q: 会违反 YouTube 服务条款吗？

A: yt-dlp 主要用于个人研究和教育目的。根据YouTube服务条款，自动化搜索行为可能受到限制。建议：
- 不要用于大规模商业爬取
- 尊重 rate limits，不要频繁请求
- 仅用于合法的搜索和分析用途

### Q: 搜索速度如何？

A: 通常单次搜索在 2-10 秒内完成，取决于：
- 网络速度
- 搜索结果的多少
- yt-dlp 的性能（通常很快）

### Q: 如何更新 yt-dlp？

A:
```bash
pip install -U yt-dlp
```

## 🐛 故障排除

### 错误: `yt-dlp: command not found`

**原因:** yt-dlp 未安装或不在 PATH 中

**解决:**
```bash
# 安装 yt-dlp
pip install yt-dlp

# 验证安装
yt-dlp --version
```

### 错误: 搜索超时

**原因:** 网络问题或YouTube反爬虫机制

**解决:**
1. 检查网络连接
2. 尝试减少 `--count` 参数
3. 添加延迟（计划功能）

### 搜索结果为空

**原因:**
- 关键词太具体
- 地区/语言限制
- 无结果匹配

**解决:**
- 尝试更通用的关键词
- 使用英文搜索测试
- 检查日期过滤设置

## 🤝 Contributing

欢迎提交 Issue 和 Pull Request！

## 📄 License

MIT License - 详见 LICENSE 文件

## 🔗 Related

- [yt-dlp GitHub](https://github.com/yt-dlp/yt-dlp)
- [Claude Code Skills](https://github.com/anthropics/claude-code)
- [YouTube Data API (对比用)](https://developers.google.com/youtube/v3)

---

**提示:** 本 skill 使用 yt-dlp 实现免费搜索，适合个人使用和研究。生产环境建议使用官方 API 以获得更好的稳定性和合规性。
