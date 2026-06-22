import csv
import os

CSV_FILE = "results.csv"


def log_result(
        question,
        generated_answer,
        ground_truth,
        qcas,
        embedding_qcas,
        trs,
        hoi,
        cl,
        verdict,
        reliability_score,
        reliability_label
):

    file_exists = os.path.isfile(CSV_FILE)

    with open(
            CSV_FILE,
            "a",
            newline="",
            encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        if not file_exists:

            writer.writerow([
                "question",
                "generated_answer",
                "ground_truth",
                "qcas",
                "embedding_qcas",
                "trs",
                "hoi",
                "cl",
                "verdict",
                "reliability_score",
                "reliability_label"
            ])

        writer.writerow([
            question,
            generated_answer,
            ground_truth,
            qcas,
            embedding_qcas,
            trs,
            hoi,
            cl,
            verdict,
            reliability_score,
            reliability_label
        ])