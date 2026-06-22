x1 = 1
x2 = 1

w1 = 0.5
w2 = 0.5
bias = -0.7

z = x1*w1 + x2*w2 + bias
output = 1 if z >= 0 else 0
print(output)

# Multiple Inputs, One Neuron
inputs = [1, 1, 0]
weights = [0.5, 0.5, 0.5]

bias = -0.7
z = 0

for x, w in zip(inputs, weights):
    z += x*w
    
z += bias
output = 1 if z>=0 else 0
print(output)