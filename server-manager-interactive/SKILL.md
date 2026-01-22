---
name: server-manager-interactive
description: Interactive Windows server management skill that provides intelligent next-step suggestions after each operation. Use for IIS administration, remote desktop connections, configuration parsing, and database management. After completing any action, the skill prompts user for follow-up actions instead of just returning results.
---

# Interactive Server Manager

Intelligent Windows server management with interactive guidance and next-step suggestions.

## Interactive Mode

The skill operates interactively - after completing any action, it suggests next steps based on context:

```markdown
/use server-manager-interactive --action list-sites
```

**After execution, you'll see:**
- Operation results
- Suggested next actions (context-aware)
- Quick command shortcuts
- Related operations

## Core Actions

### 1. IIS Sites Management

#### List All Sites
```markdown
/use server-manager-interactive --action list-sites
```
**After execution, suggests:**
- "Would you like to start/stop a specific site?"
- "View physical path for any site?"
- "Get detailed information about a site?"

#### List Sites by Status
```markdown
/use server-manager-interactive --action list-sites --status running
/use server-manager-interactive --action list-sites --status stopped
```

#### Get Site Details
```markdown
/use server-manager-interactive --action get-site --site-id 1
```
**After execution, suggests:**
- "Start this site?"
- "Stop this site?"
- "View physical path?"
- "Check site configuration?"

#### Start/Stop Site
```markdown
/use server-manager-interactive --action start-site --site-id 1
/use server-manager-interactive --action stop-site --site-id 1
```
**After execution, suggests:**
- "Verify site status?"
- "Test site accessibility?"
- "View site logs?"

### 2. Remote Desktop Connections

#### Connect via Excel Credentials
```markdown
/use server-manager-interactive --action remote-connect --excel "C:\servers.xlsx"
```
**After execution, suggests:**
- "Would you like to list IIS sites on this server?"
- "Check server status?"
- "View server configuration?"

#### Direct RDP Connection
```markdown
/use server-manager-interactive --action rdp-connect --ip "192.168.1.10" --username "Administrator" --password "pass123"
```

### 3. Configuration Parsing

#### Parse web.config
```markdown
/use server-manager-interactive --action parse-config --config "C:\sites\webapp\web.config"
```
**After execution, suggests:**
- "Connect to this database?"
- "View connection string details?"
- "Parse another configuration file?"
- "Test database connectivity?"

#### Parse appsettings.json
```markdown
/use server-manager-interactive --action parse-config --config "C:\sites\webapp\appsettings.json" --type appsettings
```

### 4. URL Processing

#### Extract Server from URL
```markdown
/use server-manager-interactive --action process-url --url "https://production-api.company.com"
```
**After execution, suggests:**
- "Connect to this server via RDP?"
- "List IIS sites on this server?"
- "Check site status?"
- "Parse configuration files?"

### 5. Complete Workflows

#### Full Server Scan
```markdown
/use server-manager-interactive --action full-scan --url "https://prod-api.company.com" --excel "C:\creds\servers.xlsx"
```
**After execution, suggests:**
- "Start/Stop any sites?"
- "Test site accessibility?"
- "Extract database connections?"
- "Create RDP connection?"

#### Database Discovery
```markdown
/use server-manager-interactive --action find-databases --config "C:\sites\webapp\web.config"
```
**After execution, suggests:**
- "Connect to database?"
- "Extract all connections from multiple files?"
- "Test database connectivity?"

## Interactive Examples

### Example 1: IIS Site Management Session

```markdown
User: /use server-manager-interactive --action list-sites

Assistant:
## IIS Sites Overview

| SiteId | Name | Status | Physical Path |
|--------|------|--------|---------------|
| 1 | Default Web Site | Running | C:\inetpub\wwwroot |
| 2 | MyApplication | Running | C:\sites\myapp |
| 3 | API_Service | Stopped | C:\sites\api |

**Suggested Next Actions:**
1. 🔄 Start site 3 (API_Service)
2. ⏹️ Stop site 2 (MyApplication)
3. 📁 View physical path for any site
4. ℹ️ Get details for a specific site

**Quick Commands:**
- `/use server-manager-interactive --action start-site --site-id 3`
- `/use server-manager-interactive --action get-site --site-id 2`

What would you like to do?
```

### Example 2: Database Connection Discovery

```markdown
User: /use server-manager-interactive --action parse-config --config "C:\sites\webapp\web.config"

Assistant:
## Database Connection Found

**Database**: 2023_ZJSS_KHJL
**Server**: .
**User**: dyadmin
**Provider**: System.Data.SqlClient

**Connection String**:
Data Source=.;Initial Catalog=2023_ZJSS_KHJL;User=dyadmin;Password=******

**Suggested Next Actions:**
1. 🔗 Connect to this database
2. 📋 Extract all connections from multiple configs
3. 🔍 Test database connectivity
4. 📄 Parse another configuration file

**Quick Commands:**
- `/use server-manager-interactive --action test-db --server "." --database "2023_ZJSS_KHJL" --user "dyadmin" --password "***"`
- `/use server-manager-interactive --action parse-config --config "C:\other\web.config"`

What would you like to do?
```

