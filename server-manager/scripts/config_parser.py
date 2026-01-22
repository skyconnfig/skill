#!/usr/bin/env python3
"""
Configuration File Parser
Extracts database connection strings from web.config and appsettings.json files.
"""

import argparse
import re
import sys
from pathlib import Path
from typing import dict, list


def parse_connection_string(conn_str: str) -> dict:
    """
    Parse connection string and extract components.
    
    Supports multiple formats:
    - SQL Server: Data Source=.;Initial Catalog=DB;User=user;Password=pass
    - MySQL: server=localhost;database=test;user=root;password=pass
    - Generic: key=value;key=value
    
    Args:
        conn_str: Connection string to parse
    
    Returns:
        Dictionary with parsed components
    """
    result = {
        'raw': conn_str,
        'database': None,
        'server': None,
        'user': None,
        'password': None,
        'provider': None,
        'extra': {}
    }
    
    # Split by semicolon
    parts = [p.strip() for p in conn_str.split(';') if p.strip()]
    
    for part in parts:
        # Skip empty parts
        if '=' not in part:
            continue
        
        key, value = part.split('=', 1)
        key = key.strip().lower()
        value = value.strip()
        
        # Map common keys
        key_mapping = {
            'data source': 'server',
            'data source': 'server',
            'server': 'server',
            'initial catalog': 'database',
            'database': 'database',
            'user': 'user',
            'user id': 'user',
            'uid': 'user',
            'password': 'password',
            'pwd': 'password',
            'provider': 'provider',
            'provider name': 'provider',
            'min pool size': 'min_pool_size',
            'max pool size': 'max_pool_size',
            'connect timeout': 'connection_timeout',
            'connection timeout': 'connection_timeout',
            'integrated security': 'integrated_security',
            'trusted connection': 'trusted_connection'
        }
        
        mapped_key = key_mapping.get(key, key)
        
        if mapped_key in ['server', 'database', 'user', 'password', 'provider']:
            result[mapped_key] = value
        else:
            result['extra'][mapped_key] = value
    
    return result


def parse_web_config(file_path: str) -> list[dict]:
    """
    Parse web.config file for connection strings.
    
    Args:
        file_path: Path to web.config file
    
    Returns:
        List of connection string dictionaries
    """
    try:
        from lxml import etree
    except ImportError:
        print("Error: lxml not installed. Run: pip install lxml")
        sys.exit(1)
    
    connections = []
    
    try:
        tree = etree.parse(file_path)
        root = tree.getroot()
        
        # Handle configuration/connectionStrings/add elements
        conn_strings = root.xpath('//configuration/connectionStrings/add')
        
        for conn in conn_strings:
            name = conn.get('name', '')
            conn_str = conn.get('connectionString', '')
            provider = conn.get('providerName', '')
            
            if conn_str:
                parsed = parse_connection_string(conn_str)
                parsed['name'] = name
                parsed['provider'] = provider
                parsed['source'] = 'web.config'
                connections.append(parsed)
        
        # Also check for appSettings (may contain connection strings)
        app_settings = root.xpath('//configuration/appSettings/add')
        for setting in app_settings:
            key = setting.get('key', '').lower()
            value = setting.get('value', '')
            
            if 'connection' in key or 'db' in key:
                parsed = parse_connection_string(value)
                parsed['name'] = key
                parsed['source'] = 'web.config'
                connections.append(parsed)
        
        return connections
        
    except etree.XMLSyntaxError as e:
        print(f"Error parsing web.config: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading web.config: {e}")
        sys.exit(1)


