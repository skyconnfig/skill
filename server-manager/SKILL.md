---
name: server-manager
description: Windows server management skill for IIS site management, remote desktop connections, and configuration parsing. Use when user needs to manage Windows servers including extracting server addresses from URLs, connecting via RDP (mstsc), reading Excel files for server credentials, managing IIS sites (list, start, stop), extracting database connection strings from web.config and appsettings.json files, and performing Windows server administration tasks.
---

# Server Manager

Manage Windows servers through IIS administration, remote desktop connections, and configuration file analysis.

## Capabilities

### URL Processing
Extract server addresses from HTTP/HTTPS links:
```bash
# Input: https://example.com/api/health
# Output: example.com
```

### Remote Desktop
Launch MSTSC connections using Excel credentials:
```bash
# Read Excel file for server IP and password
# Launch: mstsc /v:SERVER_IP /p:PASSWORD
```

### IIS Management
PowerShell-based IIS administration:
- List all sites with status
- Get site by ID
- Start/Stop sites
- Retrieve physical paths

### Configuration Parsing
Extract database names from:
- **web.config**: `Initial Catalog=DATABASE_NAME`
- **appsettings.json**: `database=DATABASE_NAME`

## Usage

### List IIS Sites
```markdown
/use server-manager --action list-sites
```

### Get Site by ID
```markdown
/use server-manager --action get-site --site-id 1
```

### Filter Sites by Status
```markdown
/use server-manager --action list-sites --status running
/use server-manager --action list-sites --status stopped
```

### Remote Desktop Connection
```markdown
/use server-manager --action remote-connect --excel "C:\servers.xlsx"
```

### Extract Database Connections
```markdown
/use server-manager --action parse-config --config "C:\sites\mysite\web.config"
/use server-manager --action parse-config --config "C:\sites\mysite\appsettings.json"
```

### Complete Workflow
```markdown
/use server-manager --url "https://production-api.company.com" --excel "C:\credentials\servers.xlsx" --action full-scan
```

## Scripts

### excel_reader.py
Read server credentials from Excel files.
```bash
python scripts/excel_reader.py "C:\servers.xlsx"
```
Expected Excel format:
| Server | IP | Password |
|--------|-----|----------|
| WEB-01 | 192.168.1.10 | pass123 |

### iis_manager.ps1
PowerShell script for IIS operations.
```powershell
# List all sites
powershell -File scripts/iis_manager.ps1 -Action ListSites

# Get specific site
powershell -File scripts/iis_manager.ps1 -Action GetSite -SiteId 1

# Start site
powershell -File scripts/iis_manager.ps1 -Action StartSite -SiteId 1

# Stop site
powershell -File scripts/iis_manager.ps1 -Action StopSite -SiteId 1
```

### config_parser.py
Parse connection strings from configuration files.
```bash
# Parse web.config
python scripts/config_parser.py "C:\site\web.config" --type webconfig

# Parse appsettings.json
python scripts/config_parser.py "C:\site\appsettings.json" --type appsettings
```

### remote_desktop.py
Launch MSTSC connections.
```bash
python scripts/remote_desktop.py --ip "192.168.1.10" --password "pass123"
```

## Examples

### Example 1: List Running Sites
```markdown
/use server-manager --action list-sites --status running
```
Output:
```
SiteId Name                 Status   Physical Path
------ ----                 ------   ------------
1      Default Web Site     Running  C:\inetpub\wwwroot
2      MyApplication       Running  C:\sites\myapp
3      API_Service         Running  C:\sites\api
```

### Example 2: Extract Database from web.config
```markdown
/use server-manager --action parse-config --config "C:\sites\webapp\web.config"
```
Input:
```xml
<add name="GeneralDB" connectionString="Data Source=.;Initial Catalog=2023_ZJSS_KHJL;User=dyadmin;Password=saSA123" providerName="System.Data.SqlClient" />
```
Output:
```
Database: 2023_ZJSS_KHJL
Server: .
User: dyadmin
Provider: System.Data.SqlClient
```

### Example 3: Extract Database from appsettings.json
```markdown
/use server-manager --action parse-config --config "C:\sites\webapp\appsettings.json"
```
Input:
```json
"DbContext": "server=.;database=FinancialSandTable;user=sa;password=0FCOwD9u74fc1VjH$d;min pool size=5;max pool size=18024;connect timeout = 20;"
```
Output:
```
Database: FinancialSandTable
Server: .
User: sa
Min Pool Size: 5
Max Pool Size: 18024
Connection Timeout: 20
```

### Example 4: Full Server Scan
```markdown
/use server-manager --url "https://prod-api.company.com" --excel "C:\creds\servers.xlsx" --action full-scan
```
Process:
1. Extract server: prod-api.company.com
2. Read Excel for credentials
3. Connect via RDP
4. List IIS sites
5. Extract all database connections

## Requirements

### Windows PowerShell
IIS management requires PowerShell 5.1+ with WebAdministration module:
```powershell
# Verify installation
Get-Module -ListAvailable WebAdministration

# If needed, install:
Install-WindowsFeature Web-Mgmt-Tools
```

### Python Dependencies
```bash
pip install openpyxl pandas lxml
```

### Excel File Format
Columns required:
- `Server` - Server name
- `IP` - IP address
- `Password` - RDP password

Optional columns:
- `Username` - RDP username (default: Administrator)

## Error Handling

- **Permission denied**: Run scripts as Administrator
- **IIS module not found**: Install WebAdministration module
- **Excel file not found**: Verify file path and permissions
- **Connection string not found**: Check config file format
- **Site not found**: Verify site ID exists

## Safety Guidelines

- **Always backup** web.config before modifications
- **Confirm before stopping** production sites
- **Use test environments** first when possible
- **Verify credentials** before remote connections
