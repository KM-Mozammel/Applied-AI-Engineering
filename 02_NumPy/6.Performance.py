# ছোট Dataset-এ Performance নিয়ে অতিরিক্ত চিন্তা করা। Optimization তখনই গুরুত্বপূর্ণ, যখন Dataset বড় হয়।

# NumPy দ্রুত নয় কারণ এটি ম্যাজিক করে; NumPy দ্রুত কারণ এটি Python-এর মতো এক একটি Element নিয়ে কাজ না করে, পুরো Array-কে একসাথে Process করে।

# Performance বলতে বোঝায়— কোনো কাজ কত দ্রুত এবং কত কম Memory ব্যবহার করে সম্পন্ন করা যায়।

# ধরো তোমাকে ১০ লক্ষ সংখ্যার সাথে ১ যোগ করতে হবে। প্রশ্ন হলো, 
# কে দ্রুত করবে? Python List? NumPy Array?

# ধরো একটি গুদামে (Warehouse) ১০,০০০টি বাক্স আছে। 
# Worker 1 (Python) সে একবারে একটি বাক্স তুলছে:

# 📦
# 📦
# 📦
# 📦

# একটি শেষ, তারপর আরেকটি।

# Worker 2 (NumPy): তার কাছে Forklift আছে।

# 📦 📦 📦 📦 📦 📦 📦 📦

# একবারেই অনেকগুলো বাক্স তুলছে। এটাই Vectorization।

# Python List: Loop লিখতে হয়েছে।
numbers = [1,2,3,4,5]

result = []

for n in numbers:
    result.append(n+1)

print(result)

# NumPy:কোণ lOOP নেই। 
import numpy as np
numbers = np.array([1,2,3,4,5])
print(numbers+1)

# Vectorization মানে: Loop না লিখে পুরো Array-এর উপর একসাথে Operation করা।

arr = np.array([1,2,3,4,5])
print(arr*10)

# Output: [10 20 30 40 50] NumPy ভিতরে Loop চালাচ্ছে। কিন্তু Python-এর মতো Interpreter-এর মাধ্যমে নয়।

# NumPy এত Fast? কারণ ৪টি প্রধান বিষয়।

# ১. Contiguous Memory:
# Python List
# 📦      📦
#         📦
# 📦

# Memory-তে ছড়িয়ে ছিটিয়ে। NumPy: 📦📦📦📦📦📦📦📦 একসাথে। CPU সহজে পড়তে পারে।

# ২. Fixed Data Type: Python List [1,"Hello",3.5,True] সব ধরনের Data থাকতে পারে। NumPy: [1,2,3,4] সব Integer। অথবা [1.2,2.5,3.7] সব Float। CPU আগে থেকেই জানে কীভাবে এগুলো Process করতে হবে।

# ৩. C Language: NumPy-এর ভিতরের Core Library লেখা হয়েছে C Language-এ। C, Python-এর তুলনায় অনেক দ্রুত।

# ৪. Vectorization: একটি করে Element নয়। পুরো Array একসাথে Process হয়।

# Speed Comparison:
result = []

for x in data:
    result.append(x*2)

# NumPy: 
result = data*2

# এক লাইন।

# Time Measure: Jupyter Notebook-এ %timeit numbers+1 অথবা

import time
start = time.time()
numbers+1
end = time.time()
print(end-start)

# Memory Efficiency: ধরো ১০ লক্ষ Integer।
# Python List: প্রতিটি Element একটি Object। অনেক Memory লাগে।
# NumPy: একটি Continuous Block। কম Memory লাগে।

# প্রশ্ন ১: NumPy কেন Python List-এর চেয়ে Fast?

# উত্তর:
# Contiguous Memory
# Fixed Data Type
# C Implementation
# Vectorization

# প্রশ্ন ২: Vectorization কী?
# উত্তর: Loop না লিখে পুরো Array-এর উপর একসাথে Operation করা।

# প্রশ্ন ৩: PyTorch এবং NumPy-এর সম্পর্ক কী?
# উত্তর: PyTorch-এর Tensor ধারণাটি NumPy Array-এর ধারণার উপর ভিত্তি করে তৈরি। তাই NumPy ভালোভাবে জানলে PyTorch শেখা অনেক সহজ হয়।

# AI-তে কেন এত গুরুত্বপূর্ণ? ধরো, একটি Image 224 × 224 × 3 Pixels ≈150,000
# Dataset: 100,000 Images
# Total: 15 Billion Pixel Python Loop দিয়ে করলে ঘন্টার পর ঘন্টা লাগতে পারে।

# NumPy

# Neural Network: Training-এর সময়
# output = X @ W + b
# এখানে,
# Matrix Multiplication
# Broadcasting
# সব NumPy-এর মতো Vectorized ধারণার উপর ভিত্তি করে।

# PyTorch:
# torch.Tensor
# NumPy Array-এর মতো।
# TensorFlow
# tf.Tensor
# এটিও একই ধারণা ব্যবহার করে।