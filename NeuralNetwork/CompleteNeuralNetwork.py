# INPUT LAYER
inputs = [1, 1] # “two strong pieces of information from the environment”

# HIDDEN LAYER
hidden_weights = [
    [0.5, 0.5],  # neuron 1
    [0.2, 0.8]   # neuron 2
] # Each neuron is a different “brain opinion unit”.

hidden_outputs = []

# Forward pass → Hidden layer
for neuron in hidden_weights:

    z = 0

    for x, w in zip(inputs, neuron):
        z += x * w

    hidden_outputs.append(z)

# OUTPUT LAYER (NEW PART)
# hidden_outputs = [1.0, 1.0]
output_weights = [0.6, 0.4]   # final decision neuron
bias = -0.5

z = 0

for x, w in zip(hidden_outputs, output_weights):
    z += x * w

z += bias

output = 1 if z >= 0 else 0

print("Hidden:", hidden_outputs)
print("Final Output:", output)

# Your network simulates how a brain takes raw signals, 
# creates internal interpretations, 
# and then makes a final decision based on those interpretations.