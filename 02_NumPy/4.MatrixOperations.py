# Neural Networks আসলে অসংখ্য Matrix-এর উপর করা Mathematical Operations ছাড়া আর কিছুই নয়। Defination of Matrix = Row + Column দিয়ে সাজানো সংখ্যার টেবিল।

# ধরো একটি স্কুলে ৩ জন ছাত্র আছে। প্রত্যেক ছাত্রের ৪টি বিষয়ের নম্বর আছে।
#           Math  Eng  Sci  ICT
# Rahim      80   75   90   88
# Karim      70   65   82   91
# Hasan      95   89   94   90

# এটি একটি Matrix। এখানে, Rows = Students, Columns = Subjects

# NumPy Matrix:
import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("Matrix:", A)
print("Shape: ", A.shape) #2 Rows 3 Columns

# Vector: [1 2 3] ->               Shape: (3,)
# Matrix: [[1, 2, 3] [4, 5, 6]] -> Shape: (2, 3)

# Matrix Addition: দুটি Matrix-এর Shape একই হলে যোগ করা যায়।
A = np.array([
    [1,2],
    [3,4]
])

B = np.array([
    [5,6],
    [7,8]
])

print(A+B)

# Scalar Multiplication:
A = np.array([
    [1,2],
    [3,4]
])
print("Scaler Multiplication \n", A*10)

# Output:
# [[10 20]
#  [30 40]]
# Broadcasting কাজ করছে।

# Multiplication * Element-wise গুন. Formula: (m,n) @ (n,p) = (m,p)
print("Element-wise")
print(A*B)

# Matrix Multiplication @ Row x Colulmn
# (m,n) @ (n,p) = (m,p)
print("Matrix Multiplication")
print(A@B)

#Transpose .T Row <-> Column
# Machine Learning-এ Feature Matrix, Weight Matrix, Gradient, Covariance Matrix সব জায়গায় Transpose লাগে।

print("Transpose")
print(A.T)

# Output: 
#     [[ 6  8]
#      [10 12]]

# Identity Matrix দেখতে এমন
# 1 0 0
# 0 1 0
# 0 0 1
# NumPy: I = np.eye(3)
# print(I)

# Output:
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# Identity Matrix-এর বিশেষ বৈশিষ্ট্য A @ I = A. যেমন 5 × 1 = 5

# AI-তে Matrix কেন এত গুরুত্বপূর্ণ? ধরো, একটি Student-এর তথ্য 

# Info: Age, Height, Weight, 
# Vector:
# [20
# 170
# 65]

# Weight Matrix:
# 0.5
# 0.3
# 0.2

# Prediction: X @ W

# Neural Network-এর প্রতিটি Layer-এ মূল কাজই হলো output = input @ weight + bias. এই একটি লাইন হাজার হাজার বার চলে।