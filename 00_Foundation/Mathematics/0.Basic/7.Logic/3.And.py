"""
===========================================================
AND Operator (Logical AND) - Logic
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
AND (Logical AND) হলো Logic এর একটি মৌলিক Logical Operator।

AND ব্যবহার করে দুই বা তার বেশি Proposition এর
মধ্যে সম্পর্ক নির্ধারণ করা হয়।

AND এর মূল নিয়ম:

সবগুলো Condition True হলে Result True হবে।

Symbol:

AND = ∧

Programming এ:

and


Example:

P AND Q


যদি:

P = True

Q = True


তাহলে:

P ∧ Q = True


"""


# ===========================================================
# 02_WhyThisConceptExistsInRelationToHistory
# ===========================================================

"""
মানুষের বাস্তব জীবনে অনেক সিদ্ধান্তের জন্য
একাধিক শর্ত পূরণ করতে হয়।

যেমন:

"আমি পরীক্ষায় পাশ করবো যদি:

- Attendance ভালো হয়
- Exam ভালো হয়"


দুইটি Condition একসাথে সত্য হতে হবে।

এই ধরনের Multiple Condition handle করার জন্য
AND Logic তৈরি হয়।


George Boole এর Boolean Algebra এ
AND একটি মৌলিক Operation হিসেবে ব্যবহৃত হয়।


Digital Computer এ:

AND Gate

এর মাধ্যমে Logical AND বাস্তবায়ন করা হয়।


"""


# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
ধরি:


P = আমার কাছে Ticket আছে

Q = আমার কাছে ID Card আছে


আমি অনুষ্ঠানে প্রবেশ করতে পারবো যদি:

Ticket AND ID Card থাকে।


Situation:


Ticket   ID Card    Entry


True     True       Yes

True     False      No

False    True       No

False    False      No



কারণ:

দুইটি শর্তই পূরণ করতে হবে।


"""


# ===========================================================
# 04_Definition
# ===========================================================

"""
Definition:

AND হলো একটি Logical Operator যা দুই বা তার বেশি
Proposition এর সবগুলো True হলে True Return করে।


Mathematical Representation:


P ∧ Q


যেখানে:

P = First Proposition

Q = Second Proposition


Truth Value:


True  ∧ True  = True

True  ∧ False = False

False ∧ True  = False

False ∧ False = False



"""


# ===========================================================
# 05_Formula
# ===========================================================

"""
AND Formula:


P ∧ Q


Truth Table:


P       Q       P ∧ Q


T       T          T

T       F          F

F       T          F

F       F          F



Binary Representation:


1 AND 1 = 1

1 AND 0 = 0

0 AND 1 = 0

0 AND 0 = 0


"""


# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
ধরি:


P = আজ বৃষ্টি হচ্ছে

Q = আমি ছাতা নিয়েছি


আমরা চাই:


"আজ বৃষ্টি হচ্ছে এবং আমি ছাতা নিয়েছি"


এটি শুধুমাত্র তখন সত্য হবে যখন:


বৃষ্টি হচ্ছে = True

ছাতা আছে = True


Case 1:

P = True

Q = True


Result = True



Case 2:

P = True

Q = False


ছাতা নেই,

তাই Result = False



Case 3:

P = False

Q = True


বৃষ্টি নেই,

তাই Statement False



Case 4:

P = False

Q = False


False



তাই AND এর নিয়ম:

সব Input True হলে Output True।
"""


# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
AND Gate:

Digital Circuit:


P ----\
       AND ---- Output
Q ----/


Input:

P = 1

Q = 1


Output:

1



অন্য সব ক্ষেত্রে:


1 AND 0 = 0

0 AND 1 = 0

0 AND 0 = 0



Computer Processor এ:

Electrical Signal:

HIGH = 1

LOW  = 0


AND Gate দুইটি Signal যাচাই করে।


Programming Example:


is_logged_in = True

has_permission = True


if is_logged_in and has_permission:

    access = True


"""


# ===========================================================
# 08_Examples
# ===========================================================

"""
Example 1:


Password এবং Username সঠিক হলে Login হবে।


username_correct = True

password_correct = True


username_correct and password_correct


Output:

True



Example 2:


Machine Learning:


condition1:

age > 18


condition2:

income > 30000



Decision:


age > 18 AND income > 30000



Example 3:


Python:


temperature = 38

has_fever = temperature > 37


has_fever and cough



"""


# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
Mistake 1:

AND কে OR এর মতো ব্যবহার করা।


Wrong:

একটি Condition True হলেই AND True হবে।


Correct:

সব Condition True হতে হবে।



Mistake 2:

Truth Table ভুল মনে রাখা।


AND:


Only:

True AND True = True



Mistake 3:

Programming এ:

& এবং and এক মনে করা।


Python:


and = Logical Operator


& = Bitwise Operator



Mistake 4:

Operator precedence ভুল করা।


Example:


A and B or C


সঠিকভাবে Parentheses ব্যবহার করা ভালো।


"""


# ===========================================================
# 10_Exercises
# ===========================================================

"""
Exercise 1:


Truth Value বের করো:


True AND True


Answer:

True



Exercise 2:


False AND True


Answer:

False



Exercise 3:


Truth Table তৈরি করো:


P ∧ Q



Exercise 4:


বাস্তব উদাহরণ:


একজন Student Scholarship পাবে যদি:


CGPA > 3.5

AND

Attendance > 80%


কখন Scholarship পাওয়া যাবে?



Exercise 5:


Python এ:


is_student = True

has_id = False


result = is_student and has_id


Output কী হবে?


"""


# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
AI এবং Machine Learning এ AND Logic এর ব্যবহার:


1. Feature Combination


Example:


Feature 1:

Age > 18


Feature 2:

Income > 50000



Decision:


Approve Loan =

Age > 18 AND Income > 50000



2. Rule Based AI


IF:

temperature_high

AND

cough_present


THEN:

possible_fever



3. Neural Network


Neuron Activation এ:

একাধিক Feature একসাথে
Decision এ প্রভাব ফেলে।



4. Data Filtering


Database:


SELECT *

FROM users

WHERE age >= 18

AND

active = True;



5. Classification


Multiple conditions ব্যবহার করে
Class Prediction করা হয়।



Conclusion:


AND হলো Logic এর একটি ভিত্তি।

এটি ব্যবহার হয়:

- Programming
- Digital Circuit
- Database
- Machine Learning
- Artificial Intelligence

সব জায়গায়।
"""


# ===========================================================
# End of AND Operator
# ===========================================================