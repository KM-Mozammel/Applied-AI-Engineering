# Exercise 1: add() Function-এর Test লিখো।
def add(a: int, b: int) -> int:
    return a + b
# --------------------------------------------------
# Exercise 2: subtract() Function-এর জন্য ৩টি assert লিখো।
def subtract(a: int, b: int) -> int:
    return a-b
# --------------------------------------------------
# Exercise 3:  Fixture তৈরি করো। যা একটি Dataset Return করবে।

def square(x):
    return x * x
# --------------------------------------------------
# Exercise 4: divide() Function-এর ZeroDivisionError Test করো।
def divide(a: int, b: int) -> int:
    return a / b

# --------------------------------------------------
# Exercise 5: LinearModel Class-এর predict() Method Test করো।

class LinearModel:
    def __init__(self, weight: float, bias: float):
        self.weight = weight
        self.bias = bias
        
    def predict(self, x: float) -> float:
        return self.weight * x + self.bias
    
model = LinearModel(weight=2, bias=1)

print(model.predict(x=5))