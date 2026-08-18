# ধরো তোমার কাছে ১০ লক্ষ ছাত্রের পরীক্ষার নম্বর আছে। 80 75 90 65 85...এখন সরকার বলল, "সবাইকে ৫ নম্বর করে Bonus দাও।" তুমি কি প্রতিটি ছাত্রকে আলাদা আলাদা যোগ করবে? না। তুমি শুধু বলবে, marks + 5; NumPy নিজেই প্রত্যেক element-এর সাথে 5 যোগ করবে। এটাই Broadcasting।

import numpy as np
arr = np.array([10, 20, 30, 40])
print("Original:", arr)
print("Add: arr+5:", arr + 5)

# আমরা তো 5 একটাই দিয়েছি। তাহলে 5 5 5 5 কোথা থেকে এলো? NumPy ভিতরে ভিতরে এমনভাবে ভাবছে: 

# [10 20 30 40]
# +
# [ 5  5  5  5]

# কিন্তু, আসলেই নতুন array বানায় না। শুধু এমন ভাব করে (virtually)। এটাই Broadcasting-এর আসল শক্তি।

# Pure Python
numbers = [1,2,3]

result = []
for n in numbers:
    result.append(n + 10)

print(result)

# NumPy-তে Loop লেখার দরকার নেই।

# Broadcasting with Two Arrays:
a = np.array([1,2,3])
b = np.array([10,20,30])
print(a+b)

a = np.array([
    [1,2,3],
    [4,5,6]
])
b = np.array([10,20,30])
print(a+b)

# Rule 1: দুই Array-এর Shape একই হলে ✔ কাজ হবে

# (3,4)
#   +
# (3,4)

# Rule 2: কোন Dimension যদি 1 হয় তাহলেও কাজ হবে।

# (2,3)
#   +
# (1,3)
# (2,3) Virtual সব ঠিক।

# Rule 3 (গভীরভাবে বোঝা): NumPy ডান দিক (Right to Left) থেকে Shape তুলনা করে।

# উদাহরণ:
# (2,3)
# (3,)
# NumPy এটাকে এমনভাবে দেখে
# (2,3)
# (1,3)
# কারণ ছোট Shape-এর সামনে 1 যোগ করে।
# তারপর
# (2,3)

# NumPy এটাকে বড় করে নেবে।

# Used In:
# Example 1: Image Brightness একটি Image
# [[100 120]
# [130 140]]
# Brightness বাড়াতে image + 30 Broadcasting।

# Example 2: Normalization
# Formula: x' = (x-mean)/std
# normalized = (data-mean)/std 
# mean একটি সংখ্যা। data লক্ষ লক্ষ সংখ্যা। Broadcasting সব কাজ করে।

# Example 3: Neural Network-ধরো Prediction
# [0.1
#  0.4
#  0.8]
# Bias 0.5 তখন prediction + bias Broadcasting।

# Example 4: RGB Image
# Image Shape: (500,500,3)
# RGB Scale: [1.2,1.0,0.8]
# image * scale
# NumPy প্রতিটি Pixel-এর Red ×1.2 Green ×1.0 Blue ×0.8করে দেয়।


import numpy as np
arr = np.array([10,20,30,40])

print(arr + 5)
print(arr * 2)
print(arr - 3)
print(arr / 10)

matrix = np.array([
    [1,2,3],
    [4,5,6]
])

vector = np.array([10,20,30])
print(matrix + vector)


# Broadcasting কি Memory-তে নতুন Array বানায়? উত্তর: না। এটি সাধারণত Virtual Expansion ব্যবহার করে। এই কারণেই এটি খুব দ্রুত এবং Memory Efficient।