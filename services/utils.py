# services/utils.py

from urllib.parse import urlparse
from typing import Dict, List, Any


def get_domain(url: str) -> str:
    """
    Extract domain name from URL.

    Example:
    https://github.com/user
    -> github.com
    """

    try:

        if not url:
            return ""

        return (
            urlparse(url)
            .netloc
            .lower()
            .replace("www.", "")
        )

    except Exception:
        return ""


def deduplicate(
    results: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """
    Remove duplicate links from search results.
    """

    seen_links = set()
    unique_results = []

    for result in results:

        link = result.get("link", "").strip()

        if not link:
            continue

        if link not in seen_links:

            seen_links.add(link)
            unique_results.append(result)

    return unique_results