from src.answer_agent import get_llm


def verify_answer(question, context, response_text):

    llm = get_llm()

    prompt = f"""
You are a verification agent.

Your job is to determine whether the reasoning
and final answer are supported by the provided context.

Question:
{question}

Context:
{context}

Response:
{response_text}

Return exactly:

VERDICT: SUPPORTED

or

VERDICT: UNSUPPORTED

Then provide a short explanation.
"""

    response = llm.invoke(prompt)

    return response.content