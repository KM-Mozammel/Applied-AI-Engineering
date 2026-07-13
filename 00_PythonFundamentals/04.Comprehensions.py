"""
============================================================
01_Introduction
============================================================
Comprehension হলো Python-এর সবচেয়ে শক্তিশালী এবং সুন্দর feature গুলোর একটি। এটি ব্যবহার করে খুব কম কোডে নতুন List, Dictionary, Set অথবা Generator তৈরি করা যায়।

Normal Loop:

result = []
for i in range(5):
    result.append(i)

List Comprehension:

result = [i for i in range(5)]

দুইটার Output একই; Output: [0, 1, 2, 3, 4]

Comprehension মূলত Loop + Condition + Expression এক লাইনে লেখার একটি উপায়। Python-এ মোট চার ধরনের comprehension আছে।

1. List Comprehension
2. Dictionary Comprehension
3. Set Comprehension
4. Generator Expression
"""

# ============================================================
# 02_WhyComprehensionsExists
# ============================================================
"""
আগে Python-এ List তৈরি করতে Loop লিখতে হতো।
numbers = []
for i in range(10):
    numbers.append(i)
এতে,
✔ বেশি কোড
✔ বেশি indentation
✔ readability কম

Python Developerরা বুঝলেন— "নতুন collection তৈরি করার কাজ প্রায় সব জায়গায় লাগে।" তাই Comprehension এসেছে। এর সুবিধা,
✔ কম কোড
✔ দ্রুত লেখা যায়
✔ সহজে বোঝা যায়
✔ Pythonic style
✔ অনেক ক্ষেত্রে Faster
"""

# ============================================================
# 03_Syntax
# ============================================================

"""
------------------------------------------------------------
1. List Comprehension
------------------------------------------------------------
[expression for variable in iterable]
"""
numbers = [i for i in range(5)]
print(numbers)

"""
Output: [0, 1, 2, 3, 4]
"""
# ------------------------------------------------------------
""" Expression পরিবর্তন করা যায়। """
square = [i * i for i in range(5)]
print(square)
"""
Output: [0, 1, 4, 9, 16]
"""
# ------------------------------------------------------------
""" Condition যোগ করা যায়। """
even = [i for i in range(10) if i % 2 == 0]
print(even)
"""
Output: [0, 2, 4, 6, 8]
"""
# ------------------------------------------------------------
"""
if else ব্যবহার করা যায়।
"""
labels = ["Even" if i % 2 == 0 else "Odd" for i in range(5)]
print(labels)
"""
Output: ['Even', 'Odd', 'Even', 'Odd', 'Even']
"""
# ------------------------------------------------------------

"""
Nested Loop
"""
pairs = [(i, j) for i in range(3) for j in range(2)]
print(pairs)
"""
Output: [(0,0),(0,1),(1,0),(1,1),(2,0),(2,1)]
"""

# ------------------------------------------------------------

"""
2. Dictionary Comprehension
Syntax: {key:value for variable in iterable}
"""
dictionary = {i: i * i for i in range(5)}
print(dictionary)
"""
Output:{ 0:0, 1:1, 2:4, 3:9, 4:16 }
"""
# ------------------------------------------------------------
""" Condition """
dictionary = {i: i * i for i in range(10) if i % 2 == 0}
print(dictionary)
""" Output: { 0:0, 2:4, 4:16, 6:36, 8:64} """
# ------------------------------------------------------------
""" 3. Set Comprehension """
myset = {i % 3 for i in range(10)}
print(myset)
""" Output: {0,1,2} | Duplicate automatically remove হয়ে যায়। """
# ------------------------------------------------------------
"""
4. Generator Expression
Syntax: (expression for variable in iterable)
"""
gen = (i * i for i in range(5))
print(gen)
""" Output: <generator object ...> Generator থেকে value বের করতে হয়। """
for value in gen:
    print(value)

""" Output: 0 1 4 9 16 """
# ============================================================
# 04_Methods
# ============================================================
"""
List Comprehension দিয়ে সবচেয়ে বেশি যেসব কাজ করা হয়।
"""
# ------------------------------------------------------------
# Mapping
# ------------------------------------------------------------
numbers = [1, 2, 3, 4]
double = [i * 2 for i in numbers]
print(double)
"""
Output: [2,4,6,8]
"""

# ------------------------------------------------------------
# Filtering
# ------------------------------------------------------------
numbers = range(10)
even = [i for i in numbers if i % 2 == 0]
print(even)
"""
Output: [0,2,4,6,8]
"""

