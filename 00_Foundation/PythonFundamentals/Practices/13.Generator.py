# Exercise 1: ১ থেকে ১০ পর্যন্ত সংখ্যা Generate করো।

# def numbers():
#     for i in range(1, 11 ):
#         yield i
        
# gen = numbers()

# for number in gen:
#     print(number)

# ---------------------------------------------------------
# Exercise 2: Even Number Generator তৈরি করো।
# def evenNumbers():
#     for i in range(1, 100):
#         if(i % 2 == 0):
#             yield i
            
# genEven = evenNumbers()

# for even in genEven:
#     print(even)


# ---------------------------------------------------------
# Exercise 3: Odd Number Generator তৈরি করো।
# def genOdd():
#     for i in range(1, 100, 2):
#         yield i

# gen = genOdd()

# for i in gen:
#     print(i)

# ---------------------------------------------------------
# Exercise 4: Infinite Counter Generator তৈরি করো।

# def infinite_counter():
#     n = 0
#     while True:
#         yield n
#         n += 1
        
# counter = infinite_counter()

# for i in counter:
#     print(i)


# ---------------------------------------------------------
# Exercise 5: Fibonacci Generator তৈরি করো।
# def genFibo():
#     a = 0;
#     b = 1;
    
#     while True:
#         yield a
#         a, b = b, a + b
        
# gen = genFibo()

# for _ in range(10):
#     print(next(gen))

# ---------------------------------------------------------
# Exercise 6: Large File Line-by-Line Read করার Generator লিখো। 
# def readLine(filename: str) -> iter[str]:
#     with open(filename, "r") as file:
#         for line in file:
#             yield line
            
# read = readLine("server.log")

# for line in read:
#     if "ERROR" in line:
#         print(line.strip())

# ---------------------------------------------------------
# Exercise 7: Batch Generator তৈরি করো।

# def batch_generator(data, batch_size):
#     batch = []

#     for item in data:
#         batch.append(item)

#         if len(batch) == batch_size:
#             yield batch
#             batch = []

#     # শুধু loop শেষ হওয়ার পর
#     if batch:
#         yield batch


# numbers = range(1, 11)

# for batch in batch_generator(numbers, 3):
#     print(batch)
# Data Insertion-------------
# users = [
#     {"name": "Alice"},
#     {"name": "Bob"},
#     {"name": "Charlie"},
#     {"name": "David"},
#     {"name": "Eva"},
#     {"name": "Frank"},
#     {"name": "Grace"},
# ]

# def batchGenerator(data, batch_size):
#     batch = []
    
#     for item in data:
#         batch.append(item)
        
#         if len(batch) == batch_size:
#             yield batch
#             batch = []
            
#     if batch:
#         yield batch
        
# def insert_many(users):
#     print(f"Inserting {len(users)} users...")
#     print(users)

# for batch in batchGenerator(users, 3):
#     insert_many(batch)

# Read Log file in batch
# from typing import Iterator

# def batchGenerator(file, batch_size):
#     batch = []
#     for line in file:
#         batch.append(line)
        
#         if len(batch) == batch_size:
#             yield batch
#             batch = []
#     if batch:
#         yield batch            

# def read_log(filename: str) -> Iterator[str]:
#     with open(filename, "r") as file:
#         for line in file:
#             yield line
            
# logs = read_log("server.log")

# for line in batchGenerator(logs, 3):
#     print(line)

# ---------------------------------------------------------
# Exercise 8: Generator Expression ব্যবহার করে Square Number তৈরি করো।
# squares = [x * x for x in range(1, 11)]

# for square in squares:
#     print(square)

# ---------------------------------------------------------
# Exercise 9: send() ব্যবহার করে Generator-এ Value পাঠাও।
# def calculator():
#     while True:
#         number = yield
#         print(f"Square = {number ** 2}")
        
# gen = calculator()
# next(gen)

# def main():
#     while True:
#         value = input("Enter a number to square: ")
#         if value.lower() == "exit":
#             break    
#         gen.send(int(value))
# main()

# ---------------------------------------------------------
# Exercise 10: নিজের Random Password Generator তৈরি করো।
# import random
# import string
# from collections.abc import Iterator

# def generatePass(length: int = 10) -> Iterator[str]:
#     chars = string.ascii_letters + string.digits + string.punctuation
    
#     while True:
#         password = "".join(random.choice(chars) for _ in range(length))
#         yield password
        
# gen = generatePass()

# for _ in range(5):
#     print(next(gen))