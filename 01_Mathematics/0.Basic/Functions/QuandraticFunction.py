# Formula: y = x**2
#  x 	y
# -3	9
# -2	4
# -1	1
#  0	0
#  1	1
#  2	4
#  3	9

# Graph:

#    *
#  *   *
# *     *
#  *   *
#    *

# একটি U-shape (Parabola)

# Real Life Example:

# বল উপরে ছুড়ে দিলে: up -> peak -> down
# তার height vs time graph প্রায় quadratic।

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)

y = x**2

plt.plot(x, y)
plt.grid()
plt.show()

# Quadratic = Curved Growth
# 1 → 4 → 9 → 16