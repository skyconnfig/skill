# 多语言 README 模板

适用于国际项目的专业README模板，包含英文和中文版本。此模板帮助项目触达全球受众。

## 🌟 模板特点

- **双语支持** - 包含英文和中文版本
- **专业结构** - 行业标准的README布局
- **易于定制** - 清晰的占位符和部分
- **跨文化设计** - 适合全球项目
- **SEO优化** - 有助于国际搜索排名

## 📦 包含内容

### 模板文件

| 文件 | 描述 | 语言 |
|------|------|------|
| `README-multilingual.md` | 包含中英文的主模板 | 双语 |
| `README_CN-multilingual.md` | 中文版本模板 | 中文 |
| `GUIDE.md` | 详细实施指南 | 英文 |

### 文件结构

```
multilingual/
├── README-multilingual.md      # 主双语模板
├── README_CN-multilingual.md   # 中文模板
└── GUIDE.md                    # 实施指南
```

## 🚀 快速开始

### 1. 复制模板

```bash
# 进入模板目录
cd githubskill/readme-templates/multilingual

# 复制两个模板到你的项目
cp README-multilingual.md /your-project/README.md
cp README_CN-multilingual.md /your-project/README_CN.md
```

### 2. 自定义模板

编辑两个文件并替换占位符：

**对于 README.md：**
| 占位符 | 替换为 |
|--------|--------|
| `# PROJECT NAME` | 你的项目名称（英文）|
| `## One-line description` | 简短的项目描述（英文）|
| `## 🎯 Overview` | 项目概述（英文）|

**对于 README_CN.md：**
| 占位符 | 替换为 |
|--------|--------|
| `# 项目名称` | 你的项目名称（中文）|
| `## 一句话描述` | 简短的项目描述（中文）|
| `## 🎯 概述` | 项目概述（中文）|

### 3. 版本间链接

在两个文件中添加指向另一语言版本的链接：

**在 README.md 中：**
```markdown
## 🌐 语言

- [中文文档](./README_CN.md)
```

**在 README_CN.md 中：**
```markdown
## 🌐 Languages

- [English](./README.md)
```

## 📝 完整模板

### README-multilingual.md（英文版）

```markdown
# 项目名称

[![许可证](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![版本](https://img.shields.io/badge/Version-1.0.0-blue.svg)](CHANGELOG.md)
[![状态](https://img.shields.io/badge/Status-Active-green.svg)]()

项目的一行简短描述。用1-2句话解释项目的功能。

## 🎯 概述

项目的详细描述。解释项目的目的、目标和主要功能。

### ✨ 功能特性

- 功能1：描述
- 功能2：描述
- 功能3：描述
- 功能4：描述

## 🚀 安装

### 前置要求

- 要求1（例如：Node.js 14+）
- 要求2（例如：Python 3.8+）
- 要求3（如适用）

### 安装步骤

```bash
# 克隆仓库
git clone https://github.com/yourusername/project-name.git

# 进入项目目录
cd project-name

# 安装依赖
npm install
```

## 🎮 使用方法

### 基本示例

```javascript
// 示例代码
const project = require('project-name');

project.initialize({
  option1: 'value1',
  option2: 'value2'
});
```

### 高级用法

```bash
# 高级命令示例
project-name --advanced --option value
```

## 🌐 语言

- [English](./README.md) - 提供英文版本

## 🤝 贡献

我们欢迎贡献！请查看我们的[贡献指南](CONTRIBUTING.md)了解更多详情。

## 📝 许可证

本项目采用MIT许可证 - 有关详细信息，请参阅[LICENSE](LICENSE)文件。

## 📞 联系方式

- 📧 邮箱：contact@project.com
- 💬 讨论：[GitHub Discussions](https://github.com/username/project-name/discussions)
- 🐛 问题：[GitHub Issues](https://github.com/username/project-name/issues)

---

用❤️由[您的姓名/组织]构建
```

### README_CN-multilingual.md（中文版）

```markdown
# 项目名称

[![许可证](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![版本](https://img.shields.io/badge/Version-1.0.0-blue.svg)](CHANGELOG.md)
[![状态](https://img.shields.io/badge/Status-Active-green.svg)]()

项目的一行简短描述。用1-2句话解释项目的功能。

## 🎯 概述

项目的详细中文描述。解释项目的目的、目标和主要功能。本节应帮助用户了解此项目是否符合他们的需求。

### ✨ 功能特性

- 功能1：描述
- 功能2：描述
- 功能3：描述
- 功能4：描述

## 🚀 安装

### 前置要求

- 要求1（例如：Node.js 14+）
- 要求2（例如：Python 3.8+）
- 要求3（如适用）

### 安装步骤

```bash
# 克隆仓库
git clone https://github.com/yourusername/project-name.git

# 进入项目目录
cd project-name

