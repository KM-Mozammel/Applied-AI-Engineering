# Definition: Decomposes a matrix into rotation, scaling, and reflection.
# Analogy: Compressing an image while keeping its essence.

import numpy as np
v = np.array([2, 3])  # 2D vector
M = np.array([[1, 2], [3, 4]])

result = np.dot(M, v)

U, s, Vt = np.linalg.svd(M)