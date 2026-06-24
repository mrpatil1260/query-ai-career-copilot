import streamlit as st


def render_code_workspace():
    """
    Render the Code Workspace.

    Returns:
        tuple[str, str, str]:
            (code_text, selected_language, selected_action)
    """

    st.header("💻 Code Intelligence")
    st.caption(
        "Paste source code and let Query AI explain, review, optimize, refactor, or generate documentation and tests."
    )

    language = st.selectbox(
        "Programming Language",
        [
            "Python",
            "Java",
            "C++",
            "JavaScript",
            "SQL",
            "HTML/CSS",
            "Other",
        ],
    )

    code = st.text_area(
        "Paste your code here",
        height=350,
        placeholder="Paste your source code...",
    )

    action = st.radio(
        "Choose an action",
        options=[
            "Explain Code",
            "Find Bugs",
            "Optimize Code",
            "Analyze Complexity",
            "Generate Documentation",
            "Suggest Best Practices",
            "Refactor Code",
            "Generate Unit Tests",
        ],
        horizontal=True,
    )

    return code, language, action