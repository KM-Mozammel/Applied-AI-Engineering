# =========================================================
# 01_Introduction
# =========================================================

"""
Control Flow কী? Control Flow হচ্ছে প্রোগ্রামের Execution কোন পথে যাবে
সেটা নিয়ন্ত্রণ করার ব্যবস্থা। Default অবস্থায় Python উপর থেকে নিচ পর্যন্ত
লাইন ধরে Code Execute করে।

Example: Line 1 -> Line 2 -> Line 3 -> Line 4

কিন্তু বাস্তব জীবনে সব সময় একই কাজ করা হয় না।

যদি বৃষ্টি হয় → ছাতা নাও
না হলে → বের হয়ে যাও
যদি টাকা থাকে → বাজার করো
না হলে → বাসায় ফিরে যাও

Programming-এও ঠিক একই জিনিস দরকার। Control Flow সেই সিদ্ধান্ত নেওয়ার ব্যবস্থা।

Python-এর প্রধান Control Flow:

1. if
2. else
3. elif
4. for
5. while
6. break
7. continue
8. pass
9. match (Python 3.10+)

"""

# =========================================================
# 02_WhyControlFlowExists
# =========================================================

"""
কেন Control Flow দরকার? ধরো AI Camera মানুষের মুখ দেখছে।

যদি মুখ পাওয়া যায় -> ছবি তুলবে
না হলে -> অপেক্ষা করবে
---------------------------------

ATM Machine:
যদি PIN সঠিক -> টাকা দাও
না হলে -> Error দেখাও
---------------------------------

Game: 
যদি Health == 0 -> Game Over
না হলে -> খেলা চলবে
---------------------------------

Robot:
যদি সামনে দেয়াল থাকে -> Left Turn
না হলে -> সামনে যাও
---------------------------------
Control Flow ছাড়া Program কখনোই
Decision নিতে পারবে না।

"""


# =========================================================
# 03_Syntax
# =========================================================

print("\n========== 03_Syntax ==========\n")

# -------------------------------
# if
# -------------------------------

age = 20

if age >= 18:
    print("Adult")


# -------------------------------
# else
# -------------------------------

age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")


# -------------------------------
# elif
# -------------------------------

marks = 75

if marks >= 80:
    print("A+")
elif marks >= 60:
    print("A")
else:
    print("Need Improvement")


# -------------------------------
# for
# -------------------------------

for i in range(5):
    print(i)


# -------------------------------
# while
# -------------------------------

count = 1

while count <= 5:
    print(count)
    count += 1


# -------------------------------
# break
# -------------------------------

for i in range(10):

    if i == 5:
        break

    print(i)


# -------------------------------
# continue
# -------------------------------

for i in range(6):

    if i == 3:
        continue

    print(i)


# -------------------------------
# pass
# -------------------------------

for i in range(3):

    if i == 1:
        pass

    print(i)


# -------------------------------
# match
# -------------------------------

day = 3

match day:
    case 1:
        print("Saturday")
    case 2:
        print("Sunday")
    case 3:
        print("Monday")
    case _:
        print("Unknown")


# =========================================================
# 04_Methods
# =========================================================

"""
Control Flow-এর বিভিন্ন Method
১) if : একটি Condition পরীক্ষা করে।
----------------------------
if condition:
    ...
----------------------------

২) else: Condition False হলে Execute হয়।
----------------------------
if condition:
    ...
else:
    ...
----------------------------

৩) elif: একাধিক Condition পরীক্ষা করে।
----------------------------

if
↓
elif
↓
elif
↓
else
----------------------------

৪) for: একটি Iterable-এর প্রতিটি Item-এর উপর Loop চালায়।
Iterable:
List
Tuple
Dictionary
String
Set
Range
----------------------------
৫) while: Condition True থাকা পর্যন্ত Loop চলে।
----------------------------

৬) break: Loop সঙ্গে সঙ্গে শেষ করে।
----------------------------

৭) continue: বর্তমান Iteration Skip করে।
----------------------------

৮) pass: কিছুই করে না। Placeholder হিসেবে ব্যবহৃত হয়।
----------------------------

৯) match: একাধিক Case Match করার জন্য ব্যবহৃত হয়। switch-case এর আধুনিক Python Version।
"""


