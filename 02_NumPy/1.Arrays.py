# একটি Array হতে পারে [10 20 30] এটি একটি 1D Array (Vector)।

# আর যদি Row এবং Column থাকে, এটি একটি Matrix।
# 1 2 3
# 4 5 6
# 7 8 9

# A NumPy Array is: A collection of elements having the "same data type", stored in contiguous memory, allowing fast mathematical operations.

# Mental Model: Never think This is a NumPy array. Instead think This is a block of computer memory organized into dimensions. That mindset will make advanced topics like reshaping, broadcasting, tensors, and PyTorch much easier to understand.


# Real-life Analogy: Imagine 100 houses.

# Python List:
# House 1  -> Dhaka
# House 2  -> Chittagong
# House 3  -> Sylhet
# House 4  -> Khulna

# The mailman travels everywhere. Slow.

# NumPy Array: Apartment Building

# 101
# 102
# 103
# 104
# 105
# 106
# 107

# Everything is together. Delivering mail becomes much faster. The CPU behaves similarly when reading memory.


# Cat Image Actually becomes [[123 120 118] [220 218 219] [ 32  30  29]] Just numbers.
# An audio file becomes [0.2 0.5 0.7 -0.3 ...] Numbers.
# A sentence becomes [0.12 0.55 0.81...] Embeddings (numbers).

# Everything in AI eventually becomes numbers stored in arrays.

import numpy as np
numbers = np.array([10, 20, 30, 40])
print("Ärray Itself: ", numbers)

# Why "n-dimensional"?
# One line -> [1 2 3] 

# Table->
# 1 2 3
# 4 5 6

# Cube --->
# Layer 1
# 1 2
# 3 4

# Layer 2
# 5 6
# 7 8   
# ->Higher dimensions... 
# Your brain cannot visualize 10 dimensions easily. NumPy can.

# How many dimensions: 
print("How many dimensions?", numbers.ndim)

# What is type?
print("What is the type?", type(numbers))

# What's its shape?
print("What's its shape? ", numbers.shape)

# How many values?
print("How many values? ", numbers.size)

# What type of data?
print("What type of data? ", numbers.dtype)