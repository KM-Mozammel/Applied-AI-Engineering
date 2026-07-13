# Exercise 1: PEP 8 অনুসারে একটি Function লিখো।
# PEP - Python Enhance Proposal-8

# def calculate_square(number: int) -> int:
#     """Return the square of a number."""
#     return number * number

# result = calculate_square(8)
# print(result)


# --------------------------------------------------
# Exercise 2: EAFP Style-এ Dictionary Access করো।
# EAFP - Easier to Ask Forgiveness than Permission 
# student = {
#     "name": "Alice",
#     "age" : 20,
#     "department": "CSE"
# }

# try:
#     print(student["name"])
#     print(student["age"])
#     print(student["email"])
# except KeyError as error:
#     print(f"Key not found: {error}")

# --------------------------------------------------
# Exercise 3: LBYL Style-এ একই Problem Solve করো।
# LBYL-Look Before You Leap
student = {
    "name": "Alice",
    "age": 20,
    "department": "CSE"
}

if "name" in student:
    print(student["name"])
    
if "age" in student:
    print(student["age"])
if "email" in student:
    print(student["email"])
else:
    print("Key not found: email")

# --------------------------------------------------
# Exercise 4: Bad Code Pythonic Code-এ Convert করো।
# Bad
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

result = []

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        result.append(numbers[i])

print(result)

# Good
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = [number for number in numbers if number % 2 == 0]
print(result)


# Bad
student = {
    "name": "Alice",
    "age": 20
}

if "name" in student:
    print(student["name"])
    
# Good
try:
    print(student["name"])
except KeyError:
    print("Key not found")
    
    
# Bad
words = ["Python", "is", "awesome"]

sentence = ""

for word in words:
    sentence += word + " "
print(sentence)


# Good
words = ["Python", "is", "awesome"]
sentence = "".join(words)
print(sentence)


# Bad
a = 10
b = 10

temp = a
a = b
b = temp

print(a, b)

# Good
a = 10
b = 10
a, b = b, a #Tuple Assignment
print(a, b)

# Bad
names = ["Alice", "Bob", "Charlie"]

for i in range(len(names)):
    print(i, names[i])
    
# Good
names = ["Alice", "Bob", "Charlie"]

for index, name in enumerate(names):
    print(index, name)
# --------------------------------------------------
# Exercise 5: নিজের লেখা পুরোনো Code PEP 8 অনুযায়ী Refactor করো।
# Old
import random,string

def generatePass(length=10):
    chars=string.ascii_letters+string.digits+string.punctuation
    password=""
    for i in range(length):
        password+=random.choice(chars)
    return password

print(generatePass())

# New: Python Enhance Protocol - 8
import random, string

def generate_pass(length: int = 10) -> str:
    """Generate a random password."""
    characters = (
        string.ascii_letters + string.digits + string.punctuation
    )
    
    password = "".join(random.choice(characters) for _ in range(length))
    return password