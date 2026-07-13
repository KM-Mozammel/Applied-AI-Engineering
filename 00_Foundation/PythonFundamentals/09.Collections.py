"""
============================================================
01_Introduction (পরিচিতি)
============================================================
collections হলো Python-এর একটি Built-in Module। এটি dict, list, tuple-এর আরও শক্তিশালী এবং বিশেষায়িত Version দেয় যাতে কিছু Common Problem খুব সহজে সমাধান করা যায়। Import করতে হয়—

from collections import Counter
from collections import defaultdict
from collections import deque
from collections import namedtuple
from collections import OrderedDict

collections Module-এর প্রধান Component

✔ Counter
✔ defaultdict
✔ deque
✔ namedtuple
✔ OrderedDict

এগুলো Python Programmer-এর অন্যতম গুরুত্বপূর্ণ Tools।
"""
# ============================================================
# 02_WhyCollectionsExists
# ============================================================
"""
Python-এর Built-in Data Structure অনেক শক্তিশালী। তবুও কিছু সমস্যা বারবার দেখা যায়। যেমন—
১। একটি List-এ কোন Element কতবার আছে? Normal dict দিয়ে করতে গেলে—t 

count = {}
for item in data:
    ...

অনেক Code লিখতে হয়। Counter এটি এক লাইনে করে।
-------------------------------------
২। Dictionary-তে Key না থাকলে? Normal dict d["apple"] KeyError দিবে। defaultdict নিজেই Default Value বানিয়ে দেয়।
-------------------------------------
৩। List-এর সামনে Insert/Delete list.insert(0,x) ধীরে কাজ করে। deque দুই পাশ থেকেই O(1) সময়ে Insert/Delete করতে পারে।
-------------------------------------
৪। Tuple-এর Index মনে রাখা কঠিন।

person[0]
person[1]
person[2]

বোঝা যায় না কোনটা Name, কোনটা Age। namedtuple Index-এর বদলে Name ব্যবহার করতে দেয়।
-------------------------------------
৫। আগে Dictionary Order রাখতো না। OrderedDict - Insertion Order ধরে রাখার জন্য তৈরি হয়েছিল। (Python 3.7+ এ সাধারণ dict-ও Order ধরে রাখে, তবুও কিছু Special Feature-এর জন্য OrderedDict ব্যবহৃত হয়।)
"""
# ============================================================
# 03_Syntax
# ============================================================
from collections import Counter
from collections import defaultdict
from collections import deque
from collections import namedtuple
from collections import OrderedDict
"""
Counter - counter = Counter(iterable)
------------------------------------
defaultdict: d = defaultdict(int)
------------------------------------
deque: dq = deque()
------------------------------------
namedtuple: Student = namedtuple("Student", ["name", "age"])
------------------------------------
OrderedDict: od = OrderedDict()
"""
# ============================================================
# 04_Methods
# ============================================================
"""
========================
Counter
========================
elements()
most_common()
update()
subtract()
total()
clear()
copy()
---------------------------------------------------
Example: 
counter = Counter("banana")
print(counter)
Output: Counter({'a':3,'n':2,'b':1})
========================
defaultdict
========================
Default Factory:

int
list
set
float
str

Example:
d = defaultdict(int)
d["apple"] += 1
print(d)
Output: defaultdict(<class 'int'>, {'apple':1})
========================
deque
========================
append()
appendleft()
pop()
popleft()
extend()
extendleft()
rotate()
reverse()
clear()

Example:
dq = deque([1,2,3])
dq.appendleft(0)
print(dq)
deque([0,1,2,3])
========================
namedtuple
========================
_make()
_asdict()
_replace()
_fields

Student = namedtuple("Student",["name","age"])
s = Student("Rahim",20)
print(s.name)
Rahim
========================
OrderedDict
========================
move_to_end()
popitem()
clear()
update()
copy()
"""
# ============================================================
# 05_TimeComplexity
# ============================================================
"""
Counter: 
Count Element - O(n)
Lookup - O(1)
------------------------------------
defaultdict: 
Lookup - O(1) 
Insert - O(1)
------------------------------------
deque: 
append() - O(1) 
appendleft() - O(1)
pop() - O(1)
popleft() - O(1)
Random Access - O(n)
------------------------------------
namedtuple:
Read - O(1)
Create - O(n)
------------------------------------
OrderedDict: 
Lookup - O(1)
Insert - O(1)
Delete - O(1)
move_to_end() - O(1)
"""
# ============================================================
# 06_InternalWorking
# ============================================================
"""
========================
Counter: Counter আসলে dict-এর উপর ভিত্তি করে তৈরি।
========================
Memory: 
Counter -> { 'a':3, 'b':1, 'n':2 }
যখন Loop চলে—
for item in iterable:
    Counter[item]+=1
একই Key বারবার এলে Count বাড়ে।
-------------------------------------
========================
defaultdict
========================
Normal Dict: d["apple"] -> Key নেই -> KeyError
-------------------------------------
defaultdict: Key নেই -> Factory Function Call -> Value তৈরি -> Dictionary-তে Insert -> Return
যেমন, defaultdict(list) Key না থাকলে [] নিজে বানিয়ে দেয়।
-------------------------------------
========================
deque
========================
deque: Double Ended Queue
এটি List-এর মতো Continuous Memory ব্যবহার করে না। বরং অনেক Block আকারে Memory রাখে।
Block:
+-----+
|1 2 3|
+-----+
↓
+-----+
|4 5 6|
+-----+
তাই, Front এবং Back দুই পাশেই O(1) সময়ে কাজ করতে পারে।
-------------------------------------
========================
namedtuple
========================
namedtuple: Tuple-এর উপর ভিত্তি করে তৈরি।
Memory: ("Rahim",20)
কিন্তু, Index Mapping
0 → name
1 → age
তাই, student.name আসলে student[0] ব্যবহার করে।
-------------------------------------
========================
OrderedDict
========================
আগে Python Dict Hash Table ছিল। Order থাকতো না। 
OrderedDict: Hash Table + Doubly Linked List ব্যবহার করতো।
Hash Table -> Fast Lookup
Linked List -> Insertion Order 
তাই move_to_end() -> O(1) সময়ে করা সম্ভব। Python 3.7+ এ সাধারণ dict-ও Insertion Order ধরে রাখে, কিন্তু OrderedDict এখনও Reordering Operation-এর জন্য ব্যবহৃত হয়।
"""
# ============================================================
# 07_Examples
# ============================================================
print("\n========== Counter ==========")
words = ["apple","banana","apple","orange","banana","apple"]
counter = Counter(words)
print(counter)
print(counter["apple"])
print(counter.most_common(2))

