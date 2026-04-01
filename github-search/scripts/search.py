#!/usr/bin/env python3
"""GitHub repository search via GitHub Search API with structured output."""

import io
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path

# Force UTF-8 output on Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

try:
    import requests
    import yaml
    from dotenv import load_dotenv
except ImportError as e:
    print(f"Error: Missing dependency - {e}", file=sys.stderr)
    print("Install with: pip install requests pyyaml python-dotenv", file=sys.stderr)
    sys.exit(1)

# Load environment variables
env_path = Path(__file__).parent.parent / ".env"
if env_path.exists():
    load_dotenv(env_path)


def load_config():
    """Load configuration from config.yaml or use defaults."""
    config_path = Path(__file__).parent.parent / "config.yaml"
    config = {
        "github": {
            "token": os.getenv("GITHUB_TOKEN"),
            "per_page": 100,
            "max_pages": 5,
            "default_sort": "stars",
            "default_order": "desc",
            "timeout": 30,
            "retry_attempts": 3,
            "retry_delay": 2,
        },
        "cache": {
            "enabled": True,
            "ttl": 1800,
            "max_size": 1000,
            "backend": "memory",
        },
        "rate_limit": {
            "requests_per_minute": 30,
            "warn_at_usage": 0.8,
            "auto_wait": True,
        },
        "output": {
            "format": "pretty",
            "include_languages": True,
            "include_topics": True,
            "include_license": True,
            "show_owner_avatar": False,
            "truncate_description": 200,
        },
        "search": {
            "default_page_size": 20,
            "max_page_size": 100,
            "exclude_forks": False,
            "exclude_archived": False,
        },
    }

    if config_path.exists():
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                user_config = yaml.safe_load(f)
                # Deep merge
                for key, value in user_config.items():
                    if key in config and isinstance(config[key], dict):
                        config[key].update(value)
                    else:
                        config[key] = value
        except Exception as e:
            print(f"Warning: Failed to load config.yaml: {e}", file=sys.stderr)

    return config


class SimpleCache:
    """Simple in-memory cache with TTL."""

    def __init__(self, ttl=1800, max_size=1000):
        self.cache = {}
        self.ttl = ttl
        self.max_size = max_size

    def get(self, key):
        if key in self.cache:
            value, timestamp = self.cache[key]
            if time.time() - timestamp < self.ttl:
                return value
            else:
                del self.cache[key]
        return None

    def set(self, key, value):
        if len(self.cache) >= self.max_size:
            # Remove oldest entry
            oldest = min(self.cache.items(), key=lambda x: x[1][1])[0]
            del self.cache[oldest]
        self.cache[key] = (value, time.time())


def get_github_headers(config):
    """Build GitHub API request headers."""
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "github-search-skill/1.0.0",
    }
    token = config["github"]["token"]
    if token:
        headers["Authorization"] = f"token {token}"
    return headers


def check_rate_limit(config):
    """Check GitHub API rate limit status."""
    headers = get_github_headers(config)
    try:
        response = requests.get(
            "https://api.github.com/rate_limit", headers=headers, timeout=config["github"]["timeout"]
        )
        response.raise_for_status()
        data = response.json()
        core = data["resources"]["core"]
        return {
            "limit": core["limit"],
            "remaining": core["remaining"],
            "reset": core["reset"],
            "reset_datetime": datetime.fromtimestamp(core["reset"]).strftime("%Y-%m-%d %H:%M:%S"),
        }
    except Exception as e:
        return {"error": str(e)}


def wait_for_rate_limit(config, remaining, reset_time):
    """Wait for rate limit to reset if needed."""
    if remaining <= 0 and reset_time:
        wait_seconds = max(0, reset_time - time.time())
        if wait_seconds > 0:
            print(f"Rate limit reached. Waiting {wait_seconds:.0f} seconds...", file=sys.stderr)
            time.sleep(wait_seconds + 1)
            return True
    return False


