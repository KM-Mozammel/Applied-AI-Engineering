# Convexity: বিজ্ঞানীরা Optimization করতে গিয়ে দেখলেন — সব Problem সমান নয়। ধরো দুটি পাহাড়: 

# প্রথমটি
#       ●
#      / \
#     /   \
# ___/     \___

# একটি মাত্র নিচের বিন্দু আছে। এখানে নিচে নামা খুব সহজ। এটিকে বলে Convex Function।

# দ্বিতীয়টি
#    /\      /\
# __/  \____/  \___

# অনেকগুলো নিচু জায়গা আছে। এখানে সহজেই ভুল জায়গায় আটকে যেতে পারো। এটিকে Non-Convex Problem বলে।

# ধারণা : Convex Function-এর একটি মাত্র Global Minimum থাকে। এ কারণে Optimization সহজ হয়। 
# উদাহরণ: f(x)=x^2, Graph y=x^2

import numpy as np

def f(x):
    return x**2

print(f(5))

# Output: 25

# ML Relation: অনেক Classical ML Algorithm Convex Optimization ব্যবহার করে। যেমন, Linear Regression, Logistic Regression, Support Vector Machine