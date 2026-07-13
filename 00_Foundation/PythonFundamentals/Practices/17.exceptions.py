# Exercise 1: Division Function তৈরি করো। ZeroDivision Handle করবে।
# def Division(a: int, b: int) -> float | str:
#     try:
#         return a/b
#     except ZeroDivisionError:
#         return "Cannot Divide by zero"
    
# print(Division(4, 8))
# print(Division(4, 0))

# --------------------------------------------------
# Exercise 2: File Open করো। File না থাকলে Message দেখাও।
# def openfile(fileName: str):
#     try:
#         with open(fileName, "r") as file:
#             a = file.read()
#             return a
#     except FileNotFoundError:
#         return "File Not Found."
    
# print(openfile("serve.log"))
# --------------------------------------------------
# Exercise 3: Negative Number দিলে raise ValueError করো।
# def calculator(a: int, b: int):
#     if a < 0 or b < 0:
#         raise ValueError("Numbers can't be negative")
#     return a + b

# print(calculator(3, 5))
# print(calculator(3, -5))

# --------------------------------------------------
# Exercise 4: API Simulation Timeout Exception Handle করো।
# import requests
# import time

# def fetchData(url: str) -> any:
#     start = time.perf_counter()
#     try:
#         response = requests.get(url, timeout=3)
#         response.raise_for_status()
#         return response.json()
#     except requests.exceptions.Timeout:
#         print("Timeout")
#         return {"Status": "backup"}
#     except requests.exceptions.RequestException as ex:
#         print(ex)
#         return None
#     finally:
#         stop = time.perf_counter()
#         print(f"Taken Time: {stop - start:.4f} seconds")
        
    
# print(fetchData("https://jsonplaceholder.typicode.com/posts/1"))
        
# --------------------------------------------------
# Exercise 5: Custom Exception Class তৈরি করো।

class InvalidAgeErro(Exception):
    pass

def register_user(age: int):
    if age < 18:
        raise InvalidAgeErro("Age must be at least 18.")
    return "Registration Successful"

try:
    print(register_user(25))
    print(register_user(15))
except InvalidAgeErro as ex:
    print(ex)