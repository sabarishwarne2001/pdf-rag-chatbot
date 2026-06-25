
# 📄 AI Document Assistant
An AI-powered Retrieval-Augmented Generation (RAG) chatbot that allows users to upload PDF documents and ask natural language questions. The application retrieves 
relevant information using semantic search with ChromaDB and generates accurate answers using the Groq API.


## ✨ Features
- Upload one or more PDF documents
- Extract text using PyPDF
- Automatic document chunking
- Semantic search with ChromaDB
- Sentence Transformer embeddings
- AI-powered answers using Groq (Llama 3.3)
- Source citation for every answer
- Multiple PDF support
- Duplicate document detection
- Clear database functionality
- Professional Streamlit chat interface
- Knowledge base statistics
- Error handling for empty or corrupted PDFs


- ## 🛠 Tech Stack
- Python
- Streamlit
- Groq API
- Llama 3.3 70B
- ChromaDB
- Sentence Transformers
- PyPDF
- UUID
- Git & GitHub


## 🏗 Architecture
'
                PDF Upload
                     │
                     ▼
              Text Extraction
                     │
                     ▼
                Chunking
                     │
                     ▼
                Embeddings
                     │
                     ▼
                 ChromaDB
                     │
               Semantic Search
                     │
                     ▼
                Groq API
                     │
                     ▼
               AI Response
                     │
                     ▼
              Source Citation


## 📂 Project Structure

pdf-rag-chatbot/

├── app.py
├── pdf_processor.py
├── vector_store.py
├── rag_engine.py
├── requirements.txt
├── .gitignore
├── data/
└── chroma_db/


## 🚀 Installation

1.Clone the repository
=> git clone <repository-url>

2.Install dependencies
=> pip install -r requirements.txt

3.Create a .env file
=> GROQ_API_KEY=your_api_key

4.Run the application
=> streamlit run app.py


## 🚀 Future Improvements

- FastAPI backend
- Website integration
- Authentication
- Cloud document storage
- Chat history persistence
- Admin dashboard
- OCR support for scanned PDFs



