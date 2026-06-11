#Runs multiple questions from questions.json

import os
import json
import time

from src.rag_pipeline import ask_question


def load_questions():

    current_dir = os.path.dirname(
        os.path.abspath(__file__)
    )

    json_path = os.path.join(
        current_dir,
        "questions.json"
    )

    with open(
            json_path,
            "r",
            encoding="utf-8"
    ) as file:

        return json.load(file)


def main():

    questions = load_questions()

    print("\n" + "=" * 60)
    print("RUNNING EXPERIMENTS")
    print("=" * 60)

    total = len(questions)

    for index, item in enumerate(
            questions,
            start=1
    ):

        question = item["question"]

        print(
            f"\n[{index}/{total}] "
            f"{question}"
        )

        try:

            result = ask_question(
                question
            )

            print(
                f"Reliability: "
                f"{result['reliability']['score']}"
            )

            print(
                f"Label: "
                f"{result['reliability']['label']}"
            )

        except Exception as e:

            print(
                f"ERROR: {e}"
            )

        time.sleep(1)

    print("\n" + "=" * 60)
    print("EXPERIMENTS FINISHED")
    print("=" * 60)

    print(
        "\nResults saved to results.csv"
    )


if __name__ == "__main__":
    main()