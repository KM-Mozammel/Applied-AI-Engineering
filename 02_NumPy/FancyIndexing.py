import numpy as np

features = np.array([[10, 11], [10, 21], [30, 31], [40, 41], [50, 51]])

batch_indices = [0, 4,2]

mini_batch = features[batch_indices]

print("Mini-batch selection: \n", mini_batch)