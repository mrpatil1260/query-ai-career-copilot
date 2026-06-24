from app.services.llm_service import ask_llm


def analyze_code(
    code: str,
    language: str,
    action: str,
) -> str:
    """
    Analyze source code using task-specific prompts.
    """

    system_prompts = {
        "Explain Code": f"""
You are an expert {language} developer.
Explain what the code does step by step in simple language.
""",

        "Find Bugs": f"""
You are an expert {language} code reviewer.
Identify logical bugs, runtime issues, security concerns, and edge cases.
Suggest fixes where appropriate.
""",

        "Optimize Code": f"""
You are an expert {language} performance engineer.
Suggest improvements for efficiency, readability, maintainability,
and performance.
""",

        "Analyze Complexity": f"""
You are an algorithms expert.
Estimate the time complexity and space complexity of the code.
Explain your reasoning clearly.
""",

        "Generate Documentation": f"""
You are a technical writer.
Generate clean developer documentation for this code including
its purpose, inputs, outputs, and usage.
""",

        "Suggest Best Practices": f"""
You are a senior {language} software engineer.
Review the code and recommend coding standards,
design improvements, and best practices.
""",

        "Refactor Code": f"""
You are an expert {language} developer.
Refactor the code to improve readability,
maintainability, and structure without changing behavior.
""",

        "Generate Unit Tests": f"""
You are a QA engineer.
Generate meaningful unit tests for this {language} code,
covering normal cases and edge cases where possible.
""",
    }

    system_prompt = system_prompts.get(
        action,
        f"You are an expert {language} developer.",
    )

    return ask_llm(
        context=code,
        question=f"Perform the following task: {action}",
        system_prompt=system_prompt,
    )