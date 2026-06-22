# how to learn the AND rule.
import numpy as np

input = np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1]
])

output = np.array([0, 0, 0, 1])

# Based on X and Y: “Only fire (1) when BOTH signals are active.”

weights = np.zeros(2)

print("Weights->", weights)

# “How easy is it for this neuron to fire?”
bias = 0
# High bias → easy to fire
# Low bias → hard to fire

lr = 0.1

for epoch in range(20):
    for i in range(len(input)):
        z = np.dot(input[i], weights) + bias
        pred = 1 if z > 0 else 0
        error = output[i] - pred
        weights += lr * error * input[i]
        bias += lr * error
        
print("Weights:", weights)
print("Bias:", bias)