from src.metrics import compute_metrics


sample = """
Step 1: SUPPORTED

Step 2: PARTIAL

Step 3: UNSUPPORTED

Step 4: SUPPORTED

Step 5: SUPPORTED
"""

result = compute_metrics(sample)

print(result)