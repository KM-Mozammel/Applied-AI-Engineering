# প্রায় প্রতিটি ML/DL অ্যালগরিদম কোনো না কোনোভাবে Random Number ব্যবহার করে।
# Random Numbers: Random Numbers হলো এমন সংখ্যা, যেগুলো আগে থেকে অনুমান করা কঠিন।

# ধরো তুমি একটি লুডু খেলছো। তুমি একটি Dice ছুঁড়লে। সম্ভাব্য ফলাফল: 1 2 3 4 5 6 আগে থেকে কেউ নিশ্চিতভাবে বলতে পারে না কোন সংখ্যা আসবে। এটাই Randomness।

# ধরো, একজন শিক্ষক ১০০ জন ছাত্রের মধ্যে থেকে একজনকে প্রশ্ন করবেন। তিনি কী করলেন? সব নাম একটি বাক্সে রাখলেন। একটি নাম তুললেন। Rahim আবার তুললেন Karim আবার তুললেন Sakib এটি Random Selection। AI-তেও Dataset Shuffle করার সময় ঠিক এমনটাই হয়।

# কিন্তু Computer কি সত্যিই Random? একটি গুরুত্বপূর্ণ প্রশ্ন। Computer আসলে নিজে থেকে সত্যিকারের Random হতে পারে না। Computer সবসময় Algorithm অনুসরণ করে। তাই NumPy যে Random Number তৈরি করে, সেটি হলো Pseudo Random Number অর্থাৎ, দেখতে Random - ব্যবহারেও Random. কিন্তু একই শুরুর অবস্থা (Seed) দিলে একই ফলাফল পাওয়া যায়। NumPy একটি Pseudo Random Number Generator (PRNG) ব্যবহার করে।

import numpy as np
print(np.random.rand())

# Output (প্রতিবার ভিন্ন হতে পারে): 0.734281 এটি 0 এবং 1-এর মধ্যে একটি Random Float দেয়।

# একাধিক Random Number: 
numbers = np.random.rand(5)
print(numbers)

# Output : [0.23 0.91 0.45 0.77 0.13] প্রতিবার Output আলাদা হবে।

# Random Matrix:
matrix = np.random.rand(3,4)
print(matrix)

# Output: 
# [[0.32 0.45 0.61 0.82]
#  [0.91 0.27 0.11 0.73]
#  [0.44 0.98 0.56 0.21]]

# Random Integer: ধরো Dice-এর মতো সংখ্যা চাই। 
np.random.randint(1,7) 
# Output : 4 কেন 7 নয়? কারণ, 
np.random.randint(start, stop) 
# এখানে stop Include হয় না। অর্থাৎ, 
np.random.randint(1,7) 
#মানে 1 2 3 4 5 6
np.random.randint(1,7)
# Shape: 3 * 4

# Normal Distribution AI-তে সবচেয়ে বেশি ব্যবহৃত Random Function np.random.randn(5)

# Output:
# [-0.52
#  0.18
#  1.31
# -0.74
#  0.06]

# এখানে সংখ্যা Positive হতে পারে - Negative হতে পারে - বেশিরভাগই 0-এর আশেপাশে থাকে। এটি Normal (Gaussian) Distribution অনুসরণ করে।

# Seed কী? এখন সবচেয়ে গুরুত্বপূর্ণ বিষয়। ধরো আমি লিখলাম

import numpy as np
np.random.seed(42)
print(np.random.rand(5))

# Output:

# [0.37454012
# 0.95071431
# 0.73199394
# 0.59865848
# 0.15601864]

# যদি পৃথিবীর যেকোনো কম্পিউটারে এই একই কোড চালাও, একই Output পাবে। "Random Generator এখান থেকেই শুরু করবে।" অর্থাৎ Random হলেও এটি Repeat করা যায়।

# ধরো Maze (গোলকধাঁধা) আছে। যদি প্রতিবার একই দরজা দিয়ে ঢোকো, তাহলে একই পথ ধরে এগোবে। Seed ঠিক সেই প্রথম দরজার মতো।

# AI-তে Seed কেন গুরুত্বপূর্ণ? ধরো, তুমি একটি Neural Network Train করলে।

# আজ Accuracy 95% আগামীকাল 93% পরশু 96% কেন?

# কারণ, Weight Initialization Random - Data Shuffle Random . তাই Experiment Repeat করতে Seed ব্যবহার করা হয়।

# Weight Initialization: Neural Network-এর শুরুতে Weight হয়

# 0.23
# -0.11
# 0.51
# 0.07

# এই সংখ্যাগুলো Random হয়। যদি সব Weight শুরুতে 0 হতো, তাহলে Network ঠিকভাবে শিখতে পারত না।