# Exercise 1: lambda দিয়ে Square Function লেখো।
def getSquare(num):
    return num ** 2
# print(getSquare(5))

square = lambda x: x*x
# print(square(5))

# -----------------------------------
# Exercise 2: map() দিয়ে [1,2,3,4] -> [10,20,30,40]
numbers = [1, 2, 3, 4]
multiply10 = map(lambda x: x*10, numbers)
# print(list(multiply10))

# -----------------------------------
# Exercise 3: filter() দিয়ে Odd Number বের করো।
numbers = [1, 2, 3, 4]
oddNumbers = filter(lambda x: x % 2 != 0, numbers)
# print(list(oddNumbers))

# -----------------------------------
# Exercise 4: reduce() দিয়ে সব সংখ্যার যোগফল বের করো।
from functools import reduce
numbers = [1, 2, 3, 4]
total = reduce(lambda x, y: x + y, numbers)
# print(total)

# -----------------------------------
# Exercise 5: zip() Name এবং Age Pair করো।
Names = ["Kader", "Jolil", "Khalek"]
Ages = [23, 54, 34]

pair = zip(Names, Ages)
# print(list(pair))
# -----------------------------------
# Exercise 6: enumerate() Index সহ Print করো।
fruits = ["Apple", "Orange", "Mango"]

# for index, fruit in enumerate(fruits):
    # print(f"Index: {index} - Fruit: {fruit}")
    
# for i in range(len(fruits)):
#     print(f"Index: {i} - Fruit: {fruits[i]}")
# -----------------------------------
# Exercise 7: Length অনুযায়ী Word Sort করো। Hint : key=len
words = ["banana", "cat", "elephant", "dog", "apple"]
sorted_words = sorted(words, key=len)
# print(sorted_words)

# -----------------------------------
# Exercise 8: Dictionary-এর List-কে Salary অনুযায়ী Sort করো।
employees = [
    {"name": "Alice", "salary": 50000},
    {"name": "Bob", "salary": 60000},
    {"name": "Charlie", "salary": 55000}
]

sorted_employees = sorted(employees, key=lambda x: x["salary"], reverse=True)
# print(sorted_employees)

# -----------------------------------
# Exercise 9: Students-দের নাম Alphabetical Order-এ Sort করো।
students = ["Zara", "Mike", "John", "Alice"]
sorted_students = sorted(students)
# print(sorted_students)

# -----------------------------------
# Exercise 10: map() + filter() একসাথে ব্যবহার করে প্রথমে Even Number বের করো, তারপর সেগুলোকে Square করো।
numbers = [1,2,3,4,5,6,7,8,9,10]

even_numbers = list(filter(
    lambda x: x % 2 == 0,
    numbers
)) # Making it a list to print. bypassing Lazy Evaluation.

print(list(even_numbers))

square_numbers = map(
    lambda x: x*x,
    even_numbers
)

print(list(square_numbers))

# যদি filter() সঙ্গে সঙ্গে একটি নতুন List বানাতো, 100,000,000 items, তাহলে প্রচুর RAM লাগত। তাই Python বলে— "আমি List বানাব না। যখন দরকার হবে, তখন একটার পর একটা Element দেব।" এটিই Lazy Evaluation।

numbers = [1,2,3,4,5,6,7,8,9,10]
transNumbers = list(map(
    lambda x : x * x,
    filter(
        lambda x : x % 2 == 0,
        numbers
    )
))

print(transNumbers)