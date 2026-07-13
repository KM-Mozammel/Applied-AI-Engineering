import numpy as np

numbers = np.array([1, 3, 4, 5, 6, 7, 4, 3, 3, 2])

print(numbers)
# print(numbers.reshape(3,3))
print(numbers.reshape(-1, 5))  # auto row