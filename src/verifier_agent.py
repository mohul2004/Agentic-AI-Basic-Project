from src.answer_agent import get_llm


def verify_answer(question, context, response_text):

    llm = get_llm()

    prompt = f"""
You are an academic answer verification agent.

Your task is to determine whether the FINAL ANSWER correctly answers the QUESTION using the CONTEXT.

Evaluation Rules:

1. First identify what the QUESTION is actually asking.

2. Determine the MAIN RULE in the context that answers the question.

3. Distinguish between:
   - General rules
   - Special cases
   - Exceptions
   - Additional conditions

4. The answer should be judged against the MAIN RULE that most directly answers the question.

5. Do NOT reject an answer simply because additional conditions exist in the context.

6. Do NOT prefer exceptions over general rules unless the question explicitly asks about exceptions.

7. If the answer correctly states the main rule, mark it SUPPORTED even if additional related information exists.

8. Mark UNSUPPORTED if:
   - the answer contradicts the context
   - the answer uses an exception instead of the general rule
   - the answer ignores the rule that most directly answers the question
   - the answer cannot be derived from the context

9. Be careful with synonymous phrases.

Examples:
- "sit for an examination"
- "appear in an examination"
- "take an examination"

should normally be treated as equivalent unless the context explicitly distinguishes them.

Output Format:

VERDICT: SUPPORTED

or

VERDICT: UNSUPPORTED

Explanation:
<short explanation>

QUESTION:
{question}

CONTEXT:
{context}

ANSWER:
{response_text}
"""

    response = llm.invoke(prompt)

    return response.content