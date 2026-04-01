# YouTube Search Skill - 变更日志

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-04-01

### Added
- 初始版本发布
- 基础 YouTube 视频搜索功能
- 支持多种输出格式（pretty, JSON, Markdown, CSV）
- 完整元数据获取（标题、描述、标签、统计等）
- 批量视频详情获取
- 频道信息查询
- 配置系统（config.yaml）
- 缓存支持（内存、文件、Redis）
- 配额管理
- 错误处理和重试机制
- 命令行接口（CLI）
- 完整的测试套件
- 设置向导
- **新功能：按播放量排序（--top-views 参数）**
- Excel 导出支持（--excel 参数）

### Features
- 按相关度、日期、浏览量排序
- 视频时长过滤（短/中/长）
- 清晰度过滤（标清/高清/超清）
- 地区和语言设置
- 互动率计算
- 缩略图URL获取
- 支持分页
- Views/Subscribers 比率分析

### Documentation
- SKILL.md - Skill 规范文档
- README.md - 用户使用指南
- config.yaml.example - 配置示例
- .env.example - 环境变量示例

### Technical
- Node.js ES Modules 架构
- YouTube Data API v3 集成
- 配额自动追踪
- 错误代码标准化

---

## [Unreleased]

### Planned
- 评论情感分析（需要Comment API）
- 自动生成摘要（需要NLP处理）
- 多语言自动翻译
- 视频字幕提取和分析
- 订阅者频道推荐
- 播放列表完整分析
- Web界面（Electron/React）
- Docker容器化
- 多账号配额聚合

### Under Consideration
- 趋势视频监控
- 自定义搜索算法
- AI生成搜索报告
- 视频质量评分系统
