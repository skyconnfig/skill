# Multilingual README Template

A professional README template with both English and Chinese versions for international projects. This template helps projects reach global audiences.

## 🌟 Template Features

- **Bilingual Support** - English and Chinese versions included
- **Professional Structure** - Industry-standard README layout
- **Easy Customization** - Clear placeholders and sections
- **Cross-cultural Design** - Suitable for global projects
- **SEO Optimized** - Helps with international search rankings

## 📦 What's Included

### Template Files

| File | Description | Language |
|------|-------------|----------|
| `README-multilingual.md` | Main template with both EN/CN | Bilingual |
| `README_CN-multilingual.md` | Chinese version template | Chinese |
| `GUIDE.md` | Detailed implementation guide | English |

### File Structure

```
multilingual/
├── README-multilingual.md      # Main bilingual template
├── README_CN-multilingual.md   # Chinese template
└── GUIDE.md                    # Implementation guide
```

## 🚀 Quick Start

### 1. Copy Templates

```bash
# Navigate to templates directory
cd githubskill/readme-templates/multilingual

# Copy both templates to your project
cp README-multilingual.md /your-project/README.md
cp README_CN-multilingual.md /your-project/README_CN.md
```

### 2. Customize Templates

Edit both files and replace placeholders:

**For README.md:**
| Placeholder | Replace With |
|-------------|--------------|
| `# Project Name` | Your project title (English) |
| `## One-line description` | Brief project description (English) |
| `## 🎯 Overview` | Project overview (English) |

**For README_CN.md:**
| Placeholder | Replace With |
|-------------|--------------|
| `# 项目名称` | Your project title (Chinese) |
| `## 一句话描述` | Brief project description (Chinese) |
| `## 🎯 概述` | Project overview (Chinese) |

### 3. Link Between Versions

Add a link to the other language version in both files:

**In README.md:**
```markdown
## 🌐 Languages

- [中文文档](./README_CN.md)
```

**In README_CN.md:**
```markdown
## 🌐 语言

- [English](./README.md)
```

## 📝 Complete Template

### README-multilingual.md

```markdown
# PROJECT NAME

[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-1.0.0-blue.svg)](CHANGELOG.md)
[![Status](https://img.shields.io/badge/Status-Active-green.svg)]()

Brief one-line description of your project in English. Explain what it does in 1-2 sentences.

## 🎯 Overview

Comprehensive project description in English. Explain the project's purpose, goals, and key features. This section should help users understand if this project meets their needs.

### ✨ Features

- Feature 1: Description
- Feature 2: Description
- Feature 3: Description
- Feature 4: Description

## 🚀 Installation

### Prerequisites

- Requirement 1 (e.g., Node.js 14+)
- Requirement 2 (e.g., Python 3.8+)
- Requirement 3 (if applicable)

### Steps

```bash
# Clone the repository
git clone https://github.com/yourusername/project-name.git

# Navigate to project directory
cd project-name

# Install dependencies
npm install
```

## 🎮 Usage

### Basic Example

```javascript
// Example code in English
const project = require('project-name');

project.initialize({
  option1: 'value1',
  option2: 'value2'
});
```

### Advanced Usage

```bash
# Advanced command example
project-name --advanced --option value
```

## 🌐 Languages

- [中文文档](./README_CN.md) - Chinese version available

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

- 📧 Email: contact@project.com
- 💬 Discussion: [GitHub Discussions](https://github.com/username/project-name/discussions)
- 🐛 Issues: [GitHub Issues](https://github.com/username/project-name/issues)

---

Built with ❤️ by [Your Name/Organization]
```

### README_CN-multilingual.md

```markdown
# 项目名称

[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-1.0.0-blue.svg)](CHANGELOG.md)
[![Status](https://img.shields.io/badge/Status-Active-green.svg)]()

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

- [English](./README.md) - English version available

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

## 📋 Implementation Checklist

### Before Publishing

- [ ] Project name translated in both languages
- [ ] Description translated accurately
- [ ] All features listed in both versions
- [ ] Installation steps verified
- [ ] Code examples working
- [ ] Cross-links between versions working
- [ ] License file included
- [ ] Contact information updated

### Best Practices

1. **Consistent Structure**
   - Keep same sections in both versions
   - Use similar headings and hierarchy
   - Maintain parallel formatting

2. **Accurate Translation**
   - Use natural language in both versions
   - Avoid machine translation
   - Keep technical terms consistent

3. **Visual Consistency**
   - Same badges and icons
   - Similar code block formatting
   - Matching section lengths

4. **Regular Updates**
   - Update both versions together
   - Keep translations in sync
   - Test links regularly

## 🎯 Use Cases

### Open Source Projects

Reach global developers:
- Chinese developers find project via Chinese README
- English speakers use English version
- Both versions link to each other

### Commercial Products

International market presence:
- Show commitment to Chinese market
- Professional bilingual documentation
- Better user experience

### Personal Projects

Showcase to global audience:
- Demonstrate internationalization skills
- Attract contributors from all countries
- Build diverse community

## 🔧 Customization Tips

### Adding More Languages

```markdown
## 🌐 Languages

- [English](./README.md)
- [中文](./README_CN.md)
- [Español](./README_ES.md)  # Add more languages
```

### Regional Variants

For different regions:
- `README_CN.md` - Simplified Chinese
- `README_TW.md` - Traditional Chinese
- `README_HK.md` - Hong Kong version

### Platform-Specific

Add platform notes:
```markdown
## 📱 Platforms

- [English](./README.md) - Global platforms
- [中文](./README_CN.md) - 中国平台
```

## 📈 Benefits of Bilingual README

### SEO Advantages

- Appears in both English and Chinese search results
- Higher ranking on Chinese search engines
- Better discoverability globally

### User Experience

- Native language documentation
- Lower barrier to entry
- Better understanding of features

### Community Building

- Attracts diverse contributors
- Shows international awareness
- Builds trust with global users

## 🚀 Advanced Examples

### With Version Badges

```markdown
# PROJECT NAME / 项目名称

![Version](https://img.shields.io/badge/Version-1.0.0-blue)
![状态](https://img.shields.io/badge/状态-活跃-green)
```

### With Download Stats

```markdown
![Downloads](https://img.shields.io/badge/Downloads-1K-blue)
![下载量](https://img.shields.io/badge/下载量-1K-blue)
```

### With Social Links

```markdown
**English:** [Twitter](link) | [WeChat](link)
**中文:** [微博](link) | [微信](link)
```

## 📚 Resources

### Translation Tools

- [DeepL](https://www.deepl.com/) - AI translation
- [Google Translate](https://translate.google.com/) - Free translation
- [Chinese Translation Services](https://www.g Cloud.google.com/translate/) - Google Cloud

### Localization Guides

- [GitHub Localization](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/about-readmes)
- [Open Source Localization](https://www.transifex.com/resource-type/open-source/)

### Related Templates

- See `../README.md` for single-language template
- See `../README-cli.md` for CLI-specific template
- See `../README-webapp.md` for web app template

## 🤝 Contributing

To improve these templates:
1. Fork the repository
2. Create feature branch
3. Add or improve templates
4. Submit pull request
5. Document changes

## 📝 License

These templates are available under MIT License. See [LICENSE](../../LICENSE) for details.

## 📞 Support

- **Issues:** Report template problems
- **Discussions:** Suggest improvements
- **Wiki:** Add your examples

---

**Template Version:** 2.0.0  
**Last Updated:** January 2024  
**Created by:** skyconnfig
