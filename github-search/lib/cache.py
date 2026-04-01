"""Cache implementations for GitHub search results."""

import time
from typing import Optional, Any


class SimpleCache:
    """Simple in-memory cache with TTL and size limit."""

    def __init__(self, ttl: int = 1800, max_size: int = 1000):
        """Initialize cache.

        Args:
            ttl: Time-to-live in seconds
            max_size: Maximum number of entries
        """
        self.cache = {}
        self.ttl = ttl
        self.max_size = max_size

    def get(self, key: str) -> Optional[Any]:
        """Get value from cache if not expired."""
        if key in self.cache:
            value, timestamp = self.cache[key]
            if time.time() - timestamp < self.ttl:
                return value
            else:
                del self.cache[key]
        return None

    def set(self, key: str, value: Any) -> None:
        """Set value in cache with current timestamp."""
        if len(self.cache) >= self.max_size:
            # Remove oldest entry (FIFO)
            oldest_key = min(self.cache.items(), key=lambda x: x[1][1])[0]
            del self.cache[oldest_key]
        self.cache[key] = (value, time.time())

    def clear(self) -> None:
        """Clear all cache entries."""
        self.cache.clear()

    def size(self) -> int:
        """Return current cache size."""
        return len(self.cache)
