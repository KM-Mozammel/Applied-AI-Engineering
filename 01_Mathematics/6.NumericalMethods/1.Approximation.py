# Approximation: ধরো, তুমি জানতে চাও Root(2) এর মান?

# এটি একটি Irrational Number। এর অসীম দশমিক সংখ্যা আছে। 1.4142135623730950488... কম্পিউটার কি অসীম সংখ্যা সংরক্ষণ করতে পারে? না।
# তাই Approximation-এর জন্ম।

# ধারণা: Exact Answer-এর পরিবর্তে, যতটা সম্ভব কাছাকাছি উত্তর বের করা।

import math

pi = math.pi
print(pi)
print(round(pi,4))

# আরেকটি উদাহরণ: ধরো e^x গণনা করতে হবে। Computer পুরো Infinite Series ব্যবহার করে না। বরং e^x ≈ 1+x+x^2/2 এই ধরনের Approximation ব্যবহার করে।

# ML Relation: Approximation ব্যবহার হয়—

# Activation Function Approximation
# Numerical Integration
# Taylor Series
# Scientific Computing
# GPU Computation