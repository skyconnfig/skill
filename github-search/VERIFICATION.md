# GitHub Search Skill - Verification Checklist

使用此清单验证 github-search skill 已正确安装和配置。

## ✅ 安装验证

### 1. 文件结构检查

运行以下命令验证所有文件存在：

```bash
cd ~/.claude/skills/github-search

# 核心文件
ls -la README.md SKILL.md QUICKSTART.md CHANGELOG.md LICENSE

# 配置文件
ls -la .env.example config.yaml.example requirements.txt .gitignore

# 脚本
ls -la scripts/search.py scripts/setup.py

# 库模块
ls -la lib/__init__.py lib/github_api.py lib/formatter.py lib/cache.py

# 测试
ls -la test_skill.py

# Claude Code 配置
ls -la .claude/settings.json .claude/github-search.md
```

**预期结果：** 所有文件应存在且可读

### 2. Python 依赖检查

```bash
python -c "import requests, yaml, dotenv; print('All dependencies OK')"
```

**预期输出：** `All dependencies OK`

如果失败，运行：
```bash
pip install -r requirements.txt
```

### 3. 脚本可执行性

```bash
python scripts/search.py --help
```

**预期结果：** 显示帮助信息，无错误

### 4. 测试套件

```bash
python test_skill.py
```

**预期输出：**
```
✓ All argument parsing tests passed
✓ All query building tests passed
✓ All cache tests passed
✓ All formatting tests passed
✓ Integration tests passed

All Tests Passed!
```

## 🔑 配置验证

### 5. GitHub Token 设置（推荐）

```bash
# 检查环境变量
echo $GITHUB_TOKEN

# 或检查 .env 文件
cat .env 2>/dev/null | grep GITHUB_TOKEN
```

**预期结果：** Token 已设置（非必需但强烈推荐）

如果没有，设置方法：
```bash
export GITHUB_TOKEN="your_token_here"
# 或
echo "GITHUB_TOKEN=your_token_here" > .env
```

### 6. 配置文件

```bash
# 如果不存在，从示例创建
cp config.yaml.example config.yaml 2>/dev/null || true

# 验证配置文件语法
python -c "import yaml; yaml.safe_load(open('config.yaml'))"
```

**预期结果：** 无错误输出

## 🧪 功能测试

### 7. 基本搜索测试

```bash
# 测试搜索功能（需要网络连接）
python scripts/search.py "claude code" --count 3
```

**预期结果：** 显示 3 个仓库结果或错误信息

如果遇到配额错误：
```
Error: API rate limit exceeded
```

**解决：** 设置 GitHub Token 或等待配额恢复

### 8. 不同格式测试

```bash
# JSON 格式
python scripts/search.py "python" --count 2 --json | python -m json.tool

# CSV 格式
python scripts/search.py "python" --count 2 --csv > test.csv
cat test.csv
```

**预期结果：** 格式正确的 JSON 或 CSV

### 9. 过滤功能测试

```bash
# 按语言过滤
python scripts/search.py "machine learning" --language python --count 3

# 按组织过滤
python scripts/search.py "" --org microsoft --sort stars --count 3

# 组合过滤
python scripts/search.py "react" --language typescript --topic "ui" --count 3
```

**预期结果：** 返回符合过滤条件的仓库

### 10. Claude Code 集成测试

如果已安装 Claude Code：

1. 启动 Claude Code
2. 输入：`/github-search "claude code" --count 5`
3. 观察输出

**预期结果：** 命令执行并显示结果

## 📊 配额检查

### 11. 速率限制状态

```bash
python -c "
import requests, os
token = os.getenv('GITHUB_TOKEN')
headers = {'Authorization': f'token {token}'} if token else {}
r = requests.get('https://api.github.com/rate_limit', headers=headers)
print(r.json())
"
```

**预期输出：**
```json
{
  "resources": {
    "core": {
      "limit": 5000,
      "remaining": 4999,
      "reset": 1234567890
    }
  }
}
```

**注意：**
- 无 Token：limit 应为 30（或 60？需要验证）
- 有 Token：limit 应为 5000
- remaining 应大于 0

## 🎯 性能验证

### 12. 缓存测试

```bash
# 第一次搜索（应较慢）
time python scripts/search.py "test query" --count 5 2>&1 | grep -i "Searching"

# 第二次搜索相同内容（应快速）
time python scripts/search.py "test query" --count 5 2>&1 | grep -i "Searching"
```

**预期结果：** 第二次搜索更快（缓存命中）

### 13. 并发请求测试

```bash
# 快速发送多个请求，观察限流
for i in 1 2 3; do
  python scripts/search.py "test" --count 1 &
done
wait
```

**预期结果：** 如果请求过快，脚本应自动等待或显示限流错误

## 🐛 故障排除

### 常见问题

| 问题 | 可能原因 | 解决方案 |
|------|----------|----------|
| `ModuleNotFoundError` | 依赖未安装 | `pip install -r requirements.txt` |
| `yt-dlp not found` | 不适用 - 这是 GitHub 搜索 | 忽略 |
| `403 Forbidden` | 无 Token 或 IP 受限 | 设置 GITHUB_TOKEN |
| `rate limit exceeded` | 配额用尽 | 等待或使用 Token |
| `JSONDecodeError` | API 返回非 JSON | 检查网络连接 |
| `ConnectionError` | 网络问题 | 检查网络/代理 |

### 调试模式

启用详细日志：

```bash
GITHUB_SEARCH_DEBUG=true python scripts/search.py "test" --count 1 2>&1 | head -50
```

**预期结果：** 显示更多调试信息

## 📝 最终检查清单

完成所有以下项，标记为 ✅：

- [ ] 所有文件已创建（参考上面的文件结构检查）
- [ ] Python 依赖已安装
- [ ] 帮助信息正常显示
- [ ] 测试套件全部通过
- [ ] 至少一次搜索成功（有返回结果）
- [ ] JSON 格式输出正确
- [ ] CSV 格式输出正确
- [ ] 过滤功能正常（language, org, topic）
- [ ] GitHub Token 已配置（强烈推荐）
- [ ] 配额检查显示合理数值
- [ ] 缓存功能正常工作
- [ ] Claude Code 命令集成正常（如适用）

## 🎉 安装完成

当所有上述检查项都标记为 ✅ 后，GitHub Search Skill 已完全安装并可以使用。

### 下一步

1. **阅读文档**
   - `QUICKSTART.md` - 快速开始
   - `README.md` - 完整使用指南
   - `SKILL.md` - 技术规范

2. **开始使用**
   ```bash
   /github-search "your first query"
   ```

3. **自定义配置**
   - 编辑 `config.yaml` 调整默认行为
   - 修改输出格式、缓存设置等

4. **探索高级功能**
   - 组合多个过滤条件
   - 导出数据进行分析
   - 集成到自动化脚本

---

**获取帮助：**
- 查看文档：`README.md`, `QUICKSTART.md`
- 运行测试：`python test_skill.py`
- 检查配置：`python scripts/search.py --help`

**报告问题：**
如在验证过程中遇到问题，请检查：
1. Python 版本是否为 3.8+
2. 是否安装了所有依赖
3. 网络连接是否正常
4. GitHub Token 是否正确设置
