import pandas as pd
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

tsv_file = BASE_DIR / "data" / "popqatest.tsv"

df = pd.read_csv(
    tsv_file,
    sep="\t"
)

questions = []

for _, row in df.head(50).iterrows():

    questions.append({
        "question": str(row["question"]),
        "ground_truth": str(row["possible_answers"])
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
    f"Created {len(questions)} PopQA questions."
)