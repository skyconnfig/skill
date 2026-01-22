#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Server Manager Script
Provides interactive guidance and next-step suggestions after each operation.
"""

import argparse
import json
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List, Optional, Any
import re


class InteractiveServerManager:
    """Interactive server manager with next-step suggestions."""

    def __init__(self):
        self.last_result = None
        self.context = {}

    def parse_args(self):
        """Parse command line arguments."""
        parser = argparse.ArgumentParser(
            description='Interactive Server Manager'
        )
        parser.add_argument(
            '--action',
            required=True,
            choices=[
                'list-sites', 'get-site', 'start-site', 'stop-site',
                'parse-config', 'remote-connect', 'rdp-connect',
                'process-url', 'full-scan', 'test-url', 'test-db',
                'find-databases', 'interactive-help'
            ],
            help='Action to perform'
        )
        parser.add_argument('--site-id', type=int, help='Site ID for site operations')
        parser.add_argument('--status', choices=['running', 'stopped'], help='Filter sites by status')
        parser.add_argument('--config', type=str, help='Path to configuration file')
        parser.add_argument('--type', choices=['webconfig', 'appsettings'], default='webconfig',
                          help='Config file type')
        parser.add_argument('--url', type=str, help='URL to process')
        parser.add_argument('--excel', type=str, help='Excel file path for credentials')
        parser.add_argument('--ip', type=str, help='Server IP address')
        parser.add_argument('--username', type=str, default='Administrator', help='RDP username')
        parser.add_argument('--password', type=str, help='RDP password or Excel cell reference')
        parser.add_argument('--server', type=str, help='Database server')
        parser.add_argument('--database', type=str, help='Database name')
        parser.add_argument('--user', type=str, help='Database user')
        parser.add_argument('--db-password', dest='db_password', help='Database password')
        parser.add_argument('--output', choices=['json', 'table'], default='table',
                          help='Output format')

        return parser.parse_args()

    def run(self):
        """Run the interactive manager."""
        args = self.parse_args()

        # Dispatch to appropriate handler
        handlers = {
            'list-sites': self.handle_list_sites,
            'get-site': self.handle_get_site,
            'start-site': self.handle_start_site,
            'stop-site': self.handle_stop_site,
            'parse-config': self.handle_parse_config,
            'remote-connect': self.handle_remote_connect,
            'rdp-connect': self.handle_rdp_connect,
            'process-url': self.handle_process_url,
            'full-scan': self.handle_full_scan,
            'test-url': self.handle_test_url,
            'test-db': self.handle_test_db,
            'find-databases': self.handle_find_databases,
            'interactive-help': self.handle_help,
        }

        handler = handlers.get(args.action)
        if handler:
            result = handler(args)
            self.last_result = result
            self.print_next_steps(args.action, result)
        else:
            print(f"Unknown action: {args.action}")

    def handle_list_sites(self, args) -> Dict:
        """List IIS sites."""
        sites = self.list_iis_sites()
        if args.status:
            sites = [s for s in sites if s['status'].lower() == args.status.lower()]

        return {
            'type': 'site-list',
            'sites': sites,
            'filter': args.status,
            'count': len(sites)
        }

    def handle_get_site(self, args) -> Dict:
        """Get site details."""
        if not args.site_id:
            return {'error': 'Site ID required'}

        site = self.get_site_details(args.site_id)
        if site:
            return {
                'type': 'site-details',
                'site': site
            }
        else:
            return {'error': f'Site {args.site_id} not found'}

    def handle_start_site(self, args) -> Dict:
        """Start a site."""
        if not args.site_id:
            return {'error': 'Site ID required'}

        success = self.start_site(args.site_id)
        return {
            'type': 'site-action',
            'action': 'started',
            'site_id': args.site_id,
            'success': success
        }

    def handle_stop_site(self, args) -> Dict:
        """Stop a site."""
        if not args.site_id:
            return {'error': 'Site ID required'}

        success = self.stop_site(args.site_id)
        return {
            'type': 'site-action',
            'action': 'stopped',
            'site_id': args.site_id,
            'success': success
        }

    def handle_parse_config(self, args) -> Dict:
        """Parse configuration file."""
        if not args.config:
            return {'error': 'Config file path required'}

        connections = self.parse_connection_string(args.config, args.type)
        return {
            'type': 'config-parsed',
            'config': args.config,
            'type': args.type,
            'connections': connections
        }

    def handle_remote_connect(self, args) -> Dict:
        """Remote connect via Excel."""
        if not args.excel:
            return {'error': 'Excel file path required'}

        credentials = self.read_excel_credentials(args.excel)
        if credentials:
            # Launch RDP for first server
            server = credentials[0]
            self.launch_rdp(server['ip'], args.username, server.get('password', ''))
            return {
                'type': 'remote-connect',
                'excel': args.excel,
                'server': server['server'],
                'ip': server['ip']
            }
        else:
            return {'error': 'Could not read Excel file'}

    def handle_rdp_connect(self, args) -> Dict:
        """Direct RDP connection."""
        if not args.ip:
            return {'error': 'IP address required'}

        self.launch_rdp(args.ip, args.username, args.password or '')
        return {
            'type': 'rdp-connect',
            'ip': args.ip,
            'username': args.username
        }

    def handle_process_url(self, args) -> Dict:
        """Process URL and extract server."""
        if not args.url:
            return {'error': 'URL required'}

        server = self.extract_server_from_url(args.url)
        return {
            'type': 'url-processed',
            'url': args.url,
            'server': server['server'],
            'protocol': server['protocol'],
            'path': server['path'],
            'domain': server['domain']
        }

    def handle_full_scan(self, args) -> Dict:
        """Full server scan workflow."""
        if not args.url:
            return {'error': 'URL required'}

        # Extract server from URL
        server_info = self.extract_server_from_url(args.url)

        # Read credentials if provided
        credentials = None
        if args.excel:
            credentials = self.read_excel_credentials(args.excel)
            server_ip = credentials[0]['ip'] if credentials else None
        else:
            server_ip = None

        # List IIS sites
        sites = self.list_iis_sites()

        # Find config files and extract databases
        databases = self.find_all_databases('.')

        return {
            'type': 'full-scan',
            'server': server_info,
            'credentials': credentials,
            'sites': sites,
            'databases': databases,
            'ip': server_ip
        }

    def handle_test_url(self, args) -> Dict:
        """Test URL accessibility."""
        if not args.url:
            return {'error': 'URL required'}

        import requests
        try:
            response = requests.get(args.url, timeout=10)
            return {
                'type': 'url-test',
                'url': args.url,
                'status_code': response.status_code,
                'response_time': response.elapsed.total_seconds(),
                'accessible': response.status_code < 400
            }
        except Exception as e:
            return {
                'type': 'url-test',
                'url': args.url,
                'error': str(e),
                'accessible': False
            }

    def handle_test_db(self, args) -> Dict:
        """Test database connectivity."""
        return {
            'type': 'db-test',
            'server': args.server,
            'database': args.database,
            'user': args.user,
            'test': 'Connection test would require actual database access'
        }

    def handle_find_databases(self, args) -> Dict:
        """Find all databases in configuration."""
        databases = self.find_all_databases(args.config if args.config else '.')
        return {
            'type': 'databases-found',
            'databases': databases,
            'count': len(databases)
        }

    def handle_help(self, args) -> Dict:
        """Show interactive help."""
        return {
            'type': 'help',
            'message': 'Use --action to perform operations'
        }

    def list_iis_sites(self) -> List[Dict]:
        """List IIS sites using PowerShell."""
        try:
            ps_script = '''
            Import-Module WebAdministration
            Get-Website | ForEach-Object {
                @{
                    SiteId = $_.Id
                    Name = $_.Name
                    Status = $_.State
                    PhysicalPath = $_.PhysicalPath
                    Bindings = ($_.Bindings.Collection | Where-Object {$_.Protocol -eq 'http'} | ForEach-Object {$_.BindingInformation}) -join ', '
                } | ConvertTo-Json
            }
            '''
            result = subprocess.run(
                ['powershell', '-Command', ps_script],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                sites = []
                for line in result.stdout.strip().split('\n'):
                    if line.strip():
                        sites.append(json.loads(line))
                return sites
        except Exception:
            pass
        return []

    def get_site_details(self, site_id: int) -> Optional[Dict]:
        """Get detailed site information."""
        sites = self.list_iis_sites()
        for site in sites:
            if site['SiteId'] == site_id:
                return site
        return None

    def start_site(self, site_id: int) -> bool:
        """Start an IIS site."""
        try:
            ps_script = f'''
            Import-Module WebAdministration
            Start-Website -Id {site_id}
            '''
            result = subprocess.run(
                ['powershell', '-Command', ps_script],
                capture_output=True,
                text=True
            )
            return result.returncode == 0
        except Exception:
            return False

    def stop_site(self, site_id: int) -> bool:
        """Stop an IIS site."""
        try:
            ps_script = f'''
            Import-Module WebAdministration
            Stop-Website -Id {site_id}
            '''
            result = subprocess.run(
                ['powershell', '-Command', ps_script],
                capture_output=True,
                text=True
            )
            return result.returncode == 0
        except Exception:
            return False

    def parse_connection_string(self, config_path: str, config_type: str) -> List[Dict]:
        """Parse connection string from config file."""
        connections = []
        try:
            if config_type == 'webconfig':
                tree = ET.parse(config_path)
                root = tree.getroot()
                for conn in root.findall(".//connectionStrings/add"):
                    name = conn.get('name', '')
                    conn_str = conn.get('connectionString', '')
                    provider = conn.get('providerName', '')

                    # Extract database name
                    db_match = re.search(r'Initial Catalog=([^;]+)', conn_str)
                    server_match = re.search(r'Data Source=([^;]+)', conn_str)
                    user_match = re.search(r'User ID=([^;]+)|User=([^;]+)', conn_str)

                    connections.append({
                        'name': name,
                        'database': db_match.group(1) if db_match else '',
                        'server': server_match.group(1) if server_match else '',
                        'user': user_match.group(1) or user_match.group(2) if user_match else '',
                        'provider': provider
                    })
            else:
                # appsettings.json
                with open(config_path, 'r') as f:
                    content = f.read()

                # Look for connection strings
                db_match = re.search(r'database=([^;]+)', content)
                if db_match:
                    connections.append({
                        'name': 'appsettings',
                        'database': db_match.group(1),
                        'server': '',
                        'user': '',
                        'provider': ''
                    })
        except Exception as e:
            connections.append({'error': str(e)})

        return connections

    def read_excel_credentials(self, excel_path: str) -> List[Dict]:
        """Read server credentials from Excel."""
        try:
            import pandas as pd
            df = pd.read_excel(excel_path)
            credentials = []
            for _, row in df.iterrows():
                credentials.append({
                    'server': str(row.get('Server', '')),
                    'ip': str(row.get('IP', '')),
                    'password': str(row.get('Password', '')),
                    'username': str(row.get('Username', 'Administrator'))
                })
            return credentials
        except Exception:
            return []

    def launch_rdp(self, ip: str, username: str, password: str):
        """Launch RDP connection."""
        try:
            subprocess.run(['mstsc', '/v', ip], check=True)
        except Exception:
            print(f"Would launch RDP to {ip} as {username}")

    def extract_server_from_url(self, url: str) -> Dict:
        """Extract server information from URL."""
        from urllib.parse import urlparse

        parsed = urlparse(url)
        return {
            'server': parsed.netloc,
            'protocol': parsed.scheme,
            'path': parsed.path,
            'domain': parsed.netloc.split(':')[0] if parsed.netloc else '',
            'port': parsed.port
        }

    def find_all_databases(self, search_path: str) -> List[Dict]:
        """Find all database connections in configuration files."""
        databases = []
        path = Path(search_path)

        for config_file in path.rglob('web.config'):
            connections = self.parse_connection_string(str(config_file), 'webconfig')
            for conn in connections:
                if 'database' in conn and conn['database']:
                    conn['config'] = str(config_file)
                    databases.append(conn)

        for config_file in path.rglob('appsettings.json'):
            connections = self.parse_connection_string(str(config_file), 'appsettings')
            for conn in connections:
                if 'database' in conn and conn['database']:
                    conn['config'] = str(config_file)
                    databases.append(conn)

        return databases

    def print_next_steps(self, action: str, result: Dict):
        """Print interactive next-step suggestions."""
        print("\n" + "=" * 60)
        print("Suggested Next Steps")
        print("=" * 60)

        # Generate context-aware suggestions
        suggestions = self.get_next_steps(action, result)

        for i, suggestion in enumerate(suggestions, 1):
            print(f"\n{i}. {suggestion['title']}")
            print(f"   Command: {suggestion['command']}")

        print("\n" + "-" * 60)
        print("Quick Reference:")
        print("-" * 60)
        self.print_quick_reference(action)

        print("\nEnter a command to continue or ask a question")

    def get_next_steps(self, action: str, result: Dict) -> List[Dict]:
        """Generate context-aware next steps."""
        suggestions = []

        if action == 'list-sites':
            if result.get('sites'):
                suggestions = [
                    {
                        'title': f'Start stopped site (SiteId: {result["sites"][0]["SiteId"]})',
                        'command': f'--action start-site --site-id {result["sites"][0]["SiteId"]}',
                        'description': 'Start the first stopped site'
                    },
                    {
                        'title': f'Get site details (SiteId: {result["sites"][0]["SiteId"]})',
                        'command': f'--action get-site --site-id {result["sites"][0]["SiteId"]}',
                        'description': 'Get detailed information about the first site'
                    }
                ]

        elif action in ['get-site', 'start-site', 'stop-site']:
            if result.get('site'):
                site_id = result['site'].get('SiteId')
                status = result['site'].get('Status', 'Unknown')
                suggestions = [
                    {
                        'title': f'Toggle site status (Current: {status})',
                        'command': f'--action {"stop-site" if status == "Running" else "start-site"} --site-id {site_id}',
                        'description': 'Start or stop this site'
                    },
                    {
                        'title': 'Test site accessibility',
                        'command': f'--action test-url --url "http://localhost:{site_id}"',
                        'description': 'Test if site is accessible'
                    }
                ]
            elif result.get('site_id'):
                suggestions = [
                    {
                        'title': 'Verify site status',
                        'command': f'--action get-site --site-id {result["site_id"]}',
                        'description': 'Confirm the operation was successful'
                    },
                    {
                        'title': 'List all sites',
                        'command': '--action list-sites',
                        'description': 'View complete site list'
                    }
                ]

        elif action == 'parse-config':
            if result.get('connections'):
                conn = result['connections'][0]
                if conn.get('database'):
                    suggestions = [
                        {
                            'title': f'Test database connection: {conn["database"]}',
                            'command': f'--action test-db --server "{conn.get("server", "")}" --database "{conn["database"]}" --user "{conn.get("user", "")}" --db-password "***"',
                            'description': 'Test database connectivity'
                        },
                        {
                            'title': 'Find more databases',
                            'command': '--action find-databases',
                            'description': 'Search all config files for database connections'
                        }
                    ]

        elif action == 'process-url':
            if result.get('server'):
                suggestions = [
                    {
                        'title': 'RDP connect to server',
                        'command': f'--action rdp-connect --ip "SERVER_IP" --username "Administrator"',
                        'description': 'Remote desktop connection to server'
                    },
                    {
                        'title': 'List IIS sites',
                        'command': '--action list-sites',
                        'description': 'View all sites on server'
                    },
                    {
                        'title': f'Test URL accessibility',
                        'command': f'--action test-url --url "{result.get("url", "")}"',
                        'description': 'Test if URL is accessible'
                    }
                ]

        elif action == 'full-scan':
            suggestions = [
                {
                    'title': 'Manage sites',
                    'command': '--action list-sites',
                    'description': 'View and manage discovered sites'
                },
                {
                    'title': 'Connect to server',
                    'command': f'--action rdp-connect --ip "{result.get("ip", "")}"',
                    'description': 'RDP connection to server'
                },
                {
                    'title': 'View database connections',
                    'command': '--action find-databases',
                    'description': 'View all discovered database connections'
                }
            ]

        else:
            # Default suggestions
            suggestions = [
                {
                    'title': 'List IIS sites',
                    'command': '--action list-sites',
                    'description': 'View all websites'
                },
                {
                    'title': 'Process URL',
                    'command': '--action process-url --url "https://example.com"',
                    'description': 'Extract server information'
                },
                {
                    'title': 'Parse config file',
                    'command': '--action parse-config --config "C:\\sites\\web.config"',
                    'description': 'Extract database connection'
                }
            ]

        return suggestions

    def print_quick_reference(self, current_action: str):
        """Print quick reference commands."""
        commands = {
            'list-sites': '--action list-sites --status running',
            'start-site': '--action start-site --site-id 1',
            'stop-site': '--action stop-site --site-id 1',
            'get-site': '--action get-site --site-id 1',
            'parse-config': '--action parse-config --config "path"',
            'remote-connect': '--action remote-connect --excel "file.xlsx"',
            'rdp-connect': '--action rdp-connect --ip "192.168.1.10"',
            'process-url': '--action process-url --url "https://..."',
            'full-scan': '--action full-scan --url "https://..." --excel "file.xlsx"',
            'test-url': '--action test-url --url "https://..."',
            'test-db': '--action test-db --server "." --database "DB_NAME"',
            'find-databases': '--action find-databases',
        }

        # Print relevant commands
        relevant = ['list-sites', 'parse-config', 'process-url']
        if current_action in relevant:
            relevant.append(current_action)

        for cmd in set(relevant):
            if cmd in commands:
                print(f"  * {cmd}: {commands[cmd]}")


def main():
    """Main entry point."""
    manager = InteractiveServerManager()
    manager.run()


if __name__ == '__main__':
    main()
