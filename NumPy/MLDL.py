import numpy as np

# Focus: Data preprocessing, Tensor shapes, and Neural Network math.
# 1. RESHAPING & TENSOR MANIPULATION (Crucial for Deep Learning

# Imagine you have 2 grayscale images, each 3x3 pixels, flattened into a 1D vector.
raw_data = np.arange(18)

print(f"Original 1D Array:\n{raw_data}\n")



















# # In AI, data comes in batches. Let's reshape this to: (batch_size, height, width)
# # We have 2 images, each 3x3
# images = raw_data.reshape(2, 3, 3)
# print(f"Reshaped Image Batch Shape: {images.shape}")
# print("First Image Matrix:\n", images[0])

# # Flattening it back (often done before feeding data into a Fully Connected layer)
# flattened = images.ravel() # or images.flatten()
# print(f"Flattened back to 1D shape: {flattened.shape}\n")


# print("--- 2. AXIS OPERATIONS (Calculating Loss & Features) ---")
# # Let's say these are model predictions for 3 samples across 4 classes (logits)
# predictions = np.array([
#     [0.1, 0.8, 0.05, 0.05],
#     [0.2, 0.1, 0.6,  0.1],
#     [0.7, 0.1, 0.1,  0.1]
# ])

# # AI engineers use 'axis' constantly. 
# # axis=1 means "operate across columns" (per sample)
# # axis=0 means "operate down rows" (per feature/class)

# # Find the predicted class index for each sample (Argmax)
# predicted_classes = np.argmax(predictions, axis=1)
# print("Predicted class index for each sample:", predicted_classes) 

# # Calculate the mean confidence score for each class across the whole batch
# mean_confidence = np.mean(predictions, axis=0)
# print("Mean confidence per class:", mean_confidence, "\n")


# print("--- 3. BROADCASTING IN ACTION (Normalizing Data) ---")
# # Standardizing features (Subtract mean, divide by standard deviation) is standard practice.
# features = np.array([
#     [10.0, 100.0],
#     [20.0, 200.0],
#     [30.0, 300.0]
# ])

# # Calculate mean along axis 0 (per feature column)
# mean = np.mean(features, axis=0) # Result shape: (2,)
# std = np.std(features, axis=0)   # Result shape: (2,)

# # Broadcasting subtracts 'mean' from every row automatically
# normalized_features = (features - mean) / std
# print("Normalized Features (Mean ~0, Std ~1):\n", normalized_features, "\n")


# print("--- 4. MASKING & CLIPPING (Activation Functions & Data Cleaning) ---")
# # ReLU (Rectified Linear Unit) is the most common activation function: f(x) = max(0, x)
# layer_outputs = np.array([-2.5, 3.1, -0.2, 5.0, 0.0, -1.1])

# # Method A: Boolean Masking
# relu_outputs_mask = layer_outputs.copy()
# relu_outputs_mask[relu_outputs_mask < 0] = 0
# print("ReLU via Masking:", relu_outputs_mask)

# # Method B: Vectorized np.maximum (Cleaner, faster)
# relu_outputs_max = np.maximum(0, layer_outputs)
# print("ReLU via np.maximum:", relu_outputs_max)

# # Exploding Gradients? Clip them between a min and max threshold
# gradients = np.array([105.2, -84.1, 12.3, -5.1])
# clipped_gradients = np.clip(gradients, -50.0, 50.0)
# print("Clipped Gradients (-50 to 50):", clipped_gradients, "\n")


# print("--- 5. RANDOMNESS & INITIALIZATION (Weight Matrices) ---")
# # Reproducibility is key in AI. Always set a random seed/generator.
# rng = np.random.default_rng(seed=42)

# # Initialize weights for a neural network layer (3 inputs, 2 outputs) using a Normal Distribution
# weights = rng.normal(loc=0.0, scale=0.1, size=(3, 2))
# print("Randomly Initialized Weights Matrix:\n", weights)