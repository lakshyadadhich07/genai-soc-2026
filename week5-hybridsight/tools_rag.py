from langchain_community.vectorstores import (
    Chroma
)

from langchain_community.embeddings import (
    HuggingFaceEmbeddings
)

from langchain_core.tools import tool


embedding_model = (
    HuggingFaceEmbeddings(
        model_name=
        "all-MiniLM-L6-v2"
    )
)


vectorstore = (
    Chroma(

        persist_directory=
        "./chroma_store",

        embedding_function=
        embedding_model,

        collection_name=
        "lecture_notes"
    )
)


@tool
def search_documents(
    query: str
):

    """
    Search uploaded PDFs.
    Use for notes,
    lecture questions,
    uploaded content.
    """

    docs = (
        vectorstore.similarity_search(
            query,
            k=3
        )
    )

    if not docs:

        return (
            "No document found."
        )

    return "\n\n".join(

        [

            doc.page_content

            for doc

            in docs

        ]

    )