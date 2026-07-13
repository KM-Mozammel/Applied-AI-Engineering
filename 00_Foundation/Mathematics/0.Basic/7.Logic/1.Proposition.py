"""
===========================================================
Proposition (প্রস্তাবনা) - Logic
===========================================================

Structure:

01_Introduction
02_WhyThisConceptExistsInRelationToHistory
03_RealLifeIntuition
04_Definition
05_Formula
06_Derivation (How the formula comes)
07_InternalWorking / Visualization
08_Examples
09_CommonMistakes
10_Exercises
11_AIUsage (Machine Learning / AI)

===========================================================
"""


# ===========================================================
# 01_Introduction
# ===========================================================

"""
প্রস্তাবনা (Proposition) হলো Logic বা যুক্তিবিদ্যার একটি মৌলিক ধারণা।

Mathematics, Computer Science এবং Artificial Intelligence এ
যে কোনো statement সত্য (True) অথবা মিথ্যা (False) কিনা
তা নির্ধারণ করার জন্য Proposition ব্যবহার করা হয়।

উদাহরণ:

"Dhaka is the capital of Bangladesh."

এটি একটি Proposition কারণ এটি সত্য।

"2 + 2 = 5"

এটিও Proposition কারণ এটি মিথ্যা।

কিন্তু:

"How are you?"

এটি Proposition নয় কারণ এর True/False value নেই।
"""


# ===========================================================
# 02_WhyThisConceptExistsInRelationToHistory
# ===========================================================

"""
মানুষ যখন যুক্তি দিয়ে চিন্তা করা শুরু করে তখন প্রশ্ন আসে:

- কোন বক্তব্য সত্য?
- কোন বক্তব্য মিথ্যা?
- দুটি বক্তব্যের মধ্যে সম্পর্ক কী?

প্রাচীন গ্রিক দার্শনিক Aristotle প্রথম Formal Logic নিয়ে কাজ করেন।

পরবর্তীতে:

George Boole (1815-1864)
Boolean Logic তৈরি করেন।

এই Boolean Logic থেকেই আধুনিক:

- Computer Circuit
- Programming Condition
- Database Query
- Artificial Intelligence Logic

তৈরি হয়েছে।

Computer শুধুমাত্র True এবং False বুঝতে পারে।

Example:

if user_logged_in:
    show_dashboard()

এখানে:

user_logged_in = True/False

"""


# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
আমাদের দৈনন্দিন জীবনের অনেক বাক্য Proposition।

Example 1:

"আজ বৃষ্টি হচ্ছে।"

এটি হতে পারে:

True অথবা False


Example 2:

"আমি আজ অফিসে যাব।"

এটি ভবিষ্যৎ পরিকল্পনা।

Context অনুযায়ী এটি True অথবা False হতে পারে।


Non Proposition:

"দরজা বন্ধ করো।"

এটি একটি Command।

এর True/False value নেই।


"তুমি কোথায় যাচ্ছ?"

এটি Question।

এর True/False value নেই।
"""


# ===========================================================
# 04_Definition
# ===========================================================

"""
Definition:

যে কোনো Declarative Statement যার নির্দিষ্ট
একটি Truth Value আছে (True অথবা False),
তাকে Proposition বলে।

Truth Value:

True  -> 1
False -> 0


Mathematical Representation:

P = Statement

P ∈ {True, False}


Example:

P: "5 is greater than 3"

Truth Value:

P = True


Q: "10 is smaller than 2"

Truth Value:

Q = False

"""


# ===========================================================
# 05_Formula
# ===========================================================

"""
Basic Proposition এর কোনো numerical formula নেই।

কিন্তু Logical Operator ব্যবহার করে
নতুন Proposition তৈরি করা যায়।

Main Logical Operators:

1. NOT (¬)

P সত্য হলে NOT P মিথ্যা হবে।


2. AND (∧)

P এবং Q দুইটিই True হলে Result True।


3. OR (∨)

P অথবা Q যেকোনো একটি True হলে Result True।


4. Implication (→)

যদি P সত্য হয় তাহলে Q সত্য হবে।


5. Equivalent (↔)

P এবং Q একই Truth Value হলে True।


"""


# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
Logic formula Truth Table থেকে আসে।

ধরি:

P = "আজ বৃষ্টি হচ্ছে"

Q = "আমি ছাতা নিব"


AND Logic:

P ∧ Q


Meaning:

আজ বৃষ্টি হচ্ছে এবং আমি ছাতা নিব।


Truth Table:


P       Q       P ∧ Q

T       T       T

T       F       F

F       T       F

F       F       F


কারণ:

AND এ দুইটি condition সত্য হতে হবে।


"""


# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
Computer ভিতরে Logic কে Binary হিসেবে দেখে।

True  = 1

False = 0


Example:

P = True
Q = False


AND:

P ∧ Q

1 AND 0

Result:

0


Programming Example:


is_logged_in = True
has_permission = False


access = is_logged_in and has_permission


Result:

False


Computer processor এর Logic Gate
এই একই নিয়ম অনুসরণ করে।

"""


# ===========================================================
# 08_Examples
# ===========================================================

"""
Example 1:

Statement:

"10 is greater than 5"


Truth Value:

True



Example 2:

Statement:

"Python is a database"


Truth Value:

False



Example 3:

Programming:

age = 20


age >= 18


Result:

True


কারণ:

20 >= 18


"""


# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
Mistake 1:

Question কে Proposition ভাবা।


Wrong:

"What is your name?"


কারণ:

এর True/False value নেই।



Mistake 2:

Opinion কে Proposition ভাবা।


Example:

"Python is the best language."


এটি subjective opinion।



Mistake 3:

Incomplete sentence কে Proposition ভাবা।


Example:

"x + 5 = 10"


x এর value না জানা পর্যন্ত এটি Proposition নয়।



Mistake 4:

Truth value পরিবর্তন হতে পারে এমন statement ভুলভাবে ব্যবহার করা।


Example:

"It is hot."

স্থান এবং সময়ের উপর নির্ভর করে।
"""


# ===========================================================
# 10_Exercises
# ===========================================================

"""
Exercise 1:

নিচের কোনগুলো Proposition?


1. Bangladesh is in Asia.

2. Close the door.

3. 7 + 8 = 15

4. What time is it?


Answer:

1 -> Proposition

2 -> Not Proposition

3 -> Proposition

4 -> Not Proposition



Exercise 2:

Truth Value বের করো:


P:

20 > 10


Q:

5 == 8



Exercise 3:

Truth Table তৈরি করো:

P AND Q

P OR Q

NOT P

"""


# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
AI এবং Machine Learning এ Proposition এর ব্যবহার:

1. Decision Making

Example:

if probability > threshold:

    make_decision()


এখানে:

probability > threshold

একটি Proposition।



2. Neural Network Output


Model Output:

prediction = True/False


Example:

Email Spam Detection:


"Email is spam"


True / False Proposition।



3. Expert System


Rules:


IF fever = True

AND

cough = True


THEN

possible_flu = True



4. Reinforcement Learning


Agent সিদ্ধান্ত নেয়:

"Action is good?"

True অথবা False হিসেবে বিচার করা হয়।



5. Database Query


SQL:

SELECT *

FROM users

WHERE age >= 18;


age >= 18

একটি Logical Proposition।



Conclusion:

Proposition হলো Logic এর ভিত্তি।

এটি Mathematics থেকে শুরু করে:

- Programming
- Computer Architecture
- Database
- Machine Learning
- Artificial Intelligence

সব জায়গায় ব্যবহৃত হয়।
"""


# ===========================================================
# End of Proposition
# ===========================================================