import numpy as np

# Vector
a = np.array([10, 20, 30])
print("Vector: ", a.shape)

#Row Matrix
a = np.array([[10, 20, 30]])
print("Row Matrix: ", a.shape)

#Column Matrix
a = np.array([
    [10], 
    [20],
    [30]
])

print("Column Matrix: ", a.shape)

#Rectangular Matrix
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("Rectangular Matrix: ", a.shape)

#Square Matrix
a = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print("Square Matrx: ", a.shape)

#3D Tensor
a = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5,6],
        [7,8]
    ]
])

print("3D Tensor: ", a.shape)

# Manual funcation to show shape
# def shape(matrix: list[int]) -> any:
#     """Return the shape of the array"""
#     return (len(matrix), len(matrix[0]))

# print(shape([0, 2, 3, 4]))


import numpy as np
import matplotlib.pyplot as plt

matrix = np.array([
    [1,2,3],
    [4,5,6]
])

plt.imshow(matrix)

for r in range(matrix.shape[0]):
    for c in range(matrix.shape[1]):
        plt.text(c, r, matrix[r,c],
                 ha="center", va="center")

plt.title("2 x 3 Matrix")
plt.colorbar()
plt.show()