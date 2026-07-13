import numpy as np
import matplotlib.pyplot as plt

width = 500
height = 500

image = np.zeros((height, width))

real = np.linspace(-2, 1, width)
imag = np.linspace(-1.5, 1.5, height)

for iy, y in enumerate(imag):

    for ix, x in enumerate(real):

        c = x + y*1j
        z = 0

        for i in range(100):

            z = z*z + c

            if abs(z) > 2:
                image[iy, ix] = i
                break

plt.imshow(image, cmap="inferno")
plt.axis("off")
plt.show()