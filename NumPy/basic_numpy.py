import numpy as np

# 1D Vector
vector = np.array([10, 20, 30])
print("1D Vector:", vector)
print("Vector Shape:", vector.shape)

# 2D Matrix
matrix_2d = np.array([
    [1, 2], 
    [3, 4]
])
print("\n2D Matrix:\n", matrix_2d)
print("Matrix Shape:", matrix_2d.shape)

# 3D Matrix (array of arrays of arrays)
matrix_3d = np.array([
    [[1, 2], [3, 4], [5, 6]],   # First "layer"
    [[7, 8], [9, 10], [11, 12]] # Second "layer"
])
print("\n3D Matrix:\n", matrix_3d)
print("Matrix Shape:", matrix_3d.shape)
