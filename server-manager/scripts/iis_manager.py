#!/usr/bin/env python3
"""
IIS Manager PowerShell Script Generator
Generates PowerShell commands for IIS site management.
"""

import argparse
import sys
from pathlib import Path


def generate_list_sites_script(status: str = None) -> str:
    """Generate PowerShell script to list IIS sites."""
    ps_script = """
Import-Module WebAdministration

Write-Host "`nIIS Sites List"
Write-Host "=" * 80

$sites = Get-Website

if (-not $sites) {
    Write-Host "No IIS sites found."
    exit 0
}

Write-Host "`nSiteId`tName`t`tStatus`t`tPhysical Path"
Write-Host "-" * 80

foreach ($site in $sites) {
    $siteId = $site.id
    $name = $site.name
    $state = $site.state
    $physicalPath = $site.physicalPath
    
    # Format output
    $stateStr = if ($state -eq 'Started') { "Running" } else { "Stopped" }
    
    Write-Host "$siteId`t$name`t$stateStr`t$physicalPath"
}

Write-Host "`nTotal sites: $($sites.Count)"
"""
    
        if status:
        # Add filtering logic
        status_value = 'Started' if status == 'running' else 'Stopped'
        filter_script = f"""
# Filter by status: {status}
$sites = Get-Website | Where-Object {{ $_.state -eq '{status_value}' }}
"""
        ps_script = filter_script + ps_script
    
    return ps_script


def generate_get_site_script(site_id: int) -> str:
    """Generate PowerShell script to get specific site."""
    return f"""
Import-Module WebAdministration

$siteId = {site_id}

Write-Host "`nIIS Site Details for ID: $siteId"
Write-Host "=" * 50

$site = Get-Website | Where-Object {{ $_.id -eq $siteId }}

if (-not $site) {{
    Write-Host "Site with ID $siteId not found."
    exit 1
}}

Write-Host "`nSite Information:"
Write-Host "  Name:       $($site.name)"
Write-Host "  ID:         $($site.id)"
Write-Host "  State:      $($site.state)"
Write-Host "  Physical Path: $($site.physicalPath)"
Write-Host "  Bindings:   $($site.bindings.collection | Format-List | Out-String)

# Get application information
$apps = Get-WebApplication -Site $($site.name)
if ($apps) {{
    Write-Host "`nApplications:"
    foreach ($app in $apps) {{
        Write-Host "  - $($app.path): $($app.physicalPath)"
    }}
}}

# Get bindings
Write-Host "`nBindings:"
foreach ($binding in $site.bindings.collection) {{
    Write-Host "  Protocol: $($binding.protocol)"
    Write-Host "  Binding:  $($binding.bindingInformation)"
}}
"""


def generate_start_site_script(site_id: int) -> str:
    """Generate PowerShell script to start a site."""
    return f"""
Import-Module WebAdministration

$siteId = {site_id}

Write-Host "Starting IIS Site with ID: $siteId"

$site = Get-Website | Where-Object {{ $_.id -eq $siteId }}

if (-not $site) {{
    Write-Host "Error: Site with ID $siteId not found."
    exit 1
}}

if ($site.state -eq 'Started') {{
    Write-Host "Site '$($site.name)' is already running."
    exit 0
}}

try {{
    Start-Website -Name $($site.name)
    Write-Host "Successfully started site: $($site.name)"
    
    # Verify status
    $updatedSite = Get-Website | Where-Object {{ $_.id -eq $siteId }}
    Write-Host "Current state: $($updatedSite.state)"
}}
catch {{
    Write-Host "Error starting site: $($_.Exception.Message)"
    exit 1
}}
"""


def generate_stop_site_script(site_id: int) -> str:
    """Generate PowerShell script to stop a site."""
    return f"""
Import-Module WebAdministration

$siteId = {site_id}

Write-Host "Stopping IIS Site with ID: $siteId"

$site = Get-Website | Where-Object {{ $_.id -eq $siteId }}

if (-not $site) {{
    Write-Host "Error: Site with ID $siteId not found."
    exit 1
}}

if ($site.state -eq 'Stopped') {{
    Write-Host "Site '$($site.name)' is already stopped."
    exit 0
}}

try {{
    Stop-Website -Name $($site.name)
    Write-Host "Successfully stopped site: $($site.name)"
    
    # Verify status
    $updatedSite = Get-Website | Where-Object {{ $_.id -eq $siteId }}
    Write-Host "Current state: $($updatedSite.state)"
}}
catch {{
    Write-Host "Error stopping site: $($_.Exception.Message)"
    exit 1
}}
"""


