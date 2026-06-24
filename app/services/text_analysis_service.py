from app.services.llm_service import ask_llm


def analyze_text(text: str, action: str) -> str:
    """
    Analyze or transform user-provided text using task-specific prompts.
    """

    system_prompts = {
        "Summarize": """
You are an expert summarizer.
Produce a concise, well-structured summary covering the main ideas and conclusions.
""",

        "Explain": """
You are an expert teacher.
Explain the text in simple, easy-to-understand language with clarity.
""",

        "Extract Key Points": """
You are an information extraction expert.
Extract the most important points and present them as bullet points.
""",

        "Simplify": """
You are an expert communicator.
Rewrite the text using simpler language while preserving its meaning.
""",

        "Generate Keywords": """
You are an NLP specialist.
Extract the most relevant keywords, concepts, technologies, and entities.
Return them as bullet points.
""",

        "Rewrite Professionally": """
You are a professional business writer.
Rewrite the text in a polished, professional, and grammatically correct style.
""",

        "Convert to Bullet Points": """
Convert the provided text into a clear, organized list of bullet points while preserving all important information.
""",

        "Correct Grammar": """
Correct all grammar, spelling, punctuation, and sentence structure issues while preserving the original meaning and tone.
""",
    }

    system_prompt = system_prompts.get(
        action,
        "You are an expert text analyst.",
    )

    return ask_llm(
        context=text,
        question=f"Perform the following task: {action}",
        system_prompt=system_prompt,
    )