# ------------------------------------------------------------
# Mapping + Filtering
# ------------------------------------------------------------
square = [i * i for i in range(10) if i % 2 == 0]
print(square)
"""
Output: [0,4,16,36,64]
"""

# ------------------------------------------------------------
# String Processing
# ------------------------------------------------------------
name = "Mozammel"
letters = [ch.upper() for ch in name]
print(letters)
"""
Output: ['M','O','Z','A','M','M','E','L']
"""

# ------------------------------------------------------------
# Flatten Nested List
# ------------------------------------------------------------
matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]
flat = [item for row in matrix for item in row]
print(flat)
"""
Output: [1,2,3,4,5,6]
"""

# ============================================================
# 05_TimeComplexity
# ============================================================
"""
Comprehension সাধারণ Loop-এর মতই iterate করে। যদি n element থাকে,
Loop: O(n)
List Comprehension: O(n)
Dictionary Comprehension: O(n)
Set Comprehension: O(n)
Generator: O(n)
তাহলে Comprehension Faster কেন?

কারণ,
✔ append method repeatedly lookup করতে হয় না
✔ Python internally optimize করে
✔ Bytecode কম হয়
তাই Practical Speed কিছুটা বেশি হয়।
"""

# ============================================================
# 06_InternalWorking
# ============================================================

"""
Example: square = [i*i for i in range(5)] - Python Internally প্রায় এমনভাবে কাজ করে।
"""
square = []
for i in range(5):
    square.append(i * i)
"""
Comprehension নতুন কোনো Algorithm নয়। এটি শুধু Loop-এর Short Form নয়। CPython-এর Compiler Comprehension-এর জন্য, বিশেষ Bytecode তৈরি করে।
Workflow:
range(5)
↓
Iterator তৈরি
↓
প্রতিটি element নেওয়া
↓
Expression Evaluate
↓
Result Store
↓
শেষে Complete List Return
"""

# ------------------------------------------------------------

"""
Generator Expression Internally: gen = (i*i for i in range(5))
এখানে List তৈরি হয় না।
Workflow:
Need Value?
↓
Next()
↓
Calculate
↓
Return
↓
Discard
↓
Next()

এ কারণেই Generator-এর Memory Usage খুব কম।
"""

# ============================================================
# 07_Examples
# ============================================================

print("\nExample 1")
numbers = [i for i in range(10)]
print(numbers)

# ------------------------------------------------------------

print("\nExample 2")
square = [i * i for i in range(10)]
print(square)

# ------------------------------------------------------------

print("\nExample 3")
odd = [i for i in range(20) if i % 2 == 1]
print(odd)

# ------------------------------------------------------------

print("\nExample 4")
words = ["apple", "banana", "cat"]
length = [len(word) for word in words]
print(length)

# ------------------------------------------------------------

print("\nExample 5")
students = ["Rahim", "Karim", "Sakib"]
upper = [student.upper() for student in students]
print(upper)

# ------------------------------------------------------------

print("\nExample 6")
dataset = [(i, 2 * i + 1) for i in range(10)]
print(dataset)

"""

তুমি আগে এই কোডটি জিজ্ঞেস করেছিলে। (i, 2*i+1) এটি একটি Tuple।

range(10):
0 : (0,1)
1 : (1,3)
2: (2,5)
3: (3,7)
...
শেষে:
[
 (0,1),
 (1,3),
 (2,5),
 ...
 (9,19)
]

এটি Machine Learning Dataset, Coordinate Data, Graph, Input-Output Pair তৈরি করতে প্রচুর ব্যবহার হয়।
"""

# ------------------------------------------------------------
print("\nExample 7")
dictionary = {i: chr(65 + i) for i in range(5)}
print(dictionary)
"""
Output:
{
 0:'A',
 1:'B',
 2:'C',
 3:'D',
 4:'E'
}
"""

# ------------------------------------------------------------

print("\nExample 8")
unique = {i % 5 for i in range(20)}
print(unique)

# ------------------------------------------------------------

print("\nExample 9")
generator = (i * i for i in range(5))
print(next(generator))
print(next(generator))
print(next(generator))

# ============================================================
# 08_CommonMistakes
# ============================================================

