# services/summary_service.py


def generate_summary(data: dict) -> str:
    """
    Generate a human-readable summary
    of the discovered digital footprint.
    """

    social = len(data.get("social_media", []))
    developer = len(data.get("developer_profiles", []))
    professional = len(data.get("professional_presence", []))
    content = len(data.get("content_platforms", []))
    community = len(data.get("community_platforms", []))
    media = len(data.get("media_platforms", []))
    portfolio = len(data.get("portfolio_platforms", []))
    research = len(data.get("research_platforms", []))
    personal = len(data.get("personal_websites", []))
    business = len(data.get("business_profiles", []))

    metrics = data.get("metrics", {})

    confidence = metrics.get(
        "identity_confidence",
        0
    )

    risk = metrics.get(
        "risk_flag",
        "Unknown"
    )

    total_profiles = (
        social +
        developer +
        professional +
        content +
        community +
        media +
        portfolio +
        research +
        personal +
        business
    )

    # ----------------------------------
    # Presence Strength
    # ----------------------------------

    if total_profiles >= 15:
        presence = "very strong"

    elif total_profiles >= 8:
        presence = "strong"

    elif total_profiles >= 3:
        presence = "moderate"

    else:
        presence = "limited"

    # ----------------------------------
    # Primary Focus
    # ----------------------------------

    if research >= 2:
        focus = "research-oriented"

    elif developer > social:
        focus = "technical/developer-focused"

    elif portfolio >= 2:
        focus = "creative portfolio-focused"

    elif business >= 2:
        focus = "business/freelance-focused"

    elif social > developer:
        focus = "socially active"

    else:
        focus = "balanced"

    # ----------------------------------
    # Content Status
    # ----------------------------------

    if content >= 3:
        content_status = (
            "active content creator"
        )

    elif content > 0:
        content_status = (
            "occasional content publisher"
        )

    else:
        content_status = (
            "no significant content publishing"
        )

    # ----------------------------------
    # Research Status
    # ----------------------------------

    if research >= 2:
        research_status = (
            "active research presence"
        )

    elif research > 0:
        research_status = (
            "some academic visibility"
        )

    else:
        research_status = (
            "limited academic visibility"
        )

    # ----------------------------------
    # Portfolio Status
    # ----------------------------------

    if portfolio >= 2:
        portfolio_status = (
            "strong portfolio presence"
        )

    elif portfolio > 0:
        portfolio_status = (
            "some portfolio visibility"
        )

    else:
        portfolio_status = (
            "no portfolio presence detected"
        )

    # ----------------------------------
    # Final Summary
    # ----------------------------------

    return (
        f"{presence.capitalize()} digital presence "
        f"with a {focus} profile. "
        f"{content_status}. "
        f"{research_status}. "
        f"{portfolio_status}. "
        f"Identity confidence is "
        f"{confidence:.2f} "
        f"with a {risk.lower()} risk profile."
    )