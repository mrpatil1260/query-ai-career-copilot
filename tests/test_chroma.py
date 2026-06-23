from app.services.embedding_service import embed_texts, embed_query
from app.services.chroma_service import add_documents, search

# Sample documents
texts = [
]

# Generate embeddings
embeddings = embed_texts(texts)

# Store them
add_documents(
    ids=["doc1", "doc2", "doc3"],
    texts=texts,
    embeddings=embeddings
)

# Ask a question
query = "Tell me about Python"

query_embedding = embed_query(query)

# Search
results = search(query_embedding)

print("\n=== SEARCH RESULTS ===\n")
print(results["documents"])