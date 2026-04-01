---
name: yt-search
description: YouTube视频搜索和分析技能 - 搜索视频、获取元数据、分析内容
version: 1.0.0
author: Claude Code
source: user-created
tags:
  - youtube
  - search
  - video
  - content-analysis
  - metadata
---

# YouTube 视频搜索 Skill

## 概述

本 skill 提供强大的 YouTube 视频搜索、元数据提取和内容分析能力。支持关键词搜索、频道搜索、播放列表分析，以及视频信息的结构化提取。

## 核心功能

### 1. 视频搜索

**基础搜索：**
- ✅ 关键词搜索视频
- ✅ 按相关度、日期、浏览量排序
- ✅ 分页获取结果（每次最多50个）
- ✅ 过滤（时长、上传日期、视频类型）

**高级搜索：**
- ✅ 频道内搜索（通过关键词包含频道名）
- ✅ 播放列表搜索
- ✅ 多关键词组合（AND/OR）
- ✅ 精确匹配搜索

### 2. 元数据获取

**视频信息：**
- ✅ 标题、描述、标签
- ✅ 上传日期、时长（ISO 8601格式）
- ✅ 观看次数、点赞数、评论数
- ✅ 缩略图URL（default/medium/high）
- ✅ 频道信息（名称、ID）
- ✅ 分类标签、语言、地区
- ✅ 视频质量（hd/sd）、字幕支持

**批量获取：**
- ✅ 一次获取多个视频的元数据（最多50个/批）
- ✅ 支持视频ID列表
- ✅ 自动分块处理

### 3. 内容分析

**统计信息：**
- ✅ 观看趋势分析
- ✅ 互动率计算（点赞率/观看数）
- ✅ 视频时长格式化（HH:MM:SS 或 MM:SS）
- ✅ 发布时间分析

**高级分析（可选）：**
- ⚠️ 自动生成摘要（需额外实现）
- ⚠️ 评论情感分析（需Comment API）
- ⚠️ 主题识别（需NLP处理）
- ⚠️ 标签相关性（需自定义算法）

## 使用方法

### 基本搜索

```
用户: 搜索"React Hooks教程"
Skill: 执行YouTube搜索，返回前10个结果，包含：
  - 视频标题
  - 频道名称
  - 观看次数
  - 上传日期
  - 视频URL
  - 缩略图（可选）
```

### 按播放量排序搜索

```
用户: 搜索"AI"并按播放量排序，返回前5个
Skill: 执行YouTube搜索，按播放量降序排列，返回前5个最热门视频
```

### 获取特定视频详情

```
用户: 获取视频abc123的详细信息
Skill: 返回完整元数据：
  {
    "title": "视频标题",
    "channel": "频道名称",
    "views": 123456,
    "likes": 7890,
    "duration": "15:30",
    "published": "2024-03-15",
    "description": "完整描述...",
    "tags": ["tag1", "tag2"],
    "thumbnail": "URL",
    "category": "教育"
  }
```

### 频道分析

```
用户: 分析频道"Traversy Media"的最新视频
Skill: 返回：
  - 频道统计（订阅数、总视频数）
  - 最新10个视频列表
  - 平均观看趋势
  - 发布频率分析
```

## 技术实现

### API选项

**方案1: YouTube Data API v3（官方）**
```javascript
// 需要API密钥
const { google } = require('googleapis');
const youtube = google.youtube('v3');

// 搜索视频
const response = await youtube.search.list({
  key: API_KEY,
  q: query,
  type: 'video',
  maxResults: 50,
  part: 'snippet',
  order: 'relevance',
});
```

**方案2: 无API scrape方案（需安装yt-dlp）**
```bash
# 安装依赖
pip install yt-dlp

# 搜索（有限制）
yt-dlp --flat-playlist "ytsearch10:query"
```

