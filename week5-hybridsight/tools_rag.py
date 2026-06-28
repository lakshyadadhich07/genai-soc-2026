from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.tools import tool


embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)


vectorstore = Chroma(
    persist_directory="./chroma_store",
    embedding_function=embedding_model,
    collection_name="lecture_notes"
)


@tool
def search_documents(query: str) -> str:
    """
    Search uploaded PDFs and return relevant document chunks.
    """

    try:

        docs = vectorstore.similarity_search(
            query=query,
            k=3
        )

        if not docs:

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
                f"Source {i}\n"
                f"Page: {page}\n\n"
                f"{doc.page_content}"
            )

        return "\n\n".join(output)

    except Exception as e:

        return str(e)