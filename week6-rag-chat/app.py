import gradio as gr

from dotenv import load_dotenv

load_dotenv()

from tools_rag import search_documents
from langchain_groq import ChatGroq


llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

def ask(query):

    context = search_documents.invoke(
        query
    )

    prompt = f"""
You are a helpful assistant.

Answer ONLY using the context.

Context:

{context}


Question:

{query}


Answer briefly.
"""

    result = llm.invoke(
        prompt
    )

    return result.content


with gr.Blocks() as app:

    gr.Markdown(
        "# Week 6 • RAG Chat"
    )

    query = gr.Textbox(
        label="Ask Question"
    )

    output = gr.Textbox(
        label="Answer",
        lines=10
    )

    submit = gr.Button(
        "Submit"
    )

    submit.click(
        ask,
        inputs=query,
        outputs=output
    )


app.launch()