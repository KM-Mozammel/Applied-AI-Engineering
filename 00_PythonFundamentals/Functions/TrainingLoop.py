def train_loop(epochs, data, labels, model):
    for epoch in range(epochs):
        predictions = model(data)
        loss = sum((predictions - labels)**2) / len(labels)
        print(f"Epoch {epoch + 1}, Loss: {loss}]")
        
# NumPy 
import numpy as np
def linear_model(X, w):
    return X @ w

X = np.array([[1], [2], [3]])
y = np.array([2, 4, 6])
w = np.array([2])

train_loop(3, X, y, lambda d: linear_model(d, w))

#Scikit-Learn
from sklearn.linear_model import LinearRegression
X = np.array([[1], [2], [3]])
y = np.array([2, 4, 6])
model = LinearRegression()
model.fit(X, y)
print("Coefficients:", model.coef_)

# Simple Linear Regression using Gradient Descent (Pure Python)

# Data: y = 2x + 1
X = [1, 2, 3, 4, 5]
y = [3, 5, 7, 9, 11]

# Initialize parameters
w = 0.0   # weight
b = 0.0   # bias
lr = 0.01 # learning rate
epochs = 1000

# Training loop
for epoch in range(epochs):
    y_pred = [w*x_i + b for x_i in X]  # forward pass
    
    # Compute loss (Mean Squared Error)
    loss = sum((y_i - y_hat)**2 for y_i, y_hat in zip(y, y_pred)) / len(y)
    
    # Compute gradients
    dw = sum(-2*x_i*(y_i - y_hat) for x_i, y_i, y_hat in zip(X, y, y_pred)) / len(y)
    db = sum(-2*(y_i - y_hat) for y_i, y_hat in zip(y, y_pred)) / len(y)
    
    # Update parameters
    w -= lr * dw
    b -= lr * db
    
    # Print progress every 100 epochs
    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Loss: {loss:.4f}, w: {w:.4f}, b: {b:.4f}")

print(f"Final model: y = {w:.2f}x + {b:.2f}")
