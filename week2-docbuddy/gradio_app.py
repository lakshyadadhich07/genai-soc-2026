import gradio as gr

# PDF Loading
from langchain_community.document_loaders import PyPDFLoader

# Chunking
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Embeddings
from langchain_community.embeddings import HuggingFaceEmbeddings

# Vector DB
from langchain_community.vectorstores import Chroma

# Groq
from groq import Groq

# Environment Variables
from dotenv import load_dotenv
import os


# =====================================
# Load Environment Variables
# =====================================

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


# =====================================
# Embedding Model
# =====================================

embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

vectorstore = None


# =====================================
# INDEX DOCUMENTS
# PDF -> Chunks -> Embeddings -> ChromaDB
# =====================================

def index_documents(pdf_paths):

    global vectorstore

    all_chunks = []

    for pdf_path in pdf_paths:

        print(f"\nLoading {pdf_path}...")

        loader = PyPDFLoader(pdf_path)

        docs = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100
        )

        chunks = splitter.split_documents(docs)

        print("Pages:", len(docs))
        print("Chunks:", len(chunks))

        all_chunks.extend(chunks)

    vectorstore = Chroma.from_documents(
        documents=all_chunks,
        embedding=embeddings,
        persist_directory="./chroma_store"
    )

    print("\nStored", len(all_chunks), "chunks in ChromaDB")


# =====================================
# ASK QUESTION
# Retriever -> Context -> Groq
# =====================================

def ask(question):

    global vectorstore

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 5}
    )

    results = retriever.invoke(question)

    context = ""

    for doc in results:
        context += doc.page_content
        context += "\n\n"

    prompt = f"""
You are a helpful assistant.

Answer ONLY using the provided context.

If the answer is not present in the context,
say "I don't have that information."

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = response.choices[0].message.content

    sources = ""
    seen = set()

    for doc in results:

        source = doc.metadata.get("source", "Unknown")
        page = doc.metadata.get("page", 0) + 1

        key = (source, page)

        if key not in seen:

            seen.add(key)

            sources += (
                f"Source: {source}\n"
                f"Page: {page}\n\n"
            )

    return answer, sources


# =====================================
# Gradio Function
# =====================================

def answer_question(question):

    answer, sources = ask(question)

    return answer, sources


# =====================================
# Load PDF Once At Startup
# =====================================

index_documents([
    "ICT Mid sem notes.pdf"
])


# =====================================
# Gradio UI
# =====================================

demo = gr.Interface(
    fn=answer_question,
    inputs=gr.Textbox(
        label="Ask a Question",
        placeholder="What is Digital Twin?"
    ),
    outputs=[
        gr.Textbox(label="Answer"),
        gr.Textbox(label="Sources")
    ],
    title="DocBuddy",
    description="Ask questions about your PDF documents."
)

demo.launch()