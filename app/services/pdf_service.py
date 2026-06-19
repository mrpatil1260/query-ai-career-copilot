import fitz  # PyMuPDF


def extract_text_from_pdf(file_path: str) -> str:
    """
    Extract all text from a PDF file.

    Args:
        file_path: Path to the PDF file.

    Returns:
        A single string containing the extracted text.
    """
    document = fitz.open(file_path)
    text = ""

    for page in document:
        text += page.get_text()

    document.close()
    return text