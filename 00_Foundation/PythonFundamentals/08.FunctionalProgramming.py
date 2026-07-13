# ============================================================
# 01_Introduction
# ============================================================
"""
Functional Programming (FP) হলো এমন একটি Programming Style যেখানে Function-কে সবচেয়ে গুরুত্বপূর্ণ অংশ হিসেবে ব্যবহার করা হয়। Object-Oriented Programming (OOP)-এ আমরা Object নিয়ে কাজ করি। Functional Programming-এ আমরা Function নিয়ে কাজ করি। Python পুরোপুরি Functional Language নয়। এটি Multi-Paradigm Language। অর্থাৎ Python দিয়ে তুমি লিখতে পারো—

✅ Procedural Programming
✅ Object-Oriented Programming
✅ Functional Programming

Functional Programming-এর প্রধান লক্ষ্য: 
• একই Input দিলে সবসময় একই Output পাওয়া
• Side Effect কমানো
• Data পরিবর্তন না করে নতুন Data তৈরি করা
• ছোট ছোট Function একত্রে ব্যবহার করা

Example:
numbers = [1,2,3,4]
result = list(map(lambda x: x*2, numbers))
Output: [2,4,6,8]
"""
# ============================================================
# 02_WhyFunctionalProgrammingExists
# ============================================================
"""
Functional Programming কেন তৈরি হয়েছে? বড় Software Project-এ Data অনেক জায়গা দিয়ে যায়।  যদি Function Data পরিবর্তন করে ফেলে, তাহলে Bug খুঁজে পাওয়া কঠিন হয়।
Example: 
--------------
balance = 100
def withdraw():
    global balance
    balance -= 20

এখানে Function Global Variable পরিবর্তন করছে। Functional Programming বলবে

def withdraw(balance):
    return balance - 20

এখন Function শুধু Input নেয় এবং Output দেয়। Global কিছু পরিবর্তন করে না।

Benefits: 
✅ কম Bug
✅ Code Reuse
✅ Testing সহজ
✅ Parallel Processing সহজ
✅ Data Pipeline তৈরি করা সহজ
"""

# ============================================================
# 03_Syntax
# ============================================================
# ------------------------------------------------------------
# lambda
# ------------------------------------------------------------
square = lambda x: x * x
print(square(5))

# Equivalent:
def square2(x):
    return x * x
print(square2(5))

# ------------------------------------------------------------
# map()
# ------------------------------------------------------------
numbers = [1, 2, 3, 4]
double = list(map(lambda x: x * 2, numbers))
print(double)

# ------------------------------------------------------------
# filter()
# ------------------------------------------------------------
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)

# ------------------------------------------------------------
# reduce()
# ------------------------------------------------------------
from functools import reduce
total = reduce(lambda x, y: x + y, numbers)
print(total)

# ------------------------------------------------------------
# zip()
# ------------------------------------------------------------
names = ["A", "B", "C"]
ages = [20, 21, 22]
print(list(zip(names, ages)))

# ------------------------------------------------------------
# enumerate()
# ------------------------------------------------------------
for index, value in enumerate(names):
    print(index, value)

# ------------------------------------------------------------
# sorted()
# ------------------------------------------------------------
nums = [5, 2, 8, 1]
print(sorted(nums))

# ------------------------------------------------------------
# key=
# ------------------------------------------------------------
students = [
    ("Rahim", 80),
    ("Karim", 65),
    ("Hasan", 95)
]
print(sorted(students, key=lambda x: x[1]))

# ============================================================
# 04_Methods
# ============================================================

"""
আজকের Data Processing-এর সবচেয়ে বেশি ব্যবহৃত Functional Tools
১. lambda: এক লাইনের ছোট Function। Example: lambda x: x*x
-----------------------------------------
২. map(): প্রত্যেক Element-এর উপর Function চালায়। Input: [1,2,3] - Output: [2,4,6]
-----------------------------------------
৩. filter(): শুধু Condition True হলে Element রাখে। Example: [2,4,6]
-----------------------------------------
৪. reduce(): সব Element Combine করে একটি Value বানায়। Example: 1+2+3+4 -> 10
-----------------------------------------
৫. zip(): একাধিক Iterable-কে Pair বানায়।
["A","B"]
[10,20]
↓
("A",10)
("B",20)
-----------------------------------------
৬. enumerate(): Index সহ Loop করার জন্য।
0 A
1 B
2 C
-----------------------------------------
৭. sorted(): নতুন Sorted List দেয়। Original List পরিবর্তন করে না।
-----------------------------------------
৮. key= Sorting-এর Rule নির্ধারণ করে। Example: Age অনুযায়ী Sort, Name অনুযায়ী Sort, Length অনুযায়ী Sort
"""
# ============================================================
# 05_TimeComplexity
# ============================================================
"""
lambda: O(1)
----------------------------------
map(): n টি Element O(n)
----------------------------------
filter(): O(n)
----------------------------------
reduce(): O(n)
----------------------------------
zip(): O(n)
----------------------------------
enumerate(): O(n)
----------------------------------
sorted(): Python TimSort ব্যবহার করে Average: O(n log n)
----------------------------------
key=: Sorting-এর অংশ, মোট Complexity O(n log n)
"""
# ============================================================
# 06_InternalWorking
# ============================================================
"""
১) map(): numbers -> Iterator তৈরি করে -> একটি Element নেয় -> Function চালায় -> Result দেয় -> পরের Element
-----------------------------------
২) filter(): Element -> Condition -> True? -> হ্যাঁ -> Return -> না -> Skip
-----------------------------------
৩) reduce(): 1 -> combine -> 3 -> combine -> 6 -> combine -> 10
-----------------------------------
৪) zip(): List1 -> A -> List2 -> 10 -> (A,10)
-----------------------------------
৫) sorted(): TimSort Algorithm -> Natural Run খুঁজে বের করে -> Merge করে -> Sorted List তৈরি করে। TimSort বাস্তবে QuickSort-এর তুলনায় অনেক ক্ষেত্রে দ্রুত কাজ করে, বিশেষ করে যখন Data আংশিকভাবে Sorted থাকে।
-----------------------------------
৬) lambda: Python Runtime-এ একটি Function Object তৈরি হয়। অর্থাৎ, lambda x:x*x এবং 
def square(x):
    return x*x
দুটিই Function Object তৈরি করে।
"""

