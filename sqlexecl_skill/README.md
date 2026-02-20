# sqlexecl_skill

A specialized AI skill for automated SQL batch generation from Excel templates in financial systems.

## 🚀 Overview

This skill transforms complex financial Excel templates into production-ready SQL batch update scripts. It handles high-precision account numbers, encryption algorithms (MD5), and complex database/table structures with a modular plugin architecture.

## ✨ Features

- **Modular Plugin System**: Support for multiple financial systems with extensible architecture
- **Smart Pattern Recognition**: Automatic detection of system types and SQL patterns
- **Data Validation**: Automatic cleaning of floating-point account numbers and special characters
- **Multi-System Support**: Ready-to-use plugins for major banking and financial systems
- **Custom Extension**: Easy to add new systems with simple configuration

## 📦 Supported Systems

| System | Keywords | SQL Template |
|--------|----------|--------------|
| **NXY_TELLER** | Rural Credit Bank, Teller, `bi_BankTeller` | `UPDATE bi_BankTeller SET Password='{pwd}', Teller_Name='{name}', [Telephone]='{dept}' WHERE Teller_No='{id}';` |
| **VTM_SYS** | VTM, Digital Currency, `tb_User` | `UPDATE [dbo].[tb_User] SET [Password]='{pwd}' WHERE [LoginNo]='{id}';` |
| **BSI_BANK** | BSI, MD5, `sys_person` | `UPDATE [dbo].[sys_person] SET [AccountPwd]=lower(CONVERT(VARCHAR(32), HASHBYTES('MD5','{pwd}'), 2)) WHERE AccountNo='{id}';` |
| **MOBILE_P2P** | Mobile Banking, Consumer Finance, `P2P_Users` | `UPDATE [库名].[dbo].[P2P_Users] SET [U_UserPwd]='{pwd}' WHERE [U_UserNo]='{id}';` |
| **CROWDFUND** | Crowdfunding, `ZC_Users` | `UPDATE [dbo].[ZC_Users] SET U_UserPwd='{pwd}' WHERE U_UserNo='{id}';` |
| **COMMON_USER** | User Info, `tb_UserInfo` | `UPDATE [tb_UserInfo] SET [UserPwd]='{pwd}', [UserName]='{name}' WHERE [UserNo]='{id}';` |
| **JXTTFW_TELLER** | Hall Service, tb_Student, JXTTFW | `UPDATE [JXTTFW_20230718_LW].[dbo].[tb_Student] SET [Name]='{name}', [Password]='{pwd}' WHERE [StudentNo]='{id}';` |

## 🛠️ Usage

### Basic Usage

```
1. Upload your Excel template with account data
2. The skill automatically detects the system type
3. Review the parsed mapping confirmation
4. Get production-ready SQL batch scripts
```

### Custom Systems

For systems not in the built-in list:

1. Provide a reference SQL statement
2. The skill extracts table names, columns, and primary keys
3. Automatically generates the appropriate SQL template

Example:
```
User: "Generate SQL using this pattern: UPDATE [MyTable] SET [Pwd]='123' WHERE [ID]='S01'"

Skill: "Custom system detected. Table: MyTable, Password column: Pwd, Primary Key: ID"
```

## 📁 File Structure

```
sqlexecl_skill/
├── SKILL.md                          # Complete skill documentation
├── README.md                         # This file (English)
├── README_CN.md                      # 中文版本
├── demo.txt                          # Sample data file
├── data.xls                          # Sample Excel data
├── NXY_update.sql                    # Generated SQL output example
└── 陕西山阳业务技能比赛暨柜员等级评定人员统计表.xlsx  # Practical example dataset
```

## 🔧 Data Cleaning Rules

The skill automatically applies these transformations:

- **Account Number Cleaning**: Removes `.0` suffix from Excel floating-point numbers
- **Null Value Handling**: Skips or sets NULL for empty fields
- **Special Character Removal**: TRIM whitespace and invisible characters
- **Batch Segmentation**: Inserts `GO` every 100 statements (SQL Server)

## 📖 Examples

### Hall Service System (JXTTFW)

**Input**: Excel file with account data (S21005, S21013, etc.)

**Generated SQL**:
```sql
UPDATE [JXTTFW_20230718_LW].[dbo].[tb_Student]
SET [Name] = '石静静', [Password] = '851858'
WHERE [StudentNo] = 'S21005';

UPDATE [JXTTFW_20230718_LW].[dbo].[tb_Student]
SET [Name] = '潘越', [Password] = '746933'
WHERE [StudentNo] = 'S21013';
```

## 🤝 Extending the Skill

Add new systems by editing `SKILL.md` and adding a row to the plugin table:

```markdown
| **NEW_SYSTEM** | System keyword, `table_name` | `UPDATE [dbo].[Table] SET [Col]='{pwd}' WHERE [ID]='{id}';` |
```

## 📝 License

This skill is part of the skill repository and follows the repository's license.

## 👤 Author

Created for financial system database operations automation.

---

**For Chinese documentation, see [README_CN.md](README_CN.md)**
