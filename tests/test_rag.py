from app.services.embedding_service import embed_texts
from app.services.chroma_service import search
from app.services.llm_service import ask_llm

question = "What programming languages does the candidate know?"

query_embedding = embed_texts([question])[0]

results = search(
    query_embedding=query_embedding,
    n_results=5,
)

context = "\n\n".join(results["documents"][0])

answer = ask_llm(
    context=context,
    question=question,
)

print(answer)