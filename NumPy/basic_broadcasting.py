import numpy as np

matrix = np.array([[1, 2], [3, 4]])

print("Add 10 to everything: \n", matrix + 10)

row = np.array([10, 20])
print("\nAdd row [10, 20] to each row of matrix:\n", matrix + row)