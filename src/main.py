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
            print("QUESTION-CONTEXT ALIGNMENT")
            print("-" * 60)

            alignment = result["alignment_report"]

            print(
                f"Embedding Similarity : "
                f"{alignment['embedding_score']}"
            )

            print(
                f"QCAS : "
                f"{alignment['qcas']}/10"
            )

            print("\n" + "-" * 60)
            print("RESPONSE")
            print("-" * 60)

            print(result["response"])

            print("\n" + "-" * 60)
            print("TRACE VERIFICATION")
            print("-" * 60)

            print(result["trace_verification"])

            print("\n" + "-" * 60)
            print("TRACE METRICS")
            print("-" * 60)

            metrics = result["metrics"]

            print(f"TRS : {metrics['trs']}")
            print(f"HOI : {metrics['hoi']}")
            print(f"CL  : {metrics['cl']}")

            print("\n" + "-" * 60)
            print("VERIFICATION")
            print("-" * 60)

            print(result["verification"])

            print("\n" + "-" * 60)
            print("RELIABILITY ENGINE")
            print("-" * 60)

            print(
                f"Reliability Score : "
                f"{result['reliability']['score']}"
            )

            print(
                f"Reliability Label : "
                f"{result['reliability']['label']}"
            )

        except Exception as e:

            print("\nError:")
            print(e)
            print()

if __name__ == "__main__":
    main()