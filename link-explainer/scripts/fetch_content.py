#!/usr/bin/env python3
"""
Fetch content from a web URL and extract main article content.
Uses requests and BeautifulSoup for parsing.
"""

import sys
import json
import re
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup


def fetch_url(url):
    """Fetch the content of a URL."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}", file=sys.stderr)
        sys.exit(1)


def extract_main_content(html):
    """Extract the main content from HTML."""
    soup = BeautifulSoup(html, 'html.parser')

    # Remove unwanted elements
    for tag in soup(['script', 'style', 'nav', 'footer', 'aside', 'header']):
        tag.decompose()

    # Try to find main content areas
    content_selectors = [
        'article',
        '[role="main"]',
        'main',
        '.post-content',
        '.article-content',
        '.entry-content',
        '.content',
        '#content'
    ]

    content = None
    for selector in content_selectors:
        elements = soup.select(selector)
        if elements:
            # Get the largest content area
            content = max(elements, key=lambda x: len(x.get_text()))
            break

    # Fallback to body if no content area found
    if not content:
        content = soup.find('body')
        if not content:
            return {"title": "", "content": "", "sections": []}

    # Extract headings and their content
    sections = []
    current_section = {"heading": "", "content": "", "level": 0}

    for elem in content.find_all(['h1', 'h2', 'h3', 'h4', 'p', 'li']):
        text = elem.get_text(strip=True)
        if not text:
            continue

        if elem.name.startswith('h'):
            # Save previous section
            if current_section["heading"] or current_section["content"]:
                sections.append(current_section)

            level = int(elem.name[1])
            current_section = {"heading": text, "content": "", "level": level}
        else:
            current_section["content"] += text + "\n\n"

    # Add final section
    if current_section["heading"] or current_section["content"]:
        sections.append(current_section)

    # Get title
    title = ""
    title_elem = soup.find('title')
    if title_elem:
        title = title_elem.get_text(strip=True)
    else:
        h1 = soup.find('h1')
        if h1:
            title = h1.get_text(strip=True)

    # Clean up content
    for section in sections:
        section["content"] = section["content"].strip()

    return {
        "title": title,
        "url": "",  # Will be filled by caller
        "content": "\n\n".join([s["heading"] + "\n" + s["content"] for s in sections]),
        "sections": sections
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python fetch_content.py <url>", file=sys.stderr)
        sys.exit(1)

    url = sys.argv[1]

    # Validate URL
    parsed = urlparse(url)
    if not parsed.scheme:
        print("Error: Invalid URL. Please include http:// or https://", file=sys.stderr)
        sys.exit(1)

    print(f"Fetching content from: {url}", file=sys.stderr)

    html = fetch_url(url)
    content_data = extract_main_content(html)
    content_data["url"] = url

    # Output as JSON
    print(json.dumps(content_data, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
