"""
==================================================
dataclass.py (বাংলা)
==================================================

Topic: dataclasses

Python Version: 3.7+

==================================================
# 01_Introduction
==================================================

dataclass হলো Python-এর একটি Decorator যা Class-এর জন্য
অনেক Boilerplate Code (একই ধরনের বারবার লিখতে হয় এমন কোড)
স্বয়ংক্রিয়ভাবে তৈরি করে দেয়।

এটি Python 3.7 থেকে Standard Library-তে যোগ হয়েছে।

Import করতে হয়—

    from dataclasses import dataclass

ধরো একটি Student Class বানাতে হবে।

সাধারণভাবে লিখতে গেলে—

- __init__()
- __repr__()
- __eq__()

এসব নিজে লিখতে হয়।

কিন্তু @dataclass ব্যবহার করলে Python এগুলো
নিজেই তৈরি করে দেয়।

Example:

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int

student = Student("Rahim", 22)

print(student)

Output

Student(name='Rahim', age=22)

দেখো,
আমরা __init__ লিখিনি,
তারপরও Object তৈরি হয়েছে।

==================================================
# 02_WhyDataclassExists
==================================================

dataclass তৈরি করার মূল কারণ হলো—

Python-এ অনেক Class শুধুমাত্র Data ধরে রাখে।

যেমন—

User
Student
Employee
Book
Address
Product
Order

এসব Class-এর কাজ শুধু Data Store করা।

আগে এমন Class লিখতে হত—

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        ...

    def __eq__(self):
        ...

এভাবে অনেক Boilerplate Code লিখতে হত।

এখন—

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int

এতেই সব হয়ে যায়।

Benefits

✅ কম Code

✅ Readable

✅ Maintainable

✅ Less Bugs

✅ Automatic Methods

==================================================
# 03_Syntax
==================================================

Basic Syntax

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

Object

person = Person("Hasan", 24)

----------------------------------

Default Value

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int = 18

student = Student("Rahim")

print(student)

Output

Student(name='Rahim', age=18)

----------------------------------

Multiple Fields

@dataclass
class Book:

    title: str
    author: str
    price: float
    stock: int

----------------------------------

Type Hint ব্যবহার করা উচিত

@dataclass
class Employee:

    id: int
    salary: float
    active: bool

==================================================
# 04_Methods
==================================================

dataclass নিজে খুব বেশি Method দেয় না।

বরং এটি Automatic Special Methods Generate করে।

--------------------------------------------------
1. __init__()
--------------------------------------------------

Automatic Constructor

@dataclass
class Student:

    name: str
    age: int

student = Student("Karim", 25)

--------------------------------------------------
2. __repr__()
--------------------------------------------------

Readable Representation

print(student)

Output

Student(name='Karim', age=25)

--------------------------------------------------
3. __eq__()
--------------------------------------------------

Object Compare

s1 = Student("A", 20)
s2 = Student("A", 20)

print(s1 == s2)

True

--------------------------------------------------
4. field()
--------------------------------------------------

Custom Field

from dataclasses import field

@dataclass
class Student:

    name: str
    marks: list = field(default_factory=list)

এটি Mutable Default Problem সমাধান করে।

--------------------------------------------------
5. asdict()
--------------------------------------------------

Object → Dictionary

from dataclasses import asdict

student = Student("Rahim", 22)

print(asdict(student))

Output

{
    "name": "Rahim",
    "age":22
}

--------------------------------------------------
6. astuple()
--------------------------------------------------

Object → Tuple

from dataclasses import astuple

print(astuple(student))

Output

("Rahim",22)

--------------------------------------------------
7. replace()
--------------------------------------------------

Copy Object with Changes

from dataclasses import replace

new_student = replace(student, age=30)

==================================================
# 05_TimeComplexity
==================================================

Object Creation

O(1)

----------------------------------

Field Access

O(1)

----------------------------------

Comparison (__eq__)

O(n)

n = Number of Fields

----------------------------------

asdict()

O(n)

----------------------------------

astuple()

O(n)

----------------------------------

replace()

O(n)

==================================================
# 06_InternalWorking
==================================================

ধরো তুমি লিখলে—

from dataclasses import dataclass

@dataclass
class Student:

    name: str
    age: int

Python আসলে এটিকে Transform করে প্রায় এমন বানায়—

class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def __repr__(self):

        return f"Student(name={self.name}, age={self.age})"

    def __eq__(self, other):

        return (
            self.name == other.name
            and
            self.age == other.age
        )

অর্থাৎ

Decorator Class-টিকে Modify করে।

এটি Compile Time-এ না,
Runtime-এ ঘটে।

==================================================
# 07_Examples
==================================================

Example 1

from dataclasses import dataclass

@dataclass
class User:

    username: str
    email: str

user = User("mozammel", "abc@gmail.com")

print(user)

----------------------------------

Example 2

@dataclass
class Product:

    name: str
    price: float

p1 = Product("Keyboard", 2500)
p2 = Product("Keyboard", 2500)

print(p1 == p2)

True

----------------------------------

Example 3

from dataclasses import asdict

@dataclass
class Car:

    brand: str
    model: str

car = Car("Toyota", "Corolla")

print(asdict(car))

----------------------------------

Example 4

from dataclasses import field

@dataclass
class Team:

    members: list = field(default_factory=list)

team1 = Team()
team2 = Team()

team1.members.append("Rahim")

print(team1.members)

['Rahim']

print(team2.members)

[]

==================================================
# 08_CommonMistakes
==================================================

১।

Mutable Default Value

Wrong

@dataclass
class Team:

    members: list = []

কারণ
সব Object একই List Share করবে।

Correct

from dataclasses import field

members = field(default_factory=list)

----------------------------------

২।

Decorator দিতে ভুলে যাওয়া

Wrong

class Student:

    name: str
    age: int

Student("A",20)

Error

Correct

@dataclass

----------------------------------

৩।

Type Hint না দেওয়া

Wrong

@dataclass
class Student:

    name
    age

Correct

name: str
age: int

----------------------------------

৪।

Business Logic বেশি রাখা

dataclass মূলত Data Container।

Complex Business Logic-এর জন্য
Normal Class ভালো।

==================================================
# 09_Exercises
==================================================

Exercise 1

Student Dataclass বানাও।

Fields

name
age
cgpa

----------------------------------

Exercise 2

Employee Dataclass বানাও।

Compare করো।

----------------------------------

Exercise 3

Book Dataclass তৈরি করে
asdict() ব্যবহার করো।

----------------------------------

Exercise 4

Library Dataclass বানাও।

Books-এর জন্য

field(default_factory=list)

ব্যবহার করো।

----------------------------------

Exercise 5

replace() ব্যবহার করে

একজন Student-এর Age Update করো।

==================================================
# 10_AIUsage (Use Case in AI Development)
==================================================

AI Project-এ dataclass অনেক জনপ্রিয়।

কারণ AI Pipeline-এ প্রচুর Configuration,
Model Parameter এবং Metadata Store করতে হয়।

উদাহরণ:

from dataclasses import dataclass

@dataclass
class TrainingConfig:

    learning_rate: float
    batch_size: int
    epochs: int
    optimizer: str

config = TrainingConfig(
    learning_rate=0.001,
    batch_size=32,
    epochs=100,
    optimizer="Adam"
)

এর সুবিধা—

✅ Model Configuration পরিষ্কার থাকে

✅ Type Hint পাওয়া যায়

✅ Debug করা সহজ হয়

✅ Configuration Copy করা সহজ (replace())

✅ Dictionary-তে রূপান্তর করা সহজ (asdict())

বাস্তব AI Framework-এ যেমন—

- PyTorch Project
- TensorFlow Project
- Hugging Face Transformers
- Stable Diffusion
- LangChain
- LlamaIndex

এসব জায়গায় Configuration Object, Dataset Metadata,
Training Parameters এবং Model Settings সংরক্ষণে
dataclass ব্যাপকভাবে ব্যবহৃত হয়।

==================================================
শেষ কথা
==================================================

dataclass হলো "Data-কেন্দ্রিক Class" লেখার সবচেয়ে সহজ ও
পরিষ্কার উপায়।

যদি Class-এর প্রধান কাজ হয় Data রাখা, তাহলে dataclass
ব্যবহার করা সবচেয়ে ভালো।

মনে রাখার জন্য:

✔ কম কোড
✔ Automatic __init__()
✔ Automatic __repr__()
✔ Automatic __eq__()
✔ Type Hint Support
✔ Mutable Field-এর জন্য field(default_factory=...)
✔ AI এবং Backend Development-এ ব্যাপক ব্যবহার
"""