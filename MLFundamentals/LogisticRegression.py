# Used for classification: Email -> Spam or Not Spam

from sklearn.linear_model import LogisticRegression
import numpy as np

X = np.array([
    [1],
    [2],
    [3],
    [4],
])

y = np.array([0, 0, 1, 1])

# 1 spam word -> Not Spam (0)
# 2 spam words -> Not Spam (0)
# 3 spam words -> Spam (1)
# 4 spam words -> Spam (1)

model = LogisticRegression()

model.fit(X, y)

print(model.predict([[2.5]]))

# Manual Programming
import math

# Training data
X = [1, 2, 3, 4]
y = [0, 0, 1, 1]

# Brain starts with no knowledge
weight = 0.0
bias = 0.0

learning_rate = 0.1

# Sigmoid activation
def sigmoid(z):
    return 1 / (1 + math.exp(-z))

# Training
for epoch in range(1000):

    for i in range(len(X)):

        # Forward pass
        z = X[i] * weight + bias
        prediction = sigmoid(z)

        # Error
        error = y[i] - prediction

        # Learning (Gradient Descent)
        weight += learning_rate * error * X[i]
        bias += learning_rate * error

print("Weight:", weight)
print("Bias:", bias)

# Test
x_new = 2.5

z = x_new * weight + bias
probability = sigmoid(z)

prediction = 1 if probability >= 0.5 else 0

print("Probability:", probability)
print("Prediction:", prediction)