#Database PDF -> Read -> Chunk -> Embed -> Store in FAISS

import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_FOLDER = os.path.join(BASE_DIR, "data")

VECTOR_STORE_PATH = os.path.join(
    BASE_DIR,
    "vectorstore",
    "faiss_index"
)

print(DATA_FOLDER)


def load_documents():
    """
    Load all PDFs from data folder.
    """

    documents = []

    for file in os.listdir(DATA_FOLDER):

        if file.endswith(".pdf"):

            pdf_path = os.path.join(DATA_FOLDER, file)

            print(f"Loading: {file}")

            loader = PyPDFLoader(pdf_path)

            documents.extend(loader.load())

    return documents


def split_documents(documents):
    """
    Split documents into chunks.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = text_splitter.split_documents(documents)

    return chunks


def create_vector_store(chunks):
    """
    Create embeddings and save FAISS index.
    """

    print("Loading embedding model...")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("Creating FAISS vector store...")

    vector_store = FAISS.from_documents(
        chunks,
        embeddings
    )

    vector_store.save_local(
        VECTOR_STORE_PATH
    )

    print("FAISS index saved successfully.")


def main():

    print("\n===== KIIT RAG INGESTION STARTED =====\n")

    documents = load_documents()

    print(f"\nTotal pages loaded: {len(documents)}")

    chunks = split_documents(documents)

    print(f"Total chunks created: {len(chunks)}")

    create_vector_store(chunks)

    print("\n===== INGESTION COMPLETED =====")


if __name__ == "__main__":
    print("Current Working Directory:")
    print(os.getcwd())
    main()