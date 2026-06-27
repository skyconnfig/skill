---
name: agnes-image-gen
description: 批量图片生成技能。用户传入主题关键词或提示词列表后，自动调用 Agnes Image 2.1 Flash API 批量生成图片并保存到本地，然后生成一个美观的 HTML 展示页面。从环境变量 AGNES_API_KEY 读取 API 密钥。
---

# Agnes Image 批量生成

## 触发条件

当用户提到以下任一需求时触发：
- 批量生成图片
- 根据关键词/提示词生成多张图片
- 使用 Agnes AI 生图
- 图片生成 + HTML 展示

## 工作流程

### 1. 准备

检查环境变量 $env:AGNES_API_KEY 是否存在。如果不存在，提示用户提供 API Key。

### 2. 解析输入

从用户的输入中提取：
- **主题关键词或提示词列表**：用户可以传入一个关键词（会扩展成多个变体），也可以传入多个关键词/提示词，用逗号分隔
- **图片数量**：每个提示词生成的图片数量（默认每张提示词生成 1 张）
- **图片尺寸**：默认 1024x1024，可选 1024x768 或 768x1024
- **输出风格偏好**：如写实、卡通、动漫、水彩等（用于增强提示词）

### 3. 执行生图

使用内置脚本 scripts/agnes_generator.py 执行批量生图：

```bash
python scripts/agnes_generator.py "关键词1,关键词2" [尺寸] [每词生成数] [风格]
```

示例：
```bash
python scripts/agnes_generator.py "猫咪,风景,城市" 1024x1024 2
python scripts/agnes_generator.py "赛博朋克,中国风" 1024x768 1
```

脚本会自动完成以下步骤：

#### 3.1 构造提示词

对于每个主题关键词，将其中文关键词翻译为适合 AI 生图的英文 prompt。

提示词结构：[主体描述] + [场景/背景] + [光照] + [构图] + [质量要求]

内置翻译映射表覆盖以下类别：猫咪、狗狗、风景、城市、人物、动物、花卉、美食、科技、动漫、水彩、抽象、建筑、星空、海洋、森林、太空、赛博朋克、中国风、机械。

如果关键词不在映射表中，使用通用模板：{keyword}, ultra detailed, high quality, professional composition。

#### 3.2 调用 API

调用 Agnes Image 2.1 Flash API：

```
POST https://apihub.agnes-ai.com/v1/images/generations
Authorization: Bearer YOUR_API_KEY
Content-Type: application/json
```

请求体：
```json
{
  "model": "agnes-image-2.1-flash",
  "prompt": "英文提示词",
  "size": "1024x1024",
  "extra_body": {
    "response_format": "url"
  }
}
```

每个请求最多重试 3 次，间隔递增。

#### 3.3 下载图片

获取图片 URL 后，下载图片二进制内容保存到本地：

输出目录结构：
```
<输出目录>/
  YYYYMMDD_HHMMSS/
    猫咪_001.jpg
    猫咪_002.jpg
    风景_001.jpg
    agnes_gallery.html
```

文件名格式：{关键词}_{序号}.jpg，序号从 001 开始。特殊字符替换为下划线。

#### 3.4 生成 HTML 展示

在所有图片下载完成后，自动生成一个深色主题的 HTML 展示页面：

- 响应式 CSS Grid 布局
- 每张图片下方标注对应的英文提示词
- 点击图片可全屏查看（模态框）
- 显示生成时间和总数统计
- 保存为 agnes_gallery.html 在输出目录中

### 4. 输出结果

向用户报告：
- 成功生成的图片数量和文件路径
- HTML 展示页面的位置
- 任何失败的请求及原因

## 注意事项

- API 调用可能需要较长时间（60s~360s），请耐心等待
- 如果某个图片生成失败，跳过并记录错误，继续处理后续图片
- 确保 AGNES_API_KEY 环境变量已正确设置
- 每次运行会在 agnes_images/ 目录下创建带时间戳的新子文件夹以避免覆盖
- 图片间间隔 1 秒发送，避免请求过快
- 脚本路径：scripts/agnes_generator.py
