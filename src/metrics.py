#Trace Verifier Output -> Parse Labels -> Compute Metrics -> TRS, HOI, CL
#TRS = Trace Reliability Score
#HOI = Hallucination Origin Index
#CL = Cascade Length

import re


def extract_labels(trace_data):

    labels = []

    for step in trace_data["steps"]:
        labels.append(step["label"])

    return labels


def calculate_trs(labels):
    weights = {
        "SUPPORTED": 1.0,
        "PARTIAL": 0.75,
        "UNSUPPORTED": 0.0
    }

    if not labels:
        return 0

    total = sum(weights[label] for label in labels)

    return round(total / len(labels), 3)


def calculate_hoi(labels):

    for i, label in enumerate(labels):

        if label in [
            "PARTIAL",
            "UNSUPPORTED",
            "CONTRADICTED"
        ]:
            return i + 1

    return None


def calculate_cl(labels, hoi):
    """
    Cascade Length
    """

    if hoi is None:
        return 0

    return len(labels) - hoi + 1


def compute_metrics(trace_verification_text):

    labels = extract_labels(trace_verification_text)

    trs = calculate_trs(labels)

    hoi = calculate_hoi(labels)

    cl = calculate_cl(labels, hoi)

    return {
        "labels": labels,
        "trs": trs,
        "hoi": hoi,
        "cl": cl
    }