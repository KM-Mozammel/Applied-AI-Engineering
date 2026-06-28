# Formula: y = mx + b
# m = slope
# b = starting point
# example: y = 2x + 1

# তুমি প্রতিদিন 100 টাকা সঞ্চয় করো।

# Day 1 = 100
# Day 2 = 200
# Day 3 = 300
# Day 4 = 400

# এটা Linear Growth।

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y = 2*x + 1

plt.plot(x, y)
plt.grid()
plt.show()

# Graph intuition: Every step in x -> adds same amount to y

# Linear = Constant Growth
# 100 → 200 → 300 → 400