# services/search_service.py

import requests

from services.utils import deduplicate


# ==================================================
# SERPAPI KEY
# ==================================================

SERP_API_KEY = "07da0cccecdb3bc72bdba94197f9b65aaea7ab69687d0c3821147d7c7b48054a"


# ==================================================
# SEARCH SERPAPI
# ==================================================

def search_serpapi(query: str) -> list:
    """
    Search Google using SerpAPI.
    """

    try:

        response = requests.get(
            "https://serpapi.com/search",
            params={
                "q": query,
                "api_key": SERP_API_KEY,
                "num": 10
            },
            timeout=20
        )

        response.raise_for_status()

        data = response.json()

        return [
            {
                "title": result.get("title", ""),
                "link": result.get("link", ""),
                "snippet": result.get("snippet", "")
            }
            for result in data.get(
                "organic_results",
                []
            )
        ]

    except Exception as e:

        print(
            f"SerpAPI Error: {e}"
        )

        return []


# ==================================================
# MULTI SEARCH
# ==================================================

def multi_search(name: str) -> list:
    """
    Discover a person's digital footprint
    across multiple platforms.
    """

    queries = [

        # General
        name,

        # Professional
        f'"{name}" LinkedIn',
        f'"{name}" site:linkedin.com',

        # Developer
        f'"{name}" GitHub',
        f'"{name}" site:github.com',
        f'"{name}" Kaggle',
        f'"{name}" site:kaggle.com',
        f'"{name}" Hugging Face',
        f'"{name}" site:huggingface.co',

        # Research
        f'"{name}" ResearchGate',
        f'"{name}" Google Scholar',
        f'"{name}" site:researchgate.net',
        f'"{name}" site:scholar.google.com',

        # Content
        f'"{name}" Medium',
        f'"{name}" site:medium.com',
        f'"{name}" Hashnode',
        f'"{name}" site:hashnode.com',

        # Social
        f'"{name}" Instagram',
        f'"{name}" Twitter',
        f'"{name}" Facebook',
        f'"{name}" Threads',

        # AI / ML
        f'"{name}" data scientist',
        f'"{name}" machine learning',
        f'"{name}" AI engineer',
        f'"{name}" deep learning',

        # Portfolio
        f'"{name}" Behance',
        f'"{name}" Dribbble',

        # Freelance
        f'"{name}" Upwork',
        f'"{name}" Fiverr'
    ]

    results = []

    for query in queries:

        try:

            search_results = search_serpapi(
                query
            )

            results.extend(
                search_results
            )

        except Exception as e:

            print(
                f"Search Error ({query}): {e}"
            )

    return deduplicate(results)