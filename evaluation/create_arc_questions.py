import pandas as pd
import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

csv_file = BASE_DIR / "data" / "ARC-Challenge-Dev.csv"

df = pd.read_csv(csv_file)

questions = []

for _, row in df.head(50).iterrows():

    question_text = str(row["question"])
    answer_key = str(row["AnswerKey"]).strip()

    option_pattern = r"\(([A-D])\)\s*(.*?)(?=\([A-D]\)|$)"

    matches = re.findall(
        option_pattern,
        question_text
    )

    correct_answer = ""

    for label, option_text in matches:

        if label == answer_key:

            correct_answer = option_text.strip()
            break

    questions.append({
        "question": question_text,
        "ground_truth": correct_answer,
        "answer_key": answer_key
    })

with open(
    BASE_DIR / "evaluation" / "questions.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        questions,
        f,
        indent=4,
        ensure_ascii=False
    )

print(
    f"Created {len(questions)} questions."
)