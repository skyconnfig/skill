#!/usr/bin/env python3
"""Test script for github-search skill."""

import sys
import time
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent / "scripts"))

from search import (
    parse_args,
    build_search_query,
    SimpleCache,
    format_number,
    format_languages,
    format_datetime,
)


def print_header(text):
    """Print a header line."""
    print(f"\n{'=' * 60}")
    print(f"  {text}")
    print(f"{'=' * 60}\n")


def test_parse_args():
    """Test argument parsing."""
    print("Testing argument parsing...")

    # Test basic query
    args = parse_args(["search.py", "claude code"])
    assert args["query"] == "claude code"
    assert args["count"] is None
    print("  ✓ Basic query parsing")

    # Test with options
    args = parse_args(["search.py", "python", "--count", "10", "--sort", "stars"])
    assert args["query"] == "python"
    assert args["count"] == 10
    assert args["sort"] == "stars"
    print("  ✓ Options parsing")

    # Test with filters
    args = parse_args(["search.py", "react", "--language", "typescript", "--org", "microsoft"])
    assert args["query"] == "react"
    assert args["language"] == "typescript"
    assert args["org"] == "microsoft"
    print("  ✓ Filter parsing")

    # Test output formats
    args = parse_args(["search.py", "test", "--json"])
    assert args["json"] is True
    assert args["output_format"] == "json"

    args = parse_args(["search.py", "test", "--csv"])
    assert args["csv"] is True
    assert args["output_format"] == "csv"
    print("  ✓ Output format parsing")

    print("✓ All argument parsing tests passed\n")


def test_build_search_query():
    """Test query building."""
    print("Testing query building...")

    # Basic query
    q = build_search_query("claude")
    assert q == "claude"
    print("  ✓ Basic query")

    # With language
    q = build_search_query("machine learning", language="python")
    assert "machine learning" in q and "language:python" in q
    print("  ✓ Query with language")

    # Multiple filters
    q = build_search_query("react", language="typescript", topic="ui", org="facebook")
    assert all(x in q for x in ["react", "language:typescript", "topic:ui", "org:facebook"])
    print("  ✓ Query with multiple filters")

    # Quoted query
    q = build_search_query("deep learning")
    assert '"deep learning"' in q
    print("  ✓ Quoted query with spaces")

    print("✓ All query building tests passed\n")


def test_cache():
    """Test cache functionality."""
    print("Testing cache...")

    cache = SimpleCache(ttl=10, max_size=10)

    # Set and get
    cache.set("key1", {"data": "test1"})
    result = cache.get("key1")
    assert result == {"data": "test1"}
    print("  ✓ Cache set/get")

    # Expiration
    time.sleep(11)  # Wait for TTL to expire
    result = cache.get("key1")
    assert result is None
    print("  ✓ Cache expiration")

    # Max size
    cache = SimpleCache(ttl=3600, max_size=3)
    cache.set("a", 1)
    cache.set("b", 2)
    cache.set("c", 3)
    cache.set("d", 4)  # Should evict oldest
    assert cache.get("a") is None  # 'a' should be evicted
    assert cache.get("d") == 4
    print("  ✓ Cache max size")

    print("✓ All cache tests passed\n")


def test_formatting():
    """Test formatting functions."""
    print("Testing formatting functions...")

    # Format numbers
    assert format_number(123) == "123"
    assert format_number(1234) == "1.2K"
    assert format_number(1234567) == "1.2M"
    assert format_number(None) == "N/A"
    print("  ✓ Number formatting")

    # Format languages
    langs = {"Python": 70, "TypeScript": 20, "HTML": 10}
    result = format_languages(langs)
    assert "Python" in result and "TypeScript" in result
    print("  ✓ Language formatting")

    # Format datetime
    result = format_datetime("2025-03-15T10:30:00Z")
    assert "ago" in result or "-" in result
    print("  ✓ Datetime formatting")

    print("✓ All formatting tests passed\n")


def test_integration():
    """Test integration (lightweight)."""
    print("Testing integration...")

    # Test that imports work
    try:
        import requests
        import yaml
        from dotenv import load_dotenv
        print("  ✓ All dependencies available")
    except ImportError as e:
        print(f"  ✗ Missing dependency: {e}")
        print("  Run: pip install -r requirements.txt")
        return False

    # Test config loading (should not fail even without files)
    try:
        from search import load_config
        config = load_config()
        assert "github" in config
        assert "cache" in config
        print("  ✓ Configuration loading")
    except Exception as e:
        print(f"  ✗ Config loading failed: {e}")
        return False

    print("✓ Integration tests passed\n")
    return True


def main():
    """Run all tests."""
    print_header("GitHub Search Skill - Test Suite")
    print("Running tests...\n")

    try:
        test_parse_args()
        test_build_search_query()
        test_cache()
        test_formatting()

        if not test_integration():
            print("Some integration tests failed!")
            return 1

        print_header("All Tests Passed!")
        print("""
Next steps:
1. Run a real search (requires GitHub token):
   python scripts/search.py "claude code" --count 5

2. Check rate limits:
   python -c "import requests; r=requests.get('https://api.github.com/rate_limit', headers={'Authorization': 'token $GITHUB_TOKEN'}); print(r.json())"

3. Review config.yaml to customize behavior
        """)
        return 0

    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return 1
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
