import numpy as np

# ========================================
# প্রয়োজনীয় ম্যাথ কনসেপ্ট (Math Concepts)
# ========================================
"""
1. Vector (1D Array):
   - এক মাত্রিক সংখ্যার সারি। উদাহরণ: গতি, বল, দূরত্ব।
2. Matrix (2D Array):
   - দ্বিমাত্রিক সংখ্যার টেবিল (rows × columns)
   - উদাহরণ: ট্রান্সফরমেশন, ইমেজ (পিক্সেল গ্রিড)
3. Tensor (3D+ Array):
   - উচ্চ মাত্রার ডেটা। Deep Learning-এ খুব ব্যবহৃত হয়।
4. Shape:
   - Array কত মাত্রার এবং প্রত্যেক মাত্রায় কয়টা উপাদান আছে।
   - উদাহরণ: (3, 4) মানে 3 rows, 4 columns
"""
"""
NumPy - 1. Array Fundamentals
================================
এই ফাইলে আমরা NumPy এর মৌলিক বিষয়গুলো শিখব।
"""
# ========================================
# 1. Array তৈরি করা (Creating Arrays)
# ========================================
# Python list থেকে array তৈরি
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)

# 2D Array (Matrix)
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])
print("\n2D Array (Matrix):\n", arr2)

# বিভিন্ন ধরনের array তৈরি
zeros = np.zeros((3, 4))           # 3x4 ম্যাট্রিক্স, সব 0
ones = np.ones((2, 3))             # সব 1
full = np.full((2, 2), 7)          # সব 7
arange = np.arange(0, 10, 2)       # 0 থেকে 10, step 2
linspace = np.linspace(0, 1, 5)    # 0 থেকে 1 এর মধ্যে 5টা সমান সংখ্যা

print("\nZeros:\n", zeros)
print("Ones:\n", ones)
print("Arange:", arange)
print("Linspace:", linspace)

# ========================================
# 2. Array Attributes (গুরুত্বপূর্ণ বৈশিষ্ট্য)
# ========================================

print("\n=== Array Attributes ===")
print("Shape:", arr2.shape)        # (rows, columns)
print("Dimension (ndim):", arr2.ndim)
print("Data Type (dtype):", arr2.dtype)
print("Total Elements (size):", arr2.size)
print("Item Size (bytes):", arr2.itemsize)

# ========================================
# 3. Data Types (dtype)
# ========================================

print("\n=== Data Types ===")
arr_int = np.array([1, 2, 3], dtype=np.int32)
arr_float = np.array([1, 2, 3], dtype=np.float64)
arr_bool = np.array([True, False, True])

print("int32:", arr_int.dtype)
print("float64:", arr_float.dtype)
print("bool:", arr_bool.dtype)

# ========================================
# 4. Reshaping Arrays (খুব গুরুত্বপূর্ণ)
# ========================================

print("\n=== Reshaping ===")
a = np.arange(12)          # 0 to 11
print("Original:", a)

print("Reshape to 3x4:\n", a.reshape(3, 4))
print("Reshape to 2x2x3:\n", a.reshape(2, 2, 3))

# ========================================
# 5. Copy vs View (খুব গুরুত্বপূর্ণ!)
# ========================================

print("\n=== Copy vs View ===")

original = np.array([1, 2, 3, 4, 5])

# View (memory share করে - পরিবর্তন হলে উভয়ে প্রভাব পড়ে)
view = original[1:4]        # Slicing করে View তৈরি হয়
view[0] = 99

print("Original after modifying view:", original)
print("View:", view)

# Copy (স্বাধীন কপি)
copy_arr = original.copy()
copy_arr[0] = 1000

print("Original after modifying copy:", original)
print("Copy:", copy_arr)

# ========================================
# Mini Exercises
# ========================================

print("\n=== Mini Exercises ===")
"""
Exercise 1: একটা 4x4 ম্যাট্রিক্স তৈরি করুন যেখানে সব উপাদান 5
Exercise 2: 0 থেকে 20 পর্যন্ত সংখ্যা নিয়ে 5x4 শেপে রিশেপ করুন
Exercise 3: একটা array তৈরি করুন এবং তার shape, ndim, dtype প্রিন্ট করুন
"""

# আপনার সমাধান এখানে লিখুন...


print("\n✅ Module 1 শেষ! এখন নিজে অনেকগুলো array তৈরি করে প্র্যাকটিস করুন।")