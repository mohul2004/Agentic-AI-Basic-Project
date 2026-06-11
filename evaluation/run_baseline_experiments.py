import json

from evaluation.run_baseline import ask_baseline


QUESTIONS_FILE = "evaluation/questions.json"


def load_questions():

    with open(
        QUESTIONS_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def main():

    questions = load_questions()

    print(
        f"\nRunning "
        f"{len(questions)} questions..."
    )

    for i, item in enumerate(
            questions,
            start=1):

        question = item["question"]

        print("\n" + "=" * 60)
        print(
            f"QUESTION {i}"
        )
        print("=" * 60)

        print(
            f"\nQuestion:\n"
            f"{question}"
        )

        answer = ask_baseline(
            question
        )

        print(
            f"\nAnswer:\n"
            f"{answer}"
        )


if __name__ == "__main__":
    main()