def build_search_query(query, language=None, topic=None, license_name=None, org=None, user=None):
    """Build GitHub search query string."""
    parts = []

    # Main query (quote if contains spaces)
    if query:
        if " " in query:
            parts.append(f'"{query}"')
        else:
            parts.append(query)

    # Filters
    if language:
        parts.append(f"language:{language}")
    if topic:
        parts.append(f"topic:{topic}")
    if license_name:
        parts.append(f"license:{license_name}")
    if org:
        parts.append(f"org:{org}")
    if user:
        parts.append(f"user:{user}")

    return " ".join(parts)


def search_repositories(query, config, page=1, per_page=None, cache=None):
    """Search GitHub repositories via Search API."""
    if per_page is None:
        per_page = config["search"]["default_page_size"]

    # Build cache key
    cache_key = f"search:{query}:page{page}:per_page{per_page}" if cache else None
    if cache and config["cache"]["enabled"]:
        cached = cache.get(cache_key)
        if cached:
            return cached

    # Build request
    headers = get_github_headers(config)
    sort = config["github"]["default_sort"]
    order = config["github"]["default_order"]

    params = {
        "q": query,
        "per_page": min(per_page, config["search"]["max_page_size"]),
        "page": page,
        "sort": sort,
        "order": order,
    }

    # Make request with retry
    url = "https://api.github.com/search/repositories"
    for attempt in range(config["github"]["retry_attempts"]):
        try:
            response = requests.get(url, headers=headers, params=params, timeout=config["github"]["timeout"])

            if response.status_code == 403:
                # Rate limit or abuse detection
                reset_time = int(response.headers.get("X-RateLimit-Reset", 0))
                remaining = int(response.headers.get("X-RateLimit-Remaining", 0))
                if remaining <= 0 and config["rate_limit"]["auto_wait"]:
                    wait_for_rate_limit(config, remaining, reset_time)
                    continue
                else:
                    response.raise_for_status()
            elif response.status_code == 422:
                print(f"Error: Invalid query - {response.json().get('message', 'Unknown error')}", file=sys.stderr)
                return None

            response.raise_for_status()
            data = response.json()

            # Cache result
            if cache and config["cache"]["enabled"]:
                cache.set(cache_key, data)

            return data

        except requests.exceptions.RequestException as e:
            if attempt < config["github"]["retry_attempts"] - 1:
                delay = config["github"]["retry_delay"] * (2**attempt)
                print(f"Request failed, retrying in {delay}s... ({attempt+1}/{config['github']['retry_attempts']})",
                      file=sys.stderr)
                time.sleep(delay)
            else:
                print(f"Error: Failed to search GitHub: {e}", file=sys.stderr)
                return None

    return None


def format_number(n):
    """Format large numbers with K/M suffixes."""
    if n is None:
        return "N/A"
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n / 1_000:.1f}K"
    return str(n)


def format_languages(languages_data):
    """Format language distribution."""
    if not languages_data:
        return "N/A"

    # Sort by percentage descending
    sorted_langs = sorted(languages_data.items(), key=lambda x: x[1], reverse=True)
    lang_strings = []
    for lang, percent in sorted_langs[:3]:  # Show top 3
        lang_strings.append(f"{lang} ({percent:.0f}%)")

    result = " + ".join(lang_strings)
    if len(sorted_langs) > 3:
        result += " + others"
    return result


def format_datetime(dt_str):
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


def format_pretty(results, config):
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
        pushed = repo.get("pushed_at", "")
        issues = repo.get("open_issues_count", 0)
        size = repo.get("size", 0)

        # Get languages if enabled
        if config["output"]["include_languages"]:
            langs_url = repo.get("languages_url")
            if langs_url:
                try:
                    lang_resp = requests.get(langs_url, headers=get_github_headers(config), timeout=10)
                    if lang_resp.status_code == 200:
                        lang_data = lang_resp.json()
                        language = format_languages(lang_data)
                except Exception:
                    pass

        # Format info
        stars_str = format_number(stars)
        forks_str = format_number(forks)
        size_str = f"{size/1024:.1f} MB" if size else "N/A"
        updated_str = format_datetime(updated)
        pushed_str = format_datetime(pushed)

        # Truncate description if needed
        max_desc = config["output"]["truncate_description"]
        if max_desc > 0 and len(description) > max_desc:
            description = description[:max_desc - 3] + "..."

        print(divider)
        print(f" {i:>2}. {full_name}")
        print(f"     ⭐ {stars_str}  ·  🍴 {forks_str}  ·  {language}")
        print(f"     {description}")
        print(f"     Issues: {issues}  ·  Size: {size_str}")
        print(f"     Updated: {updated_str}  ·  Pushed: {pushed_str}")
        print(f"     URL: {repo.get('html_url', 'N/A')}")

        # Topics
        topics = repo.get("topics", [])
        if topics and config["output"]["include_topics"]:
            topics_str = ", ".join(topics[:5])
            if len(topics) > 5:
                topics_str += f" +{len(topics)-5} more"
            print(f"     Topics: {topics_str}")

        # License
        license_info = repo.get("license")
        if license_info and config["output"]["include_license"]:
            license_name = license_info.get("spdx_id", license_info.get("name", "Unknown"))
            print(f"     License: {license_name}")

    print(divider)


