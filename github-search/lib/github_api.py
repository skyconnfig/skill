"""GitHub API wrapper for repository searching."""

import requests
import time
from typing import Optional, Dict, Any, List


class GitHubAPI:
    """Wrapper for GitHub Search API with rate limit handling."""

    BASE_URL = "https://api.github.com"

    def __init__(self, token: Optional[str] = None, timeout: int = 30):
        """Initialize GitHub API client.

        Args:
            token: GitHub personal access token (optional but recommended)
            timeout: Request timeout in seconds
        """
        self.token = token
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "github-search-skill/1.0.0"
        })
        if token:
            self.session.headers["Authorization"] = f"token {token}"

    def search_repositories(
        self,
        query: str,
        sort: str = "stars",
        order: str = "desc",
        per_page: int = 100,
        page: int = 1,
        **filters
    ) -> Optional[Dict[str, Any]]:
        """Search GitHub repositories.

        Args:
            query: Search query string
            sort: Sort by - stars, forks, updated, pushed
            order: Sort order - asc or desc
            per_page: Results per page (max 100)
            page: Page number
            **filters: Additional filters (language, topic, license, org, user, etc.)

        Returns:
            Dictionary with search results or None on error
        """
        params = {
            "q": query,
            "sort": sort,
            "order": order,
            "per_page": min(per_page, 100),
            "page": page,
        }

        # Add filters to query
        if "language" in filters:
            params["q"] += f" language:{filters['language']}"
        if "topic" in filters:
            params["q"] += f" topic:{filters['topic']}"
        if "license" in filters:
            params["q"] += f" license:{filters['license']}"
        if "org" in filters:
            params["q"] += f" org:{filters['org']}"
        if "user" in filters:
            params["q"] += f" user:{filters['user']}"

        url = f"{self.BASE_URL}/search/repositories"

        for attempt in range(3):
            try:
                response = self.session.get(url, params=params, timeout=self.timeout)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.HTTPError as e:
                if e.response.status_code == 403:
                    # Rate limit
                    reset = int(e.response.headers.get("X-RateLimit-Reset", 0))
                    remaining = int(e.response.headers.get("X-RateLimit-Remaining", 0))
                    if remaining <= 0 and reset > time.time():
                        wait_time = reset - time.time() + 1
                        print(f"Rate limit hit. Waiting {wait_time:.0f}s...")
                        time.sleep(wait_time)
                        continue
                if attempt < 2:
                    time.sleep(2 ** attempt)  # Exponential backoff
                    continue
                raise
            except requests.exceptions.RequestException:
                if attempt < 2:
                    time.sleep(2 ** attempt)
                    continue
                raise

        return None

    def get_repository_languages(self, owner: str, repo: str) -> Optional[Dict[str, int]]:
        """Get language breakdown for a repository.

        Args:
            owner: Repository owner
            repo: Repository name

        Returns:
            Dictionary mapping language names to byte counts
        """
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/languages"

        try:
            response = self.session.get(url, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return None

    def check_rate_limit(self) -> Dict[str, Any]:
        """Check current rate limit status.

        Returns:
            Dictionary with rate limit information
        """
        try:
            response = self.session.get(f"{self.BASE_URL}/rate_limit", timeout=self.timeout)
            response.raise_for_status()
            return response.json()["resources"]["core"]
        except Exception as e:
            return {"error": str(e)}
