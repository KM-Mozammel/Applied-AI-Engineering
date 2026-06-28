# Floating Point Stability -জন্ম: মানুষ ভাবত Computer সব সংখ্যা ঠিকভাবে সংরক্ষণ করতে পারে। কিন্তু বিজ্ঞানীরা দেখলেন— Computer-এর Memory সীমিত। তাই অনেক Decimal Number ঠিকভাবে রাখা যায় না।

# Floating Point Stability শেখায়— কীভাবে এমন Algorithm লিখব যাতে ছোট ছোট সংখ্যাগত (Numerical) ভুল জমে বড় ভুল না হয়ে যায়।

# Example:
print(0.1 + 0.2)
# Output: 0.30000000000000004 কেন? কারণ, 0.1 Binary-তে Exact Representation নেই।

# উদাহরণ: 
a = 100000000
b = 0.000001
print((a+b)-a)
# Output: 0.0 ছোট সংখ্যাটি হারিয়ে গেল। এটাকে বলে Loss of Precision

import numpy as np

a = np.float32(0.1)
b = np.float32(0.2)

print(a+b)

# Visualization:
# Exact -> 3.14159265358979
# Computer -> 3.1415927
# More Calculations -> 3.1415931
# More Calculations -> Error Grows

# ML Relation: Deep Learning-এ Weight Update হাজার কোটি বার হয়। যদি Floating Point Error নিয়ন্ত্রণ না করা যায়— Loss = NaN . Gradient Explosion . Gradient Vanishing . Training Failure হতে পারে।

# তাই আধুনিক AI Framework (PyTorch, TensorFlow, JAX) Floating Point Stability-এর উপর অনেক গুরুত্ব দেয়।