def format_json(results):
    """Format results as JSON."""
    print(json.dumps(results, indent=2, ensure_ascii=False))


def format_csv(results):
    """Format results as CSV."""
    import csv

    if not results or "items" not in results:
        return

    items = results["items"]
    if not items:
        return

    # CSV headers
    headers = ["full_name", "description", "language", "stargazers_count", "forks_count",
               "open_issues_count", "html_url", "updated_at", "pushed_at", "size"]

    writer = csv.writer(sys.stdout)
    writer.writerow(headers)

    for repo in items:
        row = []
        for header in headers:
            value = repo.get(header, "")
            if isinstance(value, dict):
                value = str(value)
            row.append(value)
        writer.writerow(row)


def format_markdown(results):
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

        # Topics
        topics = repo.get("topics", [])
        if topics:
            print(f"*Topics: {', '.join(topics)}*")

        print("\n---\n")


def parse_args(argv):
    """Parse command line arguments."""
    args = argv[1:]
    query_parts = []
    count = None
    sort = None
    order = None
    language = None
    topic = None
    license_name = None
    org = None
    user = None
    use_auth = True
    output_format = None
    json_output = False
    csv_output = False
    i = 0

    while i < len(args):
        arg = args[i]

        if arg == "--count" and i + 1 < len(args):
            try:
                count = int(args[i + 1])
            except ValueError:
                print(f"Error: --count requires an integer, got '{args[i + 1]}'", file=sys.stderr)
                sys.exit(1)
            i += 2

        elif arg == "--sort" and i + 1 < len(args):
            sort = args[i + 1]
            if sort not in ["stars", "forks", "updated", "pushed"]:
                print("Error: --sort must be one of: stars, forks, updated, pushed", file=sys.stderr)
                sys.exit(1)
            i += 2

        elif arg == "--order" and i + 1 < len(args):
            order = args[i + 1]
            if order not in ["asc", "desc"]:
                print("Error: --order must be asc or desc", file=sys.stderr)
                sys.exit(1)
            i += 2

        elif arg == "--language" and i + 1 < len(args):
            language = args[i + 1]
            i += 2

        elif arg == "--topic" and i + 1 < len(args):
            topic = args[i + 1]
            i += 2

        elif arg == "--license" and i + 1 < len(args):
            license_name = args[i + 1]
            i += 2

        elif arg == "--org" and i + 1 < len(args):
            org = args[i + 1]
            i += 2

        elif arg == "--user" and i + 1 < len(args):
            user = args[i + 1]
            i += 2

        elif arg == "--no-auth":
            use_auth = False
            i += 1

        elif arg == "--json":
            json_output = True
            output_format = "json"
            i += 1

        elif arg == "--csv":
            csv_output = True
            output_format = "csv"
            i += 1

        elif arg == "--format" and i + 1 < len(args):
            output_format = args[i + 1]
            if output_format not in ["pretty", "json", "csv", "markdown"]:
                print("Error: --format must be one of: pretty, json, csv, markdown", file=sys.stderr)
                sys.exit(1)
            i += 2

        elif arg == "--help":
            print_help()
            sys.exit(0)

        else:
            query_parts.append(arg)
            i += 1

    query = " ".join(query_parts)

    if not query and not org and not user:
        print("Error: Query is required (or use --org/--user for empty query)", file=sys.stderr)
        print_help()
        sys.exit(1)

    return {
        "query": query,
        "count": count,
        "sort": sort,
        "order": order,
        "language": language,
        "topic": topic,
        "license": license_name,
        "org": org,
        "user": user,
        "use_auth": use_auth,
        "output_format": output_format,
        "json": json_output,
        "csv": csv_output,
    }


