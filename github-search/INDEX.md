# GitHub Search Skill - Documentation Index

文档导航中心 - 快速找到所需信息

## 📚 文档结构

```
.github-search/
├── QUICKSTART.md          ⭐ 新手从这里开始（5分钟上手）
├── README.md              📖 完整使用指南（最全面）
├── SKILL.md               🔧 技术规格说明
├── INDEX.md               📑 本文件 - 文档导航
├── CHANGELOG.md           📜 版本历史和更新日志
├── VERIFICATION.md        ✅ 安装验证清单
├── PROJECT_SUMMARY.md     📊 项目总结（技术概览）
├── CLAUDE.md              🎯 Claude Code 专用配置
└── .claude/
    └── github-search.md  💡 Claude Code 命令定义
```

## 🎯 按需求查找

### 我是新用户，想快速上手
→ 阅读 **[QUICKSTART.md](QUICKSTART.md)**
- 5 分钟快速入门
- 安装步骤
- 基础使用示例
- 常见问题解答

### 我想了解所有功能和用法
→ 阅读 **[README.md](README.md)**
- 完整功能列表
- 详细使用说明
- 所有命令行参数
- 输出格式详解
- FAQ 和故障排除

### 我想了解技术实现细节
→ 阅读 **[SKILL.md](SKILL.md)**
- Skill 架构设计
- API 接口说明
- 返回格式规范
- 扩展开发指南
- 安全性考虑

### 我想验证安装是否正确
→ 查看 **[VERIFICATION.md](VERIFICATION.md)**
- 逐步验证清单
- 文件结构检查
- 功能测试步骤
- 配额验证方法
- 故障排除指南

### 我想了解项目历史和未来规划
→ 查看 **[CHANGELOG.md](CHANGELOG.md)**
- v1.0.0 版本特性
- 已知问题和限制
- v1.1.0/v1.2.0 计划
- 迁移指南

### 我想快速回顾项目概览
→ 查看 **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)**
- 项目结构总览
- 核心特性总结
- 技术栈说明
- 性能指标
- 扩展路线图

## 🔍 按场景查找

### 安装和配置
1. **QUICKSTART.md** - 快速安装步骤
2. **VERIFICATION.md** - 验证安装成功
3. **README.md** - 配置选项详解

### 日常使用
1. **README.md** - 基本使用和示例（📖 最常用）
2. **QUICKSTART.md** - 常见场景示例
3. **SKILL.md** - 高级功能和技术细节

### 问题解决
1. **README.md** - FAQ 和故障排除章节
2. **VERIFICATION.md** - 诊断步骤
3. **CHANGELOG.md** - 已知问题列表

### 开发和扩展
1. **SKILL.md** - 扩展开发指南
2. **PROJECT_SUMMARY.md** - 架构概览
3. **README.md** - 开发部分

### 集成到 Claude Code
1. **QUICKSTART.md** - Claude Code 集成部分
2. **CLAUDE.md** - Claude Code 特殊配置
3. **.claude/github-search.md** - 命令定义

## 📖 文档详细说明

### QUICKSTART.md
**目标读者：** 所有用户，特别是新手
**内容重点：**
- 快速安装（自动/手动）
- Token 配置（为什么重要）
- 基础使用示例
- 常用命令速查
- 故障快速解决

**阅读时间：** 5-10 分钟

### README.md
**目标读者：** 所有用户
**内容重点：**
- 完整功能列表
- 详细命令行参数
- 所有输出格式
- 配置选项
- 高级用法
- 完整的 FAQ

**阅读时间：** 15-20 分钟

### SKILL.md
**目标读者：** 开发者、贡献者、高级用户
**内容重点：**
- Skill 架构设计
- API 规范
- 数据格式
- 扩展接口
- 安全性规范

**阅读时间：** 20-30 分钟

