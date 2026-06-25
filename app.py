import streamlit as st
import os

from pdf_processor import extract_text_from_pdf, create_chunks
from rag_engine import ask_rag

from vector_store import (
    store_chunks,
    clear_database,
    has_documents,
    document_exists,
    get_chunk_count,
    get_documents
)

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Document Assistant",
    page_icon="📄",
    layout="wide"
)

# --------------------------------------------------
# Session State
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.title("⚙️ Control Panel")

st.sidebar.markdown("---")

st.sidebar.subheader("📊 Statistics")
st.sidebar.write(
    "Upload one or more PDF documents to build your AI knowledge base."
)

documents = get_documents()

col1, col2 = st.sidebar.columns(2)

with col1:
    st.metric("Docs", len(documents))

with col2:
    st.metric("Chunks", get_chunk_count())

st.sidebar.markdown("---")

st.sidebar.subheader("📚 Knowledge Base")

if documents:
    for document in documents:
        st.sidebar.write(f"✅ {document}")
else:
    st.sidebar.info("No documents indexed.")

st.sidebar.markdown("---")

if st.sidebar.button("🗑️ Clear Database"):

    clear_database()

    st.session_state.messages = []

    st.sidebar.success("Database cleared successfully!")

    st.rerun()

# --------------------------------------------------
# App Header
# --------------------------------------------------

st.title("📄 AI Document Assistant")

st.caption(
    "Ask questions across one or more PDF documents using Retrieval-Augmented Generation (RAG)."
)

# --------------------------------------------------
# PDF Upload
# --------------------------------------------------

uploaded_files = st.file_uploader(
    "Upload PDF Files",
    type=["pdf"],
    accept_multiple_files=True
)

indexed_files = []
duplicate_files = []
failed_files = []

if uploaded_files:

    with st.spinner("Processing PDFs..."):

        for uploaded_file in uploaded_files:

            os.makedirs(
                "data",
                exist_ok=True
            )

            pdf_path = f"data/{uploaded_file.name}"

            with open(pdf_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            if document_exists(uploaded_file.name):

                duplicate_files.append(uploaded_file.name)

                continue

            try:

                text = extract_text_from_pdf(pdf_path)

                if not text.strip():

                    failed_files.append(uploaded_file.name)

                    continue

                chunks = create_chunks(text)

                store_chunks(
                    chunks,
                    uploaded_file.name
                )

                indexed_files.append(uploaded_file.name)

            except Exception as e:

                failed_files.append(uploaded_file.name)

                print(e)

                continue

# --------------------------------------------------
# Upload Summary
# --------------------------------------------------

if indexed_files or duplicate_files or failed_files:

    st.subheader("📄 Upload Summary")

    if indexed_files:

        with st.expander(
            f"✅ Indexed ({len(indexed_files)})",
            expanded=True
        ):
            for file in indexed_files:
                st.write(f"• {file}")

    if duplicate_files:

        with st.expander(
            f"⚠️ Already Indexed ({len(duplicate_files)})"
        ):
            for file in duplicate_files:
                st.write(f"• {file}")

    if failed_files:

        with st.expander(
            f"❌ Failed ({len(failed_files)})"
        ):
            for file in failed_files:
                st.write(f"• {file}")

st.divider()

# --------------------------------------------------
# Chat History
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# --------------------------------------------------
# Chat Input
# --------------------------------------------------

question = st.chat_input(
    "Ask a question about your documents"
)

# --------------------------------------------------
# Chat Logic
# --------------------------------------------------

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.spinner("Thinking..."):

        if has_documents():

            answer = ask_rag(
                question,
                st.session_state.messages
                )

        else:

            answer = (
                "⚠️ Please upload and process at least one PDF first."
            )

    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
    "Powered by Streamlit • Groq • Llama 3.3 • ChromaDB"
)