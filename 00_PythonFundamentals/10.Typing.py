# ==========================================================
# typing.py
# Python Typing Module (বাংলা)
# ==========================================================

# 01_Introduction
# ==========================================================
#
# Python একটি Dynamically Typed Language।
#
# অর্থাৎ:
#
# x = 10
# x = "Hello"
#
# একই Variable-এ বিভিন্ন ধরনের Data রাখা যায়।
#
# এটি Flexible হলেও Large Project-এ Bug খুঁজে পাওয়া কঠিন হয়।
#
# এই সমস্যার সমাধানের জন্য Python-এ Type Hinting এসেছে।
#
# Type Hinting Programmer-কে বলে দেয়:
#
# - কোন Variable-এ কি Type থাকবে
# - Function কি Input নিবে
# - Function কি Return করবে
# - IDE Auto-completion দিবে
# - Code Readability বাড়বে
#
# Typing Runtime-এ Type Enforce করে না।
# এটি মূলত Developer Tool।
#
# Example:
#
# def add(a: int, b: int) -> int:
#     return a + b
#
# ==========================================================



# 02_WhyTypingExists
# ==========================================================
#
# ধরো Team Project-এ ২০ জন Developer কাজ করছে।
#
# Function:
#
# def calculate(data):
#     ...
#
# এখানে কেউ জানে না data কি।
#
# List?
# Dict?
# String?
#
# Typing ব্যবহার করলে:
#
# def calculate(data: list[int]) -> float:
#     ...
#
# এখন সবাই বুঝতে পারবে:
#
# Input  -> list[int]
# Output -> float
#
# সুবিধা:
#
# 1. Better Readability
# 2. Better Auto Completion
# 3. Easier Refactoring
# 4. Better Team Collaboration
# 5. Fewer Bugs
# 6. Professional Codebase
#
# ==========================================================



# 03_Syntax
# ==========================================================

from typing import (
    Optional,
    Union,
    Any,
    Protocol
)

import numpy as np


# Variable Type Hint

name: str = "Mozammel"
age: int = 28
salary: float = 50000.0
is_active: bool = True


# Function Type Hint

def add(a: int, b: int) -> int:
    return a + b


# Multiple Line Function Signature

def train(
    x: np.ndarray,
    y: np.ndarray
) -> float:
    """
    AI Model Training Example
    """

    accuracy = 0.95
    return accuracy


# Generic Collection Types

numbers: list[int] = [1, 2, 3]

student_marks: dict[str, int] = {
    "Rahim": 80,
    "Karim": 90
}


# ==========================================================



# 04_Methods
# ==========================================================
#
# typing Module-এ সবচেয়ে বেশি ব্যবহৃত Concepts:
#
# 1. list[int]
# 2. dict[str,int]
# 3. Optional
# 4. Union
# 5. Any
# 6. Protocol
#
# ==========================================================


# ----------------------------------------------------------
# list[int]
# ----------------------------------------------------------
#
# List-এর প্রতিটি Element int হবে।
#

numbers: list[int] = [10, 20, 30]


# ----------------------------------------------------------
# dict[str,int]
# ----------------------------------------------------------
#
# Key -> str
# Value -> int
#

marks: dict[str, int] = {
    "Math": 90,
    "English": 85
}


# ----------------------------------------------------------
# Optional
# ----------------------------------------------------------
#
# Optional[X]
#
# মানে:
#
# X অথবা None
#

def get_user_name() -> Optional[str]:
    return None


# Equivalent:

# str | None


# ----------------------------------------------------------
# Union
# ----------------------------------------------------------
#
# একাধিক Type Allow করবে।
#

def square(value: Union[int, float]) -> float:
    return value * value


# Python 3.10+

# int | float


# ----------------------------------------------------------
# Any
# ----------------------------------------------------------
#
# Any মানে:
#
# যেকোনো Type
#

def process(data: Any):
    return data


# ----------------------------------------------------------
# Protocol
# ----------------------------------------------------------
#
# Duck Typing-এর Professional Version।
#
# Object কি Class থেকে এসেছে
# সেটা Important না।
#
# Important হলো:
#
# Method আছে কি না।
#

class Drawable(Protocol):

    def draw(self) -> None:
        ...


class Circle:

    def draw(self):
        print("Drawing Circle")


class Rectangle:

    def draw(self):
        print("Drawing Rectangle")


def render(shape: Drawable):
    shape.draw()


# ==========================================================



