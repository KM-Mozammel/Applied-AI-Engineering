import numpy as np
import matplotlib.pyplot as plt

data_2d = np.arange(25).reshape(5, 5)
print(data_2d)
plt.imshow(data_2d, cmap='viridis')
plt.title("2D Data (Matrix)")
plt.colorbar()
plt.show()
