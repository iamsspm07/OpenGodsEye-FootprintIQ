# services/metrics_service.py

from typing import Dict, List, Any


def detect_behavior(data: Dict[str, List]) -> str:
    """
    Detect digital behavior pattern based on
    discovered online presence.
    """

    social = len(data.get("social_media", []))
    developer = len(data.get("developer_profiles", []))
    content = len(data.get("content_platforms", []))
    community = len(data.get("community_platforms", []))
    research = len(data.get("research_platforms", []))
    portfolio = len(data.get("portfolio_platforms", []))
    business = len(data.get("business_profiles", []))

    if research >= 2:
        return "Research-oriented professional"

    if developer > social and developer > content:
        return "Tech-focused, developer activity"

    if portfolio >= 2:
        return "Creative portfolio-focused professional"

    if business >= 2:
        return "Freelancer / business-oriented professional"

    if content >= 3:
        return "Content creator / blogger"

    if social > developer:
        return "Socially active user"

    if community >= 3:
        return "Community-driven participant"

    return "Balanced digital presence"


def calculate_risk(
    profiles_linked: int,
    avg_confidence: float
) -> str:
    """
    Calculate risk level based on
    profile linkage and confidence.
    """

    if profiles_linked >= 5 and avg_confidence >= 0.80:
        return "Low"

    if profiles_linked >= 2 and avg_confidence >= 0.50:
        return "Medium"

    return "High"


def compute_metrics(
    profiles: List[Dict[str, Any]],
    total: int,
    categorized: Dict[str, List] | None = None
) -> Dict[str, Any]:
    """
    Generate intelligence metrics.
    """

    try:

        matched_profiles = [
            profile
            for profile in profiles
            if profile.get("confidence", 0) >= 0.50
        ]

        linked_profiles = len(matched_profiles)

        average_confidence = (
            round(
                sum(
                    profile.get("confidence", 0)
                    for profile in matched_profiles
                ) / linked_profiles,
                2
            )
            if linked_profiles > 0
            else 0.0
        )

        search_accuracy = (
            round(
                (linked_profiles / total) * 100
            )
            if total > 0
            else 0
        )

        fake_accounts = max(
            len(profiles) - linked_profiles,
            0
        )

        metrics = {
            "search_accuracy": f"{search_accuracy}%",
            "identity_confidence": average_confidence,
            "profiles_linked": linked_profiles,
            "possible_fake_accounts": fake_accounts,
            "risk_flag": calculate_risk(
                linked_profiles,
                average_confidence
            )
        }

        metrics["behavior_pattern"] = (
            detect_behavior(categorized)
            if categorized
            else "Unknown"
        )

        return metrics

    except Exception as e:

        print(
            f"Metrics Calculation Error: {e}"
        )

        return {
            "search_accuracy": "0%",
            "identity_confidence": 0.0,
            "profiles_linked": 0,
            "possible_fake_accounts": 0,
            "risk_flag": "Unknown",
            "behavior_pattern": "Unknown"
        }