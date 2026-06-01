#Testing the RAG Agent

from src.retriever import get_retriever


def main():

    retriever = get_retriever()

    query = "What is the attendance requirement?"

    docs = retriever.invoke(query)

    print("\nRESULTS:\n")

    for i, doc in enumerate(docs, start=1):

        print(f"\n----- DOCUMENT {i} -----\n")

        print(doc.page_content[:1000])

        print("\nSOURCE:")
        print(doc.metadata)


if __name__ == "__main__":
    main()