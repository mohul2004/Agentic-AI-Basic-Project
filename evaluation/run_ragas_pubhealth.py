import os
import pandas as pd
from datasets import Dataset
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEmbeddings
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_precision
)

load_dotenv()

# --- Configure OpenRouter LLM ---
openrouter_llm = ChatOpenAI(
    model="meta-llama/llama-3.1-70b-instruct",
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1",
)

# --- Configure local HuggingFace Embeddings ---
hf_embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# --- Wrap for RAGAS ---
wrapped_llm = LangchainLLMWrapper(openrouter_llm)
wrapped_embeddings = LangchainEmbeddingsWrapper(hf_embeddings)

# --- Load CSV ---
df = pd.read_csv("results_pubhealth_ragas_ready.csv")

# --- Build RAGAS Dataset ---
dataset = Dataset.from_dict({
    "question": df["question"].tolist(),
    "answer": df["generated_answer"].tolist(),
    "contexts": [
        [ctx] for ctx in df["retrieved_context"].tolist()
    ],
    "ground_truth": df["ground_truth"].astype(str).tolist()
})

# --- Run Evaluation ---
result = evaluate(
    dataset,
    metrics=[
        faithfulness,
        answer_relevancy,
        context_precision
    ],
    llm=wrapped_llm,
    embeddings=wrapped_embeddings,
)

# --- Save Results ---
ragas_df = result.to_pandas()
final_df = pd.concat([df, ragas_df], axis=1)
final_df.to_csv("ragas_pubhealth_results.csv", index=False)

print("\nDone")
print(
    final_df[[
        "faithfulness",
        "answer_relevancy",
        "context_precision"
    ]].mean()
)