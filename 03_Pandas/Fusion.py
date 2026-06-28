import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Metric_A': [1.5, 2.5],
    'Metric_B': [4.0, 5.0]
})

print("Pandas DataFrame:\n", df)

# Convert to directly to a numpy array block

numpy_matrix = df.to_numpy()

print("\nConverted NumPy Matrix:\n", numpy_matrix)
print("Type after conversion:", type(numpy_matrix))