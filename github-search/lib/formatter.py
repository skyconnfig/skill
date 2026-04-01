"""Output formatters for GitHub search results."""

import json
import csv
import sys
from datetime import datetime
from typing import Dict, Any, List, Optional


def format_number(n: Optional[int]) -> str:
    """Format large numbers with K/M suffixes."""
    if n is None:
        return "N/A"
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n / 1_000:.1f}K"
    return str(n)


def format_languages(languages_data: Dict[str, int]) -> str:
    """Format language distribution as percentage string."""
    if not languages_data:
        return "N/A"

    total = sum(languages_data.values())
    if total == 0:
        return "N/A"

    # Sort by percentage descending
    sorted_langs = sorted(languages_data.items(), key=lambda x: x[1], reverse=True)

    # Calculate percentages and show top 3
    lang_strings = []
    for lang, bytes_count in sorted_langs[:3]:
        percent = (bytes_count / total) * 100
        lang_strings.append(f"{lang} ({percent:.0f}%)")

    result = " + ".join(lang_strings)
    if len(sorted_langs) > 3:
        result += " + others"
    return result


def format_datetime(dt_str: str) -> str:
    """Format datetime to relative or absolute."""
    if not dt_str:
        return "N/A"

    try:
        dt = datetime.strptime(dt_str, "%Y-%m-%dT%H:%M:%SZ")
        now = datetime.utcnow()
        diff = now - dt

        if diff.days == 0:
            hours = diff.seconds // 3600
            if hours == 0:
                minutes = diff.seconds // 60
                return f"{minutes}m ago"
            return f"{hours}h ago"
        elif diff.days < 7:
            return f"{diff.days}d ago"
        else:
            return dt.strftime("%Y-%m-%d")
    except Exception:
        return dt_str[:10]


def format_pretty(results: Dict[str, Any], include_languages: bool = True) -> None:
    """Format results for pretty console output."""
    if not results or "items" not in results:
        print("No results found.")
        return

    items = results["items"]
    total_count = results.get("total_count", len(items))
    divider = "─" * 80

    print(f"\nFound {total_count:,} repositories (showing {len(items)}):\n")

    for i, repo in enumerate(items, 1):
        full_name = repo.get("full_name", "Unknown")
        description = repo.get("description") or "No description"
        stars = repo.get("stargazers_count", 0)
        forks = repo.get("forks_count", 0)
        language = repo.get("language", "Unknown")
        updated = repo.get("updated_at", "")
        issues = repo.get("open_issues_count", 0)
        size = repo.get("size", 0)

        # Fetch languages if needed
        if include_languages and repo.get("languages_url"):
            from search import SimpleCache
            cache = SimpleCache()
            lang_key = f"lang:{repo['full_name']}"
            languages = cache.get(lang_key)
            if languages is None:
                import requests
                from search import get_github_headers, load_config
                config = load_config()
                try:
                    lang_resp = requests.get(
                        repo["languages_url"],
                        headers=get_github_headers(config),
                        timeout=10
                    )
                    if lang_resp.status_code == 200:
                        languages = lang_resp.json()
                        cache.set(lang_key, languages)
                except Exception:
                    languages = None

            if languages:
                language = format_languages(languages)

        # Format info
        stars_str = format_number(stars)
        forks_str = format_number(forks)
        size_str = f"{size/1024:.1f} MB" if size else "N/A"
        updated_str = format_datetime(updated)

        # Truncate description
        if len(description) > 200:
            description = description[:197] + "..."

        print(divider)
        print(f" {i:>2}. {full_name}")
        print(f"     ⭐ {stars_str}  ·  🍴 {forks_str}  ·  {language}")
        print(f"     {description}")
        print(f"     Issues: {issues}  ·  Size: {size_str}")
        print(f"     Updated: {updated_str}")
        print(f"     URL: {repo.get('html_url', 'N/A')}")

    print(divider)


def format_json(results: Dict[str, Any]) -> None:
    """Format results as JSON."""
    print(json.dumps(results, indent=2, ensure_ascii=False))


def format_csv(results: Dict[str, Any]) -> None:
    """Format results as CSV."""
    import csv

    if not results or "items" not in results:
        return

    items = results["items"]
    if not items:
        return

    headers = [
        "full_name", "description", "language", "stargazers_count",
        "forks_count", "open_issues_count", "html_url", "updated_at", "size"
    ]

    writer = csv.writer(sys.stdout)
    writer.writerow(headers)

    for repo in items:
        row = [repo.get(header, "") for header in headers]
        writer.writerow(row)


def format_markdown(results: Dict[str, Any]) -> None:
    """Format results as Markdown."""
    if not results or "items" not in results:
        return

    items = results["items"]
    total_count = results.get("total_count", len(items))

    print(f"# GitHub Search Results\n")
    print(f"**Query:** {results.get('query', 'Unknown')}  ")
    print(f"**Total:** {total_count:,} repositories  ")
    print(f"**Showing:** {len(items)} results\n")

    for i, repo in enumerate(items, 1):
        full_name = repo.get("full_name", "Unknown")
        description = repo.get("description") or "No description"
        stars = repo.get("stargazers_count", 0)
        forks = repo.get("forks_count", 0)
        language = repo.get("language", "Unknown")
        html_url = repo.get("html_url", "#")

        print(f"## {i}. [{full_name}]({html_url})\n")
        print(f"**⭐ {stars:,}** · **🍴 {forks:,}** · **{language}**")
        print(f"\n{description}\n")

        topics = repo.get("topics", [])
        if topics:
            print(f"*Topics: {', '.join(topics)}*")

        print("\n---\n")
