# Correlation: Covariance বলে Positive Negative কিন্তু "কতটা Strong?" এটা বলে না।
# তাই জন্ম হলো Correlation।

# Range:
# -1
# ↓
# 0
# ↓
# +1

import numpy as np
x = [1,2,3]
y = [2,4,6]
print(np.corrcoef(x,y))

# Output: 1 Perfect Correlation
# ML Relation: Feature Selection, Multicollinearity, Data Analysis