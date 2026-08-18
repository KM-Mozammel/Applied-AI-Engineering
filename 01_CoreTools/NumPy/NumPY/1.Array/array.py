points = [[1, 2], [4, 5], [-2, 3], [0, -1]]
print("Using Python Array: ", points)

# Using Numpy
import numpy as np
points = np.array([[1, 2], [4, 5], [-2, 3], [0, -1]])
print("Numpy - points: \n", points)

# Visualization:
print("\n")

import matplotlib.pyplot as plt

x = points[:, 0]
y = points[:, 1]

plt.figure(figsize = (6, 6))
plt.scatter(x, y)
plt.plot(x, y)

for px, py in points:
    plt.text(px, py, f"({px}, {py})")

plt.axhline(0)
plt.axvline(0)

plt.grid(True)
plt.title("Coordinate Geometry with NumPy")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()
