#!/usr/bin/env python3
"""
Remote Desktop Connection Launcher
Launches MSTSC connections using provided credentials.
"""

import argparse
import subprocess
import sys
from pathlib import Path


def launch_mstsc(ip: str, username: str = None, password: str = None, 
                 full_screen: bool = False, width: int = None, height: int = None):
    """
    Launch MSTSC (Remote Desktop) connection.
    
    Args:
        ip: Server IP address or hostname
        username: RDP username (optional, will prompt if not provided)
        password: RDP password (optional, will prompt if not provided)
        full_screen: Launch in full screen mode
        width: Screen width
        height: Screen height
    """
    # Build mstsc command
    cmd = ['mstsc', '/v:' + ip]
    
    if full_screen:
        cmd.append('/f')
    
    if width and height:
        cmd.append(f'/w:{width}')
        cmd.append(f'/h:{height}')
    
    # Note: Direct password passing to mstsc is not secure and has limitations
    # We'll use the /prompt option for secure credential entry
    
    if username and not password:
        # Prompt for password only
        print(f"\nConnecting to {ip} as {username}...")
        print("Password prompt will appear...")
        cmd.append('/prompt')
    
    elif username and password:
        # Both provided - use /public mode which doesn't cache credentials
        # This is a security-conscious approach
        print(f"\nConnecting to {ip} as {username}...")
        print("Note: You may need to re-enter password in the RDP session.")
        cmd.append('/public')
    
    else:
        # No credentials - will prompt for both
        print(f"\nConnecting to {ip}...")
        print("Credential prompt will appear...")
    
    # Execute command
    try:
        subprocess.Popen(cmd)
        print(f"Remote Desktop connection initiated to {ip}")
        print("MSTSC window should be opening...")
        return True
    except Exception as e:
        print(f"Error launching Remote Desktop: {e}")
        return False


def create_rdp_file(ip: str, username: str, password: str, 
                    output_path: str = None, full_screen: bool = True,
                    width: int = 1920, height: int = 1080) -> str:
    """
    Create an RDP file with embedded credentials.
    
    Note: This creates a file with credentials - use with caution and delete after use.
    
    Args:
        ip: Server IP address
        username: RDP username
        password: RDP password
        output_path: Path for RDP file (auto-generated if not provided)
        full_screen: Use full screen mode
        width: Screen width
        height: Screen height
    
    Returns:
        Path to created RDP file
    """
    # Auto-generate filename if not provided
    if not output_path:
        output_path = f"server_{ip.replace('.', '_')}.rdp"
    
    rdp_content = f"""screen mode id:i:{2 if full_screen else 1}
desktopwidth:i:{width}
desktopheight:i:{height}
session bpp:i:32
winposstr:s:0,3,0,0,800,600
compression:i:1
keyboardhook:i:2
displayconnectionbar:i:1
disable wallpaper:i:1
allow font smoothing:i:0
allow desktop composition:i:0
full address:s:{ip}
username:s:{username}
password 51:b:{generate_rdp_password(password)}
preference level:i:3
proxy mode:i:0
http proxy:i:0
https proxy:i:0
"""
    # Write RDP file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(rdp_content)
    
    return output_path


def generate_rdp_password(password: str) -> str:
    """
    Generate base64-encoded password for RDP file.
    
    This is a simplified version - real implementation requires proper encryption.
    """
    import base64
    return base64.b64encode(password.encode()).decode()


