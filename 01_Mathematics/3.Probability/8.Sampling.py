# Sampling জন্ম: মানুষ বুঝল পুরো population মাপা সম্ভব না।
# উদাহরণ: Bangladesh Population ১৮ কোটির সবার কাছে প্রশ্ন করা অসম্ভব। তাই Sample নিই

import random

population = list(range(1000))
sample = random.sample(population,10)
print(sample)

# ML Relation:
# Train/Test Split
# Mini Batch Training
# Bootstrapping