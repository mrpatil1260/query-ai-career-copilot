from app.services.pdf_service import extract_text_from_pdf
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.services.pdf_service import extract_text_from_pdf

text = extract_text_from_pdf("data/uploads/sample.pdf")
print(text[:1000])

text = extract_text_from_pdf("data/uploads/sample.pdf")

print(text[:1000])  # Print the first 1000 characters