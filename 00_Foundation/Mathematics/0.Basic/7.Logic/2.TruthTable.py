"""
===========================================================
Truth Table (সত্য সারণি) - Logic
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
Truth Table (সত্য সারণি) হলো Logic এর এমন একটি টেবিল
যেখানে Logical Expression এর সব সম্ভাব্য Input এবং
তার Output দেখানো হয়।

যেকোনো Logical Operation:

- AND
- OR
- NOT
- XOR
- NAND
- NOR
- Implication

এর আচরণ বোঝার জন্য Truth Table ব্যবহার করা হয়।

Computer Science এবং Digital Electronics এ
Truth Table অত্যন্ত গুরুত্বপূর্ণ।

"""


# ===========================================================
# 02_WhyThisConceptExistsInRelationToHistory
# ===========================================================

"""
মানুষ যখন Formal Logic তৈরি করতে শুরু করে,
তখন শুধুমাত্র কথার মাধ্যমে Logic বিশ্লেষণ করা কঠিন হয়ে যায়।

তাই প্রতিটি Logical Statement এর:

- Possible Input
- Result

একটি নির্দিষ্ট নিয়মে দেখানোর প্রয়োজন হয়।

George Boole এর Boolean Algebra
এবং পরবর্তীতে Claude Shannon এর Digital Circuit Theory
Truth Table কে Computer Science এর মূল ভিত্তি করে তোলে।


Computer Circuit এ:

ON  = True  = 1

OFF = False = 0


Processor এর Logic Gate গুলো Truth Table অনুসরণ করে কাজ করে।
"""


# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
ধরি:

P = আজ বৃষ্টি হচ্ছে

Q = আমি ছাতা নিয়েছি


আমরা জানতে চাই:

"P এবং Q দুটোই সত্য কিনা"


সম্ভাবনা:


আজ বৃষ্টি হচ্ছে | ছাতা আছে | Result

True            | True      | True

True            | False     | False

False           | True      | False

False           | False     | False


এটাই Truth Table এর ধারণা।

সব সম্ভাব্য পরিস্থিতি লিখে
শেষে সিদ্ধান্ত বের করা হয়।
"""


# ===========================================================
# 04_Definition
# ===========================================================

"""
Definition:

Truth Table হলো এমন একটি টেবিল যেখানে
একটি Logical Expression এর সকল সম্ভাব্য
Truth Value Combination এবং তাদের Output দেখানো হয়।


একটি Variable এর দুইটি Value:


True  (T)

False (F)


n সংখ্যক Variable থাকলে:

Total Combination = 2^n


Example:

1 Variable:

2¹ = 2 Combination


2 Variable:

2² = 4 Combination


3 Variable:

2³ = 8 Combination

"""


# ===========================================================
# 05_Formula
# ===========================================================

"""
Truth Table Combination Formula:


Number of Rows:

Rows = 2^n


যেখানে,

n = Number of Variables


Example:


Variables:

P, Q


n = 2


Rows:

2² = 4


তাই Truth Table:


P       Q

T       T

T       F

F       T

F       F



"""


# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
ধরি আমাদের দুইটি Variable আছে:

P এবং Q


প্রতিটি Variable এর দুইটি অবস্থা:


P:

True

False


Q:

True

False



Possible Combination:


P=True,  Q=True


P=True,  Q=False


P=False, Q=True


P=False, Q=False



মোট:


2 × 2 = 4


অর্থাৎ:

2² = 4


এই কারণেই:

n Variable হলে:

2^n rows প্রয়োজন হয়।
"""


# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
Computer ভিতরে Truth Table কে Binary হিসেবে ব্যবহার করে।


Example:


AND Gate:


Input:

P     Q


1     1

1     0

0     1

0     0



Output:


1

0

0

0



Logic Circuit:


P ----\
       AND ---- Output
Q ----/


যখন দুইটি Input High (1)
তখন Output High (1)



Programming এ:


if condition1 and condition2:

    execute()


condition1 এবং condition2
Truth Table অনুসরণ করে।


"""


# ===========================================================
# 08_Examples
# ===========================================================

"""
Example 1:

AND Truth Table


P       Q       P AND Q

T       T          T

T       F          F

F       T          F

F       F          F



Example 2:

OR Truth Table


P       Q       P OR Q

T       T          T

T       F          T

F       T          T

F       F          F



Example 3:

NOT Truth Table


P       NOT P


T          F

F          T


"""


# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
Mistake 1:

Rows এর সংখ্যা ভুল করা।


Wrong:

3 variables এর জন্য 6 rows


Correct:


2³ = 8 rows



Mistake 2:

AND এবং OR এর পার্থক্য ভুল করা।


AND:

সব True হলে True


OR:

একটি True হলেই True



Mistake 3:

NOT operator এ True/False উল্টাতে ভুল করা।



Mistake 4:

Input এবং Output গুলিয়ে ফেলা।


"""


# ===========================================================
# 10_Exercises
# ===========================================================

"""
Exercise 1:

Truth Table তৈরি করো:


P AND Q


Exercise 2:


Truth Table তৈরি করো:


P OR Q


Exercise 3:


তিনটি Variable এর জন্য
কতটি Row প্রয়োজন?


Answer:


2³ = 8


Exercise 4:


NOT(P AND Q)

এর Truth Table তৈরি করো।


"""


# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
AI এবং Machine Learning এ Truth Table এর ব্যবহার:


1. Decision Tree


Decision Tree:

Feature Condition


Example:


Age > 18

AND

Income > 50000


Decision:

Loan Approved


এই Condition গুলো Logical Table হিসেবে দেখা যায়।



2. Neural Network Activation


Neuron Output:

True / False


Example:


Prediction:

Spam = True



3. Rule Based AI


Example:


IF:

temperature > 38

AND

cough = True


THEN:

Disease possibility = True



4. Feature Engineering


Boolean Features:


is_student = True

has_job = False



5. Digital AI Hardware


AI Processor এবং Computer Chip
Logic Gate এর মাধ্যমে কাজ করে।



Conclusion:


Truth Table হলো Logic এর
একটি Visual Representation।

এটি বুঝলে:

- Programming Condition
- Boolean Logic
- Computer Hardware
- AI Decision System

সহজে বোঝা যায়।
"""


# ===========================================================
# End of Truth Table
# ===========================================================