def batch_connect_from_excel(excel_path: str, ip_column: str = 'IP', 
                             password_column: str = 'Password',
                             username_column: str = 'Username') -> bool:
    """
    Launch MSTSC connections for all servers in Excel file.
    
    Args:
        excel_path: Path to Excel file
        ip_column: Column name containing IP addresses
        password_column: Column name containing passwords
        username_column: Column name containing usernames
    
    Returns:
        True if all connections launched successfully
    """
    try:
        import pandas as pd
    except ImportError:
        print("Error: pandas not installed. Run: pip install pandas openpyxl")
        sys.exit(1)
    
    try:
        df = pd.read_excel(excel_path)
        
        # Normalize column names
        df.columns = df.columns.str.strip().str.lower()
        
        # Find columns
        ip_col = None
        pwd_col = None
        user_col = None
        
        for col in df.columns:
            if ip_column.lower() in col:
                ip_col = col
            elif password_column.lower() in col:
                pwd_col = col
            elif username_column.lower() in col:
                user_col = col
        
        if not ip_col or not pwd_col:
            print(f"Error: Could not find required columns (IP: {ip_column}, Password: {password_column})")
            sys.exit(1)
        
        # Use default username if not found
        if not user_col:
            user_col = 'administrator'
            default_username = 'Administrator'
        else:
            default_username = None
        
        success_count = 0
        
        print(f"\nServers found: {len(df)}")
        print("=" * 60)
        
        for idx, row in df.iterrows():
            ip = str(row[ip_col]).strip()
            password = str(row[pwd_col]).strip()
            username = str(row.get(user_col, default_username)).strip() if default_username else str(row[user_col]).strip()
            
            if ip and ip != 'nan' and password and password != 'nan':
                print(f"\n{idx + 1}. Connecting to {ip}...")
                if launch_mstsc(ip, username, password):
                    success_count += 1
        
        print(f"\n" + "=" * 60)
        print(f"Successfully initiated {success_count}/{len(df)} connections")
        
        return success_count > 0
        
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description='Launch Remote Desktop connections to Windows servers.'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Connect command
    connect_parser = subparsers.add_parser('connect', help='Connect to a single server')
    connect_parser.add_argument(
        'ip',
        help='Server IP address or hostname'
    )
    connect_parser.add_argument(
        '--username', '-u',
        default='Administrator',
        help='RDP username (default: Administrator)'
    )
    connect_parser.add_argument(
        '--password', '-p',
        help='RDP password'
    )
    connect_parser.add_argument(
        '--fullscreen', '-f',
        action='store_true',
        help='Launch in full screen mode'
    )
    connect_parser.add_argument(
        '--width',
        type=int,
        default=1920,
        help='Screen width (default: 1920)'
    )
    connect_parser.add_argument(
        '--height',
        type=int,
        default=1080,
        help='Screen height (default: 1080)'
    )
    
    # batch command
    batch_parser = subparsers.add_parser('batch', help='Connect to multiple servers from Excel')
    batch_parser.add_argument(
        'excel_path',
        help='Path to Excel file with server credentials'
    )
    batch_parser.add_argument(
        '--ip-column',
        default='IP',
        help='Column name for IP addresses (default: IP)'
    )
    batch_parser.add_argument(
        '--password-column',
        default='Password',
        help='Column name for passwords (default: Password)'
    )
    batch_parser.add_argument(
        '--username-column',
        default='Username',
        help='Column name for usernames (default: Username)'
    )
    
    # create-rdp command
    rdp_parser = subparsers.add_parser('create-rdp', help='Create RDP file')
    rdp_parser.add_argument(
        'ip',
        help='Server IP address or hostname'
    )
    rdp_parser.add_argument(
        'username',
        help='RDP username'
    )
    rdp_parser.add_argument(
        'password',
        help='RDP password'
    )
    rdp_parser.add_argument(
        '--output', '-o',
        help='Output RDP file path'
    )
    rdp_parser.add_argument(
        '--fullscreen',
        action='store_true',
        help='Use full screen mode'
    )
    
    args = parser.parse_args()
    
    if args.command == 'connect':
        launch_mstsc(
            args.ip,
            args.username,
            args.password,
            args.fullscreen,
            args.width,
            args.height
        )
    
    elif args.command == 'batch':
        batch_connect_from_excel(
            args.excel_path,
            args.ip_column,
            args.password_column,
            args.username_column
        )
    
    elif args.command == 'create-rdp':
        output_path = create_rdp_file(
            args.ip,
            args.username,
            args.password,
            args.output,
            args.fullscreen
        )
        print(f"RDP file created: {output_path}")
        print(f"Launch with: mstsc {output_path}")
    
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
