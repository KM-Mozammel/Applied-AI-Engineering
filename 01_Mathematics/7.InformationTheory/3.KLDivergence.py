# KL Divergence -জন্ম: Cross Entropy তৈরি হওয়ার পরে বিজ্ঞানীরা নতুন প্রশ্ন করলেন। ধরো দুটি Probability Distribution আছে। একটি বাস্তব পৃথিবী। আরেকটি Machine-এর Prediction। দুটো কতটা আলাদা? এখান থেকেই KL Divergence.

# ধারণা: KL Divergence মাপে দুটি Distribution-এর Distance।

# Example: Real Cat = 90% | Dog = 10% 
# Prediction: Cat = 88% | Dog = 12%

# KL -> ছোট। 

# আরেকটি Prediction: Cat = 20%, Dog = 80%; KL -> অনেক বড়।

# Formula: DKL(P∣∣Q) = ∑P(x)log P(x)/Q(x)

import numpy as np

P = np.array([0.9,0.1])

Q = np.array([0.8,0.2])

kl = np.sum(P*np.log(P/Q))

print(kl)

# ML Relation: KL Divergence ব্যবহার হয়

# Variational Autoencoder (VAE)
# Reinforcement Learning
# Knowledge Distillation
# Diffusion Models
# Large Language Models