# =========================================================
# 05_TimeComplexity
# =========================================================

"""
if --------O(1),
else--------O(1),
elif--------Worst Case = O(n)-কারণ সব Condition পরীক্ষা করতে হতে পারে।
for--------O(n),
while--------O(n),
break--------Best Case - O(1),
continue--------O(1),
pass--------O(1)
match--------প্রায় O(1)
কিন্তু অনেক Case হলে Worst O(n) ধরা যায়।
"""


# =========================================================
# 06_InternalWorking
# =========================================================
"""
Python Control Flow ভিতরে কীভাবে কাজ করে?

উদাহরণ: if age >= 18:

Step 1: age Variable থেকে Value নেয়।
Step 2: 18 এর সাথে Compare করে।
Step 3: Boolean Result তৈরি হয়। True / False
Step 4: True হলে Block Execute. False হলে Skip
------------------------------------
for Loop: for i in range(5)
range(5): 0 1 2 3 4
Iterator তৈরি হয়। -> প্রতিবার Next() -> Value আসে -> Body Execute হয় -> আবার Next()
------------------------------------
while Condition: True? -> Execute -> Condition আবার Check -> False? -> Loop শেষ
------------------------------------
break: Loop Exit
------------------------------------
continue: Body-এর বাকি অংশ Skip -> Next Iteration
------------------------------------
match: Expression Evaluate -> Case Compare -> Match পাওয়া গেলে Execute -> Stop
"""


# =========================================================
# 07_Examples
# =========================================================

print("\n========== 07_Examples ==========\n")

# Example 1: IF
age = 22
if age >= 18:
    print("Vote দিতে পারবে")

# Example 2: IF - ELSE
temperature = 32
if temperature > 35:
    print("Hot")
else:
    print("Normal")

# Example 3: IF-ELIF-ELSE
score = 90
if score >= 80:
    print("Excellent")
elif score >= 60:
    print("Good")
else:
    print("Fail")

# Example 4: FOR
for i in range(1, 6):
    print("Number =", i)

# Example 5: WHILE
x = 1
while x <= 5:
    print(x)
    x += 1


# Example 6: FOR IF BREAK
for i in range(10):
    if i == 4:
        break
    print(i)
    
# Example 7: FOR IF CONTINUE
for i in range(6):
    if i == 2:
        continue
    print(i)

# Example 8: FOR IF PASS
for i in range(3):
    if i == 1:
        pass
    print(i)

# Example 9: MATCH
command = "start"
match command:
    case "start":
        print("Engine Started")
    case "stop":
        print("Engine Stopped")
    case _:
        print("Invalid Command")

# =========================================================
# 08_CommonMistakes
# =========================================================

"""
১) ভুল Indentation
if True:
print("Hello")
সঠিক
if True:
    print("Hello")
--------------------------------

২) = ব্যবহার করা, if x = 5: ভুল . == ব্যবহার করতে হবে।
if x == 5:
--------------------------------

৩) Infinite While Loop:
while True:
    print("Hello")
Break না থাকলে Loop শেষ হবে না।
--------------------------------

৪) break Loop-এর বাইরে ব্যবহার করা, এটি Error দিবে।
--------------------------------

৫) continue Loop-এর বাইরে ব্যবহার করা, এটিও Error দিবে।
--------------------------------

৬) match ব্যবহার করতে Python 3.10+ লাগবে।
"""


# =========================================================
# 09_Exercises
# =========================================================

"""
Exercise 1: Input নিয়ে Positive/Negative Check করো।
----------------------------
Exercise 2: Marks নিয়ে Grade বের করো।
----------------------------
Exercise 3: for Loop দিয়ে, 1-20 Print করো।
----------------------------
Exercise 4: while দিয়ে ১০ থেকে ১ পর্যন্ত Countdown করো।
----------------------------
Exercise 5: break ব্যবহার করে, 1-100 এর মধ্যে 50 এ Loop বন্ধ করো।
----------------------------
Exercise 6: continue ব্যবহার করে, Even Number Skip করো।
----------------------------
Exercise 7: pass ব্যবহার করে, একটি Empty Function লিখো।
----------------------------
Exercise 8: match ব্যবহার করে, Week Day Print করো।
----------------------------
Exercise 9: 1-100 পর্যন্ত, সব Prime Number Print করো।
----------------------------
Exercise 10: Nested for Loop দিয়ে, Pattern Print করো।
*
**
***
****
*****
"""

