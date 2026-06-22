#Database PDF -> Read -> Chunk -> Embed -> Store in FAISS

import os
import pandas as pd
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_FOLDER = os.path.join(BASE_DIR, "data")

VECTOR_STORE_PATH = os.path.join(
    BASE_DIR,
    "vectorstore",
    "faiss_index"
)

print(DATA_FOLDER)


def load_documents():

    documents = []

    for file in os.listdir(DATA_FOLDER):

        file_path = os.path.join(
            DATA_FOLDER,
            file
        )

        print(f"Loading: {file}")

        # ---------------------
        # PDF
        # ---------------------

        if file.endswith(".pdf"):

            loader = PyPDFLoader(
                file_path
            )

            documents.extend(
                loader.load()
            )

        # ---------------------
        # CSV
        # ---------------------

        elif file.endswith(".csv"):

            df = pd.read_csv(
                file_path
            )

            for _, row in df.iterrows():

                text = " ".join(
                    str(v)
                    for v in row.values
                )

                documents.append(
                    Document(
                        page_content=text
                    )
                )

        # ---------------------
        # TSV
        # ---------------------

        elif file.endswith(".tsv"):

            df = pd.read_csv(
                file_path,
                sep="\t"
            )

            for _, row in df.iterrows():

                text = " ".join(
                    str(v)
                    for v in row.values
                )

                documents.append(
                    Document(
                        page_content=text
                    )
                )

        # ---------------------
        # PARQUET
        # ---------------------

        elif file.endswith(".parquet"):

            df = pd.read_parquet(
                file_path
            )

            print(df.columns.tolist())

            for _, row in df.iterrows():

                # ARC-Challenge

                if (
                        "question" in df.columns
                        and "answerKey" in df.columns
                ):

                    text = f"""
        Question:
        {row['question']}

        Choices:
        {row['choices']}

        Answer:
        {row['answerKey']}
        """

                # PubHealth

                elif (
                        "claim" in df.columns
                ):

                    text = f"""
        Claim:
        {row['claim']}

        Label:
        {row.get('label', '')}
        """

                # Generic fallback

                else:

                    text = " ".join(
                        str(v)
                        for v in row.values
                    )

                documents.append(
                    Document(
                        page_content=text
                    )
                )

        # ---------------------
        # TXT
        # ---------------------

        elif file.endswith(".txt"):

            with open(
                    file_path,
                    "r",
                    encoding="utf-8"
            ) as f:

                text = f.read()

            documents.append(
                Document(
                    page_content=text
                )
            )

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