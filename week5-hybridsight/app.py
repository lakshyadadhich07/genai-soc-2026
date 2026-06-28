import gradio as gr

from ingest import loader
from ingest import splitter
from ingest import embedding

from langchain_community.vectorstores import Chroma

from langchain_community.document_loaders import PyPDFLoader


from agent import ask_agent
from tools_vision import describe_image
from tools_rag import search_documents
from langchain_groq import ChatGroq
import os
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv(
        "GROQ_API_KEY"
    )
)

# ======================
# PDF INDEXING
# ======================

def index_pdf(pdf):

    try:

        if pdf is None:
            return "Upload a PDF first."

        # LOAD UPLOADED PDF
        loader = PyPDFLoader(
            pdf.name
        )

        docs = loader.load()

        # SPLIT
        chunks = splitter.split_documents(
            docs
        )

        # RESET OLD DATABASE
        Chroma.from_documents(

            documents=chunks,

            embedding=embedding,

            persist_directory="./chroma_store",

            collection_name="lecture_notes"

        )

        return (
            f"Indexed {len(chunks)} chunks."
        )

    except Exception as e:

        return str(e)

# ======================
# MAIN AGENT
# ======================
def run(query, image):

    try:

        # IMAGE
        if image is not None:

            return describe_image(
                image
            )

        # GET CONTEXT
        context = search_documents.invoke(
            query
        )

        if "No uploaded" in context:

            return "I don't know."

        # SEND TO LLM
        prompt = f"""
Use ONLY this context.

Context:
{context}

Question:
{query}

Answer naturally.
"""

        answer = llm.invoke(
            prompt
        )

        return answer.content

    except Exception as e:

        return str(e)

# ======================
# UI
# ======================

with gr.Blocks() as app:

    gr.Markdown(
        "# HybridSight"
    )

    pdf = gr.File(
        label="Upload PDF"
    )

    upload_btn = gr.Button(
        "Index PDF"
    )

    upload_status = gr.Textbox(
        label="Index Status"
    )

    upload_btn.click(

        fn=index_pdf,

        inputs=pdf,

        outputs=upload_status

    )

    query = gr.Textbox(
        label="Ask HybridSight"
    )

    image = gr.Image(
        type="filepath",
        label="Upload Image"
    )

    submit = gr.Button(
        "Submit"
    )

    answer = gr.Textbox(
        label="Answer"
    )

    submit.click(

        fn=run,

        inputs=[
            query,
            image
        ],

        outputs=answer

    )


app.launch()