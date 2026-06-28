# Formula: y = e^x -> y = 3^x
# Example: 1 - 2 - 4 - 8 - 16 - 32 - 64

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 100)
y = np.exp(x)

plt.plot(x, y)
plt.grid()
plt.show()

# Exponential = Explosive Growth
# 1 → 2 → 4 → 8 → 16