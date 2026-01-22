#!/usr/bin/env python3
"""
Excel Reader for Server Credentials
Reads server IP addresses and passwords from Excel files.
"""

import argparse
import sys
from pathlib import Path

try:
    import pandas as pd
except ImportError:
    print("Error: pandas not installed. Run: pip install pandas openpyxl")
    sys.exit(1)


def read_server_credentials(excel_path: str) -> list[dict]:
    """
    Read server credentials from Excel file.
    
    Args:
        excel_path: Path to Excel file (.xlsx or .xlsm)
    
    Returns:
        List of dictionaries containing server information
    """
    try:
        # Read Excel file
        df = pd.read_excel(excel_path)
        
        # Normalize column names (remove spaces, lowercase)
        df.columns = df.columns.str.strip().str.lower()
        
        # Map common column names
        column_mapping = {
            'server': 'server',
            'server name': 'server',
            'name': 'server',
            'ip': 'ip',
            'ip address': 'ip',
            'address': 'ip',
            'password': 'password',
            'pwd': 'password',
            'pass': 'password',
            'username': 'username',
            'user': 'username',
            'name': 'username'
        }
        
        # Rename columns based on mapping
        new_columns = {}
        for col in df.columns:
            col_lower = col.lower()
            if col_lower in column_mapping:
                new_columns[col] = column_mapping[col_lower]
        
        df = df.rename(columns=new_columns)
        
        # Validate required columns
        required_columns = ['ip', 'password']
        missing_columns = [col for col in required_columns if col not in df.columns]
        
        if missing_columns:
            print(f"Error: Missing required columns: {missing_columns}")
            print(f"Available columns: {list(df.columns)}")
            sys.exit(1)
        
        # Fill missing username with default
        if 'username' not in df.columns:
            df['username'] = 'Administrator'
        
        # Convert to list of dictionaries
        servers = df.to_dict('records')
        
        # Clean data
        for server in servers:
            server['ip'] = str(server['ip']).strip()
            server['password'] = str(server['password']).strip()
            server['username'] = str(server.get('username', 'Administrator')).strip()
            server['server'] = str(server.get('server', server['ip'])).strip()
        
        return servers
        
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        sys.exit(1)


def display_servers(servers: list[dict]):
    """Display server information in a formatted table."""
    if not servers:
        print("No servers found in Excel file.")
        return
    
    print(f"\n{'Server':<20} {'IP':<15} {'Username':<15}")
    print("-" * 50)
    
    for server in servers:
        print(f"{server['server']:<20} {server['ip']:<15} {server['username']:<15}")
    
    print(f"\nTotal servers: {len(servers)}")


def find_server_by_ip(servers: list[dict], ip: str) -> dict | None:
    """Find server by IP address."""
    for server in servers:
        if server['ip'] == ip:
            return server
    return None


def main():
    parser = argparse.ArgumentParser(
        description='Read server credentials from Excel files.'
    )
    parser.add_argument(
        'excel_path',
        help='Path to Excel file (.xlsx or .xlsm)'
    )
    parser.add_argument(
        '--ip',
        help='Find specific server by IP address'
    )
    parser.add_argument(
        '--format',
        choices=['table', 'json', 'csv'],
        default='table',
        help='Output format (default: table)'
    )
    
    args = parser.parse_args()
    
    # Validate file exists
    if not Path(args.excel_path).exists():
        print(f"Error: File not found: {args.excel_path}")
        sys.exit(1)
    
    # Read servers
    servers = read_server_credentials(args.excel_path)
    
    if args.ip:
        server = find_server_by_ip(servers, args.ip)
        if server:
            if args.format == 'json':
                import json
                print(json.dumps(server, indent=2))
            else:
                print(f"\nServer found:")
                print(f"  Server: {server['server']}")
                print(f"  IP: {server['ip']}")
                print(f"  Username: {server['username']}")
                print(f"  Password: {'*' * len(server['password'])}")
        else:
            print(f"Server with IP {args.ip} not found.")
        return
    
    # Display all servers
    if args.format == 'json':
        import json
        print(json.dumps(servers, indent=2))
    elif args.format == 'csv':
        import csv
        import sys as sys_module
        writer = csv.DictWriter(sys_module.stdout, fieldnames=servers[0].keys())
        writer.writeheader()
        writer.writerows(servers)
    else:
        display_servers(servers)


if __name__ == '__main__':
    main()
