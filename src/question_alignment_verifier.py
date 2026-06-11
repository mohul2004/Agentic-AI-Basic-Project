# Measures relevancy of retrieved context to the original question

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def embedding_alignment_score(
        question,
        context):

    q_emb = embedding_model.encode(
        [question]
    )

    c_emb = embedding_model.encode(
        [context]
    )

    score = cosine_similarity(
        q_emb,
        c_emb
    )[0][0]

    return round(float(score), 3)


def compute_qcas(
        question,
        context):

    score = embedding_alignment_score(
        question,
        context
    )

    qcas = round(score * 10, 2)

    return {
        "embedding_score": score,
        "qcas": qcas
    }