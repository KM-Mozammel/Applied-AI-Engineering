"""
=========================================================
Context Manager
=========================================================

Python Tutorial (বাংলা)

Topics
------
01_Introduction
02_WhyContextManagerExists
03_Syntax
04_Methods
05_TimeComplexity
06_InternalWorking
07_Examples
08_CommonMistakes
09_Exercises
10_AIUsage (Use Case in AI Development)

=========================================================
01_Introduction
=========================================================

Context Manager হলো Python-এর এমন একটি Feature
যা কোনো Resource নিরাপদভাবে (Safely) ব্যবহার এবং
ব্যবহার শেষে স্বয়ংক্রিয়ভাবে Release করার ব্যবস্থা করে।

Resource বলতে বোঝায়—

• File
• Database Connection
• Network Connection
• Socket
• Lock
• Thread Resource
• GPU Memory
• Temporary File

ধরো তুমি একটি File Open করলে।

file = open("data.txt")

এখন File Close করতে হবে।

file.close()

যদি Program-এর মাঝখানে Error হয়?

তাহলে close() আর Execute হবে না।

ফলে File Open অবস্থায় থেকে যেতে পারে।

এই সমস্যার সমাধানই Context Manager।

Python-এ Context Manager সাধারণত

with

Keyword-এর মাধ্যমে ব্যবহার করা হয়।

=========================================================
02_WhyContextManagerExists
=========================================================

Context Manager আসার আগে

try...

finally...

ব্যবহার করতে হতো।

Example

file = open("data.txt")

try:

    data = file.read()

finally:

    file.close()

এটি কাজ করে।

কিন্তু Code বড় হলে

বারবার

try
finally

লিখতে বিরক্তিকর হয়ে যায়।

Problems

❌ File Close করতে ভুলে যাওয়া

❌ Database Connection Open থেকে যাওয়া

❌ Memory Leak

❌ Lock Release না হওয়া

❌ Resource Waste

এই সমস্যাগুলোর সমাধানের জন্য

Context Manager এসেছে।

এর মূল কাজ

✔ Resource Acquire করা

✔ কাজ করা

✔ Resource Release করা

=========================================================
03_Syntax
=========================================================

সবচেয়ে পরিচিত Syntax

with open("data.txt", "r") as f:

    data = f.read()

print(data)

এখানে

with

Context শুরু করছে।

open()

একটি Context Manager Return করছে।

as f

File Object-কে

f

Variable-এ রাখছে।

Block শেষ হলেই

File Automatically Close হয়ে যায়।

---------------------------------------------------------

Equivalent Code

f = open("data.txt")

try:

    data = f.read()

finally:

    f.close()

---------------------------------------------------------

নিজের Context Manager

class MyContext:

    def __enter__(self):

        print("Resource Open")

        return self

    def __exit__(self, exc_type, exc_value, traceback):

        print("Resource Closed")

with MyContext():

    print("Working...")

Output

Resource Open

Working...

Resource Closed

=========================================================
04_Methods
=========================================================

Context Manager-এর সবচেয়ে গুরুত্বপূর্ণ দুটি Method

---------------------------------------------------------
1. __enter__()
---------------------------------------------------------

Context শুরু হলে Call হয়।

এখানে সাধারণত

✔ File Open

✔ Database Connect

✔ Lock Acquire

✔ Resource Allocate

করা হয়।

Example

def __enter__(self):

    print("Open")

    return self

---------------------------------------------------------
2. __exit__()
---------------------------------------------------------

Context শেষ হলে Call হয়।

এখানে

✔ File Close

✔ Connection Close

✔ Lock Release

✔ Memory Cleanup

হয়।

Example

def __exit__(self, exc_type, exc_value, traceback):

    print("Close")

---------------------------------------------------------
Parameters

exc_type

Exception-এর Type

exc_value

Exception Object

traceback

Error কোথায় হয়েছে

যদি Block-এর ভিতরে কোনো Exception না হয়

তাহলে

সবগুলো

None

হবে।

=========================================================
contextlib Module
=========================================================

Python-এর Built-in Module

contextlib

নিজের Context Manager সহজে বানাতে সাহায্য করে।

Example

from contextlib import contextmanager

@contextmanager

def my_context():

    print("Open")

    yield

    print("Close")

with my_context():

    print("Working")

Output

Open

Working

Close

এখানে

yield

এর আগের অংশ

__enter__()

এর মতো কাজ করে।

yield

এর পরের অংশ

__exit__()

এর মতো কাজ করে।

=========================================================
05_TimeComplexity
=========================================================

Context Manager নিজে কোনো Algorithm নয়।

এর Time Complexity সাধারণত

Enter

O(1)

Exit

O(1)

File Read বা Database Query-এর Complexity

Resource-এর উপর নির্ভর করে।

with

Keyword অতিরিক্ত কোনো উল্লেখযোগ্য Performance Cost যোগ করে না।

=========================================================
06_InternalWorking
=========================================================

ধরো

with open("data.txt") as f:

    data = f.read()

Python ভিতরে কী করে?

Step 1

open()

Call হয়।

↓

File Object তৈরি হয়।

↓

Step 2

__enter__()

Automatic Call হয়।

↓

Return Value

f

Variable-এ Assign হয়।

↓

Step 3

with Block Execute হয়।

↓

data = f.read()

↓

Step 4

Block শেষ হলে

__exit__()

Automatic Call হয়।

↓

File Close হয়ে যায়।

যদি Exception হয়

↓

তবুও

__exit__()

Call হয়।

অর্থাৎ

Resource Leak হয় না।

=========================================================
07_Examples
=========================================================

Example 1

with open("hello.txt") as f:

    print(f.read())

---------------------------------------------------------

Example 2

class Database:

    def __enter__(self):

        print("Connected")

        return self

    def __exit__(self, exc_type, exc_value, traceback):

        print("Disconnected")

with Database():

    print("Query Running")

Output

Connected

Query Running

Disconnected

---------------------------------------------------------

Example 3

from contextlib import contextmanager

@contextmanager

def timer():

    print("Start")

    yield

    print("End")

with timer():

    print("Working")

---------------------------------------------------------

Example 4

import threading

lock = threading.Lock()

with lock:

    print("Critical Section")

Lock Automatically Release হবে।

=========================================================
08_CommonMistakes
=========================================================

❌ File Open করে Close না করা

Wrong

f = open("a.txt")

Correct

with open("a.txt") as f:

    ...

---------------------------------------------------------

❌ __enter__() থেকে কিছু Return না করা

Wrong

def __enter__(self):

    pass

Correct

def __enter__(self):

    return self

---------------------------------------------------------

❌ __exit__() এর Parameter ভুল লেখা

সঠিক

def __exit__(self,
             exc_type,
             exc_value,
             traceback):

---------------------------------------------------------

❌ Context Manager-এর বাইরে File ব্যবহার করা

with open("a.txt") as f:

    pass

print(f.read())

এখানে Error হবে।

কারণ File ইতিমধ্যেই Close হয়ে গেছে।

=========================================================
09_Exercises
=========================================================

Exercise 1

with open()

ব্যবহার করে একটি File পড়ো।

---------------------------------------------------------

Exercise 2

নিজের Context Manager তৈরি করো।

---------------------------------------------------------

Exercise 3

__enter__()

Call হলে

"Connected"

Print করো।

---------------------------------------------------------

Exercise 4

__exit__()

Call হলে

"Disconnected"

Print করো।

---------------------------------------------------------

Exercise 5

contextlib.contextmanager

ব্যবহার করে Context Manager বানাও।

---------------------------------------------------------

Exercise 6

Timer Context Manager তৈরি করো
যা Execution Time Measure করবে।

---------------------------------------------------------

Exercise 7

Database Connection Context Manager তৈরি করো।

---------------------------------------------------------

Exercise 8

Thread Lock-এর জন্য

with lock

ব্যবহার করো।

---------------------------------------------------------

Exercise 9

একটি Temporary File Context Manager তৈরি করো।

---------------------------------------------------------

Exercise 10

নিজের Logger Context Manager তৈরি করো
যা Context Enter ও Exit হলে Log Print করবে।

=========================================================
10_AIUsage (Use Case in AI Development)
=========================================================

AI এবং Machine Learning Project-এ Context Manager
অনেক গুরুত্বপূর্ণ।

কারণ AI Project-এ প্রচুর Resource ব্যবহৃত হয়।

যেমন

• GPU Memory
• Model File
• Dataset
• Database
• Temporary Directory
• Thread Lock

Example

with torch.no_grad():

    prediction = model(x)

এখানে

torch.no_grad()

একটি Context Manager।

এটি Temporaryভাবে Gradient Calculation বন্ধ রাখে।

ফলে

✔ Memory কম লাগে

✔ Inference দ্রুত হয়

✔ GPU Efficient হয়

আরেকটি Example

from contextlib import nullcontext

from contextlib import ExitStack

এগুলো Complex Resource Management-এর জন্য ব্যবহৃত হয়।

অনেক AI Framework

TensorFlow

PyTorch

Hugging Face Transformers

LangChain

সবখানেই Context Manager ব্যবহৃত হয়।

বিশেষ করে

• Model Loading

• GPU Allocation

• Mixed Precision Training

• File Handling

• Logging

• Temporary Resources

=========================================================
সংক্ষেপে
=========================================================

Context Manager
→ Resource Safely Manage করে

with
→ Context শুরু করে

as
→ Return Value Variable-এ রাখে

__enter__()
→ Resource Acquire করে

__exit__()
→ Resource Release করে

contextlib
→ সহজে Custom Context Manager তৈরি করতে সাহায্য করে

@contextmanager
→ yield ব্যবহার করে Context Manager বানানো যায়

with open(...)
→ File Automatically Close করে

Context Manager শেখার পরে
তুমি File Handling, Database, Threading,
Networking, Async Programming, PyTorch,
TensorFlow এবং Production-level Python
অনেক সহজে বুঝতে পারবে।
"""