#Testing the RAG pipeline

from src.rag_pipeline import ask_question


def main():

    question = "What is the attendance requirement?"

    result = ask_question(question)

    print("\n===== ANSWER =====\n")

    print(result["answer"])

    print("\n===== SOURCES =====\n")

    for doc in result["documents"]:
        print(doc.metadata)


if __name__ == "__main__":
    main()