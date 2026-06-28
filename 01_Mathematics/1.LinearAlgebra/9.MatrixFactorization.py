# Matrix Factorization
# Definition: Breaking a matrix into simpler components.
# Analogy: Splitting a recipe into ingredients.

import numpy as np
M = np.array([[1, 2], [3, 4]])

U, s, Vt = np.linalg.svd(M)