# 安装依赖
npm install
```

## 🎮 使用方法

### 基本示例

```javascript
// 中文示例代码
const project = require('project-name');

project.initialize({
  option1: 'value1',
  option2: 'value2'
});
```

### 高级用法

```bash
# 高级命令示例
project-name --advanced --option value
```

## 🌐 语言

- [English](./README.md) - 提供英文版本

## 🤝 贡献

我们欢迎贡献！请查看我们的[贡献指南](CONTRIBUTING.md)了解更多详情。

## 📝 许可证

本项目采用MIT许可证 - 有关详细信息，请参阅[LICENSE](LICENSE)文件。

## 📞 联系方式

- 📧 邮箱：contact@project.com
- 💬 讨论：[GitHub Discussions](https://github.com/username/project-name/discussions)
- 🐛 问题：[GitHub Issues](https://github.com/username/project-name/issues)

---

用❤️由[您的姓名/组织]构建
```

## 📋 实施检查清单

### 发布前检查

- [ ] 项目名称已翻译为两种语言
- [ ] 描述翻译准确
- [ ] 所有功能已在两个版本中列出
- [ ] 安装步骤已验证
- [ ] 代码示例可正常运行
- [ ] 版本间交叉链接正常工作
- [ ] 许可证文件已包含
- [ ] 联系方式已更新

### 最佳实践

1. **保持结构一致**
   - 在两个版本中保持相同的章节
   - 使用相似的标题和层级
   - 保持平行的格式

2. **准确翻译**
   - 两种语言都使用自然的表达
   - 避免机器翻译
   - 保持技术术语的一致性

3. **视觉一致性**
   - 相同的徽章和图标
   - 相似的代码块格式
   - 匹配的章节长度

4. **定期更新**
   - 一起更新两个版本
   - 保持翻译同步
   - 定期测试链接

## 🎯 使用场景

### 开源项目

触达全球开发者：
- 中文开发者通过中文README找到项目
- 英语使用者使用英文版本
- 两个版本相互链接

### 商业产品

国际市场份额：
- 展示对中国市场的承诺
- 专业的双语文档
- 更好的用户体验

### 个人项目

向全球观众展示：
- 展示国际化技能
- 吸引来自各国的贡献者
- 建立多元化的社区

## 🔧 定制技巧

### 添加更多语言

```markdown
## 🌐 语言/ Languages

- [English](./README.md)
- [中文](./README_CN.md)
- [Español](./README_ES.md)  # 添加更多语言
```

### 地区变体

针对不同地区：
- `README_CN.md` - 简体中文
- `README_TW.md` - 繁体中文
- `README_HK.md` - 香港版本

### 平台特定

添加平台说明：
```markdown
## 📱 平台 / Platforms

- [English](./README.md) - 全球平台
- [中文](./README_CN.md) - 中国平台
```

## 📈 双语README的优势

### SEO优势

- 出现在英文和中文搜索结果中
- 在中国搜索引擎上排名更高
- 全球范围内更好的可发现性

### 用户体验

- 母语文档
- 更低的入门门槛
- 更好地理解功能特性

### 社区建设

- 吸引多元化的贡献者
- 展示国际化意识
- 与全球用户建立信任

## 🚀 高级示例

### 带版本徽章

```markdown
# PROJECT NAME / 项目名称

![Version](https://img.shields.io/badge/Version-1.0.0-blue)
![状态](https://img.shields.io/badge/状态-活跃-green)
```

### 带下载统计

```markdown
![Downloads](https://img.shields.io/badge/Downloads-1K-blue)
![下载量](https://img.shields.io/badge/下载量-1K-blue)
```

### 带社交链接

```markdown
**English:** [Twitter](link) | [WeChat](link)
**中文:** [微博](link) | [微信](link)
```

## 📚 资源

### 翻译工具

- [DeepL](https://www.deepl.com/) - AI翻译
- [Google翻译](https://translate.google.com/) - 免费翻译
- [Google Cloud翻译](https://cloud.google.com/translate/) - Google云端翻译

### 本地化指南

- [GitHub本地化](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/about-readmes)
- [开源本地化](https://www.transifex.com/resource-type/open-source/)

### 相关模板

- 参见 `../README.md` 获取单语言模板
- 参见 `../README-cli.md` 获取CLI特定模板
- 参见 `../README-webapp.md` 获取Web应用模板

## 🤝 贡献

要改进这些模板：
1. Fork此仓库
2. 创建功能分支
3. 添加或改进模板
4. 提交拉取请求
5. 记录更改

## 📝 许可证

这些模板可在MIT许可证下使用。详情请参阅[LICENSE](../../LICENSE)。

## 📞 支持

- **问题**：报告模板问题
- **讨论**：建议改进
- **Wiki**：添加你的示例

---

**模板版本：** 2.0.0  
**最后更新：** 2024年1月  
**创建者：** skyconnfig