def parse_appsettings_json(file_path: str) -> list[dict]:
    """
    Parse appsettings.json file for connection strings.
    
    Args:
        file_path: Path to appsettings.json file
    
    Returns:
        List of connection string dictionaries
    """
    import json
    
    connections = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        # Common patterns for connection strings in appsettings.json
        
        # Pattern 1: "ConnectionStrings": { "Default": "..." }
        if 'ConnectionStrings' in config:
            conn_section = config['ConnectionStrings']
            for key, value in conn_section.items():
                if isinstance(value, str) and ('=' in value or 'server' in value.lower() or 'database' in value.lower()):
                    parsed = parse_connection_string(value)
                    parsed['name'] = key
                    parsed['source'] = 'appsettings.json'
                    connections.append(parsed)
        
        # Pattern 2: Look for database-related keys in any section
        def search_nested(obj, path=""):
            """Recursively search for connection strings."""
            if isinstance(obj, dict):
                for key, value in obj.items():
                    search_nested(value, f"{path}.{key}" if path else key)
            elif isinstance(obj, list):
                for i, item in enumerate(obj):
                    search_nested(item, f"{path}[{i}]")
            elif isinstance(obj, str):
                # Check if string looks like a connection string
                if ('=' in obj and ('server' in obj.lower() or 
                    'database' in obj.lower() or 
                    'connection' in obj.lower())):
                    # Extract key name from path
                    key_name = path.split('.')[-1] if path else 'Unknown'
                    
                    parsed = parse_connection_string(obj)
                    parsed['name'] = key_name
                    parsed['source'] = 'appsettings.json'
                    
                    # Avoid duplicates
                    if not any(c['raw'] == parsed['raw'] for c in connections):
                        connections.append(parsed)
        
        search_nested(config)
        
        return connections
        
    except json.JSONDecodeError as e:
        print(f"Error parsing appsettings.json: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading appsettings.json: {e}")
        sys.exit(1)


def format_connection_output(conn: dict, detailed: bool = False):
    """Format connection string for display."""
    lines = []
    
    if conn.get('name'):
        lines.append(f"  Name: {conn['name']}")
    
    lines.append(f"  Database: {conn.get('database', 'N/A')}")
    lines.append(f"  Server: {conn.get('server', 'N/A')}")
    
    if conn.get('user'):
        lines.append(f"  User: {conn.get('user')}")
    
    if conn.get('provider'):
        lines.append(f"  Provider: {conn.get('provider')}")
    
    # Show extra info if requested
    if detailed and conn.get('extra'):
        lines.append("  Additional Settings:")
        for key, value in conn['extra'].items():
            lines.append(f"    {key}: {value}")
    
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(
        description='Parse connection strings from web.config and appsettings.json files.'
    )
    parser.add_argument(
        'config_path',
        help='Path to configuration file (web.config or appsettings.json)'
    )
    parser.add_argument(
        '--type',
        choices=['auto', 'webconfig', 'appsettings'],
        default='auto',
        help='Configuration file type (default: auto-detect)'
    )
    parser.add_argument(
        '--format',
        choices=['simple', 'detailed', 'json'],
        default='simple',
        help='Output format (default: simple)'
    )
    parser.add_argument(
        '--output',
        help='Output file path for results'
    )
    
    args = parser.parse_args()
    
    # Validate file exists
    if not Path(args.config_path).exists():
        print(f"Error: File not found: {args.config_path}")
        sys.exit(1)
    
    # Determine file type
    file_type = args.type
    if file_type == 'auto':
        ext = Path(args.config_path).suffix.lower()
        if ext == '.json':
            file_type = 'appsettings'
        else:
            file_type = 'webconfig'
    
    # Parse configuration
    if file_type == 'webconfig':
        connections = parse_web_config(args.config_path)
    elif file_type == 'appsettings':
        connections = parse_appsettings_json(args.config_path)
    
    # Output results
    if args.format == 'json':
        import json
        output = json.dumps(connections, indent=2)
    else:
        lines = [f"\nConnection Strings Found: {len(connections)}"]
        lines.append("=" * 60)
        
        for i, conn in enumerate(connections, 1):
            lines.append(f"\n{i}. Connection String:")
            if args.format == 'detailed':
                lines.append(format_connection_output(conn, detailed=True))
            else:
                lines.append(format_connection_output(conn))
        
        output = '\n'.join(lines)
    
    # Display or save output
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output)
        print(f"Results saved to: {args.output}")
    else:
        print(output)
    
    # Return exit code based on findings
    if not connections:
        sys.exit(1)  # No connections found
    sys.exit(0)


if __name__ == '__main__':
    main()
