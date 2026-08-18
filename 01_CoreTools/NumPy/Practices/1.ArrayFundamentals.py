import numpy as np

oneDArray= np.array([1,2 ,3,4])

# print(np.size(oneDArray))

twoDArray = np.array([
    [1,2,3,4],
    [5,6,7,8]
])

# print(np.shape(twoDArray))

zerosArray = np.zeros(5, int) #Return 5 - 0
onesArray = np.ones(5, int) #Return 5 - 1
fullArray = np.full(5, 3) #Return 5 - 3
arrange = np.arange(3, 20, 2)  #Retrun 3-20; but 2 step
linespace= np.linspace(0, 1, 5) # Return 0, 0.25, 0.5, 0.75, 1

# print(zerosArray)
# print(zerosArray)
# print(fullArray)
# print(arrange)
# print(linespace)

floatType = np.array([0,1, 2,3 ,4,], dtype=int)
boolearnArray = np.array([True, False, False, True])
# print(boolearnArray)
# print(floatType)

# Shaping
array = np.arange(0, 40)
# print(array)
# print("Reshape 4 X 5 X 2 \n", array.reshape(4, 5, 2))
# print("Reshape 10 X 2 X 2 \n", array.reshape(10, 2, 2))


# View -> Share the originals copy
rolls = np.arange(0, 5)

# print(rolls)
view = rolls[0:5]
view[2] = 25
# print("View", view)
# print("Originals: " ,rolls)

#Copy -> Create a Separate Array
marks = np.arange(1, 5)
# print("Original: ", marks)
marksCopy = marks.copy()
marksCopy[2] = 30
# print("Copy: ", marksCopy)
# print("Original: ", marks)


# Exercise 1: একটা 4x4 ম্যাট্রিক্স তৈরি করুন যেখানে সব উপাদান 5
FourXFour = np.full((4, 4), 5)
print(FourXFour)

# Exercise 2: 0 থেকে 20 পর্যন্ত সংখ্যা নিয়ে 5x4 শেপে রিশেপ করুন
array = np.arange(0, 20)
reshape = array.reshape(5, 4)
# print(reshape)

# Exercise 3: একটা array তৈরি করুন এবং তার shape, ndim, dtype প্রিন্ট করুন
desireArray = np.ones(20)

# print("Array Itself", desireArray)
# print("Shape: ", desireArray.shape)
# print("Ndim: ", desireArray.ndim)
# print("D-Type: ", desireArray.dtype)
