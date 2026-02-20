# sqlexecl_skill

专为金融系统设计的AI技能，实现Excel模板到SQL批量脚本的自动化转换。

## 🚀 概述

本技能可将复杂的金融业务Excel模板转换为生产环境可直接执行的SQL批量更新脚本。支持高精度账号处理、加密算法（MD5）以及复杂的库名/表名结构，采用模块化插件架构设计。

## ✨ 功能特点

- **模块化插件系统**：支持多种金融系统，架构可扩展
- **智能模式识别**：自动识别系统类型和SQL模式
- **数据验证清洗**：自动清理浮点账号和特殊字符
- **多系统支持**：内置主流银行和金融系统插件
- **自定义扩展**：简单配置即可添加新系统

## 📦 支持的系统

| 系统标识 | 匹配关键词 | SQL 模板 |
|----------|------------|----------|
| **NXY_TELLER** | 农信银, 柜员, `bi_BankTeller` | `UPDATE bi_BankTeller SET Password='{pwd}', Teller_Name='{name}', [Telephone]='{dept}' WHERE Teller_No='{id}';` |
| **VTM_SYS** | VTM, 数字币, `tb_User` | `UPDATE [dbo].[tb_User] SET [Password]='{pwd}' WHERE [LoginNo]='{id}';` |
| **BSI_BANK** | BSI, MD5, `sys_person` | `UPDATE [dbo].[sys_person] SET [AccountPwd]=lower(CONVERT(VARCHAR(32), HASHBYTES('MD5','{pwd}'), 2)) WHERE AccountNo='{id}';` |
| **MOBILE_P2P** | 手机银行, 消费金融, `P2P_Users` | `UPDATE [库名].[dbo].[P2P_Users] SET [U_UserPwd]='{pwd}' WHERE [U_UserNo]='{id}';` |
| **CROWDFUND** | 众筹, `ZC_Users` | `UPDATE [dbo].[ZC_Users] SET U_UserPwd='{pwd}' WHERE U_UserNo='{id}';` |
| **COMMON_USER** | 用户信息, `tb_UserInfo` | `UPDATE [tb_UserInfo] SET [UserPwd]='{pwd}', [UserName]='{name}' WHERE [UserNo]='{id}';` |
| **JXTTFW_TELLER** | 厅堂服务, tb_Student, JXTTFW | `UPDATE [JXTTFW_20230718_LW].[dbo].[tb_Student] SET [Name]='{name}', [Password]='{pwd}' WHERE [StudentNo]='{id}';` |

## 🛠️ 使用方法

### 基本使用

```
1. 上传包含账号数据的Excel模板
2. 技能自动识别系统类型
3. 确认解析的字段映射关系
4. 获取生产级SQL批量脚本
```

### 自定义系统

对于内置列表中没有的系统：

1. 提供参考SQL语句
2. 技能自动提取表名、字段和主键
3. 自动生成对应的SQL模板

示例：
```
用户: "生成SQL，使用这个模式：UPDATE [MyTable] SET [Pwd]='123' WHERE [ID]='S01'"

技能: "已识别自定义系统。表名：MyTable，密码列：Pwd，主键：ID"
```

## 📁 文件结构

```
sqlexecl_skill/
├── SKILL.md                          # 完整技能文档
├── README.md                         # 英文版说明文档
├── README_CN.md                      # 本文件（中文版）
├── demo.txt                          # 示例数据文件
├── data.xls                          # 示例Excel数据
├── NXY_update.sql                    # 生成的SQL输出示例
└── 陕西山阳业务技能比赛暨柜员等级评定人员统计表.xlsx  # 实战案例数据集
```

## 🔧 数据清洗规则

技能自动应用以下转换：

- **账号清洗**：去除Excel浮点数的`.0`后缀
- **空值处理**：跳过或设为NULL
- **特殊字符清理**：TRIM前后空格和不可见字符
- **批次分隔**：每100条语句插入`GO`（SQL Server规范）

## 📖 使用案例

### 厅堂服务系统 (JXTTFW)

**输入**：包含账号数据（S21005、S21013等）的Excel文件

**生成的SQL**：
```sql
UPDATE [JXTTFW_20230718_LW].[dbo].[tb_Student]
SET [Name] = '石静静', [Password] = '851858'
WHERE [StudentNo] = 'S21005';

UPDATE [JXTTFW_20230718_LW].[dbo].[tb_Student]
SET [Name] = '潘越', [Password] = '746933'
WHERE [StudentNo] = 'S21013';
```

## 🤝 扩展技能

通过编辑`SKILL.md`并在下表中添加一行来添加新系统：

```markdown
| **NEW_SYSTEM** | 系统关键词, `表名` | `UPDATE [dbo].[Table] SET [Col]='{pwd}' WHERE [ID]='{id}';` |
```

## 📝 许可证

本技能属于技能仓库的一部分，遵循仓库的许可证。

## 👤 作者

为金融系统数据库运维自动化而创建。

---

**英文文档请参阅 [README.md](README.md)**
