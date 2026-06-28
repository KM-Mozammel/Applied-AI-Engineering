# Stochastic Gradient Descent (SGD): Gradient Descent খুব ভালো কাজ করছিল। কিন্তু একটি সমস্যা হলো। ধরো, তোমার Dataset 100 কোটি ছবি. প্রতিবার পুরো Dataset দেখে Gradient বের করলে অনেক সময় লাগবে। তাই বিজ্ঞানীরা বললেন— "পুরো Dataset না দেখে, অল্প Sample দেখেই শেখাই।" এভাবেই জন্ম হলো, Stochastic Gradient Descent

# ধারণা: Gradient Descent, -> সব Data ব্যবহার করে। SGD ↓ একটি বা কয়েকটি Data ব্যবহার করে।

# Visualization: 
# Gradient Descent: ██████████████ -> One Update

# SGD: ██ -> Update ██ -> Update ██ -> Update

import random

weights = 5
learning_rate = 0.1

samples = [1,2,3,4,5]

for sample in samples:
    gradient = 2*weights
    weights = weights - learning_rate*gradient
    print(weights)
    
# ML Relation: Neural Networks, CNN, Transformer, LLM সবগুলো SGD-এর কোনো না কোনো Variant ব্যবহার করে।