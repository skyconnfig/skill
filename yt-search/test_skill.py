#!/usr/bin/env python3
"""Test script for yt-search skill functionality."""

import subprocess
import sys

def test_search():
    """Test basic search functionality."""
    print("Testing yt-search skill...")
    print("=" * 60)

    # Test 1: Basic search without date filter
    print("\nTest 1: Basic search (no date filter)")
    result = subprocess.run(
        [sys.executable, "scripts/search.py", "artificial intelligence", "--count", "3"],
        capture_output=True,
        text=True,
        timeout=120,
        encoding='utf-8'
    )

    if result.returncode == 0:
        print("PASS: Test 1")
        print(result.stdout[:500])  # Show first 500 chars
    else:
        print("FAIL: Test 1")
        print("STDERR:", result.stderr)
        return False

    # Test 2: Search with date filter
    print("\nTest 2: Search with date filter (last 3 months)")
    result = subprocess.run(
        [sys.executable, "scripts/search.py", "machine learning", "--count", "3", "--months", "3"],
        capture_output=True,
        text=True,
        timeout=120,
        encoding='utf-8'
    )

    if result.returncode == 0:
        print("PASS: Test 2")
    else:
        print("FAIL: Test 2")
        print("STDERR:", result.stderr)
        return False

    print("\n" + "=" * 60)
    print("All tests passed!")
    return True

if __name__ == "__main__":
    success = test_search()
    sys.exit(0 if success else 1)
