from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory="vector_db",
    embedding_function=embedding
)

while True:

    q = input("\nAsk: ")

    if q == "exit":
        break

    results = db.similarity_search(
        q,
        k=1
    )

    print("\nBest Match:\n")

    print(results[0].page_content)

    print("\n--------------------")