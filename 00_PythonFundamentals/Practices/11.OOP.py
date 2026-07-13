# Exercise 1: Student Class তৈরি করো। name, age print_info()

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def print_info(self):
        print("Name: ", self.name)
        print("Age: ", self.age)

student = Student("Rahim", 45)
# student.print_info()

# ---------------------------------------------------------
# Exercise 2: Rectangle Class length, width, area()

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        print("Area(length X width = )", self.length * self.width)
        
rect = Rectangle(5, 6)
# rect.area()

# ---------------------------------------------------------
# Exercise 3: BankAccount Class - deposit(), withdraw(), balance()
class BankAccount:
    def __init__(self):
        self.balance: int = 0
    
    def deposit(self, amount):
        self.balance += amount
        print("Deposite Amount:", amount)
        
    def withdraw(self, amount):
        self.balance -= amount
        print("Withdraw Amount", amount)
        
    def show_balance(self):
        print("Current Balance: ", self.balance)
        
account = BankAccount()

# account.show_balance()
# account.deposit(1000)
# account.show_balance()
# account.withdraw(300)
# account.show_balance()

# ---------------------------------------------------------
# Exercise 4: Animal থেকে Dog Inherit করো। Dog.sound() Override করো।
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bhew")
    
dog = Dog()
# dog.sound()


# ---------------------------------------------------------
# Exercise 5: Calculator Class: add(), subtract(), multiply(), divide()
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        print(self.num1 + self.num2)

    def subtract(self):
        print(self.num1 - self.num2)

    def multiply(self):
        print(self.num1 * self.num2)

    def divide(self):
        if self.num2 != 0:
            print(self.num1 / self.num2)
        else:
            print("Cannot divide by zero")


calc = Calculator(10, 5)

# calc.add()
# calc.subtract()
# calc.multiply()
# calc.divide()

# ---------------------------------------------------------
# Exercise 6: নিজের একটি Laptop Class তৈরি করো। Brand, RAM, Storage, show_info()
class Laptop:
    def __init__(self, brand: str, ram: int, storage: int):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        
    def show_info(self) -> None:
        print(f"Brand: {self.brand}")
        print(f"RAM: {self.ram}")
        print(f"Storage: {self.storage}")
        
laptop = Laptop("Toshiba", 8, 500)
# laptop.show_info()

# ---------------------------------------------------------
# Exercise 7: Employee Class তৈরি করে, Salary Increment Method লিখো।

class Employee:
    def __init__(self, name: str, dep: str, salary: int):
        self.Name = name
        self.Department = dep
        self.Salary = salary
        
    def salaryInc(self, amount) -> None:
        self.Salary += amount
        print("salary incresed", amount)
        
employee = Employee("Md Abul", "IT", 45000)
# print(employee.Salary)
employee.salaryInc(5000)
# print(employee.Salary)

# ---------------------------------------------------------
# Exercise 8: Magic Method (__str__) ব্যবহার করো।

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
    
student = Student("Rahim", 20)
# print(student)

# ---------------------------------------------------------
# Exercise 9: Static Method দিয়ে Celsius থেকে Fahrenheit Convert করো।
class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32
    
print(Temperature.celsius_to_fahrenheit(25))
# ---------------------------------------------------------
# Exercise 10: Library Management System-এর জন্য Book Class, Member Class, Library Class তৈরি করো।

class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def show_info(self) -> None:
        status = "Borrowed" if self.is_borrowed else "Available"

        print(f"Title : {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {status}")
        print("-" * 30)


class Member:
    def __init__(self, name: str):
        self.name = name
        self.borrowed_books: list[Book] = []

    def borrow_book(self, book: Book) -> None:
        self.borrowed_books.append(book)

    def return_book(self, book: Book) -> None:
        self.borrowed_books.remove(book)

    def show_borrowed_books(self) -> None:
        print(f"\nBooks borrowed by {self.name}:")

        if not self.borrowed_books:
            print("No borrowed books.")
            return

        for book in self.borrowed_books:
            print(f"- {book.title}")


class Library:
    def __init__(self):
        self.books: list[Book] = []
        self.members: list[Member] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def add_member(self, member: Member) -> None:
        self.members.append(member)

    def show_books(self) -> None:
        print("\nLibrary Books")

        for book in self.books:
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"{book.title} ({status})")

    def borrow_book(self, member: Member, book: Book) -> None:

        if book not in self.books:
            print("Book does not exist in library.")
            return

        if book.is_borrowed:
            print("Book is already borrowed.")
            return

        member.borrow_book(book)
        book.is_borrowed = True

        print(f"{member.name} borrowed '{book.title}'.")

    def return_book(self, member: Member, book: Book) -> None:

        if book not in member.borrowed_books:
            print(f"{member.name} doesn't have this book.")
            return 

        member.return_book(book)
        book.is_borrowed = False

        print(f"{member.name} returned '{book.title}'.")