def print_help():
    """Print help message."""
    help_text = """GitHub Repository Search

Usage:
  search.py <query> [options]

Arguments:
  <query>                    Search query (required)

Options:
  --count N                  Number of results to return (default: 20)
  --sort {stars,forks,updated,pushed}
                            Sort results by (default: stars)
  --order {asc,desc}         Sort order (default: desc)
  --language LANG            Filter by programming language
  --topic TOPIC              Filter by topic
  --license LICENSE          Filter by license (e.g., mit, apache-2.0)
  --org ORG                  Search in specific organization
  --user USER                Search in specific user account
  --no-auth                  Don't use $GITHUB_TOKEN (not recommended)
  --format {pretty,json,csv,markdown}
                            Output format (default: pretty)
  --json                     Shortcut for --format json
  --csv                      Shortcut for --format csv
  --help                     Show this help message

Examples:
  search.py "claude code"
  search.py "machine learning" --language python --count 10
  search.py "" --org microsoft --sort stars --count 15
  search.py "react components" --topic "ui" --format json
"""
    print(help_text)


def main():
    """Main entry point."""
    args = parse_args(sys.argv)

    # Load configuration
    config = load_config()

    # Override config based on options
    if args["sort"]:
        config["github"]["default_sort"] = args["sort"]
    if args["order"]:
        config["github"]["default_order"] = args["order"]

    # If use_auth is False, remove token
    if not args["use_auth"]:
        config["github"]["token"] = None
        print("Warning: Running without authentication (strict rate limits apply)", file=sys.stderr)

    # Determine output format
    output_format = args["output_format"] or config["output"]["format"]
    if args["json"]:
        output_format = "json"
    if args["csv"]:
        output_format = "csv"

    # Determine count
    count = args["count"] or config["search"]["default_page_size"]

    # Build search query
    search_query = build_search_query(
        query=args["query"],
        language=args["language"],
        topic=args["topic"],
        license_name=args["license"],
        org=args["org"],
        user=args["user"],
    )

    # Show search info
    print(f"Searching GitHub: {search_query if search_query else '(all repositories)'}",
          file=sys.stderr)

    # Check rate limit before searching
    rate_info = check_rate_limit(config)
    if "error" not in rate_info:
        remaining = rate_info["remaining"]
        if remaining < 10:
            print(f"Warning: Only {remaining} API requests remaining",
                  file=sys.stderr)
            print(f"Rate limit resets at {rate_info['reset_datetime']}", file=sys.stderr)

    # Search repositories
    cache = SimpleCache(ttl=config["cache"]["ttl"], max_size=config["cache"]["max_size"]) if config["cache"]["enabled"] else None

    # Calculate pages needed
    per_page = min(count, config["github"]["per_page"])
    pages_needed = (count + per_page - 1) // per_page
    pages_needed = min(pages_needed, config["github"]["max_pages"])

    all_items = []
    total_count = 0

    for page in range(1, pages_needed + 1):
        results = search_repositories(search_query, config, page=page, per_page=per_page, cache=cache)

        if not results or "items" not in results:
            if page == 1:
                print("No results found.")
                return
            break

        if page == 1:
            total_count = results.get("total_count", 0)

        all_items.extend(results["items"])

        # Stop if we got enough results
        if len(all_items) >= count:
            break

        # Rate limiting between pages
        if page < pages_needed:
            time.sleep(1)

    # Trim to requested count
    all_items = all_items[:count]

    # Prepare final results structure
    final_results = {
        "query": search_query,
        "total_count": total_count,
        "returned_count": len(all_items),
        "items": all_items,
    }

    # Format output
    if output_format == "json":
        format_json(final_results)
    elif output_format == "csv":
        format_csv(final_results)
    elif output_format == "markdown":
        format_markdown(final_results)
    else:  # pretty (default)
        format_pretty(final_results, config)


if __name__ == "__main__":
    main()
