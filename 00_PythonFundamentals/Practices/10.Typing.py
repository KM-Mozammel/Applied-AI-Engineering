# Exercise 1: একটি Function লেখো Input: list[int] Output: int,  Sum Return করবে।
def myList(data: list[int]) -> int:
    return sum(data)

numbers: list[int] = [1, 2, 4, 5, 6]
result = myList(numbers)
# print(result)

# Exercise 2: dict[str,int], Type Hint দিয়ে Student Marks Store করো।
marks: dict[str, int] = {}

def store(name: str, score: int) -> None:
    marks[name] = score
    
store("Rahim", 85)
store("Neon", 45)
store("Nomal", 65)

# print(marks)

# Exercise 3: Optional[str] ব্যবহার করে User Name Return করো।
from typing import Optional
def get_user_name(name: Optional[str]) -> Optional[str]:
    if name: 
        return name
    else:
        return None
    
# print(get_user_name("Mozammel"))
# print(get_user_name(None))

# Exercise 4: Union[int,float] ব্যবহার করে Calculator Function লেখো।
from typing import Union
def calculator(a: Union[int, float], b: Union[int, float], op: str) -> Union[int, float]:
    if op == "add":
        return a + b
    elif op == "sub":
        return a - b
    elif op == "mul":
        return a * b
    elif op == "div":
        if b != 0:
            return a / b
        else:
            raise ValueError("Division by zero not allowed")
    else:
        raise ValueError("Invalid operation")
    
# print(calculator(10, 5, "add"))  # Output: 15
# print(calculator(10.5, 2, "mul"))  # Output: 21.0
# print(calculator(10, 0, "div"))  # Raises ValueError

# Exercise 5: Any ব্যবহার করে Generic Logger Function লেখো।
from typing import Any

def logger(message: Any) -> None:
    print(f"[LOG]: {message}")

logger("System started")
logger(404)
logger({"user": "Rahim", "id": 1})
logger([1, 2, 3, 4, 5])

# Exercise 6: একটি Protocol তৈরি করো, নাম: Playable, Method: play()
from typing import Protocol

class Playable(Protocol):
    def play(self) -> None:
        ...
        
class Song:
    def play(self) -> None:
        print("Playing song...")
    
class Video:
    def play(self) -> None:
        print("Playing video...")
        
def start_playing(item: Playable) -> None:
    item.play()

song = Song()
video = Video()

start_playing(song)
start_playing(video)