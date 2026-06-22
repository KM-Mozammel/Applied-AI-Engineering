import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

img = Image.open("sample.jpg")
arr = np.array(img)

# plt.hist(arr.ravel(), bins=256)
# plt.title("Pixel Value Distribution")
# plt.xlabel("Pixel Value")
# plt.ylabel("Frequency")
# plt.show()

plt.imshow(arr[:, :, 0])
plt.title("Red Channel")
plt.colorbar()
plt.show()

plt.imshow(arr[:, :, 1])
plt.title("Green Channel")
plt.colorbar()
plt.show()

plt.imshow(arr[:, :, 2])
plt.title("Blue Channel")
plt.colorbar()
plt.show()