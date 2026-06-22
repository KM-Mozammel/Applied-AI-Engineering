# Analogy
# Inputs = incoming signals
# x1 = 1 → neuron A is firing strongly
# x2 = 0 → neuron B is silent
inputs = [1, 0] # 2 incoming signals from other neurons
# So the brain is saying: “I got one strong signal and one missing signal.”


# Layer = group of neurons -> You now have 2 neurons in this layer:
# Neuron 1 weights: [0.5, 0.5]
# This neuron thinks: “I care equally about both signals”

# Neuron 2 weights: [0.2, 0.8]
# This neuron thinks: “I care more about second signal than first”
layer = [
    [0.5, 0.5],    # neuron 1 weights
    [0.2, 0.8],    # neuron 2 weights
] # 2 neurons receiving the SAME inputs, but with different “trust levels” (weights)

for weights in layer:
    z = 0
    for x, w in zip(inputs, weights):
        z += x * w
    print(z)
    
    
# This is the foundation of deep learning: Instead of ONE decision, you get MANY interpretations of the same input.