"""
১. অনেক বড় Logic Comprehension-এ লিখে ফেলা। Bad:
[x**2 if x%2==0 else x**3 if x>10 else x for x in numbers]
Readable নয়।
------------------------------------------------------------

২. Comprehension ব্যবহার করে শুধু Side Effect করা। Bad
[x.append(i) for i in range(10)] এটি করা উচিত নয়। Loop ব্যবহার করো।
------------------------------------------------------------

৩. Generator এবং List Confuse করা। 
numbers = (i for i in range(10))
print(numbers) এটি List নয়।
------------------------------------------------------------

৪. Generator একবার শেষ হয়ে গেলে পুনরায় ব্যবহার করা যায় না।
------------------------------------------------------------

৫. Nested Comprehension অতিরিক্ত ব্যবহার করা। অনেক সময় Normal Loop বেশি Readable।

"""

# ============================================================
# 09_Exercises
# ============================================================

"""
Exercise 1: ১-২০ পর্যন্ত Square বের করো।
Expected: [1,4,9,...]
------------------------------------------------------------
Exercise 2: শুধু Even Number বের করো।
------------------------------------------------------------
Exercise 3: ১০ জন Student-এর নাম Uppercase করো।
------------------------------------------------------------
Exercise 4:  Dictionary বানাও
{
 1:1,
 2:4,
 3:9,
 ...
}
------------------------------------------------------------
Exercise 5: Set তৈরি করো Number % 4
------------------------------------------------------------
Exercise 6: Nested List Flatten করো।
------------------------------------------------------------
Exercise 7: Generator দিয়ে ১-১০০ পর্যন্ত Number Generate করো।
------------------------------------------------------------
Exercise 8: এই Dataset তৈরি করো। [(x,x**2) for x in range(20)]
------------------------------------------------------------
Exercise 9: Matrix-এর সব Element Double করো।
------------------------------------------------------------
Exercise 10: নিজের Name-এর প্রতিটি Character-এর ASCII Value বের করো। Hint: ord()
"""

# ============================================================
# 10_AIUsage (Use Cases in AI Development)
# ============================================================

"""
AI Developer হিসেবে Comprehension প্রায় প্রতিদিন ব্যবহার করবে।

============================================================
১. Dataset তৈরি
============================================================
dataset = [(x, 2*x + 1) for x in range(100)]
Machine Learning-এর Toy Dataset তৈরিতে।
------------------------------------------------------------
২. Label তৈরি
labels = [1 if score > 0.5 else 0 for score in predictions]
Classification Label বানাতে।
------------------------------------------------------------
৩. Image Pixel Processing: normalized = [pixel / 255 for pixel in pixels] - Image Normalization।
------------------------------------------------------------
৪. Text Processing
tokens = [word.lower() for word in sentence.split()]
NLP-এর প্রথম ধাপ।
------------------------------------------------------------
৫. Remove Stop Words
filtered = [
    word
    for word in tokens
    if word not in stop_words
]
------------------------------------------------------------
৬. Embedding Filtering
vectors = [
    v
    for v in embeddings
    if len(v) == 768
]
------------------------------------------------------------
৭. Feature Engineering
features = [
    x["age"] / 100
    for x in dataset
]
------------------------------------------------------------
৮. Batch Preparation
batches = [
    data[i:i+32]
    for i in range(0, len(data), 32)
]
Deep Learning Training।
------------------------------------------------------------
৯. Dictionary Mapping
word_to_id = {
    word: idx
    for idx, word in enumerate(vocabulary)
}
Tokenizer তৈরিতে।
------------------------------------------------------------
১০. Generator Expression
huge_dataset = (
    process(x)
    for x in million_records
)
বড় Dataset Memory-তে না এনে
একটি করে Process করা যায়।
============================================================
AI Interview Questions
============================================================
১. List Comprehension এবং Generator-এর পার্থক্য কী?
২. কখন Generator ব্যবহার করবে?
৩. Nested Comprehension কী?
৪. Comprehension কি Loop-এর চেয়ে Faster?
৫. Dictionary Comprehension কোথায় ব্যবহার করো?
৬. Generator কেন Memory Efficient?
৭. [(i,2*i+1) for i in range(10)] কী করছে?
৮. AI Dataset তৈরিতে Comprehension কেন এত জনপ্রিয়?

============================================================
Summary
============================================================

✓ List Comprehension → নতুন List
✓ Dictionary Comprehension → নতুন Dictionary
✓ Set Comprehension → Unique Data
✓ Generator Expression → Lazy Evaluation
✓ Time Complexity → O(n)
✓ Memory

List  -> বেশি Memory, Generator -> খুব কম Memory
AI Development-এ Comprehension হলো সবচেয়ে বেশি ব্যবহৃত Python Feature-গুলোর একটি।
"""