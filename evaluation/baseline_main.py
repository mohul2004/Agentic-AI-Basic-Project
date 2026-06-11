# baseline_main.py

from evaluation.run_baseline import ask_baseline


def main():

    print("\n" + "=" * 60)
    print("VANILLA RAG ASSISTANT")
    print("=" * 60)

    print("\nType 'exit' to quit.\n")

    while True:

        question = input("Question: ")

        if question.lower() == "exit":
            break

        answer = ask_baseline(question)

        print("\n" + "-" * 60)
        print("ANSWER")
        print("-" * 60)

        print(answer)

        print()


if __name__ == "__main__":
    main()