**方案3: 混合方案（推荐用于演示）**
- 使用Mock数据模拟搜索结果
- 提供真实API调用示例代码
- 支持切换不同后端

### 配置要求

```javascript
// .env 或配置文件
YOUTUBE_API_KEY=your_api_key_here
YOUTUBE_MAX_RESULTS=50
YOUTUBE_REGION=US
YOUTUBE_LANGUAGE=zh-CN
YOUTUBE_SAFE_SEARCH=moderate
```

## 返回格式

### 搜索结果（标准化）

```json
{
  "success": true,
  "query": "React Hooks教程",
  "total_results": 1234,
  "page": 1,
  "has_next": true,
  "items": [
    {
      "id": "abc123def456",
      "title": "React Hooks完整教程 - 2024最新版",
      "channel": {
        "id": "UCxxxxxx",
        "title": "前端大师",
        "subscriber_count": 150000
      },
      "thumbnails": {
        "default": "https://...",
        "medium": "https://...",
        "high": "https://..."
      },
      "published_at": "2024-03-15T10:30:00Z",
      "duration": "PT15M30S",
      "view_count": 45678,
      "like_count": 2345,
      "comment_count": 123,
      "description": "视频描述...",
      "tags": ["react", "hooks", "tutorial"],
      "category": "27",  // Education
      "live_broadcast": false,
      "url": "https://youtube.com/watch?v=abc123def456"
    }
  ]
}
```

### 元数据获取（详细）

```json
{
  "id": "abc123def456",
  "snippet": {
    "title": "...",
    "description": "...",
    "publishedAt": "...",
    "channelId": "...",
    "channelTitle": "...",
    "tags": [...],
    "category": "27"
  },
  "contentDetails": {
    "duration": "PT15M30S",
    "dimension": "2d",
    "definition": "hd",
    "caption": "true"
  },
  "statistics": {
    "viewCount": "45678",
    "likeCount": "2345",
    "commentCount": "123"
  }
}
```

## 使用限制与最佳实践

### 配额管理

**YouTube Data API v3 配额：**
- 每日免费配额：10,000 units
- 搜索操作：100 units/次
- 视频详情：1-3 units/次
- 分批查询可节省配额

**优化策略：**
- 缓存常用搜索结果
- 批量获取视频详情（单次请求最多50个ID）
- 适当降低搜索频率
- 使用`fields`参数只返回必要字段

### 错误处理

**常见错误：**
- `quotaExceeded` - API配额耗尽
- `videoNotFound` - 视频已删除或私有
- `invalidApiKey` - API密钥无效
- `rateLimitExceeded` - 请求频率超限

**应对措施：**
```javascript
try {
  const result = await searchVideos(query);
  return result;
} catch (error) {
  if (error.code === 'quotaExceeded') {
    // 通知用户配额已耗尽，建议明日重试
    return { error: 'API配额不足，请明天再试' };
  }
  if (error.code === 'rateLimitExceeded') {
    // 延迟后重试
    await delay(1000);
    return await searchVideos(query);
  }
  throw error;
}
```

## 示例工作流

### 场景1: 搜索教程视频并生成阅读列表

```
用户: 帮我找5个最好的React Hooks教程
Skill执行:
1. 搜索 "React Hooks tutorial"
2. 按"观看次数"排序
3. 过滤时长>5分钟
4. 返回前5个结果
5. 格式化为Markdown列表
   - [视频标题](URL) - 频道名 (观看:12.3K, 时长:15:30)
```

### 场景2: 分析竞品视频表现

```
用户: 分析频道"XYZ"最近30天的视频表现
Skill执行:
1. 获取频道最新50个视频
2. 计算每个视频的：
   - 观看/点赞比
   - 发布后7天增长率
   - 平均观看时长（估算）
3. 生成分析报告：
   - 最佳标题格式
   - 理想发布时间
   - 热门话题标签
```

### 场景3: 监控视频评论（需额外API）

