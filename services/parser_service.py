# services/parser_service.py

import re
from typing import Dict, List, Tuple, Any

from services.platform_registry import PLATFORM_REGISTRY
from services.utils import get_domain


def match_platform(link: str) -> Tuple[str, str]:
    """
    Match URL against known platforms.
    Returns:
        (platform_name, category)
    """

    try:
        domain = get_domain(link)

        if not domain:
            return ("Unknown", "other")

        # Normalize domain
        domain = domain.replace(
            "www.",
            ""
        ).split(":")[0]

        for platform_domain, platform_info in PLATFORM_REGISTRY.items():

            if platform_domain in domain:
                return platform_info

        return (domain, "other")

    except Exception:
        return ("Unknown", "other")


def deduplicate(
    profiles: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """
    Remove duplicate URLs.
    """

    seen_urls = set()
    unique_profiles = []

    for profile in profiles:

        url = profile.get(
            "url",
            ""
        ).strip()

        if not url:
            continue

        if url not in seen_urls:
            seen_urls.add(url)
            unique_profiles.append(profile)

    return unique_profiles


def extract_platforms(
    results: List[Dict[str, Any]]
) -> Dict[str, List[Dict[str, Any]]]:
    """
    Categorize search results
    into platform groups.
    """

    categories = {
        "social_media": [],
        "developer_profiles": [],
        "professional_presence": [],
        "content_platforms": [],
        "community_platforms": [],
        "media_platforms": [],
        "portfolio_platforms": [],
        "research_platforms": [],
        "personal_websites": [],
        "business_profiles": [],
        "other_websites": []
    }

    for result in results:

        link = result.get(
            "link",
            ""
        )

        confidence = result.get(
            "confidence",
            0
        )

        if not link:
            continue

        platform_name, category = match_platform(
            link
        )

        entry = {
            "platform": platform_name,
            "url": link,
            "confidence": confidence
        }

        if category == "social":
            categories["social_media"].append(
                entry
            )

        elif category == "developer":
            categories["developer_profiles"].append(
                entry
            )

        elif category == "professional":
            categories["professional_presence"].append(
                entry
            )

        elif category == "content":
            categories["content_platforms"].append(
                entry
            )

        elif category == "community":
            categories["community_platforms"].append(
                entry
            )

        elif category == "media":
            categories["media_platforms"].append(
                entry
            )

        elif category == "portfolio":
            categories["portfolio_platforms"].append(
                entry
            )

        elif category == "research":
            categories["research_platforms"].append(
                entry
            )

        elif category == "personal":
            categories["personal_websites"].append(
                entry
            )

        elif category == "business":
            categories["business_profiles"].append(
                entry
            )

        else:
            categories["other_websites"].append(
                entry
            )

    # Remove duplicates
    for category_name in categories:

        categories[
            category_name
        ] = deduplicate(
            categories[category_name]
        )

    return categories


def extract_hashtags(
    titles: List[str]
) -> List[str]:
    """
    Extract hashtags from titles.
    """

    hashtags = set()

    for title in titles:

        if not title:
            continue

        found_tags = re.findall(
            r"#\w+",
            str(title)
        )

        hashtags.update(found_tags)

    return sorted(
        list(hashtags)
    )