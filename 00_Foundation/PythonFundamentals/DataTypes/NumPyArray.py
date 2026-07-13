print("\n========== NUMPY ARRAY ==========")

import numpy as np

data = np.array([10, 20, 30, 40])

print("Array:", data)
print("Type:", type(data))

# Properties
print("Shape:", data.shape)
print("Size:", data.size)
print("Data Type:", data.dtype)

# Arithmetic
print("Array + 10:", data + 10)
print("Array - 5:", data - 5)
print("Array * 2:", data * 2)
print("Array / 2:", data / 2)

# Statistics
print("Mean:", np.mean(data))
print("Sum:", np.sum(data))
print("Max:", np.max(data))
print("Min:", np.min(data))
print("Std:", np.std(data))

# Indexing
print("First Item:", data[0])
print("Slice:", data[1:3])

# 2D Array
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\nMatrix:")
print(matrix)

print("Matrix Shape:", matrix.shape)

# Reshape
arr = np.array([1, 2, 3, 4, 5, 6])

print("\nReshape:")
print(arr.reshape(2, 3))

# Random Numbers
print("\nRandom Values:")
print(np.random.rand(3))

# Zeros
print("\nZeros:")
print(np.zeros((2, 3)))

# Ones
print("\nOnes:")
print(np.ones((2, 3)))

# Range
print("\nArange:")
print(np.arange(1, 10))

# Feature Vector
person = np.array([
    28,
    170,
    70
])

print("\nFeature Vector:")
print(person)

# ML Dataset Example
X = np.array([
    [18, 170],
    [22, 180],
    [25, 175]
])

y = np.array([0, 1, 1])

print("\nFeatures (X):")
print(X)

print("\nLabels (y):")
print(y)