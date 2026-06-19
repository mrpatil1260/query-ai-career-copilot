import os
import streamlit as st

from app.services.pdf_service import extract_text_from_pdf

UPLOAD_DIR = "data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

st.set_page_config(
    page_title="AI Knowledge Assistant",
    page_icon="🤖",
)

st.title("🤖 AI Knowledge Assistant")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

if uploaded_file is not None:
    save_path = os.path.join(UPLOAD_DIR, uploaded_file.name)

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("✅ PDF uploaded successfully!")

    extracted_text = extract_text_from_pdf(save_path)
    from app.services.chunk_service import chunk_text

    chunks = chunk_text(extracted_text)

    st.subheader("Number of Chunks")
    st.write(len(chunks))

    st.subheader("First Chunk")
    st.text_area(
        "Chunk Preview",
        chunks[0] if chunks else "",
        height=300,
    )

    st.subheader("Extracted Text Preview")
    st.text_area(
        "Content",
        extracted_text[:5000],
        height=300
    )