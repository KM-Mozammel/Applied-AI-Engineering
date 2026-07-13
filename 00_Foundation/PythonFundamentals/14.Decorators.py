"""
==================================================
01_Introduction
==================================================
Decorator হলো Python-এর এমন একটি Feature, যেটি কোনো Function বা Method-এর মূল Code পরিবর্তন না করে তার আচরণ (Behavior) পরিবর্তন করতে দেয়। অর্থাৎ, Function-এর উপর অতিরিক্ত Feature যোগ করা যায়। 

Decorator ব্যবহার করে আমরা ✔ Logging ✔ authentication ✔ Authorization ✔ Timing ✔ Validation ✔ Retry Logic ✔ Caching 
✔ Monitoring সহজেই যোগ করতে পারি।
--------------------------------------------------
Real Life Example: ধরো, তুমি একটি Gift Box কিনেছো। Gift-এর ভিতরের জিনিস একই থাকে। কিন্তু বাইরে Ribbon, Wrapping Paper Card যোগ করা হয়েছে। Gift পরিবর্তন হয়নি। শুধু Extra Feature যোগ হয়েছে। Decorator-ও ঠিক একই কাজ করে।
==================================================
02_WhyDecoratorsExists
==================================================
ধরো, ১০০ টি Function আছে। সব Function শুরু হওয়ার আগে print("Running...") লিখতে হবে।
Without Decorator:
def login():
    print("Running...")
    ...

def logout():
    print("Running...")
    ...

def register():
    print("Running...")
    ...

একই Code বারবার লিখতে হচ্ছে। এটাকে বলে Code Duplication
--------------------------------------------------
Decorator ব্যবহার করলে

@logger
def login():
    ...

@logger
def logout():
    ...

@logger
def register():
    ...

একটি Function দিয়েই সব Function-এর Behavior পরিবর্তন করা যায়।
==================================================
03_Syntax
==================================================

Basic Decorator____

def logger(func):
    def wrapper():
        print("Running Function")
        func()
    return wrapper
--------------------------------------------------
@logger
def hello():
    print("Hello")
    
hello()

Output: Running Function - Hello
--------------------------------------------------
Decorator আসলে hello = logger(hello) এই Code-এর Shortcut।
==================================================
04_Methods
==================================================
Decorator-এর নিজস্ব Method নেই। কিন্তু Decorator তৈরি করতে সাধারণত
১। Outer Function
২। Wrapper Function
৩। Return Wrapper

ব্যবহার করা হয়।
--------------------------------------------------
Example

def logger(func):
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper

--------------------------------------------------
Wrapper-এ *args, **kwargs ব্যবহার করলে যে কোনো Function Decorate করা যায়।
==================================================
05_TimeComplexity
==================================================
Decorator নিজে সাধারণত O(1) অতিরিক্ত সময় নেয়। মূল Function-এর Complexity পরিবর্তন করে না। Example
Original Function - O(n)
Decorator - O(1)
Final - O(n)

==================================================
06_InternalWorking
==================================================
Example: 
@logger
def hello():
    print("Hello")
--------------------------------------------------
Python Interpreter: 
Step 1 -> hello Function তৈরি হয়।
Step 2 -> @logger দেখা যায়।
Step 3 -> Python আসলে চালায় hello = logger(hello)
Step 4 -> logger() wrapper Return করে।
Step 5 -> hello এখন Original Function নয়। বরং wrapper Function
--------------------------------------------------
Memory: hello -> wrapper() -> Original hello()
--------------------------------------------------
যখন, hello() Call করা হয়, আসলে wrapper() Execute হয়।
wrapper() -> Before Code -> Original Function -> After Code
==================================================
07_Examples
==================================================
Example 1: Simple Logger

def logger(func):
    def wrapper():
        print("Running")
        func()
    return wrapper

@logger
def hello():
    print("Hello")
    
hello()

--------------------------------------------------

Example 2: Decorator with Arguments

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
def add(a,b):
    return a+b

print(add(5,3))

--------------------------------------------------

Example 3: Timing Decorator

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start=time.time()
        result=func(*args, **kwargs)
        end=time.time()
        print(end-start)
        return result

    return wrapper

--------------------------------------------------

Example 4: Your AI Training Example
Dataset -> Epoch Iterator -> Batch Generator -> @logger -> train() -> loss() -> Gradient Update
এখানে train() এবং loss() দুটিই Decorator দ্বারা Logging পাচ্ছে।

==================================================
08_CommonMistakes
==================================================
❌ Mistake 1: Wrapper Return না করা।

def logger(func):
    def wrapper():
        ...

ভুল, return wrapper দিতে হবে।
--------------------------------------------------
❌ Mistake 2: Function Call করে ফেলা। ভুল: return wrapper() ঠিক: return wrapper
--------------------------------------------------
❌ Mistake 3: *args **kwargs ব্যবহার না করা। def wrapper(): এতে Arguments নেওয়া যায় না। 
ঠিক: def wrapper(*args, **kwargs):
--------------------------------------------------
❌ Mistake 4: Result Return না করা। result = func(...); return result না দিলে Original Function-এর Return Value হারিয়ে যায়।

==================================================
09_Exercises
==================================================
Exercise 1: Logger Decorator তৈরি করো।
--------------------------------------------------
Exercise 2: Timer Decorator তৈরি করো।
--------------------------------------------------
Exercise 3: Authentication Decorator তৈরি করো। User Login না থাকলে Permission Denied Print করবে।
--------------------------------------------------
Exercise 4: Retry Decorator তৈরি করো। Function Fail করলে ৩ বার Retry করবে।
--------------------------------------------------
Exercise 5: Decorator তৈরি করো যা Function Call Count করবে। Output: Called 1 Times, Called 2 Times, Called 3 Times

==================================================
10_AIUsage (Use Case in AI Development)
==================================================
Decorator AI Engineering-এ ব্যাপকভাবে ব্যবহৃত হয়।
--------------------------------------------------
১। Training Logger: 
@logger
def train():
Training শুরু এবং শেষ Log করা।
--------------------------------------------------
২। Time Measurement:

@timer
def inference():

Inference Time Measure করা।
--------------------------------------------------
৩। GPU Monitoring: Decorator দিয়ে GPU Usage, Memory Usage Track করা হয়।
--------------------------------------------------
৪। Exception Handling: Decorator দিয়ে সব Function-এর Error Automatically Handle করা যায়।
--------------------------------------------------
৫। API Monitoring: FastAPI, Flask, Django সব Framework-এ Decorator ব্যবহৃত হয়। Example, @app.get("/predict") এটিও একটি Decorator।
--------------------------------------------------
৬। Authentication: @login_required Decorator দিয়ে User Login Check করা হয়।
--------------------------------------------------
৭। Machine Learning Experiment Tracking Decorator দিয়ে Loss, Accuracy, Epoch, Learning Rate, Automatically Log করা যায়।
--------------------------------------------------
৮। Caching: @lru_cache Decorator দিয়ে Repeated Computation এড়ানো হয়। Deep Learning এবং NLP-তে অনেক Expensive Function Cache করা হয়।
--------------------------------------------------

Summary, Decorator মানে "Function পরিবর্তন না করে তার Behavior পরিবর্তন করা" Decorator-এর সবচেয়ে বড় সুবিধা

✔ Reusable Code
✔ Cleaner Code
✔ Separation of Concerns
✔ Logging
✔ Monitoring
✔ Authentication
✔ Timing
✔ Caching

Backend Development, AI Engineering, Data Engineering, FastAPI, Flask, Django, PyTorch, TensorFlow— সব জায়গাতেই Decorator অত্যন্ত গুরুত্বপূর্ণ।
"""