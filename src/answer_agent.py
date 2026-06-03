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
You are a reasoning agent for a university handbook assistant.

Using ONLY the provided context:

1. Create a reasoning trace.
2. Use numbered reasoning steps.
3. Keep each step concise.
4. Then provide a final answer.

Format exactly as:

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