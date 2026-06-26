from dotenv import load_dotenv
import os

load_dotenv()
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
import os

embedding = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory="vector_db",
    embedding_function=embedding
)

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

prompt = PromptTemplate(
input_variables=[
"context",
"question"
],
template="""
You are HybridSight.

Answer ONLY using facts.

Rules:
- Read ALL facts.
- Combine relevant facts.
- Do NOT stop after first fact.
- Keep answer short.

Facts:
{context}

Question:
{question}

Answer:
"""
)
while True:

    q = input("\nAsk: ")

    if q == "exit":
        break

    retriever = db.as_retriever(
    search_kwargs={
        "k": 3
    }
)

    docs = retriever.invoke(q) #list of document objects

    context = ""

    for i, doc in enumerate(docs, start=1):
        context += (
            f"Fact {i}: "
            f"{doc.page_content}\n"
        )

    final_prompt = prompt.format(
        context=context,
        question=q
    )

    response = llm.invoke(
    final_prompt,
    temperature=0
)

    print("\nContext Used:\n")
    print(context)

    print("\nAnswer:\n")
    print(response.content)