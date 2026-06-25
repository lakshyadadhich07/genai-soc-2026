from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

loader = TextLoader(
    "docs/notes.txt",
    encoding="utf-8"
)

docs = loader.load()

splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=50,
    chunk_overlap=0
)

chunks = splitter.split_documents(docs)

print("Chunks created:")
for c in chunks:
    print("---")
    print(c.page_content)

embedding = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

db = Chroma.from_documents(
    chunks,
    embedding,
    persist_directory="vector_db"
)

print("\nRAG database created")