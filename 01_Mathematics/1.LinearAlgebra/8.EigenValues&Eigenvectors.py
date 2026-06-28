# Eigenvalues & Eigenvectors: Reveal directions that remain unchanged under transformations, crucial for PCA and embeddings.
# Definition: Directions that remain unchanged under transformation.
# Analogy: Resonant frequencies of a system.

import numpy as np
M = np.array([[1, 2], [3, 4]])
eigvals, eigvecs = np.linalg.eig(M)