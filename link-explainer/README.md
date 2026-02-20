# 🌸 Link Explainer Pink Skill

![Version](https://img.shields.io/badge/version-2.0.0-blue)
![Author](https://img.shields.io/badge/author-Sisyphus-green)
![Theme](https://img.shields.io/badge/theme-pink-pink)

将技术文档转换为**淡粉色主题**的动画 HTML 页面，使用简单易懂的语言解释专业术语。生成适合初学者的可视化学习材料。

## ✨ 特性

### 视觉设计
- **淡粉色渐变背景**：从 `#fff5f8` 到 `#ffe4ec` 再到 `#ffd6e4`
- **卡片弹性入场动画**：使用 cubic-bezier 曲线实现自然的弹跳效果
- **闪光扫过效果**：卡片上有彩虹光效果扫过
- **标题渐变色**：粉色系渐变配合脉冲动画
- **下划线展开动画**：标题下的线条逐渐延伸
- **专业术语简单解释**：使用比喻和小贴士让复杂概念变得易懂

### 动画效果 (17种动画)
1. `cardEntrance` - 卡片弹性缩放入场 (0.8s)
2. `shimmer` - 闪光扫过效果 (3s循环)
3. `titlePulse` - 标题脉冲效果 (3s循环)
4. `underlineExpand` - 下划线展开动画
5. `sparkle` - 图标闪烁 (2s循环)
6. `stepSlideIn` - 步骤滑入效果
7. `numberBounce` - 数字弹跳 (1s循环)
8. `flowerSway` - 花朵摇摆 (2s循环)
9. `featureFloat` - 功能卡片浮动 (3s循环)
10. `methodPulse` - 安装方法脉冲 (3s循环)
11. `progressStripes` - 进度条条纹移动
12. `progressShine` - 进度条闪光扫过
13. `commandGlow` - 命令框发光 (2s循环)
14. `badgeShine` - 徽章闪光 (2s循环)
15. `codeBlockPulse` - 代码块脉冲 (3s循环)
16. `tipSlide` - 提示框滑入
17. `emojiBounce` - emoji 弹跳

## 🚀 快速开始

### 基本用法

```bash
# 1. 获取网页内容
python scripts/fetch_content.py "https://example.com/article" > content.json

# 2. 简化内容（解释专业术语）
python scripts/simplify_content.py content.json > simplified.json

# 3. 生成动画 HTML
python scripts/generate_html.py simplified.json
```

### 输出
生成的文件：`explanation.html`

## 📁 文件结构

```
link-explainer/
├── skill.json           # 技能配置
├── README.md           # 本文档
├── scripts/
│   ├── fetch_content.py      # 获取网页内容
│   ├── simplify_content.py   # 简化内容、解释术语
│   └── generate_html.py      # 生成动画 HTML
└── assets/
    ├── template.html         # HTML 模板
    └── styles.css            # 样式文件
```

## 🎨 配色方案

```css
--primary: #ff6b9d        /* 主色调 - 粉色 */
--secondary: #ff8fab      /* 次要色 - 浅粉色 */
--accent: #ffb3c6         /* 强调色 - 淡粉色 */
--background-start: #fff5f8 /* 背景起始色 */
--background-middle: #ffe4ec /* 背景中间色 */
--background-end: #ffd6e4   /* 背景结束色 */
--text-primary: #5a4a5a     /* 主文本色 */
--text-secondary: #7a6a7a   /* 次文本色 */
```

## 📖 使用示例

### 完整流程

```bash
# Step 1: 获取 OpenCode 文档
python scripts/fetch_content.py "https://opencode.ai/docs" > content.json

# Step 2: 简化内容
python scripts/simplify_content.py content.json > simplified.json

# Step 3: 生成 HTML
python scripts/generate_html.py simplified.json

# Step 4: 查看结果
open explanation.html
```

### 自定义标题

```bash
python scripts/fetch_content.py "https://opencode.ai/docs" | \
  python scripts/simplify_content.py --title "我的自定义标题" | \
  python scripts/generate_html.py
```

## 🎯 最佳实践

### 1. 专业术语解释
技能会自动识别并解释以下类型的术语：

- **技术概念**：API、数据库、算法、云服务等
- **编程术语**：变量、函数、递归、异步等
- **工具名称**：Git、Docker、React、Node 等
- **架构概念**：前端、后端、服务器、缓存等

### 2. 比喻说明
每个专业术语都会配有通俗易懂的比喻，例如：

```
API (应用程序接口)
├── 解释：不同程序之间交流的方式
└── 比喻：像餐厅的服务员 - 你告诉服务员要什么，他去厨房拿给你
```

### 3. 步骤分解
如果内容包含步骤说明，会自动转换为步骤卡片格式：

```
步骤 1: 执行连接命令
步骤 2: 访问认证页面
步骤 3: 获取 API 密钥
步骤 4: 粘贴密钥
```

## 🔧 自定义配置

### 修改颜色主题

编辑 `assets/styles.css` 中的颜色变量：

```css
:root {
  --primary: #your-color;
  --secondary: #your-color;
  /* ... */
}
```

### 添加新的专业术语

编辑 `scripts/simplify_content.py` 中的 `JARGON_DICT`：

```python
JARGON_DICT = {
  "your_term": {
    "explanation": "Your explanation",
    "analogy": "Your analogy"
  }
}
```

## 📱 响应式设计

页面会自动适应不同屏幕尺寸：
- **桌面端**：多列布局，完整动画
- **平板端**：自适应列数
- **移动端**：单列布局，简化动画

## 🎬 动画禁用

对于 prefers-reduced-motion 用户，部分动画会被禁用：

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

## 📦 依赖

- Python 3.7+
- requests
- beautifulsoup4

安装依赖：
```bash
pip install requests beautifulsoup4
```

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

---

**Made with 💖 by Sisyphus**
