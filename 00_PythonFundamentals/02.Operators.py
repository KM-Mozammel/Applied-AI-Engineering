# ============================================================
# 01_Introduction
# ============================================================

"""
Operator কী? Operator হলো এমন একটি Symbol বা Keyword যা একটি বা একাধিক Value-এর উপর। 

কোনো Operation করে একটি Result তৈরি করে। যেমন: 5 + 3 | এখানে, 5 এবং 3 = Operand | + = Operator | Result = 8
"""

# ============================================================
# 02_WhyOperatorsExists
# ============================================================
"""
Hardware Diagram of Opertors:
        Register A
             │
             ▼
         +---------+
         |         |
         |         |
         |   ALU   | ----------> Result Register
         |         |
         |         |
         +---------+
             ▲
             │
        Register B
        
"""
"""
Programming এ Operator কেন দরকার?

✔ সংখ্যা যোগ করতে
✔ সংখ্যা বিয়োগ করতে
✔ তুলনা করতে
✔ Logic তৈরি করতে
✔ Bit Level এ কাজ করতে
✔ Membership Check করতে
✔ Identity Check করতে

Operator ছাড়া Programming কল্পনাই করা যায় না।
"""

# ============================================================
# 03_Syntax
# ============================================================

"""
Arithmetic: + - * / // % **
Comparison: ==
Identity: is
Membership: in | not in
Logical: and | or
Bitwise: & | >> << 
"""

# ============================================================
# 04_Methods / Categories
# ============================================================

"""
Operators সাধারণত কয়েকটি ভাগে বিভক্ত।

1. Arithmetic Operator: + - * / // % **
2. Comparison Operator: ==
3. Identity Operator: is
4. Membership Operator: in | not in
5. Logical Operator: and | or
6. Bitwise Operator: & | >> << 
"""

# ============================================================
# 05_TimeComplexity
# ============================================================

"""
বেশিরভাগ Operator, Time Complexity = O(1)। কারণ CPU একটি নির্দিষ্ট সংখ্যক Instruction-এ এগুলো Execute করে। 
Exception: in operator
List এর ক্ষেত্রে x in list
Worst Case: O(n). কারণ পুরো List Search করতে হতে পারে।

Set: O(1)
Dictionary: O(1)
String: O(n)
"""

# ============================================================
# 06_InternalWorking
# ============================================================

"""
Python Operator দেখলে আসলে Special Method Call করে। 
+ = a + b = a.__add__(b)
- = a.__sub__(b)
* = a.__mul__(b)
/ = a.__truediv__(b)
// = a.__floordiv__(b)
% = a.__mod__(b)
** = a.__pow__(b)
== = a.__eq__(b)
is = id(a) == id(b)
in = obj.__contains__()
and = Short Circuit Evaluation
Bitwise = Binary Level এ কাজ করে।
"""

# ============================================================
# 07_Examples
# ============================================================

print("========== Arithmetic ==========")

a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

print()

print("========== Comparison ==========")

print(5 == 5)
print(5 == 6)

print()

print("========== Identity ==========")

x = [1, 2]
y = x
z = [1, 2]

print(x is y)
print(x is z)

print()

print("========== Membership ==========")

numbers = [10, 20, 30]

print(20 in numbers)
print(50 in numbers)

print(50 not in numbers)

print()

print("========== Logical ==========")

age = 25
salary = 50000

print(age > 18 and salary > 30000)
print(age > 30 or salary > 30000)

print()

print("========== Bitwise ==========")

a = 5
b = 3

print(a & b)
print(a | b)

print(a >> 1)
print(a << 1)

# ============================================================
# 08_CommonMistakes
# ============================================================

"""
১. = এবং == এক জিনিস না। = Assignment, == Comparison
২. is দিয়ে Value Compare করা। Wrong a = [1], b = [1], print(a is b). False | Correct | print(a == b) | True
৩. List এ in ব্যবহার করলে O(n) হতে পারে।
৪. / সবসময় Float Return করে। 10 / 2 = 5.0 অনেকে Integer আশা করে।
৫. ** এবং ^ এক জিনিস না। ^ - Bitwise XOR | ** Powers
"""

# ============================================================
# 09_Exercises
# ============================================================

"""
Exercise 1: ১০ এবং ৪ এর + - * / // % ** Print করো।
----------------------------
Exercise 2: Check করো 20 in [10,20,30]
----------------------------
Exercise 3: Difference বের করো, == is
----------------------------
Exercise 4: Binary বের করো 5 10 20 তারপর & | ব্যবহার করো।
----------------------------
Exercise 5:  Shift Operator ব্যবহার করো। 10 >> 1 | 10 << 2 Output Explain করো।
"""

