import pandas as pd
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

tsv_file = BASE_DIR / "data" / "pubhealth.tsv"

df = pd.read_csv(
    tsv_file,
    sep="\t"
)

questions = []

for _, row in df.sample(
        n=50,
        random_state=42
).iterrows():

    claim = str(
        row["claim"]
    )

    label = str(
        row["label"]
    )

    question = (
        "Determine whether the following "
        "health claim is true or false:\n\n"
        + claim
    )

    questions.append({
        "question": question,
        "ground_truth": label
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
    f"Created {len(questions)} PubHealth questions."
)