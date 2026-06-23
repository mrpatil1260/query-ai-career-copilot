import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def ask_llm(context: str, question: str) -> str:
    prompt = f"""
    You are a helpful AI assistant.

    Answer ONLY using the provided context.

    If the answer cannot be found in the context, reply exactly:
    "I cannot find that information in the uploaded document."

    Do not make up facts or use outside knowledge.

    Context:
    {context}

    Question:
    {question}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content