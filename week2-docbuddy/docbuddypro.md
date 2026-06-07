# 📄 DocBuddy

DocBuddy is a Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions about their content.

The system processes uploaded PDFs, converts the text into embeddings, stores them in a vector database, retrieves relevant chunks based on user queries, and uses a Large Language Model (LLM) to generate grounded answers.

---

## Features

* Upload PDF documents
* Automatic text chunking
* Semantic search using embeddings
* ChromaDB vector database
* Groq LLM integration
* Source citation with page numbers
* Interactive Gradio web interface

---

## Tech Stack

* Python
* LangChain
* HuggingFace Embeddings (all-MiniLM-L6-v2)
* ChromaDB
* Groq API
* Gradio

---

## Architecture

PDF Upload → PDF Loader → Text Splitter → Embeddings → ChromaDB → Retriever → Groq LLM → Answer + Sources

---

## Project Workflow

1. Upload a PDF document.
2. Extract text using PyPDFLoader.
3. Split text into chunks using RecursiveCharacterTextSplitter.
4. Generate vector embeddings using HuggingFace Embeddings.
5. Store vectors inside ChromaDB.
6. Retrieve the most relevant chunks for a user query.
7. Send retrieved context to Groq LLM.
8. Display grounded answers along with sources.

---

## Example Questions

* What is Digital Twin?
* Explain Cyber Physical Systems.
* Summarize the document.
* What are the applications of IoT?

---

## Future Improvements

* Multiple PDF support
* Chat history
* Better UI design
* Conversation memory
* Cloud deployment
* Hybrid search (keyword + semantic)

---
The screenshots are:-
![alt text](<Screenshot 2026-06-06 142706.png>)
![alt text](<Screenshot 2026-06-07 102855.png>)

## Author

Lakshya Dadhich
