---
name: frontend-design-system
description: 前端UI设计最佳实践 - 8pt Grid、设计系统变量、排版层级、响应式设计
version: 1.0.0
author: Claude Code
source: user-created
tags:
  - frontend
  - ui-design
  - tailwind
  - design-system
  - react
---

# 前端UI设计最佳实践 Skill

## 概述

本skill提供高端SaaS网页应用的前端设计最佳实践，基于8pt Grid布局系统、设计系统变量和响应式设计原则。

## 核心设计规范

### 1. 8pt Grid 布局系统

**原则：** 所有间距（padding、margin、gap）使用8的倍数

**间距尺度：**
- 4, 8, 12, 16, 24, 32, 40, 48 (单位: px)

**应用规则：**
```
容器padding: 16px或24px
元素间距: 8px或12px
卡片间距: 16px或24px
Section间距: 32px或48px
```

### 2. 设计系统变量

**配色方案：**
- 主色（Primary）：统一品牌色
- 辅助色（Secondary）：与主色协调
- 中性色（Neutral）：灰度层级（50-900）
- 避免过多彩虹色调

**圆角（Border Radius）：**
- 统一使用：`10px`（可调整：4-12px范围）
- 小型元素：4-6px
- 卡片/按钮：8-10px
- 大型容器：12px

**阴影（Shadows）：**
- 简洁2层阴影系统：
  - `shadow-sm`: 轻微提升
  - `shadow-md`: 标准阴影
  - `shadow-lg`: 悬停效果

**避免：** 过多阴影层次（≤3层）

### 3. 排版层级和行高

**字号阶梯：**
- H1: `32px` (1.4行高)
- H2: `24px` (1.4行高)
- H3: `20px` (1.4行高)
- 正文: `16px` (1.6行高)
- 辅助文本: `14px` (1.6行高)
- 小字: `12px` (1.5行高)

**字体权重：**
- 标题: `font-semibold` 或 `font-bold`
- 正文: `font-normal`
- 强调: `font-medium`

### 4. 卡片设计规范

**卡片结构：**
```
┌─────────────────────┐
│  [主标题]           │  ← H3/H4, 1个
│  [辅助信息1]        │  ← 14px, 1行
│  [辅助信息2]        │  ← 12px, 1行
└─────────────────────┘
```

**卡片样式：**
- 背景: `bg-white` 或 `bg-gray-50`
- Padding: `p-4` (16px)
- 圆角: `rounded-lg` (10px)
- 阴影: `shadow-md`
- 悬停: `hover:shadow-lg transition-shadow`

### 5. 响应式设计

**断点系统（Tailwind）：**
```
sm: 640px   (移动端)
md: 768px   (平板)
lg: 1024px  (桌面)
xl: 1280px  (大屏)
2xl: 1536px (超大屏)
```

**响应式策略：**
- 字体: 移动端-1级，桌面端标准级
- 间距: 移动端紧凑，桌面端舒适
- 布局: 单列→多列渐变
- Card数量: 移动端1列→平板2列→桌面3-4列

### 6. 设计系统实现（shadcn/ui + Tailwind）

**Tailwind配置：**
```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#f0f9ff',
          100: '#e0f2fe',
          500: '#0ea5e9', // 主色
          600: '#0284c7',
          900: '#0c4a6e',
        },
        neutral: {
          50: '#fafafa',
          100: '#f5f5f5',
          200: '#e5e5e5',
          300: '#d4d4d4',
          400: '#a3a3a3',
          500: '#737373',
          600: '#525252',
          700: '#404040',
          800: '#262626',
          900: '#171717',
        },
      },
      borderRadius: {
        'sm': '4px',
        'md': '6px',
        'lg': '10px',
        'xl': '12px',
      },
      boxShadow: {
        'sm': '0 1px 2px 0 rgba(0, 0, 0, 0.05)',
        'md': '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1)',
        'lg': '0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1)',
      },
      fontSize: {
        'h1': ['32px', { lineHeight: '1.4', fontWeight: '600' }],
        'h2': ['24px', { lineHeight: '1.4', fontWeight: '600' }],
        'h3': ['20px', { lineHeight: '1.4', fontWeight: '600' }],
        'body': ['16px', { lineHeight: '1.6' }],
        'sm': ['14px', { lineHeight: '1.6' }],
        'xs': ['12px', { lineHeight: '1.5' }],
      },
      spacing: {
        '18': '4.5rem',
        '22': '5.5rem',
      },
    },
  },
}
```

## 组件示例

### Card 组件（React + Tailwind）

```jsx
import React from 'react';

const Card = ({ title, mainInfo, subInfo, className = '', onClick }) => {
  return (
    <div
      className={`
        bg-white
        p-4
        rounded-lg
        shadow-md
        hover:shadow-lg
        transition-shadow
        duration-200
        cursor-pointer
        ${className}
      `}
      onClick={onClick}
    >
      <h3 className="text-h3 font-semibold text-gray-900 mb-2">
        {title}
      </h3>
      <p className="text-sm text-gray-600 mb-1">
        {mainInfo}
      </p>
      <p className="text-xs text-gray-400">
        {subInfo}
      </p>
    </div>
  );
};

export default Card;
```

### 响应式 Grid 布局

```jsx
const GridContainer = ({ children }) => {
  return (
    <div className="
      grid
      grid-cols-1
      sm:grid-cols-2
      md:grid-cols-3
      lg:grid-cols-4
      gap-4
      p-4
      md:p-6
      lg:p-8
    ">
      {children}
    </div>
  );
};
```

### 页面布局模板

```jsx
const PageLayout = ({ title, children }) => {
  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow-sm border-b border-gray-200">
        <div className="
          mx-auto
          max-w-7xl
          px-4
          sm:px-6
          lg:px-8
          py-4
        ">
          <h1 className="text-h1 text-gray-900">{title}</h1>
        </div>
      </header>

      {/* Main Content */}
      <main className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-8">
        {children}
      </main>

      {/* Footer */}
      <footer className="bg-white border-t border-gray-200 mt-auto">
        <div className="mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8">
          <p className="text-xs text-gray-500 text-center">
            © 2024 Your Company
          </p>
        </div>
      </footer>
    </div>
  );
};
```

## 使用指南

### 何时使用此skill？

当您需要：
- ✅ 创建新的SaaS网页应用
- ✅ 重构现有前端项目以提升设计一致性
- ✅ 建立统一的设计系统
- ✅ 实现响应式布局
- ✅ 生成符合高端设计标准的UI组件

### 输入要求

用户应提供：
1. **项目类型**（SaaS仪表板、电商、落地页等）
2. **技术栈**（React/Vue/Angular + Tailwind/其他CSS方案）
3. **设计需求**（品牌色、主要功能模块）
4. **响应式要求**（需要支持的设备范围）

### 输出内容

此skill将提供：
1. 完整的设计token配置（Tailwind配置）
2. 可复用的React/Vue组件
3. 页面布局模板
4. 最佳实践检查清单
5. 常见错误的避免建议

## 最佳实践检查清单

### ✅ 必须遵循
- [ ] 所有间距使用8的倍数
- [ ] 使用设计系统变量而非硬编码值
- [ ] 统一圆角（通常10px）
- [ ] 限制阴影层次（≤3层）
- [ ] 标题行高1.4，正文行高1.6
- [ ] Card包含主标题+2个辅助信息

### ✅ 强烈推荐
- [ ] 使用Tailwind CSS
- [ ] 配置shadcn/ui风格的设计token
- [ ] 实现响应式断点
- [ ] 添加hover/focus微交互
- [ ] 保持配色方案简洁（主色+辅助色+中性色）

### ❌ 应避免的常见错误
- [ ] 混用不同间距尺度（如4px和6px并存）
- [ ] 使用过多颜色（>5种非中性色）
- [ ] 圆角不一致（按钮4px，卡片12px）
- [ ] 忽略移动端体验
- [ ] 卡片信息过载（>3行）
- [ ] 未使用CSS变量，导致主题切换困难

## 高级技巧

### 1. 微动效增强
```jsx
// 平滑过渡
className="transition-all duration-200 ease-in-out"

// 悬停效果组合
className="hover:scale-105 hover:shadow-lg transition-transform transition-shadow"
```

### 2. 主题切换支持
```javascript
// tailwind.config.js 使用CSS变量
colors: {
  primary: {
    500: 'var(--color-primary-500)',
  },
}
```

### 3. CSS Variables 实现主题
```css
/* 浅色主题（默认） */
:root {
  --bg-primary: #ffffff;
  --bg-secondary: #fafafa;
  --text-primary: #171717;
  --text-secondary: #525252;
  --border-color: #e5e5e5;
}

/* 深色主题 */
[data-theme="dark"] {
  --bg-primary: #171717;
  --bg-secondary: #262626;
  --text-primary: #fafafa;
  --text-secondary: #d4d4d4;
  --border-color: #404040;
}

body {
  background: var(--bg-primary);
  color: var(--text-primary);
}

.card {
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
}
```

