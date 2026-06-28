# Variance: দুটি ক্লাস

# Class A

# 49
# 50
# 51
# 50

# Class B

# 10
# 50
# 90
# 50

# Mean দুটোরই প্রায় একই। কিন্তু Class B অনেক বেশি ছড়ানো। তাই জন্ম হলো Variance।

# ধারণা: Mean থেকে ডেটা কত দূরে ছড়িয়ে আছে। Variance= n / ∑(x−μ)2

import numpy as np
data = [49,50,51,50]
print(np.var(data))

# ML Relation: Feature Selection, Risk Analysis, Finance