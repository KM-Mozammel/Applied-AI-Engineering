import numpy as np

matrix = np.array([
    [1, 2],
    [3, 4]
])

print("Sum down columns (axis=0):", np.sum(matrix, axis=0))
print("Sum across rows (axis=1):", np.sum(matrix, axis=1))