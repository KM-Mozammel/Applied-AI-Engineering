import numpy as np

# ======================================================
# প্রয়োজনীয় ম্যাথ কনসেপ্ট (Math Concepts)
# ======================================================
"""
1. Coordinate (Index):
   - Array-এর প্রতিটি উপাদানের একটি অবস্থান (position) থাকে।
   - 1D Array → একটি Index
   - 2D Array → (Row, Column)

2. Interval:
   - Slicing মূলত একটি Interval নির্বাচন করে।
   - start : stop : step

3. Matrix Navigation:
   - Row এবং Column ধরে Matrix থেকে Data বের করা।
"""

# Indexing & Slicing: এই ফাইলে আমরা শিখব কীভাবে Array থেকে Data Access করতে হয়।
# ======================================================
# 1. 1D Indexing
# ======================================================
numbers = np.arange(10, 60, 10)
# print("Array: ", numbers)

# print("First Element: ", numbers[0])
# print("Second Element: ", numbers[1])
# print("Last Element: ", numbers[- 1])
# print("Second Last Element: ", numbers[-2])
# print("Third Last Element: ", numbers[-3])

# ======================================================
# 2. 2D Indexing
# ======================================================

matrix = np.arange(10, 100, 10).reshape(3, 3)
# print(matrix)

# print("Row 0 col 0:", matrix[0, 0])
# print("Row 1 col 2:", matrix[1, 2])
# print("Row 2 col 1:", matrix[2, 1])


# ======================================================
# 3. Basic Slicing
# ======================================================

numbers = np.arange(10)
# print(numbers)
# print("0:3 ->", numbers[0:3])
# print("1:4 ->", numbers[1:4])
# print(":3 ->", numbers[:3])
# print("2: ->", numbers[2:])
# print(": ->", numbers[:])

# ======================================================
# 4. Step Slicing
# ======================================================
# print("Every 2nd:", numbers[::2])
# print("Every 3rd:", numbers[::3])
# print("Reverse:",numbers[::-1])

# ======================================================
# 5. Row Selection
# ======================================================
# print(matrix)
# print("First Row: ", matrix[0])
# print("Second Row: ", matrix[1])
# print("Last Row: ", matrix[-1])

# ======================================================
# 6. Column Selection
# ======================================================
# print(matrix)

# print("First Column",matrix[:, 0])
# print("Second Column",matrix[:, 1])
# print("Last Column",matrix[:, -1])

# ======================================================
# 7. Row & Column Slicing
# ======================================================
matrix = np.array([
    [10, 20, 30, 10],
    [40, 50, 60, 20],
    [70, 80, 90, 30],
    [20, 34, 56, 34]
])


# print(matrix)
# print(matrix[:])
# print("Top Left 2x2: \n", matrix[:2, :2])
# print("Bottom Right 2x2: \n", matrix[1:2, 1:2])
# print("First Two Rows: \n", matrix[:2])
# print("Last Two Columns: \n", matrix[:, 1:])

# ======================================================
# 8. Fancy Indexing
# ======================================================

numbers = np.array([10, 20, 30, 40, 50])
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Original \n", matrix)
lastRow = matrix[2]
print("Last Row: ", lastRow)
firstCol = matrix[:,0]
print("\nFirst Col: ", firstCol)

matrixCopy = matrix.copy()
print("Copyed Matrix \n", matrixCopy)
matrixCopy[:,0] = firstCol + 1
print("Manupulated Copyed Matrix \n", matrixCopy)

# print(numbers[[0,2,4]])
# print(matrix[[0,2]])