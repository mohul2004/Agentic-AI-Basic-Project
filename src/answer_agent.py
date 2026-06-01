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
You are the KIIT Student Handbook Assistant.

Answer ONLY using the provided context.

If the answer is not found in the context, say:
"I could not find that information in the provided documents."

Question:
{question}

Context:
{context}

Answer:
"""

    response = llm.invoke(prompt)

    return response.content