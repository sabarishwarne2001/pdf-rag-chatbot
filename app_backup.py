# EXTRACT TEXT FROM PDF
# from pdf_processor import extract_text_from_pdf
# pdf_path = "data/sample.pdf"
# text = extract_text_from_pdf(pdf_path)
# print(text)
# from pypdf import PdfReader

# CHUNK CREATE
# def create_chunks(text, chunk_size=500):
#     """
#     Split text into smaller chunks.
#     """
#     chunks = []
#     for i in range(0, len(text), chunk_size):
#         chunk = text[i:i + chunk_size]
#         chunks.append(chunk)
#     return chunks

# CHUNK TO EMBEDDINGS
# from sentence_transformers import SentenceTransformer
# # Load embedding model
# embedding_model = SentenceTransformer(
#     "all-MiniLM-L6-v2"
# )
# def create_embeddings(chunks):
#     """
#     Convert chunks into embeddings.
#     """
#     embeddings = embedding_model.encode(chunks)
#     return embeddings
