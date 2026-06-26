from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader

loader = DirectoryLoader(
    "docs",
    glob="*.txt",
    loader_cls=TextLoader
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