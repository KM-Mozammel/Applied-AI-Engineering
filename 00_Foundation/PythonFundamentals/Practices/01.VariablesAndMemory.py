# Exercise 1: x=[10,20], y=x | id(x), id(y) কি Output হবে?
x = [10, 20] 
y = x 
print(id(x))
print(id(y))
print("Ending Exercise 1\n")

# Exercise 2: x=[1,2], y=x.copy(), x.append(100) Print করলে কী হবে?
x = [1, 2]
y = x.copy()
x.append(100)
print(x)
print(y)
print("Ending Exercise 2\n")


# Exercise 3: Nested List নিয়ে copy() এবং deepcopy() এর পার্থক্য বের করুন।
nestedList = [[1, 2], [3, 4], [5, 6]]
copiedList = nestedList.copy()
copiedList[0][0] = 100  # Modifying the first element of the first sublist
import copy
deepCopiedList = copy.deepcopy(nestedList)
deepCopiedList[0][0] = 500

print("Nested List:", nestedList)
print("Copied List:", copiedList)
print("Deep Copied List:", deepCopiedList)
print("Ending Exercise 3\n")

# Exercise 4: নিজে ১০টি Variable তৈরি করে, id() Compare করুন।
x1 = 5
x2 = 5
x3 = [1, 2, 3]
x4 = [1, 2, 3]
x5 = (1, 2, 3)
x6 = (1, 2, 3)
x7 = "hello"
x8 = "hello"
x9 = 10.5
x10 = 10.5

print("Exercise 4:")
print(f"id(x1): {id(x1)}")
print(f"id(x2): {id(x2)}")
print(f"id(x3): {id(x3)}")
print(f"id(x4): {id(x4)}")
print(f"id(x5): {id(x5)}")
print(f"id(x6): {id(x6)}")
print(f"id(x7): {id(x7)}")
print(f"id(x8): {id(x8)}")
print(f"id(x9): {id(x9)}")
print(f"id(x10): {id(x10)}")
print("Ending Exercise 4\n")

# Exercise 5: is এবং == এর পার্থক্য নিজের ভাষায় লিখুন।
# is: Checks if two variables refer to the same object in memory.
# ==: Checks if two variables have the same value.