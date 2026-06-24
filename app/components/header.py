import streamlit as st


def render_header():
    """Render the Query AI hero section."""

    st.title("🧠 Query AI")

    st.caption("AI-powered Document, Code & Career Intelligence")

    st.markdown(
        """
Chat with documents, summarize text, analyze source code,
compare resumes with job descriptions, identify skill gaps,
and prepare for interviews from one unified workspace.
"""
    )

    st.divider()