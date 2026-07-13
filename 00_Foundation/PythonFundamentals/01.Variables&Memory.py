# ==========================================================
# Variable & Memory in Python
# ==========================================================
#
# 01_Introduction
# 02_WhyVariable&MemoryExists
# 03_Syntax
# 04_Methods
# 05_TimeComplexity
# 06_InternalWorking
# 07_Examples
# 08_CommonMistakes
# 09_Exercises
# 10_AIUsage-usecase in ai development
#
# ==========================================================

# ==========================================================
# 01_Introduction (ভ্যারিয়েবল ও মেমোরি কী?)
# ==========================================================

"""
অনেক নতুন প্রোগ্রামার মনে করেন — x = 10. মানে x এর ভিতরে 10 রাখা হয়েছে। কিন্তু Python এ আসলে তা নয়। Python-এ Variable কোন ডাটা সংরক্ষণ করে না।
Variable শুধু Memory-তে থাকা একটি Object-এর Reference (ঠিকানা) ধরে রাখে।

অর্থাৎ— Variable ---------> Object in Memory

যখনই নতুন Object তৈরি হয়, Python সেটিকে RAM-এর একটি Memory Location-এ রাখে।

Variable শুধু সেই Object-এর দিকে নির্দেশ করে। এই Concept টি ভালোভাবে বুঝতে পারলে ভবিষ্যতে Copy, Function, Class, List, Dictionary, Pandas, NumPy,
PyTorch—সবকিছু অনেক সহজ হয়ে যাবে।
"""

# ==========================================================
# 02_Why Variable & Memory Exists
# ==========================================================

"""
ধরুন আপনার কাছে একটি বিশাল List আছে। data = [.....10,00,000 elements.....] আপনি যদি b = data করেন, তাহলে Python নতুন List তৈরি করে না। কারণ, এত বড় List বারবার Copy করা অনেক Slow হবে এবং Memory নষ্ট করবে। তাই Python শুধু Reference Copy করে। 

এতে—
✔ Memory কম লাগে
✔ Speed বেশি হয়
✔ Performance ভালো হয়

এই কারণেই Variable & Memory Concept তৈরি হয়েছে।
"""

# ==========================================================
# 03_Syntax
# ==========================================================

# সাধারণ Assignment:
x = 10

# Reference Copy: memory address ধরে রাখে।
y = x

# Mutable Object: Mutable মানে object‑এর ভিতরের data পরিবর্তন করা যায়।
numbers = [1, 2, 3]
another = numbers

# Shallow Copy: Shallow copy নতুন object তৈরি করে, কিন্তু ভিতরের nested object‑গুলোর reference একই থাকে।
copy_list = numbers.copy()

# Deep Copy: Deep copy পুরো object tree নতুন করে তৈরি করে।
import copy
deep_copy = copy.deepcopy(numbers)

# Memory Address: প্রতিটি object‑এর একটি unique memory address থাকে। Python‑এ id(a) দিয়ে সেটা দেখা যায়। যদি a আর b একই object‑কে নির্দেশ করে, তাহলে id(a) == id(b) হবে।প্রতিটি object‑এর একটি unique memory address থাকে।
print(id(numbers))

# ==========================================================
# 04_Methods
# ==========================================================

"""
Variable & Memory বোঝার জন্য গুরুত্বপূর্ণ Method গুলো—

১. id(): Object-এর Memory Identity দেখায়।
২. copy(): Shallow Copy তৈরি করে।
৩. copy.copy(): Shallow Copy
৪. copy.deepcopy(): সম্পূর্ণ আলাদা Object তৈরি করে।
৫. is: দুইটি Variable একই Object কে নির্দেশ করছে কিনা।
৬. == দুই Object-এর Value একই কিনা।

"""

# ==========================================================
# 05_Time Complexity
# ==========================================================

"""
Assignment: a = b || Time Complexity = O(1) || কারণ শুধু Reference Copy হয়।
--------------------
Shallow Copy: a.copy() || Time Complexity = O(n) - কারণ নতুন Container তৈরি হয়।
--------------------
Deep Copy: copy.deepcopy() || Time Complexity = O(n) || Nested Structure হলে আরও সময় লাগতে পারে। || Memory Complexity = O(n)
"""


# ==========================================================
# 06_Internal Working
# ==========================================================

"""
Example: x = [1,2]

Memory:
+----------------------+
| [1,2]                |
+----------------------+
          ▲
          |
          x

এরপর: y = x

+----------------------+
| [1,2]                |
+----------------------+
      ▲          ▲
      |          |
      x          y

এখানে x এবং y একই Object কে নির্দেশ করছে। এখন যদি লিখি, x.append(100) । তাহলে Memory

+----------------------+
| [1,2,100]            |
+----------------------+
      ▲          ▲
      |          |
      x          y

কারণ Object একটাই। এখন, z = x.copy()

Memory:
+----------------------+
| [1,2,100]            |
+----------------------+
      ▲        ▲
      |        |
      x        y


+----------------------+
| [1,2,100]            |
+----------------------+
          ▲
          |
          z

এখন z আলাদা List।
"""

# ==========================================================
# 07_Examples
# ==========================================================

