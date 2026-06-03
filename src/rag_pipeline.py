#Connecting (PDF -> FAISS -> Retriever) with (Question + Context -> OpenRouter LLM -> Answer)

from src.retriever import get_retriever
from src.answer_agent import generate_answer
from src.verifier_agent import verify_answer


def ask_question(question):

    retriever = get_retriever()

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    answer_response = generate_answer(
        question,
        context
    )

    verification = verify_answer(
        question,
        context,
        answer_response
    )

    return {
        "response": answer_response,
        "verification": verification,
        "documents": docs
    }