# Entropy -জন্ম: Shannon বুঝলেন, সব Message সমান Information বহন করে না।

# উদাহরণ, আজ সকালে সূর্য উঠেছে। এতে অবাক হওয়ার কিছু নেই। Information খুব কম। কিন্তু আজ সূর্য পশ্চিমে উঠেছে। এটি অসম্ভবের কাছাকাছি। Information অনেক বেশি। তিনি বললেন, যত Uncertainty বেশি, Information তত বেশি। এটাই Entropy

# ধারণা: Entropy = Uncertainty-এর পরিমাপ।

# Example-> Coin: Head, Tail 50% - 50% তুমি জানো না কী আসবে। Entropy -> High . আরেকটি Coin: Head -> 99%; Tail -> 1% প্রায় নিশ্চিত। Entropy Low

# Formula: H(X) = −∑p(x)logp(x)

import math

p = 0.5

entropy = -2*(p*math.log2(p))

print(entropy)

# Output: 1.0
# আরেকটি,
p = 0.99
entropy = -(p*math.log2(p)+(1-p)*math.log2(1-p))
print(entropy)

# Entropy -> খুব কম।

# ML Relation: Entropy ব্যবহার হয়
# Decision Tree
# Information Gain
# Compression
# Language Models