print("\n========== Example 1 ==========")
x = [1, 2]
y = x
print(x)
print(y)
print(id(x))
print(id(y))
print(x is y)
print("Ending First Example")


print("========== Example 2 ==========")

x.append(100)

print(x)
print(y)

# দুইটাতেই পরিবর্তন হবে


print("\n========== Example 3 ==========")

z = x.copy()

print(id(x))
print(id(z))

print(x is z)

z.append(999)

print(x)
print(z)

# এখানে x পরিবর্তন হবে না


print("\n========== Example 4 ==========")

a = 100

b = a

print(a is b)

# Immutable Object


print("\n========== Example 5 ==========")

name = "Python"

another = name

print(name is another)



print("\n========== Example 6 ==========")

import copy
nested = [[1, 2], [3, 4]]
deep = copy.deepcopy(nested)
deep[0].append(100)
print(nested)
print(deep)

# Deep Copy হওয়ায় Original পরিবর্তন হয়নি

# ==========================================================
# Mutable vs Immutable
# ==========================================================

"""
Mutable Object মানে Object পরিবর্তন করা যায়।

উদাহরণ, 
✔ list
✔ dict
✔ set
✔ bytearray
----------------------------------
Immutable Object পরিবর্তন করা যায় না। পরিবর্তন করলে নতুন Object তৈরি হয়।
✔ int
✔ float
✔ bool
✔ tuple
✔ string
✔ frozenset

"""

# ==========================================================
# Reference
# ==========================================================

"""
Reference মানে Object-এর Address নয়, বরং Object-এর দিকে নির্দেশ করা একটি Link। Variable আসলে Reference ধরে রাখে।
"""

# ==========================================================
# Copy
# ==========================================================

"""
Shallow Copy: শুধু Outer Object Copy হয়। Nested Object একই থাকে।

Example: 
a = [[1],[2]]
b = a.copy()

এখন, b[0].append(10), Original-ও পরিবর্তন হবে। কারণ Inner List একই।
"""

# ==========================================================
# Deep Copy
# ==========================================================

"""
Deep Copy সব Nested Object-ও Copy হয়। Original-এর সাথে কোন সম্পর্ক থাকে না। সবচেয়ে নিরাপদ Copy।
"""

# ==========================================================
# id()
# ==========================================================

"""
id(): Object-এর Unique Identity Return করে। এটি দেখে বোঝা যায়, দুইটি Variable একই Object কে নির্দেশ করছে কিনা।
"""

# ==========================================================
# Memory
# ==========================================================

"""
RAM-এর ভিতরে প্রতিটি Object-এর একটি Memory Location থাকে। Variable সেই Object-এর Reference ধরে রাখে। একই Object-এর অনেকগুলো Variable থাকতে পারে।
"""

# ==========================================================
# 08_Common Mistakes
# ==========================================================

"""
❌ Mistake 1: a = [1,2], b = a ভাবা— b আলাদা List - আসলে নয়।
----------------------------------------
❌ Mistake 2: Nested List এ copy() ব্যবহার করা। copy() - Deep Copy নয়।
----------------------------------------
❌ Mistake 3: == এবং is গুলিয়ে ফেলা। == Value Compare করে। is Reference Compare করে.
----------------------------------------
❌ Mistake 4: Immutable Object ও Mutable Object একইভাবে কাজ করে মনে করা। ওরা একদম আলাদা আচরণ করে।
"""

# ==========================================================
# 09_Exercises
# ==========================================================

"""
Exercise 1: x=[10,20], y=x | id(x), id(y) কি Output হবে?
----------------------------------------
Exercise 2: x=[1,2], y=x.copy(), x.append(100) Print করলে কী হবে?
----------------------------------------
Exercise 3: Nested List নিয়ে copy() এবং deepcopy() এর পার্থক্য বের করুন।
----------------------------------------
Exercise 4: নিজে ১০টি Variable তৈরি করে, id() Compare করুন।
----------------------------------------
Exercise 5: is এবং == এর পার্থক্য নিজের ভাষায় লিখুন।
"""

# ==========================================================
# 10_AI Usage
# ==========================================================

"""
AI Engineer হিসেবে Variable & Memory Concept অত্যন্ত গুরুত্বপূর্ণ।

এটি ব্যবহৃত হয়—
✔ NumPy Array Copy
✔ Pandas DataFrame Copy
✔ PyTorch Tensor Clone
✔ Tensor Detach
✔ Machine Learning Dataset
✔ Data Augmentation
✔ Neural Network Weight Copy
✔ Model Checkpoint
✔ Reinforcement Learning
✔ Computer Vision
✔ NLP
✔ Multi-threading
✔ Multiprocessing
✔ Large Dataset Processing
✔ GPU Memory Optimization
✔ Cache Management
✔ Object Sharing
✔ Performance Optimization

যদি Variable & Memory Concept পরিষ্কার থাকে, তাহলে Debugging অনেক সহজ হবে, Memory Leak কম হবে, এবং বড় AI Project-এ Bug অনেক কম হবে। এই একটি Concept ভবিষ্যতে শত শত Bug হওয়া থেকে আপনাকে বাঁচাতে পারে।
"""