# GitHub Releases 发布检查清单

**版本**: 1.0.0  
**更新日期**: 2026-01-22  
**用途**: GitHub Release 发布前的系统化检查

---

## 📋 检查清单

使用指南：
- [ ] = 未开始
- [ ] = 进行中
- [x] = 已完成

---

## 1️⃣ 代码准备检查

### 1.1 代码状态

- [ ] 所有新功能已实现并测试通过
- [ ] Bug 已修复并验证
- [ ] 代码已审查 (Code Review)
- [ ] 文档已更新
- [ ] 无临时调试代码
- [ ] 无敏感信息 (API Keys, 密码等)

### 1.2 Git 状态

- [ ] 所有更改已提交
- [ ] 提交信息清晰规范
- [ ] 代码已推送到远程仓库
- [ ] 无未提交的更改
- [ ] 分支已合并到主分支

### 1.3 版本标签

- [ ] 决定版本号 (Semantic Versioning)
- [ ] 创建版本标签
- [ ] 标签已推送到远程

```bash
# 标签命令
git tag v1.0.0
git push origin v1.0.0
```

---

## 2️⃣ 打包检查

### 2.1 生成资源文件

- [ ] ZIP 文件已生成
- [ ] TAR.GZ 文件已生成
- [ ] SHA256 校验和已生成
- [ ] 文件大小合理 (< 2GB)

```bash
# 打包命令
./githubskill/scripts/package-release.sh v1.0.0 ./releases
```

### 2.2 资源文件验证

- [ ] ZIP 文件可正常解压
- [ ] TAR.GZ 文件可正常解压
- [ ] 校验和验证通过
- [ ] 包含所有必要文件

```bash
# 验证命令
sha256sum -c releases/project-v1.0.0.zip.sha256
unzip -t releases/project-v1.0.0.zip
tar -tzf releases/project-v1.0.0.tar.gz | head
```

---

## 3️⃣ 发布说明检查

### 3.1 发布说明模板

- [ ] 标题已填写
- [ ] 新功能已列出
- [ ] Bug 修复已列出
- [ ] 已知问题已说明
- [ ] 快速开始指南已添加
- [ ] 下载链接已添加

### 3.2 发布说明内容

- [ ] 拼写检查通过
- [ ] 语法正确
- [ ] 链接有效
- [ ] 代码示例正确
- [ ] 无敏感信息

---

## 4️⃣ GitHub 配置检查

### 4.1 权限验证

- [ ] GitHub CLI 已安装
- [ ] 已登录 GitHub
- [ ] 有仓库写入权限

```bash
# 检查命令
gh --version
gh auth status
```

### 4.2 仓库信息

- [ ] 仓库 URL 正确
- [ ] 仓库存在
- [ ] Release 标签不重复

```bash
# 验证命令
gh repo view owner/repo
gh release list
```

---

## 5️⃣ 发布前最终检查

### 5.1 自动化测试

- [ ] 单元测试通过
- [ ] 集成测试通过
- [ ] E2E 测试通过 (如适用)

```bash
# 测试命令示例
npm test
pytest
cargo test
```

### 5.2 安全检查

- [ ] 无依赖漏洞
- [ ] 无已知安全漏洞

```bash
# 安全检查命令
npm audit
snyk test
```

### 5.3 文档检查

- [ ] README.md 已更新
- [ ] CHANGELOG.md 已更新
- [ ] API 文档已更新 (如适用)
- [ ] 许可证文件存在

---

## 6️⃣ 发布执行检查

### 6.1 创建 Release

- [ ] Release 已创建
- [ ] 标题正确
- [ ] 发布说明已添加
- [ ] 标签正确

```bash
# 创建命令
gh release create v1.0.0 --title "v1.0.0 Release" --notes "Release notes here"
```

### 6.2 上传资源

- [ ] ZIP 已上传
- [ ] TAR.GZ 已上传
- [ ] 校验和文件已上传

```bash
# 上传命令
gh release upload v1.0.0 ./releases/project-v1.0.0.zip
gh release upload v1.0.0 ./releases/project-v1.0.0.tar.gz
```

### 6.3 发布确认

- [ ] Release 预览无误
- [ ] 资源可下载
- [ ] 链接可访问
- [ ] 状态设为已发布 (非草稿)

```bash
# 查看命令
gh release view v1.0.0

# 发布命令 (如需要)
gh release edit v1.0.0 --draft=false
```

---

## 7️⃣ 发布后检查

### 7.1 验证发布

- [ ] Release 页面可访问
- [ ] 下载链接有效
- [ ] 资源文件可下载
- [ ] 发布说明显示正确

### 7.2 通知相关人员

- [ ] 团队已通知
- [ ] 用户已通知 (如需要)
- [ ] 社交媒体已更新 (如需要)

---

## 📝 快速检查命令

### 一键检查脚本

```bash
#!/bin/bash
echo "🔍 发布前快速检查"
echo "================================"

# 1. 检查 Git 状态
echo "📌 Git 状态:"
git status --short

# 2. 检查未推送的提交
echo "\n📌 未推送的提交:"
git log origin/main..HEAD --oneline 2>/dev/null || echo "  无"

# 3. 检查标签
echo "\n📌 最新标签:"
git describe --tags --abbrev=0

# 4. 检查资源文件
echo "\n📌 资源文件:"
ls -lh ./releases/ 2>/dev/null || echo "  未找到"

# 5. 检查 GitHub CLI
echo "\n📌 GitHub CLI:"
gh --version | head -1

# 6. 检查认证
echo "\n📌 GitHub 认证:"
gh auth status 2>&1 | head -3

echo "\n✅ 检查完成"
```

---

## 🚨 常见问题快速参考

| 问题 | 解决方案 |
|------|----------|
| gh 命令未找到 | 安装 GitHub CLI |
| 未认证 | 运行 `gh auth login` |
| 标签已存在 | 使用新版本号或删除旧标签 |
| 资源上传失败 | 检查文件大小 (<2GB) 和权限 |
| 校验和不匹配 | 重新生成并验证 |

---

## 📞 紧急联系

如遇问题，请参考：
- [故障排除指南](./references/RELEASES_BEST_PRACTICE.md#故障排除)
- [GitHub CLI 文档](https://cli.github.com/manual/)
- [GitHub Actions 文档](https://docs.github.com/en/actions)

---

**使用说明**:  
将本检查清单复制到您的项目中，在发布前逐项检查。完成所有检查项后，即可放心发布 Release！

✅ **祝您发布顺利！**
