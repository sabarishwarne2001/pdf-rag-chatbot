
# 📄 AI Document Assistant

An AI-powered Retrieval-Augmented Generation (RAG) chatbot that enables users to upload one or more PDF documents and ask natural language questions. The application retrieves relevant information using semantic search with ChromaDB and generates accurate responses using Groq's Llama 3.3 model.

---

## 📖 Project Overview

This project demonstrates how Large Language Models (LLMs) can answer questions using private documents instead of relying solely on their pretrained knowledge.

Users can upload multiple PDF files, which are processed into semantic embeddings and stored in a ChromaDB vector database. When a question is asked, the application retrieves the most relevant document chunks and sends them to the Groq Llama 3.3 model to generate an accurate, context-aware response.

The project was designed as a production-quality portfolio application and includes multiple features commonly required in real-world business solutions.

---

## ✨ Features

- 📄 Upload one or more PDF documents
- 🔍 Semantic search using ChromaDB
- 🤖 AI-powered answers using Groq (Llama 3.3)
- 🧠 Sentence Transformer embeddings
- 📚 Multiple PDF support
- 📌 Source citation for every response
- 🆔 UUID-based chunk IDs
- 📊 Knowledge Base dashboard
- 🗂 Duplicate document detection
- 🧹 Clear database functionality
- 💬 Chat-style interface
- ⚠ Error handling for empty or corrupted PDFs

---

## 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Frontend | Streamlit |
| LLM | Groq (Llama 3.3 70B) |
| Vector Database | ChromaDB |
| Embedding Model | Sentence Transformers (all-MiniLM-L6-v2) |
| PDF Processing | PyPDF |
| Version Control | Git & GitHub |

---

## 🏗 Architecture

```text
                PDF Upload
                     │
                     ▼
            Text Extraction (PyPDF)
                     │
                     ▼
               Text Chunking
                     │
                     ▼
      Sentence Transformer Embeddings
                     │
                     ▼
            ChromaDB Vector Store
                     │
              Semantic Search
                     │
                     ▼
          Relevant Context Chunks
                     │
                     ▼
           Groq (Llama 3.3 70B)
                     │
                     ▼
          AI Response + Sources
```

---

## 📂 Project Structure

```text
pdf-rag-chatbot/

├── app.py                 # Streamlit UI
├── pdf_processor.py       # PDF extraction & chunking
├── vector_store.py        # ChromaDB operations
├── rag_engine.py          # RAG pipeline & Groq API
├── requirements.txt
├── README.md
├── .gitignore
├── data/
└── chroma_db/
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/pdf-rag-chatbot.git
```

### Navigate to the project

```bash
cd pdf-rag-chatbot
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Create a `.env` file

```env
GROQ_API_KEY=your_api_key
```

### Run the application

```bash
streamlit run app.py
```

---

## 💻 Usage

1. Launch the application.
2. Upload one or more PDF documents.
3. Wait for the documents to be indexed.
4. Ask questions in natural language.
5. Receive AI-generated answers with source citations.

---

## 🔮 Future Improvements

- FastAPI backend
- Website integration
- Cloud document storage
- Authentication & user accounts
- OCR support for scanned PDFs
- Persistent chat history
- Admin dashboard
- Docker deployment

---

## 👨‍💻 Author

**Sabarish**

Aspiring AI Automation Developer focused on building practical AI solutions for businesses.

GitHub: https://github.com/sabarishwarne2001

