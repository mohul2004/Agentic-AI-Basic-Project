# Helps measure and judge the entire process


def compute_reliability(
        qcas,
        trs,
        hoi,
        cl,
        verifier_verdict
):

    q = qcas / 10

    t = trs

    v = (
        1.0
        if verifier_verdict == "SUPPORTED"
        else 0.0
    )

    hoi_penalty = (
        min(hoi / 10, 1.0)
        if hoi is not None
        else 0.0
    )

    cl_penalty = min(cl / 10, 1.0)

    score = (
        0.35 * q +
        0.35 * t +
        0.25 * v -
        0.03 * hoi_penalty -
        0.02 * cl_penalty
    )

    score = max(
        0.0,
        min(score, 1.0)
    )

    if score >= 0.80:
        label = "RELIABLE"

    elif score >= 0.60:
        label = "QUESTIONABLE"

    else:
        label = "UNRELIABLE"

    return {
        "score": round(score, 3),
        "label": label
    }