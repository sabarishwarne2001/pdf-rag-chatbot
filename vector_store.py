from sentence_transformers import SentenceTransformer
import chromadb


embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = client.get_or_create_collection(
    name="pdf_chunks"
)


def create_embeddings(chunks):
    return embedding_model.encode(chunks)


def store_chunks(chunks):
    """
    Store chunks in ChromaDB
    """

    embeddings = create_embeddings(chunks)

    ids = []

    for i in range(len(chunks)):
        ids.append(str(i))

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings.tolist()
    )