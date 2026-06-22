# Two incoming signals from earlier neurons:

# x1 = 1 → strong signal
# x2 = 1 → strong signal

# So the brain is receiving: “two strong pieces of information”
inputs = [1, 1]

hidden_weights = [
    [0.5, 0.5],  # neuron 1 -> “I trust both inputs equally” -> balanced thinker
    [0.2, 0.8]   # neuron 2 -> “I care more about second input than first” => Biased thinker
]

hidden_outputs = []

for neuron in hidden_weights: # “Take one neuron at a time from the layer”

    z = 0 # “This neuron starts fresh, no memory of previous signals”

    for x, w in zip(inputs, neuron):
        z += x * w

    hidden_outputs.append(z)

print(hidden_outputs)