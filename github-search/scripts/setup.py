#!/usr/bin/env python3
"""Setup script for github-search skill."""

import os
import shutil
import subprocess
import sys
from pathlib import Path


def print_header(text):
    """Print a header line."""
    print(f"\n{'=' * 60}")
    print(f"  {text}")
    print(f"{'=' * 60}\n")


def print_success(text):
    """Print success message."""
    print(f"[OK] {text}")


def print_warning(text):
    """Print warning message."""
    print(f"[WARNING] {text}")


def print_error(text):
    """Print error message."""
    print(f"[ERROR] {text}")


def check_python():
    """Check Python version."""
    print_header("Checking Python installation...")

    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print_error(f"Python 3.8+ required, found {version.major}.{version.minor}.{version.micro}")
        return False

    print_success(f"Python {version.major}.{version.minor}.{version.micro} detected")
    return True


def install_dependencies():
    """Install Python dependencies."""
    print_header("Installing dependencies...")

    requirements_file = Path(__file__).parent.parent / "requirements.txt"
    if not requirements_file.exists():
        print_error("requirements.txt not found")
        return False

    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", str(requirements_file)])
        print_success("Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print_error(f"Failed to install dependencies: {e}")
        return False


def check_github_token():
    """Check if GitHub token is configured."""
    print_header("Checking GitHub token...")

    token = os.getenv("GITHUB_TOKEN")

    if token:
        print_success("GitHub token found in environment variables")
        return True
    else:
        print_warning("GitHub token not found in environment variables")
        print("\nTo avoid strict rate limits (30 requests/hour vs 5000/hour),")
        print("we strongly recommend setting up a GitHub token.\n")

        # Check if .env file exists
        env_file = Path(__file__).parent.parent / ".env"
        if env_file.exists():
            print("Found .env file. Make sure it contains:")
            print("  GITHUB_TOKEN=your_token_here\n")
        else:
            print("You can create a .env file with:")
            print("  GITHUB_TOKEN=your_token_here\n")

        print("To get a token:")
        print("1. Go to https://github.com/settings/tokens")
        print("2. Click 'Generate new token'")
        print("3. Select 'Fine-grained tokens' or 'Classic tokens'")
        print("4. Grant 'public_repo' permission (read-only)")
        print("5. Copy the token and add to .env or environment\n")

        response = input("Continue without token? (y/n): ").strip().lower()
        return response in ["y", "yes"]


def create_command_file():
    """Create Claude Code command file."""
    print_header("Setting up Claude Code command...")

    claude_commands_dir = Path.home() / ".claude" / "commands"
    claude_commands_dir.mkdir(parents=True, exist_ok=True)

    command_file = claude_commands_dir / "github-search.md"

    command_content = """---
description: "Search GitHub repositories and return structured results"
argument-hint: "<query> [--count N] [--sort stars|forks|updated|pushed] [--language LANG]"
allowed-tools:
  - Bash
---

Run the GitHub search script with the user's arguments and present the results.

Execute this:

```
python ~/.claude/skills/github-search/scripts/search.py $ARGUMENTS
```

Present the output directly to the user. If the script reports an error, explain it and suggest fixes.
"""

    try:
        with open(command_file, "w", encoding="utf-8") as f:
            f.write(command_content)
        print_success(f"Command file created: {command_file}")
        return True
    except Exception as e:
        print_error(f"Failed to create command file: {e}")
        return False


def create_config_file():
    """Create config.yaml from example if it doesn't exist."""
    print_header("Setting up configuration...")

    skill_dir = Path(__file__).parent.parent
    config_example = skill_dir / "config.yaml.example"
    config_file = skill_dir / "config.yaml"

    if config_file.exists():
        print_warning("config.yaml already exists, skipping...")
        return True

    if not config_example.exists():
        print_error("config.yaml.example not found")
        return False

    try:
        shutil.copy(config_example, config_file)
        print_success(f"Configuration file created: {config_file}")
        print("\nYou can customize settings in config.yaml")
        return True
    except Exception as e:
        print_error(f"Failed to create config file: {e}")
        return False


def verify_installation():
    """Verify the installation by running a test search."""
    print_header("Verifying installation...")

    script_path = Path(__file__).parent.parent / "scripts" / "search.py"

    try:
        # Run with --help to verify script works
        result = subprocess.run(
            [sys.executable, str(script_path), "--help"],
            capture_output=True,
            text=True,
            timeout=10
        )

        if result.returncode == 0:
            print_success("Installation verified - script is working")
            return True
        else:
            print_error(f"Script verification failed: {result.stderr}")
            return False
    except Exception as e:
        print_error(f"Failed to verify installation: {e}")
        return False


def main():
    """Main setup routine."""
    print_header("GitHub Search Skill Setup")
    print("This script will set up the github-search skill for Claude Code.\n")

    # Check Python
    if not check_python():
        sys.exit(1)

    # Install dependencies
    if not install_dependencies():
        response = input("\nContinue despite dependency installation failure? (y/n): ").strip().lower()
        if response not in ["y", "yes"]:
            sys.exit(1)

    # Check GitHub token
    if not check_github_token():
        sys.exit(1)

    # Create config file
    if not create_config_file():
        print_warning("Config file creation failed, but continuing...")

    # Create command file
    if not create_command_file():
        print_warning("Command file creation failed, but continuing...")

    # Verify installation
    if not verify_installation():
        print_warning("Installation verification failed")

    # Success message
    print_header("Setup Complete!")
    print("""
Usage in Claude Code:
  /github-search "claude code"
  /github-search "machine learning" --language python --count 10
  /github-search "" --org microsoft --sort stars

For more information, see README.md
    """)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nSetup cancelled by user")
        sys.exit(130)
    except Exception as e:
        print_error(f"Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