def generate_get_physical_path_script(site_id: int) -> str:
    """Generate PowerShell script to get physical path."""
    return f"""
Import-Module WebAdministration

$siteId = {site_id}

$site = Get-Website | Where-Object {{ $_.id -eq $siteId }}

if (-not $site) {{
    Write-Host "Error: Site with ID $siteId not found."
    exit 1
}}

Write-Host "Physical Path for Site ID $siteId:"
Write-Host "$($site.physicalPath)"

# Also check if path exists
if (Test-Path $($site.physicalPath)) {{
    Write-Host "Path exists: YES"
    
    # List web.config if exists
    $webConfig = Join-Path $($site.physicalPath) "web.config"
    if (Test-Path $webConfig) {{
        Write-Host "web.config found: YES"
        Write-Host "web.config path: $webConfig"
    }}
}}
else {{
    Write-Host "Path exists: NO"
}}
"""


def execute_powershell(script: str, script_path: str = None):
    """Execute PowerShell script."""
    import subprocess
    
    try:
        if script_path:
            # Save script to file
            with open(script_path, 'w', encoding='utf-8') as f:
                f.write(script)
            
            # Execute
            result = subprocess.run(
                ['powershell', '-File', script_path],
                capture_output=True,
                text=True,
                timeout=30
            )
        else:
            # Execute inline
            result = subprocess.run(
                ['powershell', '-Command', script],
                capture_output=True,
                text=True,
                timeout=30
            )
        
        if result.returncode != 0:
            print(f"PowerShell Error: {result.stderr}")
            sys.exit(1)
        
        print(result.stdout)
        
    except subprocess.TimeoutExpired:
        print("Error: PowerShell execution timed out")
        sys.exit(1)
    except Exception as e:
        print(f"Error executing PowerShell: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description='Generate and execute IIS management PowerShell scripts.'
    )
    parser.add_argument(
        '--action',
        choices=['list-sites', 'get-site', 'start-site', 'stop-site', 'get-path'],
        required=True,
        help='IIS management action'
    )
    parser.add_argument(
        '--site-id',
        type=int,
        help='Site ID for get-site, start-site, stop-site, get-path actions'
    )
    parser.add_argument(
        '--status',
        choices=['running', 'stopped'],
        help='Filter sites by status'
    )
    parser.add_argument(
        '--execute',
        action='store_true',
        help='Execute the generated PowerShell script'
    )
    parser.add_argument(
        '--output',
        help='Output file path for PowerShell script'
    )
    
    args = parser.parse_args()
    
    # Generate script
    script = ""
    
    if args.action == 'list-sites':
        script = generate_list_sites_script(args.status)
    elif args.action == 'get-site':
        if not args.site_id:
            print("Error: --site-id required for get-site action")
            sys.exit(1)
        script = generate_get_site_script(args.site_id)
    elif args.action == 'start-site':
        if not args.site_id:
            print("Error: --site-id required for start-site action")
            sys.exit(1)
        script = generate_start_site_script(args.site_id)
    elif args.action == 'stop-site':
        if not args.site_id:
            print("Error: --site-id required for stop-site action")
            sys.exit(1)
        script = generate_stop_site_script(args.site_id)
    elif args.action == 'get-path':
        if not args.site_id:
            print("Error: --site-id required for get-path action")
            sys.exit(1)
        script = generate_get_physical_path_script(args.site_id)
    
    # Display or execute script
    if args.execute:
        script_path = args.output or 'temp_iis_script.ps1'
        execute_powershell(script, script_path)
        
        # Clean up temp file
        if not args.output and Path(script_path).exists():
            Path(script_path).unlink()
    else:
        print("Generated PowerShell Script:")
        print("=" * 50)
        print(script)
        print("=" * 50)
        print("\nTo execute, use: --execute")


if __name__ == '__main__':
    main()
