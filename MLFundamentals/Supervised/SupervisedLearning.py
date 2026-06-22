import numpy as np

# =========================
# 1. TRAINING DATA
# =========================
# X = input values
# y = labels (0 = small, 1 = big)

X = np.array([1, 2, 3, 10])
y = np.array([0, 0, 0, 1])

# =========================
# 2. LEARNING PHASE
# =========================
# Find boundary between class 0 and class 1

max_class_0 = max(X[y == 0])
min_class_1 = min(X[y == 1])

threshold = (max_class_0 + min_class_1) / 2

print("Training complete")
print("Learned threshold:", threshold)

# =========================
# 3. PREDICTION FUNCTION
# =========================
def predict(x):
    if x > threshold:
        return 1
    else:
        return 0

# =========================
# 4. TESTING
# =========================
test_values = [0, 2, 4, 7, 12]

print("\nPredictions:")
for val in test_values:
    print(f"Input: {val} → Prediction: {predict(val)}")
    



# Using Library (sklearn)
import numpy as np
from sklearn.linear_model import LogisticRegression

# =========================
# 1. TRAINING DATA
# =========================
X = np.array([[1], [2], [3], [10]])  # must be 2D for sklearn
y = np.array([0, 0, 0, 1])

# =========================
# 2. CREATE MODEL
# =========================
model = LogisticRegression()

# =========================
# 3. TRAIN (FIT)
# =========================
model.fit(X, y)

print("Training complete!")

# =========================
# 4. TESTING
# =========================
test_values = np.array([[0], [2], [4], [7], [12]])

predictions = model.predict(test_values)

print("\nPredictions:")
for val, pred in zip(test_values, predictions):
    print(f"Input: {val[0]} → Prediction: {pred}")