### VERIFICATION.md
**目标读者：** 安装遇到问题的用户
**内容重点：**
- 验证清单
- 测试步骤
- 诊断流程
- 常见错误及解决

**阅读时间：** 10-15 分钟

## 💡 快速参考

### 最常用命令

```bash
# 基础搜索
/github-search "query"

# 按 stars 排序，取前 10 个
/github-search "query" --count 10

# 按语言过滤
/github-search "query" --language python

# 搜索特定组织
/github-search "" --org microsoft

# 获取 JSON 格式
/github-search "query" --json

# 导出 CSV
/github-search "query" --csv > results.csv
```

### 关键配置

```yaml
# config.yaml
github:
  default_sort: "stars"     # 默认排序
  per_page: 100             # 每页结果数

cache:
  enabled: true             # 启用缓存
  ttl: 1800                 # 缓存时间（30分钟）

output:
  format: "pretty"         # 输出格式
```

### 环境变量

```bash
GITHUB_TOKEN=your_token_here        # GitHub API Token（强烈推荐）
DEFAULT_COUNT=20                    # 默认结果数
DEFAULT_SORT=stars                  # 默认排序
```

## 🆘 获取帮助

### 快速帮助
```bash
python scripts/search.py --help
```

### 查看具体示例
```bash
# 查看 README 中的示例
cat README.md | grep -A 3 "示例"

# 查看 QUICKSTART 中的场景
cat QUICKSTART.md | grep -A 5 "###"
```

### 运行测试
```bash
python test_skill.py
```

### 检查配额
```bash
python -c "import requests, os; token=os.getenv('GITHUB_TOKEN'); headers={'Authorization': f'token {token}'} if token else {}; print(requests.get('https://api.github.com/rate_limit', headers=headers).json())"
```

## 📊 文档统计

| 文档 | 字数（估算） | 阅读时间 | 适合人群 |
|------|-------------|---------|---------|
| QUICKSTART.md | ~3,500 | 5-10 min | 所有用户 |
| README.md | ~8,000 | 15-20 min | 所有用户 |
| SKILL.md | ~10,000 | 20-30 min | 开发者 |
| VERIFICATION.md | ~4,000 | 10-15 min | 安装用户 |
| PROJECT_SUMMARY.md | ~2,500 | 5-10 min | 技术负责人 |
| CHANGELOG.md | ~1,500 | 3-5 min | 所有用户 |
| INDEX.md | ~1,200 | 3-5 min | 所有用户 |

**总文档量：** ~30,700 字（约 60 页）

## 🎯 推荐阅读路径

### 路径 1：快速上手（30 分钟）
1. QUICKSTART.md（10 min）
2. README.md - 基本使用部分（10 min）
3. 实际运行几个示例（10 min）

### 路径 2：深入了解（60 分钟）
1. QUICKSTART.md（10 min）
2. README.md（20 min）
3. SKILL.md - 核心功能部分（15 min）
4. 实际练习（15 min）

### 路径 3：开发贡献（90 分钟）
1. QUICKSTART.md（10 min）
2. README.md - Development 部分（10 min）
3. SKILL.md - 完整阅读（30 min）
4. PROJECT_SUMMARY.md（10 min）
5. 查看源代码（30 min）

## 🔗 在线资源

- **GitHub Search API 文档：** https://docs.github.com/en/rest/search/search
- **GitHub API 配额：** https://docs.github.com/en/rest/overview/resources-in-the-rest-api#rate-limiting
- **GitHub Token 设置：** https://github.com/settings/tokens
- **Python requests 库：** https://requests.readthedocs.io/

## 📝 文档维护

本文档集由以下人员维护：
- 原始作者：Claude Code
- 更新日期：2026-04-01
- 版本：1.0.0

如需更新文档，请：
1. 编辑对应的 `.md` 文件
2. 更新本 INDEX.md 中的相关链接
3. 提交 Pull Request

---

**快速提示：** 不确定读哪个？先看 **QUICKSTART.md** ！
