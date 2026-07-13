# Exercise 1: Loop এবং List Comprehension timeit দিয়ে Compare করো।
import timeit

# def using_loop():
#     result = []
    
#     for i in range(100000):
#         result.append(i * i)
#     return result

# def using_comprehension():
#     return [i * i for i in range(100000)]

# loop_time = timeit.timeit(using_loop, number = 100)
# comprehension_time = timeit.timeit(using_comprehension, number=100)

# print(f"For Loop Time: {loop_time:.6f} seconds")
# print(f"List Comprehension: {comprehension_time:.6f} seconds")

# if loop_time > comprehension_time:
#     print("List Comprehension is Faster")
# else:
#     print("For Loop is faster")

# --------------------------------------------------
# Exercise 2: একটি Function cProfile দিয়ে Analyze করো।
import cProfile
import random 

# def square(x):
#     return x * x

# def calculate():
#     total = 0
#     for i in range(1_000_000):
#         total += square(i)
#     return total

# cProfile.run("calculate()")

# def sort_numbers():
#     numbers = [random.randint(1, 1_000_000) for _ in range(100000)]
#     numbers.sort()
    
# cProfile.run("sort_numbers()")

# --------------------------------------------------
# Exercise 3: Memory Profile করো। একটি বড় List তৈরি করে।
# import tracemalloc

# tracemalloc.start()

# numbers = [i for i in range(1_000_000)]

# current, peak = tracemalloc.get_traced_memory()

# print(f"Current Memory: {current / 1024 / 1024:.2f} MB")
# print(f"Peak Memory: {peak / 1024 / 1024:.2f} MB")

# tracemalloc.stop()


# --------------------------------------------------
# Exercise 4: Loop দিয়ে Square বের করো। তারপর NumPy দিয়ে একই কাজ করো।
# import numpy as np
# import timeit

# def squareLoop():
#     result = []

#     for i in range(1_000_000):
#         result.append(i * i)

#     return result


# def numpySquare():
#     arr = np.arange(1_000_000)
#     return np.square(arr)


# loop_time = timeit.timeit(squareLoop, number=10)
# numpy_time = timeit.timeit(numpySquare, number=10)

# print(f"Loop Time  : {loop_time:.4f} sec")
# print(f"NumPy Time : {numpy_time:.4f} sec")

# --------------------------------------------------
# Exercise 5: ১ মিলিয়ন সংখ্যার উপর Loop vs Vectorization Compare করো।

import timeit
import numpy as np

# Python Loop
def square_loop():
    result = []

    for i in range(1_000_000):
        result.append(i * i)

    return result


# NumPy Vectorization
def square_numpy():
    arr = np.arange(1_000_000)
    return arr * arr
    # অথবা:
    # return np.square(arr)


# Measure execution time
loop_time = timeit.timeit(square_loop, number=10)
numpy_time = timeit.timeit(square_numpy, number=10)

print(f"Loop Time       : {loop_time:.4f} seconds")
print(f"NumPy Time      : {numpy_time:.4f} seconds")
print(f"Speedup         : {loop_time / numpy_time:.2f}x")