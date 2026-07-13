"""
==================================================
01_Introduction
==================================================
Pythonic Coding বলতে বোঝায় Python Language-এর Philosophy অনুসরণ করে Readable, Simple, Elegant, Maintainable Code লেখা। Python-এ শুধু Code কাজ করলেই হবে না। Professional Developer-রা এমনভাবে Code লেখেন, যাতে ✔ সহজে পড়া যায়, ✔ সহজে Maintain করা যায়, ✔ Team-এর সবাই বুঝতে পারে, ✔ Future-এ Modify করা সহজ হয়
--------------------------------------------------
Pythonic Coding-এর মূল বিষয়গুলো: ✔ PEP 8, ✔ Zen of Python, ✔ EAFP, ✔ LBYL, ✔ Clean Code, ✔ Professional Habits
--------------------------------------------------
Remember, Python Code Computer-এর জন্য নয়। মানুষের পড়ার জন্য।

==================================================
02_WhyPythonicCodingExists
==================================================
ধরো, দুইজন Developer একই Problem Solve করলো।
Developer A:
def f(a):
    return[a*2 for a in a]

--------------------------------------------------
Developer B:
def double_numbers(numbers):
    return [number * 2 for number in numbers]

দুটোই কাজ করে। কিন্তু দ্বিতীয়টি অনেক বেশি Readable। Professional Company-তে Code Years ধরে থাকে। তাই, Readable Code সবচেয়ে গুরুত্বপূর্ণ।

==================================================
03_Syntax
==================================================
PEP 8: Python-এর Official Style Guide।
--------------------------------------------------
Variable: user_name ✔ - UserName ❌
--------------------------------------------------
Constant: MAX_SIZE=100
--------------------------------------------------
Function: 
def calculate_total():
    ...
--------------------------------------------------
Class:
class Student:
    ...
--------------------------------------------------
Import:

import os
import sys

--------------------------------------------------
Indentation: 4 Spaces
==================================================
04_Methods
==================================================
PEP 8: Official Style Guide
--------------------------------------------------
Zen of Python: 

import this

Output: Beautiful is better than ugly. Simple is better than complex. Readability counts.
...
--------------------------------------------------
EAFP: Easier to Ask Forgiveness than Permission

try:
    value=data["name"]

except KeyError:
    value="Unknown"

--------------------------------------------------
LBYL: Look Before You Leap

if "name" in data:
    value=data["name"]

--------------------------------------------------
Professional Habit: Meaningful Variable Name, Small Function, Docstring, Type Hint, Logging, Testing

==================================================
05_TimeComplexity: Pythonic Coding Algorithm-এর Complexity পরিবর্তন করে না। কিন্তু Maintainability, Readability, Development Speed অনেক Improve করে।
==================================================
06_InternalWorking
==================================================
Example:

try:
    value=data["name"]
except KeyError:
    ...
--------------------------------------------------
Step 1: Interpreter: Dictionary Access করে।
Step 2: Key থাকলে Value Return।
Step 3: Key না থাকলে KeyError Raise।
Step 4: except Handle করে।
--------------------------------------------------
LBYL:
Step 1: "name" in data -> True -> Access অথবা False -> Skip
==================================================
07_Examples
==================================================
Example 1: Bad Variable Name
x=10
y=20
z=x+y
--------------------------------------------------
Pythonic: 
first_number=10
second_number=20
total=first_number+second_number
--------------------------------------------------

Example 2:
PEP 8
def calculate_area(radius):
    return 3.1416*radius**2
--------------------------------------------------

Example 3: EAFP
data={}
try:
    age=data["age"]

except KeyError:
    age=0

--------------------------------------------------

Example 4: LBYL

data={}

if "age" in data:
    age=data["age"]

else:
    age=0

--------------------------------------------------
Example 5: Professional Function:

def normalize(values):
    # Normalize values between 0 and 1.
    maximum=max(values)
    return [ value/maximum for value in values ]

==================================================
08_CommonMistakes
==================================================
❌ Mistake 1: Meaningless Variable - a, b, c, 
✔ student_name, learning_rate, batch_size
--------------------------------------------------
❌ Mistake 2:  Very Long Function - 500 Lines ভুল। ছোট Function লেখো।
--------------------------------------------------
❌ Mistake 3: PEP 8 Ignore করা। Mixed Naming, Random Spacing Avoid করো।
--------------------------------------------------
❌ Mistake 4: Comment দিয়ে সব Explain করা। ভুল, Good Code নিজেই Explain করবে।

==================================================
09_Exercises
==================================================
Exercise 1: PEP 8 অনুসারে একটি Function লিখো।
--------------------------------------------------
Exercise 2: EAFP Style-এ Dictionary Access করো।
--------------------------------------------------
Exercise 3: LBYL Style-এ একই Problem Solve করো।
--------------------------------------------------
Exercise 4: Bad Code Pythonic Code-এ Convert করো।
--------------------------------------------------
Exercise 5: নিজের লেখা পুরোনো Code PEP 8 অনুযায়ী Refactor করো।

==================================================
10_AIUsage (Use Case in AI Development)
==================================================
AI Engineering-এ Pythonic Coding অত্যন্ত গুরুত্বপূর্ণ।
--------------------------------------------------
১। Readable Training Pipeline: Dataset -> Preprocessing -> Training -> Evaluation -> Prediction প্রতিটি Step আলাদা Function-এ লেখা হয়।
--------------------------------------------------
২। Team Collaboration একাধিক AI Engineer একই Codebase-এ কাজ করে। Readable Code Maintenance সহজ করে।
--------------------------------------------------
৩। Model Configuration: Meaningful Variable, learning_rate, batch_size, num_epochs, dropout_rate
--------------------------------------------------
৪। MLOps: Production Pipeline-এ Logging, Testing, Type Hint, Docstring, PEP 8 সব Follow করা হয়।
--------------------------------------------------
৫। LLM Application: Prompt Builder, Vector Search, Embedding, API Client সব Modular Function-এ ভাগ করা হয়।
--------------------------------------------------
৬। Open Source AI: PyTorch, TensorFlow, NumPy, Pandas, FastAPI সব Project PEP 8 এবং Pythonic Style অনুসরণ করে।
--------------------------------------------------
৭। Professional Development Habit: 

✔ Meaningful Naming
✔ Small Functions
✔ Type Hints
✔ Docstrings
✔ Logging
✔ Testing
✔ Exception Handling
✔ Code Review
✔ Refactoring
✔ Consistent Formatting

==================================================
Summary
==================================================

PEP 8: Official Python Style Guide: 
Zen of Python - Python-এর Design Philosophy
EAFP: আগে চেষ্টা করো Error হলে Handle করো
LBYL: আগে Check করো, তারপর কাজ করো
Professional Habits
↓
Readable Code
↓
Maintainable Code
↓
Reliable Code
↓
Production Ready Code

Pythonic Coding-এর মূল লক্ষ্য "Code এমনভাবে লেখো, যাতে ছয় মাস পরে নিজেই পড়ে বুঝতে পারো, আর Team-এর অন্য Developer-ও সহজে বুঝতে পারে।" Professional AI Engineering, Backend Development, Data Engineering, Machine Learning এবং Open Source Project-এ Pythonic Coding একটি অপরিহার্য Skill।
"""