### 3. 性能优化
- 使用`@apply`提取重复样式
- 避免深层嵌套选择器
- 利用Tailwind的JIT模式减少CSS体积

### 4. 无障碍访问
- 确保颜色对比度≥4.5:1
- 提供焦点可见性（`focus:ring`）
- 语义化HTML结构
- ARIA标签支持

## 相关资源

- [Tailwind CSS文档](https://tailwindcss.com/docs)
- [shadcn/ui组件库](https://ui.shadcn.com/)
- [8pt Grid系统](https://8ptgrid.com/)
- [WCAG无障碍指南](https://www.w3.org/WAI/WCAG21/quickref/)

## Skill使用示例

### 用户请求
"创建一个SaaS仪表板，使用React + Tailwind，主色调蓝色，需要数据卡片和图表区域"

### Skill响应
1. 提供tailwind.config.js配置
2. 给出Card组件实现
3. 提供Dashboard布局模板
4. 列出响应式设计建议
5. 提供配色方案参考

## 生产环境部署

### 资源本地化策略

**❌ 避免使用CDN（生产环境）：**
```html
<!-- 错误：依赖外部CDN -->
<script src="https://cdn.tailwindcss.com"></script>
```

**✅ 推荐：本地化CSS文件**
```html
<!-- 正确：零外部依赖 -->
<link rel="stylesheet" href="assets/css/styles.css">
```

### 纯CSS实现方案（无需Tailwind构建）

如果不想使用Tailwind CDN或构建流程，可以使用**原生CSS + CSS变量**：

```css
/* assets/css/styles.css */
:root {
  /* Design Tokens */
  --color-primary-500: #0ea5e9;
  --color-neutral-900: #171717;
  --radius-lg: 10px;
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  --spacing-4: 1rem;    /* 16px */
  --spacing-6: 1.5rem;  /* 24px */
}

/* Base Styles */
* { box-sizing: border-box; }
body {
  font-family: system-ui, -apple-system, sans-serif;
  font-size: 16px;
  line-height: 1.6;
  color: var(--color-neutral-900);
  background: var(--color-neutral-50);
}

/* Typography */
.text-h1 { font-size: 2rem; line-height: 1.4; font-weight: 600; }
.text-h2 { font-size: 1.5rem; line-height: 1.4; font-weight: 600; }
.text-h3 { font-size: 1.25rem; line-height: 1.4; font-weight: 600; }

/* Components */
.card {
  background: white;
  padding: var(--spacing-4);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-md);
  transition: box-shadow 0.2s ease;
}
.card:hover { box-shadow: var(--shadow-lg); }
```

**优势：**
- ✅ 零构建步骤
- ✅ 完全离线可用
- ✅ 无外部依赖
- ✅ 易于理解和修改
- ✅ 适合小型项目

### 响应式设计（纯CSS）

```css
/* Mobile First → Desktop */
.container {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 var(--spacing-4);
}

@media (min-width: 640px) {
  .container { padding: 0 var(--spacing-6); }
  .grid-2 { grid-template-columns: repeat(2, 1fr); }
}

@media (min-width: 1024px) {
  .container { padding: 0 var(--spacing-8); }
  .grid-3 { grid-template-columns: repeat(3, 1fr); }
}
```

### HTML结构示例（完整博客页面）

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>个人博客</title>
  <link rel="stylesheet" href="assets/css/styles.css">
</head>
<body>
  <!-- Navigation -->
  <nav class="sticky top-0 bg-white shadow-sm z-50">
    <div class="container">
      <!-- Navigation content -->
    </div>
  </nav>

  <!-- Hero Section -->
  <header class="bg-gradient-to-br from-primary-400 to-primary-800 text-white py-24">
    <div class="container text-center">
      <h1 class="text-h1 mb-6">文章标题</h1>
      <p class="text-body mb-8">文章摘要...</p>
    </div>
  </header>

  <!-- Articles Grid -->
  <section class="py-16">
    <div class="container">
      <h2 class="text-h2 text-center mb-12">最新文章</h2>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        <!-- Article Cards -->
        <article class="card p-6 flex flex-col h-full">
          <span class="badge mb-4">分类</span>
          <h3 class="text-h3 mb-3 flex-grow">文章标题</h3>
          <p class="text-sm text-neutral-600 mb-4 line-clamp-3">摘要...</p>
          <div class="meta border-t pt-4 mt-auto">
            <time>2026-04-01</time>
            <span>👁 128</span>
          </div>
        </article>
      </div>
    </div>
  </section>
</body>
</html>
```

### 图标策略

**✅ 推荐：内联 SVG**
```html
<!-- 直接嵌入SVG，无需字体文件 -->
<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
        d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
</svg>
```

**❌ 避免：图标字体**
- Font Awesome CDN
- IconFont字体文件
- 会增加额外的HTTP请求和字体加载延迟

### 图片优化

```html
<!-- 1. 使用WebP格式（现代浏览器） -->
<img src="image.webp" alt="描述" class="w-full h-auto rounded-lg" loading="lazy">

<!-- 2. 提供JPEG兜底 -->
<picture>
  <source srcset="image.webp" type="image/webp">
  <img src="image.jpg" alt="描述" loading="lazy">
</picture>

<!-- 3. 响应式图片 -->
<img src="small.jpg"
     srcset="small.jpg 640w, medium.jpg 1024w, large.jpg 1920w"
     sizes="(max-width: 640px) 100vw, (max-width: 1024px) 50vw, 33vw"
     alt="描述">
```

### 字体优化（如需自定义字体）

```css
/* 使用本地字体文件，避免Google Fonts CDN */
@font-face {
  font-family: 'Inter';
  src: url('../fonts/inter-regular.woff2') format('woff2');
  font-weight: 400;
  font-display: swap;  /* 避免阻塞渲染 */
}

body {
  font-family: 'Inter', system-ui, sans-serif;
}
```

### 性能优化清单

- [ ] CSS文件内联或压缩（< 14KB）
- [ ] 图片压缩和懒加载
- [ ] SVG图标内联（< 10个图标时）
- [ ] 移除未使用的CSS规则
- [ ] 启用Gzip/Brotli压缩
- [ ] 设置合适的Cache-Control头
- [ ] 使用`loading="lazy"`延迟非关键图片
- [ ] 关键CSS内联到`<head>`

### 浏览器兼容性

| 浏览器 | 支持版本 |
|--------|---------|
| Chrome | ✅ 最新2版 |
| Firefox | ✅ 最新2版 |
| Safari | ✅ 最新2版 |
| Edge | ✅ 最新2版 |
| IE11 | ❌ 不支持（如需支持需加前缀） |

## 快速开始模板

### 项目结构
```
my-blog/
├── index.html              # 主页面
├── assets/
│   ├── css/
│   │   └── styles.css      # 主样式文件
│   └── fonts/              # (可选) 自定义字体
├── images/                 # 图片资源
│   ├── avatar.webp
│   └── post-thumbnails/
└── README.md
```

### 5分钟快速搭建

1. **复制CSS文件**
   - 将上面的 `tailwind.css` 或 `styles.css` 放入 `assets/css/`

2. **创建HTML文件**
   - 使用 `index-local.html` 作为模板

3. **自定义内容**
   - 修改 `:root` 中的颜色变量
   - 替换文章卡片内容
   - 更新个人信息

4. **测试**
   ```bash
   python -m http.server 8000
   # 访问 http://localhost:8000
   ```

5. **部署**
   - 上传所有文件到服务器
   - 确保 `assets/css/styles.css` 路径正确

## 常见问题

### Q: Tailwind CDN vs 本地CSS？
**A:** CDN适合开发/演示，本地CSS适合生产。本地CSS加载更快、无外部依赖、可离线运行。

### Q: 如何处理大量图标？
**A:** 5个以下用内联SVG；5-50个用SVG Sprite（`<defs><symbol>`）；50个以上考虑图标字体或图标组件库。

### Q: 如何添加暗黑模式？
**A:** 使用CSS变量：
```css
:root { --bg-primary: #fff; --text-primary: #000; }
[data-theme="dark"] { --bg-primary: #000; --text-primary: #fff; }
body { background: var(--bg-primary); color: var(--text-primary); }
```

### Q: 是否需要JavaScript框架？
**A:** 个人博客不需要。纯HTML+CSS足够；如需动态功能，原生JS或Alpine.js即可。

## 版本历史

- **1.0.0** (2026-04-01): 初始版本，基于用户提供的设计最佳实践
- **1.1.0** (2026-04-01): 添加纯CSS实现方案、资源本地化指南、生产部署建议

---

**提示：** 使用此skill时，结合具体项目需求调整设计token值，保持设计系统的一致性和可维护性。对于生产环境，务必使用本地化资源而非CDN。
