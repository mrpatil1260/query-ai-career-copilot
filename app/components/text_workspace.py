import streamlit as st


def render_text_workspace():
    """
    Render the Text Workspace.
    Returns:
        tuple[str, str] -> (input_text, selected_action)
    """

    st.header("📝 Text Intelligence")
    st.caption("Paste any text and use AI to summarize, explain, simplify, rewrite, or extract insights.")

    input_text = st.text_area(
        "Paste your text here",
        height=300,
        placeholder="Paste notes, articles, documentation, emails, or any text...",
    )

    action = st.radio(
        "Choose an action",
        options=[
            "Summarize",
            "Explain",
            "Extract Key Points",
            "Simplify",
            "Generate Keywords",
            "Rewrite Professionally",
            "Convert to Bullet Points",
            "Correct Grammar",
        ],
        horizontal=True,
    )

    return input_text, action