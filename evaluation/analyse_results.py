import pandas as pd

df = pd.read_csv("results.csv")

print("\n========================")
print("EXPERIMENT RESULTS")
print("========================")

print(
    f"Average QCAS : "
    f"{df['qcas'].mean():.3f}"
)

print(
    f"Average TRS : "
    f"{df['trs'].mean():.3f}"
)

print(
    f"Average HOI : "
    f"{df['hoi'].mean():.3f}"
)

print(
    f"Average CL : "
    f"{df['cl'].mean():.3f}"
)

print(
    f"Average Reliability : "
    f"{df['reliability_score'].mean():.3f}"
)

# ------------------
# Accuracy
# ------------------

correct = 0

for _, row in df.iterrows():

    answer = str(
        row["generated_answer"]
    ).lower()

    truth = str(
        row["ground_truth"]
    ).lower()

    if truth in answer:
        correct += 1

accuracy = (
    correct / len(df)
) * 100

print(
    f"Accuracy : "
    f"{accuracy:.2f}%"
)