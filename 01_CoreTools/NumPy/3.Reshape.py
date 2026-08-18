# ধরো তোমার কাছে ১২টি ইট আছে।
# প্রথমে এভাবে রাখা আছে:
# 🧱 🧱 🧱 🧱 🧱 🧱 🧱 🧱 🧱 🧱 🧱 🧱
# এখন তুমি এগুলো দিয়ে দেয়াল বানালে:

# 🧱 🧱 🧱 🧱
# 🧱 🧱 🧱 🧱
# 🧱 🧱 🧱 🧱

# ইট পরিবর্তন হয়েছে? ❌ না। শুধু সাজানোর ধরন পরিবর্তন হয়েছে। Reshape ঠিক এটিই করে। reshape অনেক ক্ষেত্রে view তৈরি করে, নতুন ডেটা কপি করে না। তাই এটি খুব দ্রুত কাজ করে।

# Row × Column = Total Elements অর্থাৎ,
# 3 × 4 = 12
# 2 × 6 = 12
# 1 × 12 = 12


numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
matrix = [
    numbers[0:4],
    numbers[4:8],
    numbers[8:12]
]
print("Numbers list:", numbers)
print("Matrix List:\n", matrix)

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# arr = np.arange(1, 13)
print("Original:", arr)
print("\nReshape: 3 x 4:\n", arr.reshape(3, 4))
print("\nReshape: 4 x 3:\n", arr.reshape(4, 3))
print("\nReshape: 2 x 6:\n", arr.reshape(2, 6))
print("\nReshape: 6 x 2:\n", arr.reshape(6, 2))
print("\nAuto Column (3, -1):\n", arr.reshape(3, -1))
print("\nAuto Row (-1, 4):\n", arr.reshape(-1, 4))

# reshape() কি নতুন array তৈরি করে? সবসময় না। অনেক ক্ষেত্রে এটি একই memory-এর একটি view দেয়। তবে যদি সেই shape-এ view তৈরি করা সম্ভব না হয়, তাহলে NumPy নতুন memory allocate করতে পারে।

# Camera থেকে একটি সাদা-কালো ছবি এসেছে। 28 × 28 মানে 784 pixels. অনেক ML মডেল সরাসরি ২D ছবি নেয় না। তারা চায় 784 একটি লম্বা ভেক্টর। তখন image.reshape(784)

# ধরো 1000 images প্রত্যেকটি 28 × 28 তখন shape হবে (1000,28,28) CNN-এর জন্য আবার লাগতে পারে (1000,28,28,1). এই অতিরিক্ত 1 হলো Channel Dimension (গ্রেস্কেল ইমেজের জন্য)। তখন reshape বা expand_dims() ব্যবহার করা হয়।