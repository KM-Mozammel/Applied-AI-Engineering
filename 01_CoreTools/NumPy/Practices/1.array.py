import numpy as np

numbers = np.array([10, 20, 30, 40])

# print("Array Itself: ", numbers)
# print("Dimensions: ", numbers.ndim)
# print("Type: ", type(numbers))
# print("Size: ", numbers.size)
# print("Type of Data: ", numbers.dtype)

numbers2 = np.array([[10, 20, 30, 40], [10, 20, 30, 40]])

numbers3 = np.array(
    [
        [
            [10, 20, 30, 40],
            [10, 20, 30, 40],
            [10, 20, 30, 40],
        ]
    ]
)


print("Dimensions: ", numbers2.ndim)
print("Dimensions: ", numbers3.ndim)
