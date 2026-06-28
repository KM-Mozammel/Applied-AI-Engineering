# Covariance: বিজ্ঞানীরা জানতে চাইলেন, "দুটি জিনিস একসাথে পরিবর্তিত হয়?"

# Example: Height ↑ - Weight ↑
# Covariance: Positive
# অন্যদিকে Temperature ↑ - Jacket Sales ↓
# Covariance: Negative


import numpy as np

height = [150,160,170]
weight = [50,60,70]
print(np.cov(height,weight))

# ML Relation: Feature Relationship, Principal Component Analysis (PCA)