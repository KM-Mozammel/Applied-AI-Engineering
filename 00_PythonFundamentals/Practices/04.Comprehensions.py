# # Normal Loop:
# result = []
# for i in range(5):
#     result.append(i)
    
# print(result, "\n")

# # List Comprehension
# result = [i for i in range(5)]
# print(result)

# Expression for variable in iterable
numbers = [i for i in range(5)]

# square
square = [i * i for i in range(5)]
# print(square)

# add condition: if - even number
even = [i for i in range(10) if i % 2 == 0]
# print(even)

# add condition: if else
labels = ["Even" if i % 2 == 0 else "Odd" for i in range(5)]
# print(labels)

# Nested Loops:
pairs = [
    (i, j) 
    for i in range(3) 
    for j in range(2)
]
# print(pairs)


# Dictionary Comprehensions:
dictionary = {i: i * i for i in range(5)}
# print(dictionary)

dictionary = {i: i * i for i in range(10) if i % 2 == 0}
# print(dictionary)

# Set Comprehension:
myset = {i % 3 for i in range(10)}
# print(myset)


# Exercise 1: ১-২০ পর্যন্ত Square বের করো।
square = [i * i for i in range(1, 21)]
# print(square)

# Expected: [1,4,9,...]
# ------------------------------------------------------------
# Exercise 2: শুধু Even Number বের করো।
evenNumber = [i for i in range(1, 21) if i % 2 == 0]
# print(evenNumber)

# ------------------------------------------------------------
# Exercise 3: ১০ জন Student-এর নাম Uppercase করো।
students = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ivy", "Jack"]
upperStundents = [student.upper() for student in students]
# print(upperStundents)

# ------------------------------------------------------------
# Exercise 4:  Dictionary বানাও
# {
#  1:1,
#  2:4,
#  3:9,
#  ...
# }
dictionary = {i: i * i for i in range(1, 21)}
# print(dictionary)
# ------------------------------------------------------------
# Exercise 5: Set তৈরি করো Number % 4
setMaker = {i % 4 for i in range(1, 21)}
# print(setMaker)

# ------------------------------------------------------------
# Exercise 6: Nested List Flatten করো।
nestedList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flattenedList = []
for sublist in nestedList:
    for item in sublist:
        flattenedList.append(item)

flattenedList = [item for sublist in nestedList for item in sublist]
# print(flattenedList)
# ------------------------------------------------------------
# Exercise 7: Generator দিয়ে ১-১০০ পর্যন্ত Number Generate করো।
generated = (i for i in range(1, 101))
number = list(generated)
# print(number)
# ------------------------------------------------------------
# Exercise 8: এই Dataset তৈরি করো। [(x,x**2) for x in range(20)]
dataset = [(x, x ** 2) for x in range(20)]
# print(dataset)
# ------------------------------------------------------------
# Exercise 9: Matrix-এর সব Element Double করো।
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# doubledMatrix = [[i * 2 for i in row] for row in matrix]
doubledMatrix = [[i * 2 for i in row] for row in matrix]
# print(doubledMatrix)
# ------------------------------------------------------------
# Exercise 10: নিজের Name-এর প্রতিটি Character-এর ASCII Value বের করো। Hint: ord()
name = "Mozammel"  # Replace with your actual name
ascii_values = [ord(char) for char in name]
print(ascii_values)