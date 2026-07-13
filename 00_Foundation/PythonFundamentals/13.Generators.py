"""
=========================================================
01_Introduction
=========================================================
Generator হলো Python-এর একটি বিশেষ ধরনের Iterator যা একসাথে সব Data Memory-তে Load না করে, প্রয়োজন অনুযায়ী (On-Demand) একটি করে Value Return করে। Generator-এর সবচেয়ে গুরুত্বপূর্ণ Keyword হলো yield সাধারণ Function - return দিয়ে শেষ হয়ে যায়।
কিন্তু Generator, yield দিয়ে Value Return করার পরে তার বর্তমান State (অবস্থা) মনে রাখে। পরবর্তীতে আবার Call করলে সেখান থেকেই Execute শুরু হয়। Generator-এর মূল উদ্দেশ্য, 
✔ Memory Save করা
✔ Lazy Evaluation
✔ Infinite Data Stream তৈরি করা
✔ Large Dataset Handle করা

=========================================================
02_WhyGeneratorsExist
=========================================================
ধরো তোমার কাছে, ১ কোটি সংখ্যা আছে।
Normal Function:

def numbers():
    return list(range(100000000))

এখানে, পুরো List Memory-তে Load হবে। ফলে
❌ অনেক RAM লাগবে
❌ Start হতে সময় লাগবে
❌ Memory শেষ হয়ে যেতে পারে
Generator ব্যবহার করলে

def numbers():
    for i in range(100000000):
        yield i

এখন, একবারে মাত্র একটি Value তৈরি হবে। পরের Value, শুধু প্রয়োজন হলে তৈরি হবে। এটাকেই বলে, Lazy Evaluation Generator-এর সুবিধা - ✔ কম Memory, ✔ Faster Startup, ✔ Large File Process করা সহজ, ✔ Infinite Sequence তৈরি করা যায়।
=========================================================
03_Syntax
=========================================================
Generator Function
def numbers():
    yield 1
    yield 2
    yield 3

gen = numbers()

print(next(gen))
Output: 1
print(next(gen))
Output: 2
print(next(gen))
Output: 3
---------------------------------------------------------

Generator Expression: numbers = (x*x for x in range(5))
print(next(numbers))
Output: 0
---------------------------------------------------------

for Loop:

def numbers():
    for i in range(5):
        yield i

for value in numbers():
    print(value)

=========================================================
04_Methods
=========================================================
Generator Object-এর গুরুত্বপূর্ণ Method
---------------------------------------------------------
1. next(): পরবর্তী Value Return করে। gen = numbers(); print(next(gen))
---------------------------------------------------------
---------------------------------------------------------
2. send()
---------------------------------------------------------
Generator-এর ভিতরে Value পাঠানো যায়।

def demo():
    x = yield
    print(x)

---------------------------------------------------------
3. throw(): Generator-এর ভিতরে Exception Throw করা যায়।
---------------------------------------------------------
---------------------------------------------------------
4. close(): Generator বন্ধ করে দেয়। gen.close() এরপর আর Value Generate হবে না।
---------------------------------------------------------
=========================================================
05_TimeComplexity
=========================================================

Generator তৈরি করা - O(1)
next() - O(1) কারণ, একবারে শুধু একটি Value তৈরি হয়।
Memory Complexity - O(1) যদি Generator নিজে বড় Data Store না করে।
অন্যদিকে, List, Memory - O(n)
কারণ, সব Element Memory-তে থাকে।

=========================================================
06_InternalWorking
=========================================================
ধরো, 
def numbers():
    yield 1
    yield 2
    yield 3

gen = numbers()
Python ভিতরে কী করে?
Step 1: numbers() Call হলে, Function Execute হয় না। বরং, Generator Object তৈরি হয়। gen -> Generator Object
Step 2: next(gen) Call হয়। Function Execute শুরু হয়। yield 1 - 1 Return হয়। Function Pause হয়। State Memory-তে Save থাকে।
Step 3: আবার next(gen) - আগের জায়গা থেকে Execute শুরু হয়। yield 2 আবার Pause। শেষ পর্যন্ত StopIteration Exception Raise হয়।

=========================================================
07_Examples
=========================================================

Example 1:

def count():
    yield 1
    yield 2
    yield 3

for i in count():
    print(i)

---------------------------------------------------------

Example 2: 
def even_numbers():
    for i in range(10):
        if i % 2 == 0:
            yield i

---------------------------------------------------------

Example 3 (Infinite Generator):
import random
def data_stream():
    while True:
        yield random.randint(0,100)

gen = data_stream()

for _ in range(5):
    print(next(gen))

---------------------------------------------------------

Example 4 (Batch Generator): 

def batch_generator(data, batch_size):
    for i in range(0, len(data), batch_size):
        yield data[i:i+batch_size]

dataset = list(range(1,11))

for batch in batch_generator(dataset,3):
    print(batch)

---------------------------------------------------------
Example 5 (Generator Expression):

square = (x*x for x in range(5))

for i in square:

    print(i)

=========================================================
08_CommonMistakes
=========================================================

❌ yield-এর জায়গায় return ব্যবহার করা

Wrong

def numbers():
    return 1
    return 2

Correct:

def numbers():
    yield 1
    yield 2

---------------------------------------------------------
❌ Generator একবার শেষ হলে আবার ব্যবহার করা

gen = numbers()

for i in gen:
    ...

for i in gen:
    ...

দ্বিতীয় Loop-এ কিছুই পাওয়া যাবে না। নতুন Generator তৈরি করতে হবে।
---------------------------------------------------------
❌ next() বেশি Call করা next(gen) সব Value শেষ হয়ে গেলে StopIteration - Exception হবে।
---------------------------------------------------------
❌ Generator-কে List মনে করা, Generator Index Support করে না। gen[0] Error হবে।
=========================================================
09_Exercises
=========================================================
Exercise 1: ১ থেকে ১০ পর্যন্ত সংখ্যা Generate করো।
---------------------------------------------------------
Exercise 2: Even Number Generator তৈরি করো।
---------------------------------------------------------
Exercise 3: Odd Number Generator তৈরি করো।
---------------------------------------------------------
Exercise 4: Infinite Counter Generator তৈরি করো।
---------------------------------------------------------
Exercise 5: Fibonacci Generator তৈরি করো।
---------------------------------------------------------
Exercise 6: Large File Line-by-Line Read করার Generator লিখো।
---------------------------------------------------------
Exercise 7: Batch Generator তৈরি করো।
---------------------------------------------------------
Exercise 8: Generator Expression ব্যবহার করে Square Number তৈরি করো।
---------------------------------------------------------
Exercise 9: send() ব্যবহার করে Generator-এ Value পাঠাও।
---------------------------------------------------------
Exercise 10: নিজের Random Password Generator তৈরি করো।
=========================================================
10_AIUsage (Use Case in AI Development)
=========================================================
Generator AI এবং Machine Learning-এ অত্যন্ত গুরুত্বপূর্ণ। কারণ AI Dataset সাধারণত অনেক বড় হয়।
যেমন, 

• Image Dataset
• Video Dataset
• Audio Dataset
• Text Dataset

সব Data একসাথে RAM-এ Load করা সম্ভব নয়। তাই Generator ব্যবহার করা হয়।
Example,

def batch_generator(data, batch_size):
    for i in range(0, len(data), batch_size):
        yield data[i:i+batch_size]

Training: 
for batch in batch_generator(dataset, 32):
    train(batch)

এখানে, এক Batch Train হয়। তারপর, পরবর্তী Batch তৈরি হয়। Memory খুব কম লাগে।
---------------------------------------------------------

Infinite Data Stream:

import random

def data_stream():
    while True:
        yield random.randint(0,100)

AI Model:

gen = data_stream()
sample = next(gen)

এটি Sensor Data, IoT, Streaming Data, Real-time Prediction এর জন্য ব্যবহৃত হয়।
---------------------------------------------------------

Deep Learning Framework: TensorFlow, PyTorch, Keras সবখানেই Generator বা Data Loader ব্যবহার করা হয়।
কারণ, 

✔ Lazy Loading
✔ Streaming Dataset
✔ Mini Batch Training
✔ Memory Efficient Processing

"""