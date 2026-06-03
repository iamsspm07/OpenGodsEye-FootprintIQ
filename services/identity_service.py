from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from rapidfuzz import fuzz
import streamlit as st


@st.cache_resource
def load_model():
    """
    Load and cache the SentenceTransformer model.
    This prevents reloading the model on every Streamlit rerun.
    """
    return SentenceTransformer("all-MiniLM-L6-v2")


model = load_model()


def compute_identity(name: str, profiles: list) -> list:
    """
    Compute confidence scores for profiles using:
    - Semantic Similarity (70%)
    - Fuzzy String Matching (30%)

    Parameters
    ----------
    name : str
        Input person name.

    profiles : list
        Search results containing titles.

    Returns
    -------
    list
        Profiles enriched with confidence scores.
    """

    if not profiles:
        return []

    try:
        # Create corpus
        texts = [name]

        for profile in profiles:
            texts.append(
                profile.get("title", "")
            )

        # Generate embeddings
        embeddings = model.encode(
            texts,
            convert_to_numpy=True,
            show_progress_bar=False
        )

        # Compute semantic similarity
        similarity_scores = cosine_similarity(
            [embeddings[0]],
            embeddings[1:]
        )[0]

        # Calculate confidence score
        for idx, profile in enumerate(profiles):

            title = profile.get(
                "title",
                ""
            )

            fuzzy_score = (
                fuzz.token_sort_ratio(
                    name,
                    title
                ) / 100
            )

            semantic_score = max(
                float(similarity_scores[idx]),
                0.0
            )

            confidence = (
                semantic_score * 0.70
                + fuzzy_score * 0.30
            )

            # Ensure confidence remains between 0 and 1
            confidence = min(
                max(confidence, 0.0),
                1.0
            )

            profile["confidence"] = round(
                confidence,
                2
            )

        return profiles

    except Exception as e:

        print(
            f"Identity Matching Error: {e}"
        )

        # Fallback confidence
        for profile in profiles:
            profile["confidence"] = 0.0

        return profiles