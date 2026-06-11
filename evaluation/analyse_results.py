import pandas as pd


CSV_FILE = "results.csv"


def main():

    df = pd.read_csv(CSV_FILE)

    print("\n" + "=" * 60)
    print("RESULTS SUMMARY")
    print("=" * 60)

    print(
        f"\nTotal Questions : {len(df)}"
    )

    print(
        f"Average QCAS    : {df['qcas'].mean():.3f}"
    )

    print(
        f"Average TRS     : {df['trs'].mean():.3f}"
    )

    print(
        f"Average HOI     : {df['hoi'].fillna(0).mean():.3f}"
    )

    print(
        f"Average CL      : {df['cl'].mean():.3f}"
    )

    print(
        f"Average Reliability : "
        f"{df['reliability_score'].mean():.3f}"
    )

    print("\n" + "=" * 60)
    print("LABEL DISTRIBUTION")
    print("=" * 60)

    print(
        df["reliability_label"]
        .value_counts()
    )

    print("\n" + "=" * 60)
    print("VERDICT DISTRIBUTION")
    print("=" * 60)

    print(
        df["verdict"]
        .value_counts()
    )

    print("\n" + "=" * 60)
    print("HIGHEST RELIABILITY")
    print("=" * 60)

    best = df.loc[
        df["reliability_score"].idxmax()
    ]

    print(
        f"\nQuestion:\n"
        f"{best['question']}"
    )

    print(
        f"\nReliability: "
        f"{best['reliability_score']}"
    )

    print(
        f"HOI: {best['hoi']}"
    )

    print(
        f"CL : {best['cl']}"
    )

    print("\n" + "=" * 60)
    print("LOWEST RELIABILITY")
    print("=" * 60)

    worst = df.loc[
        df["reliability_score"].idxmin()
    ]

    print(
        f"\nQuestion:\n"
        f"{worst['question']}"
    )

    print(
        f"\nReliability: "
        f"{worst['reliability_score']}"
    )

    print(
        f"HOI: {worst['hoi']}"
    )

    print(
        f"CL : {worst['cl']}"
    )

    print("\n" + "=" * 60)
    print("HIGHEST HOI")
    print("=" * 60)

    max_hoi = df["hoi"].max()

    hoi_rows = df[
        df["hoi"] == max_hoi
    ]

    for _, row in hoi_rows.iterrows():

        print(
            f"\nQuestion:\n"
            f"{row['question']}"
        )

        print(
            f"HOI: {row['hoi']}"
        )

        print(
            f"CL : {row['cl']}"
        )

    print("\n" + "=" * 60)
    print("HIGHEST CL")
    print("=" * 60)

    max_cl = df["cl"].max()

    cl_rows = df[
        df["cl"] == max_cl
    ]

    for _, row in cl_rows.iterrows():

        print(
            f"\nQuestion:\n"
            f"{row['question']}"
        )

        print(
            f"HOI: {row['hoi']}"
        )

        print(
            f"CL : {row['cl']}"
        )


if __name__ == "__main__":
    main()