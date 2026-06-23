import os
import streamlit as st

from app.services.pdf_service import extract_text_from_pdf
from app.services.chunk_service import chunk_text
from app.services.embedding_service import embed_texts, embed_query
from app.services.chroma_service import (
    add_documents,
    search,
    reset_collection,
)
from app.services.llm_service import ask_llm

st.set_page_config(
    page_title="AI Knowledge Assistant",
    page_icon="📚",
)

st.title("📚 AI Knowledge Assistant")

# Initialize session state
if "indexed_file" not in st.session_state:
    st.session_state.indexed_file = None

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"],
)

if uploaded_file is not None:

    os.makedirs("data/uploads", exist_ok=True)

    upload_path = os.path.join(
        "data",
        "uploads",
        uploaded_file.name,
    )

    # Save uploaded file
    with open(upload_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Only index if this is a new file
    if st.session_state.indexed_file != uploaded_file.name:

        with st.spinner("Processing PDF and creating vector index..."):

            # Remove old vectors
            reset_collection()

            # Extract text
            text = extract_text_from_pdf(upload_path)

            # Split into chunks
            chunks = chunk_text(text)

            # Generate embeddings
            embeddings = embed_texts(chunks)

            # Create IDs
            ids = [f"chunk_{i}" for i in range(len(chunks))]

            # Store in ChromaDB
            add_documents(
                ids=ids,
                texts=chunks,
                embeddings=embeddings,
            )

            # Remember indexed file
            st.session_state.indexed_file = uploaded_file.name

        st.success(f"✅ Indexed {len(chunks)} chunks successfully!")

    st.divider()

    question = st.text_input(
        "Ask a question about the uploaded PDF"
    )

    if question:

        with st.spinner("Searching and generating answer..."):

            # Embed the question
            query_embedding = embed_query(question)

            # Retrieve relevant chunks
            results = search(
                query_embedding=query_embedding,
                n_results=5,
            )

            retrieved_docs = results.get("documents", [[]])

            if (
                not retrieved_docs
                or not retrieved_docs[0]
            ):
                st.warning("No relevant information found.")
            else:
                context = "\n\n".join(retrieved_docs[0])

                answer = ask_llm(
                    context=context,
                    question=question,
                )

                st.subheader("🤖 Answer")
                st.write(answer)