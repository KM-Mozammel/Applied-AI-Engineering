"""
===========================================================
NOR Operator (NOT OR) - Logic
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
NOR (NOT OR) হলো Logic এর একটি গুরুত্বপূর্ণ
Logical Operator।

NOR এর পূর্ণরূপ:

NOT + OR


মূল নিয়ম:

OR Operation এর Result কে উল্টে দেয়।


অর্থাৎ:


OR True হলে NOR False হবে।

OR False হলে NOR True হবে।


Symbol:

↓


Formula:


P NOR Q = ¬(P ∨ Q)


Programming এ সরাসরি NOR Operator নেই।

ব্যবহার করা যায়:


not (P or Q)


"""


# ===========================================================
# 02_WhyThisConceptExistsInRelationToHistory
# ===========================================================

"""
বাস্তব জীবনে অনেক সময় এমন Condition প্রয়োজন হয়:

"যদি কোনো Condition সত্য না হয়"


OR Logic বলে:

যেকোনো একটি True হলে Result True।


কিন্তু NOR বলে:

কোনোটিই True না হলে Result True।


George Boole এর Boolean Algebra এ
NOR একটি গুরুত্বপূর্ণ Logical Operation।


Digital Electronics এ:

NOR Gate

একটি Universal Gate।


শুধুমাত্র NOR Gate ব্যবহার করে:


- NOT Gate
- OR Gate
- AND Gate


তৈরি করা যায়।


"""


# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
ধরি:


P = Door Open

Q = Window Open



OR Logic:


Door অথবা Window খোলা হলে:

Security Alert = True



NOR Logic:


কোনোটিই খোলা না থাকলে:

Security System Safe = True



Situation:


Door    Window     NOR Output


True    True          False


True    False         False


False   True          False


False   False         True



কারণ:

শুধুমাত্র সব Condition False হলে
NOR True দেয়।
"""


# ===========================================================
# 04_Definition
# ===========================================================

"""
Definition:


NOR হলো এমন একটি Logical Operator যা
OR Operation এর বিপরীত Output দেয়।


Mathematical Representation:


P ↓ Q


বা:


¬(P ∨ Q)



যেখানে:


P = First Proposition

Q = Second Proposition



Truth Rule:


শুধুমাত্র:


False OR False


হলে NOR True।


"""


# ===========================================================
# 05_Formula
# ===========================================================

"""
NOR Formula:


P NOR Q


= ¬(P ∨ Q)



Truth Table:


P       Q       P NOR Q


T       T          F


T       F          F


F       T          F


F       F          T



Binary:


1 NOR 1 = 0


1 NOR 0 = 0


0 NOR 1 = 0


0 NOR 0 = 1



"""


# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
ধরি:


P = User Active

Q = User Verified



প্রথমে OR:


P ∨ Q



Truth Table:


P       Q       OR


T       T       T

T       F       T

F       T       T

F       F       F



এখন NOT প্রয়োগ করি:


NOR = NOT(OR)



P       Q       NOR


T       T       F

T       F       F

F       T       F

F       F       T



তাই:

OR Output উল্টালে NOR পাওয়া যায়।
"""


# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
NOR Gate:


P ----\
       OR ---- NOT ---- Output
Q ----/



Step 1:


দুইটি Input OR Gate এ যায়।



Step 2:


OR Result তৈরি হয়।



Step 3:


NOT Gate Result Invert করে।



Example:


Input:


P = 0

Q = 0



OR:


0 OR 0 = 0



NOT:


NOT 0 = 1



Final:


NOR = 1



Digital Circuit এ:

NOR Gate একটি Universal Gate।


"""


# ===========================================================
# 08_Examples
# ===========================================================

"""
Example 1:


Python:


a = False

b = False


result = not(a or b)


Output:


True



Example 2:


Security System:


Motion Detected

OR

Door Open



NOR ব্যবহার করে:


কোনো Activity না থাকলে
System Ready।



Example 3:


Digital Electronics:


Memory Circuit

Control Circuit

Logic Controller


এ NOR Gate ব্যবহৃত হয়।



Example 4:


Boolean Logic:


NOT(P OR Q)


মানে:

P এবং Q দুইটিই False হতে হবে।


"""


# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
Mistake 1:


NOR কে NAND মনে করা।


NAND:


AND এর বিপরীত


NOR:


OR এর বিপরীত



Mistake 2:


Formula ভুল লেখা।


Wrong:


¬P ∨ Q


Correct:


¬(P ∨ Q)



Mistake 3:


NOR এ True কখন হয় ভুলে যাওয়া।


মনে রাখার নিয়ম:


NOR = None True


অর্থাৎ:

সব False হলে True।



Mistake 4:


OR এবং NOR এর Output একই মনে করা।


Difference:


OR:

F,F -> F


NOR:

F,F -> T


"""


# ===========================================================
# 10_Exercises
# ===========================================================

"""
Exercise 1:


Calculate:


False NOR False


Answer:


True



Exercise 2:


True NOR False


Answer:


False



Exercise 3:


Truth Table তৈরি করো:


P ↓ Q



Exercise 4:


Python:


x = False

y = True


result = not(x or y)


Output কী হবে?



Exercise 5:


Explain:


কেন NOR কে Universal Gate বলা হয়?


"""


# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
AI এবং Machine Learning এ NOR Logic এর ব্যবহার:


1. Neural Network Research


Logic Gate Simulation এ:


AND

OR

XOR

NAND

NOR


ব্যবহার করে Neural Network এর
ক্ষমতা বোঝা হয়।



2. Digital AI Hardware


AI Processor এবং Logic Chip এ
NOR Gate ব্যবহৃত হয়।



3. Rule Based AI


Example:


IF:


NOT(
    rain OR storm
)


THEN:


safe_condition = True



4. Feature Engineering


Example:


not(
    error OR failure
)


মানে:

কোনো Error নেই।



5. Decision System


Multiple Negative Condition
Handle করতে NOR ব্যবহার করা হয়।



Conclusion:


NOR হলো একটি Universal Logic Gate।

এটি ব্যবহৃত হয়:

- Computer Hardware
- Digital Circuit
- AI Hardware
- Boolean Logic
- Machine Learning Research


কারণ শুধুমাত্র NOR Gate দিয়েও
সম্পূর্ণ Logic System তৈরি করা সম্ভব।
"""


# ===========================================================
# End of NOR Operator
# ===========================================================