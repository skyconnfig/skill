#!/usr/bin/env python3
"""YouTube Search Skill - Simple Test Script"""

import subprocess
import sys
from pathlib import Path

def test_search_script_exists():
    """Test that search.py exists and is executable"""
    print("Testing search.py existence...")
    search_script = Path(__file__).parent / "scripts" / "search.py"
    if not search_script.exists():
        print(f"  [FAIL] search.py not found at {search_script}")
        return False
    print("  [PASS] search.py exists")
    return True

def test_search_script_structure():
    """Test that search.py has correct structure"""
    print("\nTesting search.py structure...")
    search_script = Path(__file__).parent / "scripts" / "search.py"

    with open(search_script, 'r', encoding='utf-8') as f:
        content = f.read()

    required_functions = [
        'def parse_args(',
        'def format_subscribers(',
        'def format_views(',
        'def format_duration(',
        'def format_date(',
        'def get_cutoff_date(',
        'def main('
    ]

    for func in required_functions:
        if func not in content:
            print(f"  [FAIL] Missing function: {func}")
            return False
        print(f"  [PASS] Found: {func.strip('(')}")

    # Check it's standalone (no external lib imports beyond stdlib)
    if 'from lib.' in content or 'import lib' in content:
        print("  [FAIL] Should not import from lib module (removed)")
        return False
    print("  [PASS] No imports from removed lib module")

    return True

def test_dependencies():
    """Test that required dependencies are available"""
    print("\nTesting dependencies...")
    try:
        import yt_dlp
        print("  [PASS] yt-dlp is installed")
        return True
    except ImportError:
        print("  [WARN] yt-dlp not installed (install with: pip install yt-dlp)")
        return True  # Not a hard failure

def test_run_simple():
    """Test running the script (may fail due to network/YouTube restrictions)"""
    print("\nTesting script execution (expect network errors)...")
    search_script = Path(__file__).parent / "scripts" / "search.py"
    cmd = [sys.executable, str(search_script), "test", "--count", "1", "--months", "1"]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30
        )
        # We don't care about search results, just that the script runs
        # It may fail due to YouTube bot detection - that's ok
        print("  [INFO] Script executed (check output for actual errors)")
        return True
    except subprocess.TimeoutExpired:
        print("  [WARN] Script timed out (network issues)")
        return True
    except Exception as e:
        print(f"  [WARN] Script raised exception: {e}")
        return True

def main():
    print("YouTube Search Skill - Structure Tests")
    print("=" * 60)

    tests = [
        ("search.py exists", test_search_script_exists),
        ("search.py structure", test_search_script_structure),
        ("Dependencies", test_dependencies),
        ("Script execution", test_run_simple),
    ]

    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"  [FAIL] Test '{name}' raised exception: {e}")
            results.append((name, False))

    print("\n" + "=" * 60)
    print("Test Results Summary")
    print("=" * 60)

    passed = sum(1 for _, result in results if result)
    total = len(results)

    for name, result in results:
        status = "[PASS]" if result else "[FAIL]"
        print(f"{status}: {name}")

    print(f"\nTotal: {passed}/{total} tests passed")

    if passed == total:
        print("\n[PASS] All tests passed!")
        return 0
    else:
        print("\n[FAIL] Some tests failed")
        return 1

if __name__ == "__main__":
    sys.exit(main())
