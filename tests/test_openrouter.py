# tests/test_openrouter.py

from src.answer_agent import generate_answer


def main():

    answer = generate_answer(
        "Can students consume alcohol in the hostel?",
        """
        Smoking and consumption of alcoholic drinks
        and/or narcotic drugs in the hostel premises
        is strictly prohibited.
        """
    )

    print(answer)


if __name__ == "__main__":
    main()