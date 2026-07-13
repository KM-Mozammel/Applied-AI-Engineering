fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]

count = {}

for fruit in fruits:
    if fruit in count:
        count[fruit] += 1
    else:
        count[fruit] = 1

# print(count)


# Exercise 1: একটি String-এর Character Count বের করো। Hint: Counter()
string = "Mozammel"
string = string.lower()  # Convert to lowercase for uniformity
from collections import Counter, defaultdict

# print(Counter(string))
# ------------------------------------
# Exercise 2: একটি Paragraph-এর Word Frequency বের করো।
paragraph = (
    "Python is a programming language. Python is easy to learn. Python is popular."
)
words = paragraph.lower().split()  # Convert to lowercase and split into words
word_count = Counter(words)
# print(word_count)

# ------------------------------------
# Exercise 3: defaultdict(list) ব্যবহার করে, Student Group তৈরি করো। Output: Python Rahim Karim AI Hasan
studentGroup = defaultdict(list)
studentGroup["Python"].append("Rahim")
studentGroup["Python"].append("Karim")
studentGroup["AI"].append("Hasan")
# print(studentGroup)

# ------------------------------------
# Exercise 4: deque ব্যবহার করে Queue তৈরি করো। enqueue(), dequeue()
from collections import deque

myQueue = deque()


def enqueue(item):
    myQueue.append(item)


enqueue("Rahim")
enqueue("Karim")
# print(myQueue)


def dequeue():
    if myQueue:
        return myQueue.popleft()
    else:
        return "Queue is empty"


dequeue()
dequeue()

# print(myQueue)

# ------------------------------------
# Exercise 5: deque ব্যবহার করে Browser History Simulation বানাও।
forwared = deque()
backward = deque()
current = None

# print("Forward:", forwared)
# print("Backward:", backward)
# print("Current:", current)

def visit(page):
    global current

    if current is not None:
        backward.append(current)

    current = page
    forwared.clear()  # Clear forward history when visiting a new

visit("https://www.google.com")

# print("Forward:", forwared)
# print("Backward:", backward)
# print("Current:", current)

visit("https://www.youtube.com")

# print("Forward:", forwared)
# print("Backward:", backward)
# print("Current:", current)

visit("https://www.soundcloud.com")

# print("Forward:", forwared)
# print("Backward:", backward)
# print("Current:", current)

def go_back():
    global current
    if not backward:
        print("No backward history.")
        return
    forwared.append(current)
    current = backward.pop()
    
go_back()

# print("Forward:", forwared)
# print("Backward:", backward)
# print("Current:", current)

# ------------------------------------
# Exercise 6: namedtuple ব্যবহার করে, Employee Object তৈরি করো। Fields, id, name, salary
from collections import namedtuple

Employee = namedtuple("Employee", ["id", "name", "salary"])

employee = Employee(id=1, name="Rahim", salary=50000)

# print(employee.id)      # Output: 1
# print(employee.name)    # Output: Rahim
# print(employee.salary)  # Output: 50000
# ------------------------------------
# Exercise 7: OrderedDict ব্যবহার করে, LRU(Least Recently Used) Cache-এর Basic Version তৈরি করো।

from collections import OrderedDict
cache = OrderedDict()
CACHE_SIZE = 3

def put(key, value):
    if key in cache:
        cache.move_to_end(key)
    cache[key] = value
    
    if len(cache) > CACHE_SIZE:
        removed = cache.popitem(last=False)
        print("Removed: ", removed)
        
def get(key):
    if key not in cache:
        return "Not Found"

    cache.move_to_end(key)
    
    return cache[key]

put("A", 10)
put("B", 20)
put("C", 30)

print(cache)
print("Getting B-", get("B"))
put("D", 40)
print(cache)


# ------------------------------------
# Exercise 8: Counter.most_common() ব্যবহার করে, Top 3 Frequent Word বের করো।
# print("Top 3 Frequent Words:")
words = [
    "python", "java", "python", "c++", "java", "python", "c#", "java", "c++", "python"
]
word_count = Counter(words)
top_words = word_count.most_common(3)
# print(top_words)
