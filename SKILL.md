---
name: adsense-lint
description: "AdSense 多专家 AI 审查系统 — 全面的网站 AdSense 合规性审计"
tools:
  - Read
  - Write
  - Bash
  - AskUserQuestion
  - Agent
  - Grep
  - Glob
---

# AdSense Lint Skill

你是 AdSense 多专家 AI 审查系统的入口点。

## 启动

首先，读取核心审计指令：

```
Read: shared/adsense-lint.md
```

该文件包含完整的审计流程：参数解析、模式判断、飞行前检查、会话设置、专家编排、汇总规则和输出格式。按其中定义的逻辑执行。

## Claude-Specific 适配

以下是与 Claude Code 平台绑定的具体实现细节。

### 飞行前检查 — 文件验证

验证工作流和参考文件存在：

```bash
SKILL_DIR="$HOME/.claude/skills/adsense-lint"
test -f "$SKILL_DIR/references/scoring-rubric.md" && echo "OK: rubric" || echo "MISSING: rubric"
test -f "$SKILL_DIR/references/report-template.md" && echo "OK: template" || echo "MISSING: template"
```

如有缺失：**立即停止**，提示用户运行 `ait install` 重新安装。

### 分两批并行启动 8 位专家

为避免单次并行过多导致 timeout，将 8 位专家分为两批，每批 4 个。第一批完成后立即启动第二批。

**第一批（轻量/中等负载）：**

| 专家 | subagent_type | 输出路径 |
|------|--------------|----------|
| Policy | `ads-policy-expert` | `<SESSION_DIR>/01-policy/report.json` |
| E-E-A-T | `ads-eeat-expert` | `<SESSION_DIR>/02-eeat/report.json` |
| Cookie | `ads-cookie-expert` | `<SESSION_DIR>/04-cookie/report.json` |
| Tech | `ads-tech-expert` | `<SESSION_DIR>/07-tech/report.json` |

**第二批（重负载）：**

| 专家 | subagent_type | 输出路径 |
|------|--------------|----------|
| Content | `ads-content-expert` | `<SESSION_DIR>/03-content/report.json` |
| Traffic | `ads-traffic-expert` | `<SESSION_DIR>/05-traffic/report.json` |
| AdPlacement | `ads-adplacement-expert` | `<SESSION_DIR>/06-adplacement/report.json` |
| Legal | `ads-legal-expert` | `<SESSION_DIR>/08-legal/report.json` |

调用示例（远程模式）：

```
Agent(subagent_type="ads-policy-expert", description="Policy audit",
  prompt="审查 <url>。将结果写入 <SESSION_DIR>/01-policy/report.json。评分 0-100。输出合法 JSON，字段：expert, score, maxScore, weight, status, findings[], summary。每个 finding 必须有 severity/category/title/description/evidence/recommendation。")
```

调用示例（本地模式）：

```
Agent(subagent_type="ads-policy-expert", description="Policy audit",
  prompt="你是 AdSense 政策合规专家。这是本地代码审查——不要使用 WebFetch。使用 Read 和 Grep 扫描项目 <project_path> 中的所有 HTML/JSX/TSX/Vue/Markdown 文件。查找：禁止内容、隐藏文本、关键词堆砌、门页、重复内容。将结果写入 <SESSION_DIR>/01-policy/report.json。评分 0-100。输出合法 JSON。")
```

**关键：每批 4 个 Agent 调用必须在同一轮中发出，利用并行 tool calls。两批之间串行，等第一批全部完成后再发第二批。不得使用中介 agent 做编排。**

### 超时与重试

等待每批 4 个 Agent 返回结果：
- 若某位专家返回 **timeout** 或 **failed**，在发下一批之前单独对该专家**重试一次**。
- 重试时精简 prompt，仅保留核心审查指令和输出路径，避免重复说明背景规则。
- 若重试仍失败，汇总阶段为该专家写入备用 report.json：
  - `score: 0`, `status: "failed"`
  - 一条 critical 发现，标题 `审计执行失败`，描述说明超时或失败原因。
- **不要因为单个专家失败而阻塞整体审计。**

### 交互确认

远程模式下，如果未指定 `--auto`，使用 `AskUserQuestion` 向用户确认 URL 和审计范围。

### 汇总

参考 `shared/adsense-lint.md` 中的评分公式和输出格式，生成 `report-final.json`、`report-final.html` 和 `action-plan.md`。


---

## 版本历史


### v1.2（2026-06-01）— 基于社交信号和作者署名的补充迭代

基于 LXS Tools 第二轮优化，新增以下检查维度：

**E-E-A-T（作者署名质量评估）：**
- 新增作者署名真实性检测：真实姓名 vs 泛团队名（"LXS Tools Team"、"Admin"等）
- 带作者简介 +3 分，使用泛团队名 -5 分

**Content（博客内容量评分）：**
- 新增 Blog 文章数量评分阈值表：0-2篇(<60)、3-5篇(60-70)、6-8篇(70-80)、9+篇(80-90)
- Blog 内容量作为内容厚度调节因子

**Traffic（社交信号评估）：**
- 新增社交资料链接评分：每个真实社交链接 +2 分，4+ 平台为强信号
- 新增社交分享按钮评分：每个渠道 +2 分
- 新增 Newsletter 订阅检测：存在 +5 分，占位 URL +2 分
### v1.1（2026-06-01）— 基于真实项目修复的最佳实践迭代

基于 LXS Tools 项目实际修复的 AdSense 合规问题，对 skill 进行以下增强：

**Cookie 合规（Consent Mode v2 完整性）：**
- 新增 Consent Mode v2 信号检查：d_user_data、d_personalization、ds_data_redaction、url_passthrough、wait_for_update
- 新增同意库实现质量检查：mode: 'opt-in' vs opt-out、回调函数完整性
- 新增同意后回调验证：用户操作后是否正确更新所有 v2 信号
- 更新评分标准：v2 信号缺失直接标记 critical

**法律页面（隐私政策一致性检查）：**
- 新增"隐私政策与网站行为一致性"检查维度：声明不使用第三方广告但加载 AdSense、声明不收集数据但使用 Google Fonts 等
- 新增 DMCA 章节完整性检查：7 项要素至少覆盖 4 项
- 新增政策矛盾自动检测逻辑

**E-E-A-T（关于页面质量评估）：**
- 新增关于页面"真实感"评估维度：创始人姓名、具体故事、个人语气、技术理念、邀请交互
- 新增 5 项真人写作加分信号和 5 项 AI/模板扣分信号
- 评分调整：真实感加分最多 +15 分，模板化扣分每项 -5 分

**Content（新增 AI 模式检测 + 工具页内容检查）：**
- 新增 4 类 AI 模式检测：第一人称伪装句式、模糊具体化句式、警示性框架句式、工具/产品描述 AI 模式
- 新增工具页面专项检测：内容厚度、模板化程度、独立描述文本检查
- 工具页面薄弱内容每项扣 3-5 分

**Traffic（社交分享和订阅信号强化）：**
- 新增社交分享按钮检测（X/Twitter、LinkedIn 等）
- 新增 NewsLetter 订阅表单检测（Mailchimp 等）
- 新增社交资料链接检测（GitHub、Twitter 等）
- 参与信号加分：分享按钮 +2 分/个，订阅 +5 分，社交链接 +2 分/个

**Policy（隐私政策矛盾检测）：**
- 新增欺骗性行为子类：隐私政策与网站行为矛盾
- 声明与事实矛盾直接触发 critical 级别发现，可导致否决

