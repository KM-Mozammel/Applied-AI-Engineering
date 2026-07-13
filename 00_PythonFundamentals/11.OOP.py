"""
=========================================================
01_Introduction
=========================================================
OOP (Object-Oriented Programming) হলো এমন একটি Programming Paradigm যেখানে আমরা Real World Object-কে Programming এর মাধ্যমে Model করি। যেমন বাস্তব জীবনে— মানুষ, গাড়ি, মোবাইল, ব্যাংক একাউন্ট, কুকুর, ছাত্র এসবের Properties (Data) এবং Behaviors (Functions) থাকে। Programming-এ এগুলোকে Object হিসেবে তৈরি করা হয়। Example, একটি Car- 
Properties:- Brand, Color, Speed
Behaviors:- Start(), Stop(), Brake(), Accelerate()
Python-এ এগুলো Class দিয়ে তৈরি করা হয়। Object হলো Class-এর Instance।

=========================================================
02_WhyOOPExists
=========================================================
OOP আসার আগে Procedural Programming বেশি ব্যবহৃত হতো। Example, student_name - student_age - student_marks - teacher_name- teacher_salary - employee_name - employee_salary সব Variable আলাদা রাখতে হতো।
যত Project বড় হতো, তত Code Messy হয়ে যেত। Problems
❌ অনেক Variable
❌ Duplicate Code
❌ Maintain করা কঠিন
❌ Reuse করা কঠিন
❌ Bug বেশি
এই সমস্যাগুলো সমাধানের জন্য OOP এসেছে।

OOP এর লক্ষ্য: 
✔ Code Reuse
✔ Organization
✔ Encapsulation
✔ Abstraction
✔ Polymorphism
✔ Inheritance

=========================================================
03_Syntax
=========================================================
Class তৈরি - 
class Student:
    pass

Object তৈরি - 
student = Student()

Constructor - 
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student = Student("Rahim", 20)
print(student.name)

Output: Rahim

Method -
class Student:
    def say_hello(self):
        print("Hello")

student = Student("Rahim",20)
student.say_hello()

Output: Hello

---------------------------------------------------------
self কী?: self বর্তমান Object-কে নির্দেশ করে।
---------------------------------------------------------
Example: 
student1 = Student("Rahim",20)
student2 = Student("Karim",22)

student1.name: Rahim
student2.name: Karim

দুইটি Object হলেও Method একই। self-এর কারণে Python বুঝতে পারে কোন Object নিয়ে কাজ হচ্ছে।

=========================================================
04_Methods
=========================================================
OOP-এ Method কয়েক ধরনের হতে পারে।
---------------------------------------------------------
1. Instance Method: সবচেয়ে বেশি ব্যবহৃত।
---------------------------------------------------------
class Student:
    def hello(self):
        print("Hello")
        
---------------------------------------------------------
2. Class Method: @classmethod ব্যবহার হয়।
---------------------------------------------------------
class Student:
    total = 0
    @classmethod
    def count(cls):
        return cls.total
cls পুরো Class-কে নির্দেশ করে।

---------------------------------------------------------
3. Static Method: @staticmethod ব্যবহার হয়।
---------------------------------------------------------
class Math:
    @staticmethod
    def add(a,b):
        return a+b

এখানে self বা cls লাগে না।

---------------------------------------------------------
4. Magic Method
---------------------------------------------------------
__init__
__str__
__repr__
__len__
__eq__

ইত্যাদি।
Example:
class Student:
    def __str__(self):
        return self.name

=========================================================
OOP-এর ৪টি Pillar
=========================================================
১. Encapsulation: Data এবং Method একসাথে রাখা।
class BankAccount:
    def __init__(self,balance):
        self.balance = balance

-----------------------------------
২. Inheritance: এক Class থেকে আরেক Class তৈরি করা।

class Animal:
    pass

class Dog(Animal):
    pass

Dog এখন Animal-এর সব Feature পাবে।
-----------------------------------

৩. Polymorphism: একই Method বিভিন্নভাবে কাজ করতে পারে।
Example:
Dog.sound()
Cat.sound()
দুটো Method-এর নাম একই। কিন্তু Output আলাদা।
-----------------------------------

৪. Abstraction: ভিতরের Complexity লুকিয়ে, শুধু প্রয়োজনীয় Interface দেওয়া। যেমন, গাড়ি চালাতে Engine কীভাবে কাজ করে তা জানার প্রয়োজন হয় না। শুধু, Start() - Brake() - Accelerate() জানলেই চলে।

=========================================================
05_TimeComplexity
=========================================================
OOP নিজে কোনো Algorithm নয়। তাই OOP-এর নিজস্ব Time Complexity নেই। তবে Method Call-এর Complexity সাধারণত O(1)
Example: student.name Dictionary Lookup-এর মতোই প্রায় Constant Time। Object তৈরি Student() Memory Allocate করতে হয়। তাই Time O(1) Memory Object-এর Property অনুযায়ী বাড়ে।

=========================================================
06_InternalWorking
=========================================================
ধরো,
class Student:
    def __init__(self,name):
        self.name=name

student = Student("Rahim")

কি ঘটে? 
Step 1 -> Python Class পড়ে।
Step 2 -> Class Object তৈরি করে।
Step 3 -> Student() Call হয়।
Step 4 -> Memory-তে নতুন Object Allocate হয়।
Heap Memory
+---------------------+
| Student Object      |
|---------------------|
| name="Rahim"        |
+---------------------+
student Variable -> Reference ধরে।

Stack: student
   │
   ▼
Heap: Student Object

Step 5 -> __init__() Automatic Call হয়।
Step 6 -> self.name = "Rahim" Assign হয়।

=========================================================
07_Examples
=========================================================
Example 1:

class Student:
    def __init__(self,name):
        self.name=name

student=Student("Rahim")
print(student.name)

Output: Rahim
---------------------------------------------------------
Example 2:
class Calculator:
    def add(self,a,b):
        return a+b

cal=Calculator()
print(cal.add(5,7))
Output: 12
---------------------------------------------------------
Example 3 (Inheritance):
class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        print("Woof")

dog=Dog()
dog.sound()
Output: Woof
---------------------------------------------------------
Example 4 (Encapsulation):

class Bank:
    def __init__(self,balance):
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount

=========================================================
08_CommonMistakes
=========================================================
❌ self লিখতে ভুলে যাওয়া
Wrong
class Student:
    def hello():
        pass

Correct: 
class Student:
    def hello(self):
        pass

---------------------------------------------------------
❌ Object না বানিয়ে Method Call করা Student.hello() সাধারণ Instance Method এ Error হবে। সঠিক
student=Student()
student.hello()
---------------------------------------------------------
❌ Constructor-এর Parameter ভুল দেওয়া Student() যখন __init__(name) আছে।
---------------------------------------------------------
❌ Class Variable ও Instance Variable গুলিয়ে ফেলা
---------------------------------------------------------
❌ সব জায়গায় OOP ব্যবহার করা: ছোট Script-এর জন্য Function-ই যথেষ্ট।
=========================================================
09_Exercises
=========================================================
Exercise 1: Student Class তৈরি করো। name, age print_info()
---------------------------------------------------------
Exercise 2: Rectangle Class length, width, area()
---------------------------------------------------------
Exercise 3: BankAccount Class - deposit(), withdraw(), balance()
---------------------------------------------------------
Exercise 4: Animal থেকে Dog Inherit করো। Dog.sound() Override করো।
---------------------------------------------------------
Exercise 5: Calculator Class: add(), subtract(), multiply(), divide()
---------------------------------------------------------
Exercise 6: নিজের একটি Laptop Class তৈরি করো। Brand, RAM, Storage, show_info()
---------------------------------------------------------
Exercise 7: Employee Class তৈরি করে, Salary Increment Method লিখো।
---------------------------------------------------------
Exercise 8: Magic Method (__str__) ব্যবহার করো।
---------------------------------------------------------
Exercise 9: Static Method দিয়ে Celsius থেকে Fahrenheit Convert করো।
---------------------------------------------------------
Exercise 10: Library Management System-এর জন্য Book Class, Member Class, Library Class তৈরি করো।

=========================================================
10_AIUsage (Use Case in AI Development)
=========================================================
AI এবং Machine Learning Project-এ OOP ব্যাপকভাবে ব্যবহৃত হয়। কারণ AI Project সাধারণত অনেক বড় হয়।
যেমন, Dataset, Model, Trainer, Optimizer, Loss Function, Inference সবকিছুকে আলাদা Class হিসেবে তৈরি করা হয়।
Example:

class Dataset:
    pass

class Model:
    pass

class Trainer:
    pass

class Evaluator:
    pass

class Predictor:
    pass

TensorFlow, PyTorch, Scikit-learn, LangChain, Transformers এই সব Library-ই মূলত OOP ভিত্তিক।

উদাহরণ (PyTorch)
class MyModel(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        ...

এখানে, nn.Module থেকে Inheritance নেওয়া হয়েছে।
এর ফলে, ✔ Code Reuse, ✔ Clean Architecture, ✔ Easy Debugging, ✔ Modular Design, ✔ Large Scale AI Development সহজ হয়ে যায়।
"""