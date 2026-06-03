import streamlit as st

from services.search_service import multi_search
from services.identity_service import compute_identity
from services.parser_service import (
    extract_platforms,
    extract_hashtags
)
from services.metrics_service import compute_metrics
from services.summary_service import generate_summary


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="GodsEye Tracker",
    page_icon="🧠",
    layout="wide"
)

# ==================================================
# HEADER
# ==================================================

st.title("🧠 GodsEye - Digital Presence Tracker")

st.markdown(
    """
Track social, developer, professional,
research, portfolio, business, and web presence
across the internet.
"""
)

# ==================================================
# INPUT
# ==================================================

name = st.text_input(
    "Enter Name",
    "Sujit Shibaprasad Maity"
)

# ==================================================
# SEARCH BUTTON
# ==================================================

if st.button("Search 🔍"):

    if not name.strip():

        st.warning(
            "Please enter a valid name."
        )

        st.stop()

    with st.spinner(
        "🔎 Scanning global internet..."
    ):

        try:

            # ======================================
            # SEARCH
            # ======================================

            results = multi_search(
                name
            )

            # ======================================
            # IDENTITY RESOLUTION
            # ======================================

            profiles = compute_identity(
                name,
                results
            )

            # ======================================
            # PLATFORM EXTRACTION
            # ======================================

            categorized = extract_platforms(
                profiles
            )

            # ======================================
            # HASHTAGS
            # ======================================

            hashtags = extract_hashtags(
                [
                    result.get(
                        "title",
                        ""
                    )
                    for result in results
                ]
            )

            # ======================================
            # METRICS
            # ======================================

            metrics = compute_metrics(
                profiles,
                len(results),
                categorized
            )

            # ======================================
            # SUMMARY
            # ======================================

            summary = generate_summary(
                {
                    **categorized,
                    "metrics": metrics
                }
            )

            data = {
                **categorized,
                "hashtags": hashtags,
                "metrics": metrics,
                "summary": summary
            }

        except Exception as e:

            st.error(
                f"Error: {e}"
            )

            st.stop()

    # ==================================================
    # ANALYSIS COMPLETE
    # ==================================================

    st.success(
        "✅ Analysis Complete"
    )

    st.info(
        f"Found {len(results)} search results | "
        f"Linked Profiles: "
        f"{metrics.get('profiles_linked', 0)}"
    )

    # ==================================================
    # SOCIAL MEDIA
    # ==================================================

    st.subheader(
        "🌐 Social Media"
    )

    social = data.get(
        "social_media",
        []
    )

    if social:

        for profile in social:

            st.markdown(
                f"• **{profile['platform']}** → "
                f"[Open Profile]({profile['url']})"
            )

    else:

        st.write(
            "No data found"
        )

    # ==================================================
    # DEVELOPER
    # ==================================================

    st.subheader(
        "👨‍💻 Developer Profiles"
    )

    developer = data.get(
        "developer_profiles",
        []
    )

    if developer:

        for profile in developer:

            st.markdown(
                f"• **{profile['platform']}** → "
                f"[Open Profile]({profile['url']})"
            )

    else:

        st.write(
            "No data found"
        )

    # ==================================================
    # PROFESSIONAL
    # ==================================================

    st.subheader(
        "💼 Professional Presence"
    )

    professional = data.get(
        "professional_presence",
        []
    )

    if professional:

        for profile in professional:

            st.markdown(
                f"• **{profile['platform']}** → "
                f"[View]({profile['url']})"
            )

    else:

        st.write(
            "No data found"
        )

    # ==================================================
    # RESEARCH
    # ==================================================

    st.subheader(
        "📚 Research Profiles"
    )

    research = data.get(
        "research_platforms",
        []
    )

    if research:

        for profile in research:

            st.markdown(
                f"• **{profile['platform']}** → "
                f"[Open]({profile['url']})"
            )

    else:

        st.write(
            "No data found"
        )

    # ==================================================
    # PORTFOLIO
    # ==================================================

    st.subheader(
        "🎨 Portfolio Platforms"
    )

    portfolio = data.get(
        "portfolio_platforms",
        []
    )

    if portfolio:

        for profile in portfolio:

            st.markdown(
                f"• **{profile['platform']}** → "
                f"[View Portfolio]({profile['url']})"
            )

    else:

        st.write(
            "No data found"
        )

    # ==================================================
    # CONTENT
    # ==================================================

    st.subheader(
        "✍️ Content Platforms"
    )

    content = data.get(
        "content_platforms",
        []
    )

    if content:

        for profile in content:

            st.markdown(
                f"• **{profile['platform']}** → "
                f"[Read]({profile['url']})"
            )

    else:

        st.write(
            "No data found"
        )

    # ==================================================
    # COMMUNITY
    # ==================================================

    st.subheader(
        "💬 Community Platforms"
    )

    community = data.get(
        "community_platforms",
        []
    )

    if community:

        for profile in community:

            st.markdown(
                f"• **{profile['platform']}** → "
                f"[Visit]({profile['url']})"
            )

    else:

        st.write(
            "No data found"
        )

    # ==================================================
    # MEDIA
    # ==================================================

    st.subheader(
        "🎥 Media Platforms"
    )

    media = data.get(
        "media_platforms",
        []
    )

    if media:

        for profile in media:

            st.markdown(
                f"• **{profile['platform']}** → "
                f"[Watch]({profile['url']})"
            )

    else:

        st.write(
            "No data found"
        )

    # ==================================================
    # BUSINESS
    # ==================================================

    st.subheader(
        "💼 Business Profiles"
    )

    business = data.get(
        "business_profiles",
        []
    )

    if business:

        for profile in business:

            st.markdown(
                f"• **{profile['platform']}** → "
                f"[Visit]({profile['url']})"
            )

    else:

        st.write(
            "No data found"
        )

    # ==================================================
    # PERSONAL WEBSITES
    # ==================================================

    st.subheader(
        "🔗 Personal Websites"
    )

    personal = data.get(
        "personal_websites",
        []
    )

    if personal:

        for profile in personal:

            st.markdown(
                f"• **{profile['platform']}** → "
                f"[Visit]({profile['url']})"
            )

    else:

        st.write(
            "No data found"
        )

    # ==================================================
    # OTHER
    # ==================================================

    st.subheader(
        "🌍 Other Websites"
    )

    others = data.get(
        "other_websites",
        []
    )

    if others:

        for profile in others:

            st.markdown(
                f"• **{profile['platform']}** → "
                f"[Visit]({profile['url']})"
            )

    else:

        st.write(
            "No data found"
        )

    # ==================================================
    # HASHTAGS
    # ==================================================

    st.subheader(
        "#️⃣ Hashtags"
    )

    if hashtags:

        st.write(
            ", ".join(hashtags)
        )

    else:

        st.write(
            "No hashtags found"
        )

    # ==================================================
    # METRICS
    # ==================================================

    st.subheader(
        "📊 Metrics"
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Search Accuracy",
        metrics.get(
            "search_accuracy",
            "0%"
        )
    )

    col2.metric(
        "Identity Confidence",
        metrics.get(
            "identity_confidence",
            0
        )
    )

    col3.metric(
        "Profiles Linked",
        metrics.get(
            "profiles_linked",
            0
        )
    )

    col4, col5 = st.columns(2)

    col4.metric(
        "Possible Fake Accounts",
        metrics.get(
            "possible_fake_accounts",
            0
        )
    )

    col5.metric(
        "Risk Level",
        metrics.get(
            "risk_flag",
            "Unknown"
        )
    )

    st.info(
        f"🧠 Behavior Pattern: "
        f"{metrics.get('behavior_pattern', 'Unknown')}"
    )

    # ==================================================
    # SUMMARY
    # ==================================================

    st.subheader(
        "🧾 Summary"
    )

    st.success(
        data.get(
            "summary",
            "No summary available"
        )
    )

    # ==================================================
    # RAW SEARCH RESULTS
    # ==================================================

    with st.expander(
        "🔍 Raw Search Results"
    ):

        st.json(results)