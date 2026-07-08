# Traces reasoning steps and verifies each step
# against the most relevant evidence chunk.

import re

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from src.answer_agent import get_llm


embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def extract_steps(reasoning_trace):

    pattern = r"Step\s+\d+:\s*(.*)"

    matches = re.findall(
        pattern,
        reasoning_trace
    )

    return matches


def get_best_evidence_chunk(
        step,
        context
):

    chunks = context.split("\n\n")

    step_embedding = embedding_model.encode(
        [step]
    )

    best_similarity = -1
    best_chunk = ""

    for chunk in chunks:

        chunk_embedding = embedding_model.encode(
            [chunk]
        )

        similarity = cosine_similarity(
            step_embedding,
            chunk_embedding
        )[0][0]

        if similarity > best_similarity:

            best_similarity = similarity
            best_chunk = chunk

    return (
        best_chunk,
        round(float(best_similarity), 3)
    )


def verify_reasoning_step(
        llm,
        question,
        evidence,
        step
):

    prompt = f"""
You are a strict reasoning verification agent.

QUESTION:
{question}

EVIDENCE:
{evidence}

REASONING STEP:
{step}

Classify the reasoning step.

SUPPORTED:
- Directly supported by evidence.

PARTIAL:
- Some support exists.
- Contains assumptions.
- Extends beyond evidence.

UNSUPPORTED:
- Contradicts evidence.
- Introduces facts not present.
- Makes conclusions not justified.

Respond with ONLY one word:

SUPPORTED

or

PARTIAL

or

UNSUPPORTED
"""

    response = llm.invoke(prompt)

    label = response.content.strip().upper()

    if label not in [
        "SUPPORTED",
        "PARTIAL",
        "UNSUPPORTED"
    ]:
        label = "PARTIAL"

    return label


def verify_trace(
        question,
        context,
        reasoning_trace
):

    llm = get_llm()

    steps = extract_steps(
        reasoning_trace
    )

    results = []

    for idx, step in enumerate(
            steps,
            start=1):

        evidence_chunk, similarity = (
            get_best_evidence_chunk(
                step,
                context
            )
        )

        label = verify_reasoning_step(
            llm,
            question,
            evidence_chunk,
            step
        )

        results.append(
            {
                "step": idx,
                "text": step,
                "evidence": evidence_chunk,
                "similarity": similarity,
                "label": label
            }
        )

    return {
        "steps": results
    }

