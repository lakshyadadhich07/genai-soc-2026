from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.tools import tool


embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)


vectorstore = Chroma(
    persist_directory="./vector_db",
    embedding_function=embedding_model
)


@tool
def search_documents(query: str) -> str:
    """
    Search uploaded PDF documents.
    """

    try:

        docs = vectorstore.similarity_search(
            query,
            k=3
        )

        if len(docs) == 0:

            return (
                "No uploaded documents found.\n"
                "Please upload a PDF first."
            )

        output = []

        for i, doc in enumerate(
            docs,
            start=1
        ):

            page = doc.metadata.get(
                "page",
                "unknown"
            )

            output.append(

                f"""
Source {i}
Page: {page}

{doc.page_content}
"""

            )

        return "\n".join(
            output
        )

    except Exception as e:

        return str(e)