# 05_TimeComplexity
# ==========================================================
#
# Typing Runtime Complexity বাড়ায় না।
#
# কারণ:
#
# Type Hint সাধারণত Runtime-এ Execute হয় না।
#
# Example:
#
# def add(a:int,b:int)->int:
#     return a+b
#
# এখানে Type Hint CPU-এর Extra Calculation করে না।
#
#
# Complexity:
#
# Type Hint Reading = O(1)
#
# Runtime Cost ≈ 0
#
# ==========================================================



# 06_InternalWorking
# ==========================================================
#
# Python Interpreter Type Hint Ignore করে।
#
# Example:
#
# def add(a:int,b:int)->int:
#     return a+b
#
# Runtime-এ:
#
# def add(a,b):
#     return a+b
#
# এর মতোই Execute হয়।
#
#
# Type Information Store হয়:
#
# __annotations__
#
# Example:
#

def multiply(a: int, b: int) -> int:
    return a * b


print(multiply.__annotations__)

#
# Output:
#
# {
#   'a': int,
#   'b': int,
#   'return': int
# }
#
#
# IDE, Linter, Mypy
# এই Metadata ব্যবহার করে।
#
# ==========================================================



# 07_Examples
# ==========================================================

# Example 1

def greet(name: str) -> str:
    return f"Hello {name}"


# Example 2

def calculate_total(prices: list[float]) -> float:
    return sum(prices)


# Example 3

def get_age(user_id: int) -> Optional[int]:
    return 25


# Example 4

def convert(value: Union[int, float]) -> float:
    return float(value)


# Example 5

def save(data: Any):
    print(data)


# Example 6

model_accuracy: float = train(
    np.array([[1, 2]]),
    np.array([1])
)

# ==========================================================



# 08_CommonMistakes
# ==========================================================

# Mistake 1
#
# Wrong

numbers: list = [1, 2, 3]

#
# Better
#

numbers: list[int] = [1, 2, 3]


# ----------------------------------------------------------

# Mistake 2
#
# Any অতিরিক্ত ব্যবহার করা
#

def process_data(data: Any):
    pass

#
# Better
#

def process_data(data: dict[str, str]):
    pass


# ----------------------------------------------------------

# Mistake 3
#
# Return Type না দেওয়া
#

def add1(a: int, b: int):
    return a + b

#
# Better
#

def add2(a: int, b: int) -> int:
    return a + b


# ----------------------------------------------------------

# Mistake 4
#
# Optional ব্যবহার না করা
#

# Wrong

user_name: str = None

#
# Correct
#

user_name: Optional[str] = None

# ==========================================================



# 09_Exercises
# ==========================================================

# Exercise 1
#
# একটি Function লেখো
#
# Input:
# list[int]
#
# Output:
# int
#
# Sum Return করবে।.


# Exercise 2
#
# dict[str,int]
#
# Type Hint দিয়ে Student Marks Store করো।


# Exercise 3
#
# Optional[str]
#
# ব্যবহার করে User Name Return করো।


# Exercise 4
#
# Union[int,float]
#
# ব্যবহার করে Calculator Function লেখো।


# Exercise 5
#
# Any ব্যবহার করে Generic Logger Function লেখো।


# Exercise 6
#
# একটি Protocol তৈরি করো
#
# নাম:
# Playable
#
# Method:
#
# play()
#
# ==========================================================



# 10_AIUsage-usecase in ai development
# ==========================================================
#
# AI Development-এ Typing অত্যন্ত গুরুত্বপূর্ণ।
#
# কারণ:
#
# AI Project-এ Data Structure বড় হয়।
#
# Example:
#

def train_model(
    x: np.ndarray,
    y: np.ndarray
) -> float:

    return 0.95


#
# এখন Function Signature দেখেই বোঝা যায়:
#
# x -> Feature Matrix
# y -> Labels
# return -> Accuracy
#
#
# Real AI Libraries:
#
# TensorFlow
# PyTorch
# HuggingFace
# LangChain
# OpenAI SDK
#
# সব জায়গায় Type Hint ব্যাপকভাবে ব্যবহৃত হয়।
#
#
# Benefits:
#
# ✅ Better Documentation
# ✅ Better IDE Support
# ✅ Easier Refactoring
# ✅ Fewer Bugs
# ✅ Enterprise Ready Code
# ✅ Large Team Collaboration
#
#
# Professional Python Developer
# হলে Typing জানা বাধ্যতামূলক।
#
# ==========================================================
#
# Summary
#
# list[int]
# dict[str,int]
# Optional
# Union
# Any
# Protocol
#
# এগুলো Python Typing-এর সবচেয়ে গুরুত্বপূর্ণ Concepts।
#
# Professional Python Codebase-এ এগুলো প্রতিদিন ব্যবহার করা হয়।
#
# ==========================================================