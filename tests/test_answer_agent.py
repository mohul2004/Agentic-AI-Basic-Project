#Questions from this answer agent to straight to Gemini

from src.answer_agent import generate_answer


def main():

    question = "Can students consume alcohol inside the hostel?"

    context = """
Smoking and consumption of alcoholic drinks and/or narcotic drugs
in the hostel premises is strictly prohibited.
"""

    answer = generate_answer(
        question,
        context
    )

    print("\nANSWER:\n")

    print(answer)


if __name__ == "__main__":
    main()