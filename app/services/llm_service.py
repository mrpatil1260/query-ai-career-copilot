import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def ask_llm(
    context: str,
    question: str,
    system_prompt: str | None = None,
) -> str:
    """
    Generic LLM helper that supports custom system prompts.
    """

    if system_prompt is None:
        system_prompt = """
You are an AI Knowledge Assistant.

Answer the user's question ONLY using the provided context.

Rules:
1. Use only the supplied context.
2. Do not invent facts.
3. If the answer cannot be determined from the context, reply:
'I cannot find that information in the uploaded document.'
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": f"""
Context:
{context}

Question:
{question}
""",
            },
        ],
    )

    return response.choices[0].message.content.strip()