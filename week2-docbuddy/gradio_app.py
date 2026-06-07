import gradio as gr

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

from groq import Groq
from dotenv import load_dotenv

import os

# =====================================
# Load API Key
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
# PDF -> Chunks -> ChromaDB
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

    import shutil

    if os.path.exists("./chroma_store"):
        shutil.rmtree("./chroma_store")
    
    vectorstore = Chroma.from_documents(
        documents=all_chunks,
        embedding=embeddings,
        persist_directory="./chroma_store"
    )

    print(f"\nStored {len(all_chunks)} chunks in ChromaDB")

    return f"Successfully indexed {len(all_chunks)} chunks."


# =====================================
# Upload PDF
# =====================================

def upload_pdf(pdf_file):

    if pdf_file is None:
        return "Please upload a PDF."

    return index_documents([pdf_file.name])


# =====================================
# Ask Question
# =====================================

def ask(question):

    global vectorstore

    if vectorstore is None:
        return (
            "Please upload and process a PDF first.",
            ""
        )

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 5}
    )

    results = retriever.invoke(question)

    context = ""

    for doc in results:
        context += doc.page_content + "\n\n"

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

    seen = set()
    sources = ""

    for doc in results:

        source = doc.metadata.get(
            "source",
            "Unknown"
        )

        page = doc.metadata.get(
            "page",
            0
        ) + 1

        key = (source, page)

        if key not in seen:

            seen.add(key)

            sources += (
                f"Source: {source}\n"
                f"Page: {page}\n\n"
            )

    return answer, sources


# =====================================
# Gradio UI
# =====================================

with gr.Blocks() as demo:

    gr.Markdown("# 📄 DocBuddy")

    gr.Markdown(
        "Upload a PDF and ask questions about it."
    )

    pdf_file = gr.File(
        label="Upload PDF",
        file_types=[".pdf"]
    )

    upload_btn = gr.Button(
        "Process PDF"
    )

    upload_status = gr.Textbox(
        label="Status"
    )

    upload_btn.click(
        fn=upload_pdf,
        inputs=pdf_file,
        outputs=upload_status
    )

    question = gr.Textbox(
        label="Question",
        placeholder="What is Digital Twin?"
    )

    ask_btn = gr.Button(
        "Ask"
    )

    answer_box = gr.Textbox(
        label="Answer",
        lines=6
    )

    sources_box = gr.Textbox(
        label="Sources",
        lines=4
    )

    ask_btn.click(
        fn=ask,
        inputs=question,
        outputs=[
            answer_box,
            sources_box
        ]
    )

demo.launch()