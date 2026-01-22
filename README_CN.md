# 技能仓库 (Skill Repository)

这是一个为AI助手提供专业能力的综合技能集合，涵盖开发、设计、文档和自动化等各种任务。

## 🎯 概述

技能仓库由多个专业技能目录组成，每个技能都设计用于处理特定类型的任务。这些技能在不同领域增强了AI助手的能力。

## 📦 可用技能

### 开发与工程
- **algorithmic-art** - 使用p5.js创建算法艺术，具有随机种子和交互式参数探索功能
- **canvas-design** - 使用设计理念创建美观的PNG和PDF文档视觉艺术
- **command-development** - 创建Claude Code斜杠命令的指南
- **coding** - 通用编码和开发能力
- **frontend-design** - 创建独特的生产级前端界面
- **githubskill** - 全面的GitHub仓库管理和git操作
- **mcp-builder** - 创建高质量MCP（模型上下文协议）服务器的指南
- **mcp-integration** - 将MCP服务器集成到Claude Code插件中
- **skill-creator** - 创建扩展AI能力的有效技能指南
- **webapp-testing** - 使用Playwright与本地Web应用程序交互和测试的工具包

### 文档与写作
- **doc-coauthoring** - 协同撰写文档的结构化工作流程
- **docs-write** - 按照Metabase的对话风格编写文档
- **docx** - 创建和编辑.docx文件的综合工具
- **internal-comms** - 编写内部沟通的资源
- **link-explainer** - 将复杂的网络文章转换为简单、动画的HTML解释
- **pdf** - 综合PDF操作工具包
- **pptx** - 演示文稿的创建、编辑和分析
- **xlsx** - 电子表格的创建、编辑和分析综合工具

### 设计与创意
- **brand-guidelines** - 应用Anthropic官方品牌色彩和排版
- **brainstorming** - 在实施前探索用户意图、需求和设计
- **planning-with-files** - 基于文件的规划和文档系统
- **slack-gif-creator** - 创建针对Slack优化的动画GIF
- **theme-factory** - 使用预设主题为工件设置样式的工具包
- **ui-ux-pro-max** - 跨多个平台的专业UI/UX

### AI与自动化
- **notebooklm-py** - 非官方Google NotebookLM Python API
- **paper-to-webpage** - 将学术论文转换为Web内容
- **playwright** - 通过Playwright MCP实现浏览器自动化
- **prompt-lookup** - 发现、检索和改进AI提示词
- **skill-lookup** - 查找和安装可复用的AI能力
- **superpowers** - 编码代理的完整软件开发工作流程

## 🚀 安装

### Claude Code用户

1. 克隆此仓库：
```bash
git clone https://github.com/skyconnfig/skill.git
```

2. 技能已准备好与Claude Code一起使用。只需在需要时引用技能名称即可。

### 💡 快速提示

**直接克隆：**
即使不点Star，也可以在终端直接克隆仓库：
```bash
git clone https://github.com/skyconnfig/skill.git
```
如果仓库是公开的（Public），通常可以直接下载。

**查看 Releases：**
点击页面右侧的 **Releases** 栏目，看看是否有已经打包好的压缩包供下载。

**顺手点个 Star ⭐️：**
如果这个项目对你有帮助，点击 Star 也是对开发者的一种鼓励！点完后，刷新页面看看 README 里的内容是否发生了变化（通常是通过 JS 动态加载的）。

### 其他AI助手

技能可以适应其他支持基于技能的架构的AI助手。每个技能包含：
- `SKILL.md` - 技能定义和使用说明
- 所需文件和依赖项
- 使用示例和文档

## 📖 使用方法

每个技能目录都包含自己的`SKILL.md`文档。通用使用模式：

### 在Claude Code中使用技能

```markdown
/use skill-name [参数]
```

### 按任务类型分类的技能

**视觉与设计任务：**
- canvas-design, frontend-design, theme-factory, ui-ux-pro-max, brand-guidelines

**文档与内容：**
- docx, pdf, pptx, xlsx, docs-write, internal-comms

**开发与工程：**
- githubskill, command-development, mcp-builder, webapp-testing, playwright

**AI与自动化：**
- notebooklm-py, skill-creator, skill-lookup, prompt-lookup

**创意与沟通：**
- algorithmic-art, slack-gif-creator, link-explainer, brainstorming

## 📁 目录结构

```
skill/
├── algorithmic-art/          # 算法艺术创作
├── brainstorming/            # 创意规划和构思
├── brand-guidelines/         # 品牌样式工具包
├── canvas-design/            # 视觉艺术创作
├── coding/                   # 开发能力
├── command-development/      # 斜杠命令创建
├── doc-coauthoring/          # 文档协同撰写
├── docs-write/               # 文档编写
├── docx/                     # Word文档处理
├── frontend-design/          # 前端界面设计
├── githubskill/              # GitHub操作
├── internal-comms/           # 内部沟通
├── link-explainer/           # 网络文章解释
├── mcp-builder/              # MCP服务器开发
├── mcp-integration/          # MCP集成指南
├── notebooklm-py/            # NotebookLM自动化
├── paper-to-webpage/         # 论文转换
├── pdf/                      # PDF操作
├── planning-with-files/      # 基于文件的规划
├── playwright/               # 浏览器自动化
├── pptx/                     # PowerPoint处理
├── prompt-lookup/            # 提示词发现
├── skill-creator/            # 技能开发指南
├── skill-lookup/             # 技能管理
├── slack-gif-creator/        # GIF创建
├── superpowers/              # 代理开发框架
├── theme-factory/            # 主题工具包
├── ui-ux-pro-max/            # UI/UX设计系统
├── webapp-testing/           # Web应用程序测试
├── web-artifacts-builder/    # Web工件开发
└── xlsx/                     # 电子表格处理
```

## 🤝 贡献

### 添加新技能

1. 创建具有描述性名称的新目录
2. 添加包含以下内容的`SKILL.md`：
   - 技能描述
   - 使用示例
   - 参数和选项
   - 依赖项
3. 使用各种输入测试技能
4. 提交拉取请求

### 修改现有技能

1. 更新相应的`SKILL.md`文件
2. 在本地测试更改
3. 确保与其他技能的兼容性
4. 记录重大更改

## 📝 许可证

每个技能可能有自己的许可证。请检查各个技能目录的许可证信息。

## 📞 支持

- **问题**：通过GitHub Issues报告问题
- **文档**：请参阅各个`SKILL.md`文件
- **更新**：关注仓库以获取新技能和改进

## 🔗 链接

- [GitHub仓库](https://github.com/skyconnfig/skill)
- [技能文档](./)
- [贡献指南](#贡献)

---

用❤️为AI助手和开发者构建
