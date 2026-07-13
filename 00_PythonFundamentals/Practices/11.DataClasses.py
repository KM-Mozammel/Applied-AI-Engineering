# Exercise 1: Student Dataclass বানাও। Fields: name, age, cgpa
from dataclasses import dataclass, asdict
@dataclass
class Student:
    name: str
    age: int
    cgpa: float
    
student1: Student = Student("Rahim", 34, 3.45)
# print(student1)

# ----------------------------------
# Exercise 2: Employee Dataclass বানাও। Compare করো।
@dataclass
class Employee:
    Name: str
    Department: str
    Salary: float

employee1 = Employee("Kader", "IT", 4500)
employee2 = Employee("Leo", "IT", 4500)


# print(employee1 == employee2)

# ----------------------------------
# Exercise 3: Book Dataclass তৈরি করে, asdict() ব্যবহার করো।
@dataclass
class Book:
    Name: str
    Category: str
    Price: float
    
book1 = Book("Python Basics", "Programming", 550.0)

bookdict = asdict(book1)

# print(book1)
# print(bookdict)

# ----------------------------------
# Exercise 4: Library Dataclass বানাও। Books-এর জন্য field(default_factory=list) ব্যবহার করো।
from typing import List
from dataclasses import field

@dataclass
class Library:
    Books: List[Book] = field(default_factory = list)
    
book2 = Book("AI Essentials", "Machine Learning", 750.0)

library = Library()
library.Books.append(book1)
library.Books.append(book2)

print(library)
print(asdict(library))

# ----------------------------------
# Exercise 5: replace() ব্যবহার করে, একজন Student-এর Age Update করো।
from dataclasses import dataclass, replace

@dataclass
class Student:
    name: str
    age: int
    cgpa: float
    
student1 = Student("Rahim", 21, 3.75)

student2 = replace(student1, age = 22)

print(student1)
print(student2)