# =========================================================
# 10_AIUsage
# =========================================================

"""
Python Control Flow AI Development-এ কোথায় ব্যবহৃত হয়? Control Flow হচ্ছে AI-এর Decision Making-এর ভিত্তি। Machine Learning, Deep Learning, Reinforcement Learning, LLM Agent, Robotics—সব জায়গাতেই Control Flow ব্যবহৃত হয়।
=========================================================
১. Data Preprocessing
=========================================================
Dataset-এর প্রতিটি Row পরীক্ষা করা হয়।
উদাহরণ: 
for row in dataset:
    if row is valid:
        Process
    else:
        Skip
---------------------------------------------------------

=========================================================
২. Data Cleaning
=========================================================
Missing Value থাকলে
if value is None:
    Fill Mean
else:
    Keep Original
---------------------------------------------------------

=========================================================
৩. Model Training
=========================================================
Epoch Loop:
for epoch in range(100):
    Train()
    Validate()
---------------------------------------------------------

=========================================================
৪. Batch Processing
=========================================================
for batch in dataloader:
    prediction = model(batch)
---------------------------------------------------------

=========================================================
৫. Early Stopping
=========================================================
Validation Loss বাড়তে থাকলে
if validation_loss > previous_loss:
    break
Training বন্ধ হয়ে যায়।

---------------------------------------------------------

=========================================================
৬. Reinforcement Learning
=========================================================
while not done:
    action = agent()
    reward = environment()
    Learn()
Episode শেষ হলে Loop শেষ।
---------------------------------------------------------

=========================================================
৭. AI Chatbot
=========================================================
if user asks weather:
    Weather API
elif asks math:
    Calculator
else:
    LLM Response

---------------------------------------------------------

=========================================================
৮. Computer Vision
=========================================================
for image in dataset:
    Detect Object
    if person_found:
        Draw Bounding Box

---------------------------------------------------------

=========================================================
৯. Natural Language Processing (NLP)
=========================================================
for sentence in corpus:
    Tokenize
    Remove Stop Words
    Encode
---------------------------------------------------------

=========================================================
১০. LLM Agent
=========================================================
Agent-এর Planning Loop
while task_not_completed:
    Think()
    Call Tool()
    Observe()
    Decide Next Action()
---------------------------------------------------------

=========================================================
১১. Robotics
=========================================================
if obstacle:
    Turn Left
else:
    Move Forward
---------------------------------------------------------

=========================================================
১২. Autonomous Vehicle
=========================================================

if traffic_light == "RED":
    Stop
elif traffic_light == "GREEN":
    Move
else:
    Slow Down

---------------------------------------------------------

=========================================================
১৩. AI Pipeline
=========================================================
Load Data
    ↓
Clean Data
    ↓
Feature Engineering
    ↓
Train Model
    ↓
Evaluate
    ↓
Deploy

প্রতিটি ধাপেই if, for, while, break, continue ব্যবহৃত হয়।
---------------------------------------------------------
শেখার Outcome:
✓ AI Pipeline বুঝতে পারবে
✓ Training Loop বুঝতে পারবে
✓ Data Processing করতে পারবে
✓ Reinforcement Learning-এর Episode Loop বুঝবে
✓ LLM Agent কীভাবে সিদ্ধান্ত নেয় বুঝবে
✓ Robotics ও Computer Vision-এর Control Logic বুঝতে পারবে
অর্থাৎ, Python-এর Control Flow আয়ত্ত করা মানে, AI System-এর Decision Making-এর ভিত্তি আয়ত্ত করা।
"""

print("\n========== End of Control Flow Tutorial ==========")