# ============================================================
# 10_AIUsage
# ============================================================

# ============================================================
# 10_AIUsage
# ============================================================

"""
Python Operators AI Development-এ কোথায় ব্যবহৃত হয়? Operators হচ্ছে AI-এর সমস্ত Mathematical, Logical এবং
Decision Making-এর মূল ভিত্তি।

Machine Learning, Deep Learning, Computer Vision,
Natural Language Processing (NLP), Reinforcement Learning,
LLM এবং Robotics—সব জায়গাতেই Operators ব্যবহৃত হয়।
=========================================================
১. Data Preprocessing
=========================================================
Missing Value Check
if value == None:
    Fill Missing Value
Logical Operators ব্যবহার করে একাধিক Condition পরীক্ষা করা হয়।
---------------------------------------------------------

=========================================================
২. Feature Engineering
=========================================================
নতুন Feature তৈরি করতে Arithmetic Operators ব্যবহৃত হয়।
BMI = weight / (height ** 2)
Profit = income - expense
Age Group = age + 5
---------------------------------------------------------

=========================================================
৩. Machine Learning Training
=========================================================
Loss Function গণনা loss = prediction - target, 
Gradient Update weight = weight - learning_rate * gradient 
এখানে +, -, *, / সবচেয়ে বেশি ব্যবহৃত হয়।
---------------------------------------------------------

=========================================================
৪. Neural Networks
=========================================================
প্রতিটি Layer-এ Output = Weight * Input + Bias তারপর Activation Function প্রয়োগ হয়।

---------------------------------------------------------

=========================================================
৫. Model Evaluation
=========================================================
if accuracy >= 95:
    Save Model
else:
    Continue Training
Comparison Operators Model-এর Performance মূল্যায়নে ব্যবহৃত হয়।
---------------------------------------------------------

=========================================================
৬. Reinforcement Learning
=========================================================
if reward > best_reward:
    Update Policy
Reward Calculation-এ Arithmetic এবং Comparison Operators ব্যবহৃত হয়।

---------------------------------------------------------

=========================================================
৭. Computer Vision
=========================================================
if confidence >= 0.80:
    Draw Bounding Box
Object Detection-এ Comparison Operators গুরুত্বপূর্ণ।
---------------------------------------------------------

=========================================================
৮. Natural Language Processing (NLP)
=========================================================
if token != "<PAD>":
    Process Token
String Comparison এবং Logical Operators ব্যাপকভাবে ব্যবহৃত হয়।
---------------------------------------------------------

=========================================================
৯. LLM Agent
=========================================================
if tool_required:
    Call Tool
else:
    Generate Response
Agent-এর সিদ্ধান্ত গ্রহণে Logical Operators ব্যবহৃত হয়।

---------------------------------------------------------

=========================================================
১০. Robotics
=========================================================
if distance < 20:
    Stop Robot
else:
    Move Forward
Sensor Data বিশ্লেষণে Comparison Operators ব্যবহৃত হয়।
---------------------------------------------------------

=========================================================
১১. Computer Networks
=========================================================
Bitwise Operators: &, |, ^, <<, >>
IP Address
Subnet Mask
Permission Bits
Packet Processing,
এসব ক্ষেত্রে Bitwise Operators অত্যন্ত গুরুত্বপূর্ণ।
---------------------------------------------------------
=========================================================
১২. Operating Systems
=========================================================
File Permission
Memory Management
Process Flags
Interrupt Handling
এসব ক্ষেত্রে Bitwise Operators ব্যবহৃত হয়।
---------------------------------------------------------
=========================================================
১৩. AI Pipeline
=========================================================

Load Data
    ↓
Clean Data
    ↓
Create Features
    ↓
Train Model
    ↓
Calculate Loss
    ↓
Update Weights
    ↓
Evaluate
    ↓
Deploy

এই পুরো Pipeline-এ প্রতিটি ধাপে কোনো না কোনো ধরনের
Python Operator ব্যবহৃত হয়।
---------------------------------------------------------
শেখার Outcome,
✓ Mathematical Computation বুঝতে পারবে
✓ AI Model-এর Loss Calculation বুঝবে
✓ Weight Update বুঝবে
✓ Decision Making Logic বুঝবে
✓ Data Filtering করতে পারবে
✓ Bitwise Operators-এর বাস্তব ব্যবহার বুঝবে
✓ Machine Learning ও Deep Learning-এর Mathematical Foundation শক্ত হবে
অর্থাৎ, Python Operators আয়ত্ত করা মানে, AI-এর Mathematical ও Logical Foundation আয়ত্ত করা।
"""