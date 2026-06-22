# Connecting:
# Dataset -> FAISS -> Retriever
# Question + Context -> LLM -> Answer

from src.retriever import get_retriever
from src.answer_agent import generate_answer
from src.verifier_agent import verify_answer
from src.trace_verifier import verify_trace
from src.metrics import compute_metrics
from src.question_alignment_verifier import compute_qcas
from src.reliability_engine import compute_reliability
from src.logger import log_result

from src.verifier_agent import extract_final_answer

import re


def extract_verdict(text):

    match = re.search(
        r"VERDICT:\s*(SUPPORTED|UNSUPPORTED)",
        text
    )

    if match:
        return match.group(1)

    return "UNKNOWN"


def ask_question(
        question,
        ground_truth=""
):

    # -------------------------
    # Retrieval
    # -------------------------

    retriever = get_retriever()

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    # -------------------------
    # Question Context Alignment
    # -------------------------

    alignment_data = compute_qcas(
        question,
        context
    )

    qcas = alignment_data["qcas"]

    embedding_qcas = alignment_data[
        "embedding_score"
    ]

    # -------------------------
    # Answer Generation
    # -------------------------

    answer_response = generate_answer(
        question,
        context
    )

    # -------------------------
    # Trace Verification
    # -------------------------

    trace_verification = verify_trace(
        question,
        context,
        answer_response
    )

    metrics = compute_metrics(
        trace_verification
    )

    # -------------------------
    # Final Answer Extraction
    # -------------------------

    final_answer = extract_final_answer(
        answer_response
    )

    # -------------------------
    # Answer Verification
    # -------------------------

    verification = verify_answer(
        question,
        context,
        final_answer
    )

    verdict = extract_verdict(
        verification
    )

    # -------------------------
    # Reliability Engine
    # -------------------------

    reliability = compute_reliability(
        qcas=qcas,
        trs=metrics["trs"],
        hoi=metrics["hoi"],
        cl=metrics["cl"],
        verifier_verdict=verdict
    )

    # -------------------------
    # CSV Logging
    # -------------------------

    log_result(
        question=question,
        generated_answer=final_answer,
        ground_truth=ground_truth,
        qcas=qcas,
        embedding_qcas=embedding_qcas,
        trs=metrics["trs"],
        hoi=metrics["hoi"],
        cl=metrics["cl"],
        verdict=verdict,
        reliability_score=reliability["score"],
        reliability_label=reliability["label"]
    )

    # -------------------------
    # Return Everything
    # -------------------------

    return {
        "response": answer_response,
        "trace_verification": trace_verification,
        "verification": verification,
        "alignment_report": alignment_data,
        "qcas": qcas,
        "embedding_qcas": embedding_qcas,
        "metrics": metrics,
        "verdict": verdict,
        "documents": docs,
        "reliability": reliability,
        "final_answer": final_answer
    }