import pandas as pd

df = pd.read_parquet(
    r"..\data\WiKiEvaltrain-00000-of-00001-385c01e94624e9b7.parquet"
)

print(df.columns)

df.to_csv(
    r"..\data\WikiEval.csv",
    index=False
)

print("Done")