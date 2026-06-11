#Basic RAG

from src.retriever import get_retriever
from src.answer_agent import generate_answer


def ask_baseline(question):

    retriever = get_retriever()

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    answer = generate_answer(
        question,
        context
    )

    return answer