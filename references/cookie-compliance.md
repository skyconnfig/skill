# GDPR / CCPA / AdSense Cookie 合规检查清单

## 同意横幅要求

### 必须存在
- 首次访问时显示可见的横幅、模态框或弹窗
- 必须在任何非必要 Cookie 设置之前出现

### 可检测信号
HTML/JS 中的关键词：
- `cookie-consent`, `CookieConsent`, `gdpr`, `ccpa`
- `cookie-banner`, `cookie_banner`, `cookieconsent`

已知库：
- `react-cookie-consent`
- `@segment/consent-manager`
- `cookiebot`, `cookiebot-react`
- `vanilla-cookieconsent`
- `cookie-consent-js`

组件引用：
- `<CookieConsent`, `import { CookieConsent }`
- `<ConsentManager`, `import { ConsentManager }`
- `<CookieBanner`, `import { CookieBanner }`

自定义实现：
- `useEffect` 结合 `localStorage`/`sessionStorage` 和 cookie 关键词
- 状态变量如 `showBanner`, `setCookieConsent`, `consentGiven`

### 横幅内容
必须说明：
1. 使用了哪些 Cookie（必要、分析、广告）
2. 使用原因（个性化、测量、广告）
3. 如适用，提及第三方广告（Google AdSense）
4. 用户如何管理或撤回同意

### 同意库实现最佳实践

检测使用的 Cookie 同意库：

- **vanilla-cookieconsent**（轻量，推荐前端项目）：
  - 使用 `mode: 'opt-in'`（默认拒绝模式），而非 `opt-out`
  - 分类推荐：`necessary: { readOnly: true }`（必要 Cookie 不可关闭）+ `ads: { enabled: false }`（广告默认关闭）
  - 布局推荐：`consentModal` 用 `layout: 'bar'` + `position: 'bottom'`（底部通栏）
  - `preferencesModal` 用 `layout: 'box'` + `position: 'right'`
  - 必须包含中文和英文双语翻译
  - 使用 `onFirstConsent`、`onConsent`、`onChange` 回调，在用户操作后调用 `gtag('consent', 'update', ...)`
- cookiebot、onetrust、cookielaw 等商业方案
- 自定义实现：检查 `useEffect` + `localStorage` 结合 cookie 关键词

### 用户选择
- 必须提供 **接受** 选项
- 必须提供 **拒绝 / decline / 管理偏好** 选项
- 仅包含 "OK" 或 "Got it" 的横幅不符合 GDPR 要求

## AdSense 同意模式

如果网站上存在 AdSense：
- 应实现 Google 同意模式（`gtag('consent', ...)`）
- 默认状态应拒绝 `ad_storage` 和 `analytics_storage`，直到获得同意
- 欧洲经济区/英国用户需要此功能才能展示个性化广告

### Consent Mode v2 必须信号（2024 年 3 月生效）

Google Consent Mode v2 要求以下信号，**缺失 `ad_user_data` 或 `ad_personalization` 属于严重违规**：

| 信号 | 默认值 | 说明 |
|---------|--------|----------|
| `ad_storage` | `denied` | 广告 Cookie 存储 |
| `ad_user_data` | `denied` | 用户数据发送至 Google 用于广告（v2 新增） |
| `ad_personalization` | `denied` | 个性化广告（v2 新增） |
| `analytics_storage` | `denied` | 分析 Cookie |
| `functionality_storage` | `granted` | 功能性 Cookie |
| `security_storage` | `granted` | 安全 Cookie |

**推荐实现模式（在 `<head>` 顶部，任何第三方脚本之前）：**
```javascript
gtag('consent', 'default', {
  'ad_storage': 'denied',
  'ad_user_data': 'denied',
  'ad_personalization': 'denied',
  'analytics_storage': 'denied',
  'functionality_storage': 'granted',
  'security_storage': 'granted',
  'wait_for_update': 500,
});
gtag('set', 'ads_data_redaction', true);
gtag('set', 'url_passthrough', true);
```

**检查要点：**
- `ads_data_redaction: true` — 拒绝时脱敏广告数据（v2 推荐）
- `url_passthrough: true` — 通过 URL 传递同意状态（v2 推荐）
- `wait_for_update: 500` — 等待 CMP 更新的时间（毫秒）
- 用户接受时调用：`gtag('consent', 'update', { ad_storage: 'granted', ad_user_data: 'granted', ad_personalization: 'granted', analytics_storage: 'granted' })`
- 用户拒绝时调用：`gtag('consent', 'update', { ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied', analytics_storage: 'denied' })`

### 同意后回调检查

必须验证用户操作后是否正确调用了 `gtag('consent', 'update', ...)`：
- 用户点击"接受全部"时 → 更新所有存储类型为 `granted`
- 用户点击"仅必要"或"拒绝全部"时 → 保持广告/分析为 `denied`
- 用户在偏好弹窗中切换分类时 → 根据变更的分类更新对应信号

**常见错误：** 仅更新 `ad_storage` 但忽略 `ad_user_data` 和 `ad_personalization`。这会使 Consent Mode v2 不完整。

## 同意前拦截

非必要脚本（分析、广告、社交像素）不得在用户同意前加载。

检查：
- Google Analytics 脚本是否在 `<head>` 中无条件加载
- AdSense 脚本是否在同意横幅之前加载
  - 注意：AdSense 脚本（`adsbygoogle.js`）通常需在 `<head>` 中同步加载，这不矛盾。同意通过 Consent Mode 控制，而非脚本加载时间
- Facebook Pixel 或其他跟踪像素是否无条件加载

## 评分

| 条件 | 扣分 |
|-----------|---------|
| 无横幅 | 严重 |
| 有横幅但无 Consent Mode v2 | 严重 |
| 有横幅但缺少 `ad_user_data` 或 `ad_personalization` | 严重 |
| 有横幅但未在用户操作后更新同意信号 | 严重 |
| 使用 `opt-out`（默认接受）而非 `opt-in`（默认拒绝） | 警告 |
| 有横幅但无拒绝选项 | 警告 |
| 有横幅但缺少 `ads_data_redaction` 或 `url_passthrough` | 警告 |
| 有横幅但缺少 `wait_for_update` | 信息 |
| 使用旧版 Consent Mode（仅 `ad_storage` + `analytics_storage`） | 警告（建议升级至 v2） |
| 缺少 AdSense 同意模式 | 警告 |
| 同意前加载跟踪脚本 | 警告 |
| 横幅文本模糊（未提及广告） | 信息 |
