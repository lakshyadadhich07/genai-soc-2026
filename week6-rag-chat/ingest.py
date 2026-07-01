from langchain_text_splitters import CharacterTextSplitter

from langchain_community.document_loaders import (
    DirectoryLoader,
    PyPDFLoader
)

from langchain_huggingface import (
    HuggingFaceEmbeddings
)

from langchain_community.vectorstores import (
    Chroma
)


# LOAD PDFS

loader = DirectoryLoader(
    "docs",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs = loader.load()

print(
    f"Loaded {len(docs)} pages"
)


if len(docs) == 0:

    raise Exception(
        "No PDFs found inside docs/"
    )


# SPLIT

splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_documents(
    docs
)

print(
    f"Chunks created: {len(chunks)}"
)


# EMBEDDING

embedding = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)


# STORE

db = Chroma.from_documents(
    chunks,
    embedding,
    persist_directory="./vector_db"
)

print(
    "\nDatabase created"
)