#Retriever -> Relevant Chunks -> Gemini -> Answer

import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


def get_llm():

    api_key = os.getenv("OPENROUTER_API_KEY")

    llm = ChatOpenAI(
        model="meta-llama/llama-3.1-8b-instruct",
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
        temperature=0
    )

    return llm


def generate_answer(question, context):

    llm = get_llm()

    prompt = f"""
    You are a retrieval-grounded reasoning agent.

    Your task is to answer the user's question using ONLY the retrieved context.

    Rules:

    1. Use only information present in the context.
    2. Do not use outside knowledge.
    3. Generate at most 3 reasoning steps.
    4. Every reasoning step must directly support the final answer.
    5. Ignore unrelated information.
    6. Prefer the main rule over exceptions unless the question explicitly asks about exceptions.
    7. Interpret synonymous phrases naturally.
       Example:
       - "sit for an exam"
       - "appear in an exam"
       should be treated as equivalent unless the context explicitly distinguishes them.
    8. Before producing the final answer, ensure it is consistent with all reasoning steps.
    9. If the context contains multiple rules, identify the rule that most directly answers the question.
    10. If the answer cannot be determined from the context, explicitly state:
        "Insufficient information in the provided context."

    Output format:

    REASONING TRACE

    Step 1: ...

    Step 2: ...

    Step 3: ...

    FINAL ANSWER

    ...

    Question:
    {question}

    Context:
    {context}
    """

    response = llm.invoke(prompt)

    return response.content