```
用户: 监控视频abc123的最新评论
Skill执行:
1. 获取评论列表（最新优先）
2. 提取：
   - 评论数量
   - 正面/中性/负面比例
   - 高频关键词
   - 热门评论
3. 总结用户反馈
```

## 安全性考虑

- ✅ 不要在前端暴露 API 密钥
- ✅ 使用服务端代理或Serverless函数
- ✅ 验证用户输入，防止XSS
- ✅ 限制搜索频率，避免误用
- ✅ 日志记录（仅用于调试，不存储用户隐私数据）
- ⚠️ 遵守YouTube服务条款
- ⚠️ 尊重版权，不下载视频内容

## 扩展功能（可选）

### 1. 智能推荐
```javascript
// 基于观看历史推荐相关视频
async function recommendVideos(watchedVideoIds, limit = 10) {
  const metadata = await batchGetVideoMetadata(watchedVideoIds);
  const tags = extractTopTags(metadata, 20);
  return await searchByTags(tags, limit);
}
```

### 2. 数据导出
- CSV导出（Excel可读）
- JSON格式
- Markdown报告
- RSS订阅生成

### 3. 定时监控
- 特定关键词的新视频通知
- 频道更新提醒
- 观看趋势警报

### 4. 多语言支持
- 设置`regionCode`和`relevanceLanguage`
- 自动翻译标题/描述（需额外API）
- 本地化搜索结果

## 配置文件示例

```yaml
# yt-search.config.yaml
api:
  key: ${YOUTUBE_API_KEY}  # 从环境变量读取
  max_results: 50
  default_order: relevance  # relevance, date, viewCount, rating

search:
  safe_search: moderate
  type: video
  video_embedding: false
  video_definition: any  # any, standard, high, ultra_high

cache:
  enabled: true
  ttl: 3600  # 1小时
  backend: memory  # memory, redis, file

rate_limit:
  requests_per_second: 10
  daily_quota: 10000

output:
  format: json  # json, csv, markdown
  include_thumbnails: true
  max_thumb_size: medium
```

## 限制与注意事项

### YouTube API限制
1. **每日配额** 10,000 units
2. **搜索频率** 不能过高（每秒≤10次）
3. **结果数量** 单次最多50条，需分页获取更多
4. **地区限制** 某些视频受地理限制
5. **年龄限制** 某些视频需要登录查看

### 法律与合规
- ⚠️ 遵守[YouTube服务条款](https://www.youtube.com/t/terms)
- ⚠️ 不得用于自动化观看、刷量等违规行为
- ⚠️ 尊重版权，仅获取元数据
- ⚠️ 保护用户隐私，不收集个人数据
- ✅ 仅用于合法的搜索、分析、研究目的

## 调试与日志

启用调试模式：
```javascript
YT_SEARCH_DEBUG=true yt-search "React Hooks"
```

会输出：
- API请求详情
- 配额使用情况
- 响应时间
- 缓存命中率

## 替代方案

如果YouTube API配额不足，可以考虑：

1. **yt-dlp**（命令行工具）
   - 优点：免费，无配额限制
   - 缺点：无官方支持，可能违反ToS

2. **SerpAPI / RapidAPI**
   - 优点：封装好，易用
   - 缺点：付费，有调用次数限制

3. **自建爬虫**
   - 优点：完全可控
   - 缺点：需要维护，反爬虫挑战

## 版本历史

- **1.0.0** (2026-04-01): 初始版本，支持基础搜索和元数据获取

## 获取帮助

- 📖 [YouTube Data API v3 文档](https://developers.google.com/youtube/v3)
- 🔧 [API配额计算器](https://developers.google.com/youtube/v3/getting-started#quota)
- 💬 问题反馈：在项目仓库提交Issue

---

**提示：** 使用此 skill 时，建议先用测试查询验证配额和功能。对于生产环境，务必实现配额监控和优雅降级机制。
