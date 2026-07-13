# Exercise 1: Logger Decorator তৈরি করো।

# import logging

# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s | %(levelname)s | %(message)s"
# )

# def logger(func: any):
#     def wrapper(*args, **kwargs) -> any:
#         logging.info(f"Calling function: {func.__name__}")
#         return func(*args, **kwargs)
#     return wrapper

# @logger
# def greet(name: str):
#     print(f"Hello, {name}!")

# greet("Mozammel")

# --------------------------------------------------
# Exercise 2: Timer Decorator তৈরি করো।
# import time

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
        
#         result = func(*args, **kwargs)
        
#         end = time.perf_counter()
        
#         print(f"{func.__name__} took {end - start:.6f} seconds")
        
#         return result
    
#     return wrapper

# @timer
# def slow_task():
#     time.sleep(2)
#     print("Task completed.")
    
# slow_task() 

# --------------------------------------------------
# Exercise 3: Authentication Decorator তৈরি করো। User Login না থাকলে Permission Denied Print করবে।
# users = {
#     "Mozammel" : "1234",
#     "Karim": "abcd",
#     "Rahim": "pass123"
# }

# def authentication(func: any):
#     def wrapper(username, password):
#         if username not in users:
#             print("User not found!")
#             return
        
#         if users[username] != password:
#             print("Ïnvalid password!")
#             return
#         print("Authentication Successfull!")
        
#         return func(username, password)
#     return wrapper            
            
# @authentication
# def login(username: str, password: str) -> None:
#     print(f"Welcome, {username}")

# login("Mozammel", "1234")
# login("Karim", "abcd")
# --------------------------------------------------
# Exercise 4: Retry Decorator তৈরি করো। Function Fail করলে ৩ বার Retry করবে।
# from functools import wraps

# def retry(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         max_retries = 3

#         for attempt in range(1, max_retries + 1):
#             try:
#                 return func(*args, **kwargs)
#             except Exception as e:
#                 print(f"Attempt {attempt} failed: {e}")

#                 if attempt == max_retries:
#                     print("All retry attempts failed.")

#     return wrapper


# @retry
# def divide(a: float, b: float) -> float:
#     return a / b


# print(divide(10, 0))


# --------------------------------------------------
# Exercise 5: Decorator তৈরি করো যা Function Call Count করবে। Output: Called 1 Times, Called 2 Times, Called 3 Times
def call_counter(func):
    count = 1
    
    def wrapper(*args, **kwargs):
        nonlocal count
        print(f"{func.__name__} function Calling {count}")
        count += 1
        return func(*args, **kwargs)
    return wrapper

@call_counter
def greet():
    print("Hello!")
    
greet()
greet()