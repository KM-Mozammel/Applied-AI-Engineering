"""
04_numpy_ultimate_pipeline.py
Focus: Fancy indexing, Dimension adjustment, Concatenation, and Vectorized Thresholding.
"""
import numpy as np

# 1. Initialize random generator for reproducibility
rng = np.random.default_rng(seed=2026)

print("--- STEP 1: CONCATENATION & STACKING ---")
# Simulating two independent data source streams (Features for 2 samples each)
stream_a = np.array([[0.5, 1.5], [2.3, 0.7]])
stream_b = np.array([[1.1, -0.4], [0.1, 3.2]])

# Merge streams vertically to form a single combined dataset
dataset = np.vstack((stream_a, stream_b))
print(f"Combined Dataset Matrix Shape {dataset.shape}:\n{dataset}")


print("\n--- STEP 2: FANCY INDEXING (Mini-batching) ---")
# Randomly select sample indices to simulate training batch steps
shuffled_indices = rng.choice(len(dataset), size=2, replace=False)
print(f"Selected Batch Indices: {shuffled_indices}")

mini_batch = dataset[shuffled_indices]
print(f"Extracted Mini-Batch:\n{mini_batch}")


print("\n--- STEP 3: EXPANDING DIMENSIONS (Framework Alignment) ---")
# Select a single sample feature vector
single_sample = dataset[0] # Shape: (2,)
print(f"Raw Sample Shape: {single_sample.shape}")

# Add a batch dimension so Deep Learning layers accept it
model_ready_sample = single_sample[np.newaxis, :]
print(f"Model-Ready Shape: {model_ready_sample.shape}")


print("\n--- STEP 4: VECTORIZED LOGIC (np.where) ---")
# Simulating continuous final layer prediction logits
logits = np.array([-1.2, 0.8, 2.5, -0.3])

# Binary classification: If logit > 0 -> Class 1, else Class 0
predictions = np.where(logits > 0.0, 1, 0)
print(f"Logits: {logits}")
print(f"Generated Binary Predictions: {predictions}")