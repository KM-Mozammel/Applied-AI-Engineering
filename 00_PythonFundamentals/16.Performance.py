"""
==================================================
01_Introduction
==================================================
Performance Optimization হলো এমন একটি Process যার মাধ্যমে Program-কে ✔ Faster, ✔ Memory Efficient, ✔ CPU Efficient করা হয়। 
Python-এ Performance Measure করার জন্য সবচেয়ে গুরুত্বপূর্ণ Tools: ✔ timeit, ✔ cProfile, ✔ Memory Profiling, ✔ Vectorization (NumPy)
--------------------------------------------------
Real Life Example: ধরো, দুটি Route আছে। Road A - ২০ মিনিট, Road B - ৫ মিনিট; দুটোই Destination-এ পৌঁছায়। কিন্তু Road B Performance ভালো। Programming-এও একই বিষয়।

==================================================
02_WhyPerformanceOptimizationExists
==================================================
ধরো, একটি AI Model ১০ লাখ Data Process করবে। Slow Code - 30 Seconds; Fast Code - 2 Seconds
--------------------------------------------------
যদি একদিনে 1000 বার Run হয় তাহলে অনেক সময় Save হবে।
--------------------------------------------------
Performance গুরুত্বপূর্ণ, ✔ AI, ✔ Backend, ✔ Data Engineering, ✔ Scientific Computing, ✔ High Frequency Systems

==================================================
03_Syntax
==================================================
timeit:

import timeit
print(timeit.timeit("sum(range(100))", number=1000))
--------------------------------------------------
cProfile:

import cProfile
cProfile.run("main()")
--------------------------------------------------

Memory:

from memory_profiler import profile

@profile
def process():
    ...
--------------------------------------------------
Vectorization:

import numpy as np

arr=np.arange(1000000)
arr=arr*2

==================================================
04_Methods
==================================================
timeit: Execution Time Measure করে।
--------------------------------------------------
cProfile: Function অনুযায়ী, Execution Time দেখায়।
--------------------------------------------------
memory_profiler: RAM Usage Measure করে।
--------------------------------------------------
Vectorization: Loop বাদ দিয়ে C-Level Operation ব্যবহার করে।

==================================================
05_TimeComplexity
==================================================
Performance Tool: Algorithm পরিবর্তন করে না। Measurement করে।
--------------------------------------------------
Vectorization: Loop - O(n) -> Vectorized - O(n) ই থাকে কিন্তু Constant Factor অনেক কমে যায়।

==================================================
06_InternalWorking
==================================================
Example: timeit.timeit(...)
--------------------------------------------------
Step 1: Python Code অনেকবার Execute করে।
Step 2: High Resolution Timer Start
Step 3: Code Execute
Step 4: Timer Stop -> Average Time Return
--------------------------------------------------
cProfile: Program -> Every Function Call -> Execution Time -> Call Count -> Report
--------------------------------------------------
Vectorization: Python Loop -> Interpreter -> One By One
--------------------------------------------------
NumPy: C Library -> SIMD -> Optimized CPU Instructions

==================================================
07_Examples
==================================================
Example 1: timeit

import timeit

result=timeit.timeit(
    "sum(range(1000))",
    number=10000
)
print(result)
--------------------------------------------------
Example 2: cProfile

import cProfile

def calculate():
    total=0
    for i in range(100000):
        total+=i
cProfile.run("calculate()")
--------------------------------------------------
Example 3: Memory Profiling

from memory_profiler import profile

@profile
def create():
    data=[i for i in range(100000)]
    return data
create()
--------------------------------------------------
Example 4: Loop

numbers=[1,2,3,4]
result=[]
for n in numbers:
    result.append(n*2)
--------------------------------------------------

Example 5: Vectorization

import numpy as np

numbers=np.array([1,2,3,4])
result=numbers*2
print(result)

==================================================
08_CommonMistakes
==================================================
❌ Mistake 1: Performance আন্দাজ করা। ✔timeit ব্যবহার করো।
--------------------------------------------------
❌ Mistake 2: Loop দিয়ে Large Array Process করা। ✔ NumPy Vectorization ব্যবহার করো।
--------------------------------------------------
❌ Mistake 3: Optimization করার আগে Profile না করা। ✔ প্রথমে cProfile তারপর Optimization।
--------------------------------------------------
❌ Mistake 4: অপ্রয়োজনীয় Object তৈরি করা। Loop-এর ভিতরে বারবার List তৈরি করলে Memory Waste হয়।

==================================================
09_Exercises
==================================================
Exercise 1: Loop এবং List Comprehension timeit দিয়ে Compare করো।
--------------------------------------------------
Exercise 2: একটি Function cProfile দিয়ে Analyze করো।
--------------------------------------------------
Exercise 3: Memory Profile করো। একটি বড় List তৈরি করে।
--------------------------------------------------
Exercise 4: Loop দিয়ে Square বের করো। তারপর NumPy দিয়ে একই কাজ করো।
--------------------------------------------------
Exercise 5: ১ মিলিয়ন সংখ্যার উপর Loop vs Vectorization Compare করো।

==================================================
10_AIUsage (Use Case in AI Development)
==================================================
Performance Optimization AI Engineering-এর সবচেয়ে গুরুত্বপূর্ণ Skill-গুলোর একটি।
--------------------------------------------------
১। Model Training: Training Slow হলে Profile করে Bottleneck খুঁজে বের করা হয়।
--------------------------------------------------
২। Data Preprocessing: Normalization, Encoding, Scaling, Vectorization দিয়ে Faster করা হয়।
--------------------------------------------------
৩। Inference Optimization: Prediction Time Measure করা হয়।
--------------------------------------------------
৪। Large Dataset: ১০ কোটি Row Loop দিয়ে নয় NumPy, Pandas ব্যবহার করা হয়।
--------------------------------------------------
৫। Memory Optimization: Dataset RAM-এ Fit না করলে Memory Profile করা হয়।
--------------------------------------------------
৬। GPU Pipeline: CPU Bottleneck -> Detect -> Optimize
--------------------------------------------------
৭। LLM Inference: Token Generation Time, Latency, Memory Usage সব Measure করা হয়।
--------------------------------------------------
Summary: 
timeit -> Execution Time Measure
cProfile -> Function Bottleneck খুঁজে
memory_profiler -> RAM Usage Measure
Vectorization -> Loop বাদ দিয়ে Optimized C-Level Execution

Professional AI, Machine Learning, Deep Learning, Data Engineering, Scientific Computing এবং High Performance Python Programming-এ Performance Profiling একটি অপরিহার্য Skill।
"""