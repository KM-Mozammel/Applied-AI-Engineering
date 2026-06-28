# Matrix multiplication: 
# Definition: Combines transformations or applies them to vectors.
# Analogy: Rotating and scaling an image.

import numpy as np
v = np.array([2, 3])  # 2D vector
M = np.array([[1, 2], [3, 4]])

result = np.dot(M, v)

print(result)