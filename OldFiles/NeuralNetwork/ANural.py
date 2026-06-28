import numpy as np

# Step 1: Input data (customer behavior)
# [Browsed, Visited]
input = np.array([[0, 0],   # Did not browse, did not visit
                  [0, 1],   # Did not browse, but visited
                  [1, 0],   # Browsed, but did not visit
                  [1, 1]])  # Browsed and visited

# Step 2: Target output (purchase decision)
# 0 = No purchase, 1 = Purchase
TargetOutput = np.array([[0], [1], [1], [1]])

# Step 3: Initialize weights randomly
np.random.seed(42)
W1 = np.random.rand(2, 2)   # hidden layer weights
W2 = np.random.rand(2, 1)   # output layer weights

# Step 4: Activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Step 5: Forward pass
def forward(Input):
    hidden_input = np.dot(Input, W1)
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, W2)
    final_output = sigmoid(final_input)

    return final_output

# Step 6: Run the network
output = forward(input)
print("Customer Behavior (Browsed, Visited):\n", input)
print("Predicted Purchase Probability:\n", output)
