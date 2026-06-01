#Main file for interactable questions

from src.rag_pipeline import ask_question


def main():

    print("\n" + "=" * 60)
    print("KIIT STUDENT HANDBOOK RAG ASSISTANT")
    print("=" * 60)

    print("\nAsk questions about:")
    print("- Academic Regulations")
    print("- Examination Rules")
    print("- Hostel Rules")
    print("- Code of Conduct")

    print("\nType 'exit' to quit.\n")

    while True:

        question = input("Question: ").strip()

        if question.lower() == "exit":
            print("\nGoodbye!")
            break

        if not question:
            continue

        try:

            result = ask_question(question)

            print("\n" + "-" * 60)
            print("ANSWER")
            print("-" * 60)

            print(result["answer"])

            print("\nSOURCES")

            shown_sources = set()

            for doc in result["documents"]:

                source = doc.metadata.get("source", "Unknown")

                if source not in shown_sources:
                    print(f"- {source}")
                    shown_sources.add(source)

            print("\n")

        except Exception as e:

            print("\nError:")
            print(e)
            print()

if __name__ == "__main__":
    main()