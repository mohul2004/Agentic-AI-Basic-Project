from src.answer_agent import get_llm


def extract_final_answer(response_text):

    if "FINAL ANSWER" in response_text:

        return response_text.split(
            "FINAL ANSWER"
        )[-1].strip()

    return response_text

def verify_answer(question, context, response_text):

    llm = get_llm()

    prompt = f"""
    You are a strict answer verification agent.

    Your task is to determine whether the FINAL ANSWER is supported by the CONTEXT and correctly answers the QUESTION.

    Verification Procedure:

    STEP 1:
    Identify what the QUESTION is asking.

    STEP 2:
    Identify the key facts in the CONTEXT relevant to the question.

    STEP 3:
    Determine whether the FINAL ANSWER can be reasonably derived from those facts.

    Important Rules:

    1. Focus on semantic meaning, not exact wording.

    2. Treat synonymous phrases as equivalent.

    Examples:
    - appear in an examination
    - sit for an examination
    - take an examination

    may be treated as equivalent unless explicitly distinguished.

    3. An answer may be more concise than the context.

    4. An answer does NOT need to repeat every supporting fact.

    5. If the answer correctly captures the meaning of the relevant evidence, mark SUPPORTED.

    6. Mark UNSUPPORTED only if:
       - it contradicts evidence
       - it introduces unsupported claims
       - it cannot be derived from evidence
       - it answers a different question

    7. Do NOT reject an answer merely because additional details exist in the context.

    Output format:

    VERDICT: SUPPORTED

    or

    VERDICT: UNSUPPORTED

    Explanation:
    <1-2 sentence explanation>

    QUESTION:
    {question}

    CONTEXT:
    {context}

    ANSWER:
    {response_text}
    """

    response = llm.invoke(prompt)

    return response.content