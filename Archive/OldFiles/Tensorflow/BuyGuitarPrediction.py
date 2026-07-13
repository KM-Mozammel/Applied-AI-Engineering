import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Example training data (age, store_visit, buy_guitar)
# Let's say buy_guitar = 1 if they bought, 0 otherwise
X = np.array([
    [18, 2, 0],
    [25, 5, 1],
    [30, 3, 1],
    [40, 1, 0],
    [22, 4, 1],
    [35, 2, 0]
])

# Labels (type: Beginner=0, Intermediate=1, Pro=2)
y = np.array([0, 1, 2, 0, 1, 2])

# Build a very basic neural network
model = Sequential([
    Dense(8, input_dim=3, activation='relu'),
    Dense(6, activation='relu'),
    Dense(3, activation='softmax')  # 3 output classes
])

# Compile the model
model.compile(loss='sparse_categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# Train the model
model.fit(X, y, epochs=50, verbose=0)

# Test prediction
test_data = np.array([[28, 4, 1]])  # Age 28, 4 visits, bought guitar
prediction = model.predict(test_data)
predicted_class = np.argmax(prediction)

print("Predicted type:", predicted_class)