### Example 3: Server URL Processing

```markdown
User: /use server-manager-interactive --action process-url --url "https://2025lcjl.dianyuesoft.com/logon"

Assistant:
## URL Analysis

**Server**: 2025lcjl.dianyuesoft.com
**Protocol**: HTTPS
**Path**: /logon
**Type**: Login page

**Suggested Next Actions:**
1. 🖥️ Connect to server via RDP
2. 📋 List IIS sites on this server
3. 🔍 Check site status
4. 📄 Parse configuration files on server
5. 🌐 Test URL accessibility

**Quick Commands:**
- `/use server-manager-interactive --action rdp-connect --ip "SERVER_IP" --username "Administrator" --password "***"`
- `/use server-manager-interactive --action list-sites`
- `/use server-manager-interactive --action test-url --url "https://2025lcjl.dianyuesoft.com/logon"`

What would you like to do?
```

## Common Workflows

### Workflow 1: Server Investigation
1. Process URL → Extract server address
2. Connect via RDP → Access server
3. List IIS sites → Identify target site
4. Parse config → Extract database info
5. Test connectivity → Verify setup

### Workflow 2: Site Management
1. List sites → View all sites
2. Get details → Understand site config
3. Start/Stop → Manage site status
4. Test accessibility → Verify changes

### Workflow 3: Database Discovery
1. Parse config → Extract connection string
2. Find databases → Identify all databases
3. Test connections → Verify accessibility
4. Document findings → Save for reference

## Response Templates

### After List Sites
```
## IIS Sites

[Results table]

## What to do next?

1. **Manage Sites**
   - Start: `--action start-site --site-id N`
   - Stop: `--action stop-site --site-id N`
   - Details: `--action get-site --site-id N`

2. **Server Actions**
   - RDP Connect: `--action remote-connect --excel "file.xlsx"`
   - Full Scan: `--action full-scan --url "URL"`

3. **Configuration**
   - Parse Config: `--action parse-config --config "path"`
   - Find Databases: `--action find-databases --config "path"`

Choose an action or ask a question.
```

### After Config Parse
```
## Database Connection

[Connection details]

## What to do next?

1. **Database Actions**
   - Test Connection: `--action test-db --server "..." --database "..."`
   - List Tables: `--action list-tables --connection "..."`

2. **Configuration**
   - Parse Another: `--action parse-config --config "path"`
   - Find All: `--action find-databases --config "path"`

3. **Server Actions**
   - RDP Connect: `--action remote-connect --excel "file.xlsx"`
   - List Sites: `--action list-sites`

Choose an action or ask a question.
```

### After URL Processing
```
## Server Information

[Server details]

## What to do next?

1. **Connect**
   - RDP: `--action rdp-connect --ip "..."`
   - Excel: `--action remote-connect --excel "file.xlsx"`

2. **Investigate**
   - List Sites: `--action list-sites`
   - Parse Config: `--action parse-config --config "path"`

3. **Test**
   - Test URL: `--action test-url --url "..."`
   - Test Site: `--action test-site --site-id N`

Choose an action or ask a question.
```

## Error Recovery

When errors occur, the skill provides:

1. **Error Description**: Clear explanation of what went wrong
2. **Possible Causes**: Common reasons for the error
3. **Suggested Solutions**: Steps to resolve the issue
4. **Alternative Actions**: Different approaches to try
5. **Help Command**: How to get more assistance

## Best Practices

1. **Always show next steps** - Never leave user wondering what to do
2. **Provide quick commands** - Make it easy to take action
3. **Context-aware suggestions** - Suggest relevant actions based on recent operations
4. **Offer alternatives** - If one approach fails, suggest others
5. **Document findings** - Keep track of discovered information

## Quick Reference

| Action | Command |
|--------|---------|
| List sites | `--action list-sites` |
| Start site | `--action start-site --site-id N` |
| Stop site | `--action stop-site --site-id N` |
| Get site details | `--action get-site --site-id N` |
| Parse config | `--action parse-config --config "path"` |
| RDP connect | `--action rdp-connect --ip "..."` |
| Excel connect | `--action remote-connect --excel "file.xlsx"` |
| Process URL | `--action process-url --url "..."` |
| Full scan | `--action full-scan --url "..." --excel "file.xlsx"` |
| Test database | `--action test-db --server "..." --database "..."` |
| Test URL | `--action test-url --url "..."` |

## Requirements

### Windows PowerShell
```powershell
# Required module
Install-WindowsFeature Web-Mgmt-Tools

# Verify installation
Get-Module -ListAvailable WebAdministration
```

### Python Dependencies
```bash
pip install openpyxl pandas lxml requests
```

### Excel Format
| Server | IP | Password |
|--------|-----|----------|
| WEB-01 | 192.168.1.10 | pass123 |

Optional: Username column (default: Administrator)

## Safety Guidelines

- **Always backup** before major changes
- **Confirm stopping** production sites
- **Use test environments** first
- **Verify credentials** before connections
- **Document changes** for audit trail