# ============================================================
# 07_Examples
# ============================================================
print("\n========== lambda ==========")
cube = lambda x: x ** 3
print(cube(3))

print("\n========== map ==========")
nums = [1, 2, 3, 4]
print(list(map(lambda x: x + 100, nums)))

print("\n========== filter ==========")
print(list(filter(lambda x: x > 2, nums)))

print("\n========== reduce ==========")
from functools import reduce
product = reduce(lambda x, y: x * y, nums)
print(product)

print("\n========== zip ==========")
names = ["A", "B", "C"]
marks = [80, 90, 95]
print(list(zip(names, marks)))

print("\n========== enumerate ==========")
for i, value in enumerate(names):
    print(i, value)

print("\n========== sorted ==========")
words = ["banana", "cat", "apple", "kiwi"]
print(sorted(words))
print(sorted(words, key=len))

print("\n========== key ==========")
employees = [
    {"name": "Rahim", "salary": 50000},
    {"name": "Karim", "salary": 35000},
    {"name": "Hasan", "salary": 70000},
]
print(sorted(employees, key=lambda emp: emp["salary"]))

# Reverse Sort
print(sorted(employees,
             key=lambda emp: emp["salary"],
             reverse=True))

# ============================================================
# 08_CommonMistakes
# ============================================================

"""
১. map() ব্যবহার করে list() না দিলে Result দেখা যায় না। Wrong: map(...) - Correct: list(map(...))
----------------------------------
২. filter(): Boolean Return করতে হবে।
----------------------------------
৩. reduce() Import করতে হয়। from functools import reduce
----------------------------------
৪. lambda-এর ভিতরে অনেক Logic লিখো না। খুব জটিল হয়ে যায়।
----------------------------------
৫. sorted() Original List পরিবর্তন করে না। nums.sort() Original পরিবর্তন করে। sorted(nums) নতুন List দেয়।
----------------------------------
৬. key= Value Return করবে। Boolean নয়। Wrong: key=lambda x:x>5 - Correct: key=lambda x:x[1]
"""
# ============================================================
# 09_Exercises
# ============================================================
"""
Exercise 1: lambda দিয়ে Square Function লেখো।
-----------------------------------
Exercise 2: map() দিয়ে [1,2,3,4] -> [10,20,30,40]
-----------------------------------
Exercise 3: filter() দিয়ে Odd Number বের করো।
-----------------------------------
Exercise 4: reduce() দিয়ে সব সংখ্যার যোগফল বের করো।
-----------------------------------
Exercise 5: zip() Name এবং Age Pair করো।
-----------------------------------
Exercise 6: enumerate() Index সহ Print করো।
-----------------------------------
Exercise 7: Length অনুযায়ী Word Sort করো। Hint : key=len
-----------------------------------
Exercise 8: Dictionary-এর List-কে Salary অনুযায়ী Sort করো।
-----------------------------------
Exercise 9: Students-দের নাম Alphabetical Order-এ Sort করো।
-----------------------------------
Exercise 10: map() + filter() একসাথে ব্যবহার করে প্রথমে Even Number বের করো, তারপর সেগুলোকে Square করো।
"""
# ============================================================
# 10_AIUsage (Use Cases in AI Development)
# ============================================================
"""
AI, Data Science এবং Machine Learning-এ Functional Programming খুব বেশি ব্যবহৃত হয়।
১. Data Preprocessing: 
texts = [" AI ", " Python ", " ML "]
clean = list(map(str.strip, texts))
Output: ['AI', 'Python', 'ML']
------------------------------------------------
২. Dataset Filtering:
scores = [45, 80, 60, 20]
passed = list(filter(lambda x: x >= 50, scores))
------------------------------------------------
৩. Feature Engineering: 
features = list(map(lambda x: x / 255, pixels))
Image Normalization-এর সময় প্রায়ই করা হয়।
------------------------------------------------
৪. Sorting Prediction: 
predictions = [
    ("Cat", 0.45),
    ("Dog", 0.91),
    ("Bird", 0.20)
]

best = sorted(
    predictions,
    key=lambda x: x[1],
    reverse=True
)
------------------------------------------------
৫. Token Processing (NLP): 
tokens = ["the", "cat", "is", "running"]
upper = list(map(str.upper, tokens))
------------------------------------------------
৬. Batch Processing: একসাথে হাজার হাজার Data-এর উপর একই Function চালাতে map() ব্যবহার করা যায়।
------------------------------------------------
"""