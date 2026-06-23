from pdf_processor import extract_text_from_pdf
from pdf_processor import create_chunks

from vector_store import store_chunks


text = extract_text_from_pdf(
    "data/sample.pdf"
)

chunks = create_chunks(text)

store_chunks(chunks)

print("Chunks stored successfully.")