print("\n========== defaultdict ==========")
students = defaultdict(list)
students["Python"].append("Rahim")
students["Python"].append("Karim")
students["AI"].append("Hasan")
print(students)

print("\n========== deque ==========")
dq = deque([1,2,3])
dq.append(4)
dq.appendleft(0)
dq.pop()
dq.popleft()
print(dq)

print("\n========== namedtuple ==========")
Student = namedtuple("Student",["name","age"])
s = Student("Rahim",25)
print(s.name)
print(s.age)
print(s)

print("\n========== OrderedDict ==========")
od = OrderedDict()
od["A"] = 10
od["B"] = 20
od["C"] = 30
print(od)
od.move_to_end("A")
print(od)

# ============================================================
# 08_CommonMistakes
# ============================================================
"""
১। Counter থেকে Normal dict আশা করা। Counter নিজেও dict-এর Child Class।
------------------------------------
২। defaultdict-এর Factory Function দিতে ভুলে যাওয়া। Wrong, defaultdict(), Correct, defaultdict(list)
------------------------------------
৩। deque-কে Random Access-এর জন্য ব্যবহার করা। Wrong -> dq[500000]. deque-এর শক্তি হলো Front এবং Back Operation।
------------------------------------
৪। namedtuple Immutable। Wrong -> student.age = 30 Error
------------------------------------
৫। Python 3.7+ এ সব জায়গায় OrderedDict ব্যবহার করা। সাধারণ dict-ও এখন Order ধরে রাখে। শুধু Extra Feature লাগলে OrderedDict ব্যবহার করো।
"""
# ============================================================
# 09_Exercises
# ============================================================
"""
Exercise 1: একটি String-এর Character Count বের করো। Hint: Counter()
------------------------------------
Exercise 2: একটি Paragraph-এর Word Frequency বের করো।
------------------------------------
Exercise 3: defaultdict(list) ব্যবহার করে, Student Group তৈরি করো। Output: Python Rahim Karim AI Hasan
------------------------------------
Exercise 4: deque ব্যবহার করে Queue তৈরি করো। enqueue(), dequeue()
------------------------------------
Exercise 5: deque ব্যবহার করে Browser History Simulation বানাও।
------------------------------------
Exercise 6: namedtuple ব্যবহার করে, Employee Object তৈরি করো। Fields, id, name, salary
------------------------------------
Exercise 7: OrderedDict ব্যবহার করে, LRU Cache-এর Basic Version তৈরি করো।
------------------------------------
Exercise 8: Counter.most_common() ব্যবহার করে, Top 3 Frequent Word বের করো।
"""
# ============================================================
# 10_AIUsage (Use Case in AI Development)
# ============================================================
"""
AI, Machine Learning এবং NLP-তে collections Module প্রচুর ব্যবহৃত হয়।
==================================================
Counter
==================================================
✔ Word Frequency
✔ Token Count
✔ Vocabulary তৈরি
✔ Character Frequency

Example: Counter(tokens) Language Model Training-এর প্রথম ধাপগুলোর একটি।
--------------------------------------------------
==================================================
defaultdict
==================================================
✔ Graph তৈরি
✔ Adjacency List
✔ Grouping Data
✔ Inverted Index
Search Engine-এ ব্যাপক ব্যবহার হয়।
--------------------------------------------------
==================================================
deque
==================================================
✔ BFS (Breadth First Search)
✔ Sliding Window
✔ Streaming Data
✔ Chat History
✔ Conversation Buffer
Large Language Model-এর Memory Window Simulation-এও Queue ধারণা ব্যবহৃত হয়।
--------------------------------------------------
==================================================
namedtuple
==================================================
✔ Dataset Record
✔ Coordinate
✔ Bounding Box
✔ Prediction Result
ছোট Immutable Object সংরক্ষণে কার্যকর।
--------------------------------------------------
==================================================
OrderedDict
==================================================
✔ LRU Cache
✔ Model Configuration
✔ Ordered Pipeline
✔ Feature Processing
--------------------------------------------------
AI Interview-তে জানতে চাইতে পারে—
1. Counter এবং dict-এর পার্থক্য কী?
2. defaultdict কেন KeyError দেয় না?
3. deque কেন list-এর চেয়ে Queue হিসেবে দ্রুত?
4. namedtuple এবং dataclass-এর পার্থক্য কী?
5. OrderedDict এখনো কেন ব্যবহৃত হয়?
6. Counter.most_common() কীভাবে কাজ করে?
7. deque-এর Internal Structure কী?
8. AI/NLP-তে Counter কোথায় ব্যবহার হয়?
9. BFS-এ deque কেন ব্যবহৃত হয়?
10. defaultdict(list) দিয়ে Graph কীভাবে তৈরি করা যায়?
"""