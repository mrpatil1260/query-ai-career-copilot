from app.services.llm_service import ask_llm


def analyze_code(
    code: str,
    language: str,
    action: str,
) -> str:
    """
    Analyze source code using a code-specialized prompt.
    """

    system_prompt = f"""
You are an expert {language} software engineer and code reviewer.

Your job is to analyze the provided source code.

The requested task is:
{action}

Guidelines:
- If the task is "Explain Code", explain what the code does in simple terms.
- If the task is "Find Bugs", identify logical errors, potential bugs, edge cases, and security issues.
- If the task is "Optimize Code", suggest performance, readability, and maintainability improvements.
- If the task is "Analyze Complexity", estimate time and space complexity and explain your reasoning.
- If the task is "Generate Documentation", produce clear developer-friendly documentation.

Do NOT mention uploaded documents.
Base your answer only on the supplied source code.
Format the response using headings and bullet points where appropriate.
"""

    return ask_llm(
        context=code,
        question=f"Perform this task: {action}",
        system_prompt=system_prompt,
    )