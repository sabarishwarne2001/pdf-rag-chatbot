from pdf_processor import extract_text_from_pdf
from pdf_processor import create_chunks
from vector_store import store_chunks
from rag_engine import ask_rag
from vector_store import clear_database
import streamlit as st
from vector_store import has_documents


# Sidebar
st.sidebar.title("Database Controls")

if st.sidebar.button("🗑️ Clear Database"):

    clear_database()

    st.session_state.messages = []

    st.sidebar.success(
        "Database cleared successfully!"
    )

    st.rerun()


# Session State
if "messages" not in st.session_state:
    st.session_state.messages = []


# Title
st.title("📄 PDF RAG Chatbot")


# PDF Upload
uploaded_files = st.file_uploader(
    "Upload a PDF",
    type=["pdf"],
    accept_multiple_files=True
)

# UPLOAD AREA
if uploaded_files:

    with st.spinner("Processing PDFs..."):

        for uploaded_file in uploaded_files:

            pdf_path = f"data/{uploaded_file.name}"

            with open(pdf_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            text = extract_text_from_pdf(pdf_path)

            chunks = create_chunks(text)

            store_chunks(chunks,uploaded_file.name)

    st.success(f"{len(uploaded_files)} PDF(s) processed successfully!")


# Display Chat History
for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):
        st.markdown(
            message["content"]
        )


# Chat Input
question = st.chat_input(
    "Ask a question about your PDF"
)


# Chat Logic
if question:

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    # Display user message
    with st.chat_message("user"):
        st.markdown(question)

    # Generate answer
    with st.spinner("Thinking..."):
        
        if not has_documents():

            answer = (
        "⚠️ Please upload and process "
        "at least one PDF first."
        )

        else:
            answer = ask_rag(question)

    # Display assistant answer
    with st.chat_message("assistant"):
        st.markdown(answer)

    # Store assistant answer
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )