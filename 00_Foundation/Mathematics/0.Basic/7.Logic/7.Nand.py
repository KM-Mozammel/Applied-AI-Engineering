"""
===========================================================
NAND Operator (NOT AND) - Logic
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
NAND (NOT AND) হলো Logic এর একটি গুরুত্বপূর্ণ
Universal Logical Operator।

NAND এর পূর্ণরূপ:

NOT + AND


মূল নিয়ম:

AND এর Result কে উল্টে দেয়।


অর্থাৎ:


AND True হলে NAND False হবে।

AND False হলে NAND True হবে।


Symbol:

↑


Formula:


P NAND Q = ¬(P ∧ Q)


Programming এ সরাসরি NAND Operator নেই,
তবে ব্যবহার করা যায়:


not (P and Q)



"""


# ===========================================================
# 02_WhyThisConceptExistsInRelationToHistory
# ===========================================================

"""
Computer Science এ এমন একটি Logic Gate প্রয়োজন ছিল
যেটি দিয়ে সব ধরনের Logic Circuit তৈরি করা যায়।


NAND Gate একটি Universal Gate।


শুধুমাত্র NAND Gate ব্যবহার করে:


- AND Gate
- OR Gate
- NOT Gate


সব তৈরি করা যায়।


Digital Electronics এবং Computer Processor
Design এ NAND Gate অত্যন্ত গুরুত্বপূর্ণ।


Claude Shannon এর Boolean Logic ভিত্তিক
Digital Circuit Theory তে NAND গুরুত্বপূর্ণ ভূমিকা রাখে।


"""


# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
ধরি:


P = Machine Running

Q = Safety Lock Enabled



AND Logic:


Machine চলবে যদি:

Machine Running

AND

Safety Lock Enabled



NAND Logic:


"এই দুইটি Condition একসাথে True হলে
Result False হবে।"


Situation:


Machine   Lock       NAND Output


True      True          False


True      False         True


False     True          True


False     False         True



কারণ:

শুধুমাত্র দুইটি Condition True হলে
NAND False দেয়।
"""


# ===========================================================
# 04_Definition
# ===========================================================

"""
Definition:


NAND হলো এমন একটি Logical Operator যা
AND Operation এর বিপরীত Output দেয়।


Mathematical Representation:


P ↑ Q


বা


¬(P ∧ Q)



যেখানে:


P = First Proposition

Q = Second Proposition



Truth Rule:


শুধুমাত্র:

True AND True


হলে NAND False।


"""


# ===========================================================
# 05_Formula
# ===========================================================

"""
NAND Formula:


P NAND Q


= ¬(P ∧ Q)



Truth Table:


P       Q       P NAND Q


T       T          F


T       F          T


F       T          T


F       F          T



Binary:


1 NAND 1 = 0


1 NAND 0 = 1


0 NAND 1 = 1


0 NAND 0 = 1



"""


# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
ধরি:


P = User Logged In

Q = Password Correct



AND:


P ∧ Q


শুধুমাত্র:

Logged In এবং Password Correct

হলে True হবে।



Truth:


P       Q       AND


T       T       T

T       F       F

F       T       F

F       F       F



এখন NOT প্রয়োগ করি:


NAND = NOT(AND)



P       Q       NAND


T       T       F

T       F       T

F       T       T

F       F       T



তাই:

AND এর Output উল্টালে NAND পাওয়া যায়।
"""


# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
NAND Gate:


P ----\
       AND ---- NOT ---- Output
Q ----/



Step 1:


Input দুইটি AND Gate এ যায়।



Step 2:


AND Result পাওয়া যায়।



Step 3:


NOT Gate Result Invert করে।



Example:


Input:


P = 1

Q = 1



AND:


1 AND 1 = 1



NOT:


NOT 1 = 0



Final:


NAND = 0



Digital Circuit এ NAND Gate
সবচেয়ে বেশি ব্যবহৃত Gate গুলোর একটি।


"""


# ===========================================================
# 08_Examples
# ===========================================================

"""
Example 1:


Python:


a = True

b = True


result = not (a and b)


Output:


False



Example 2:


Security System:


Door Open

AND

Alarm Activated



NAND ব্যবহার করে:

দুইটি Condition একসাথে True হলে
Alert বন্ধ করা।



Example 3:


Computer Hardware:


Memory Circuit

Processor Circuit

Control Logic


এ NAND Gate ব্যবহৃত হয়।



"""


# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
Mistake 1:


NAND কে OR মনে করা।


NAND:

শুধুমাত্র True AND True হলে False।



Mistake 2:


Formula ভুল লেখা।


Wrong:


¬P ∧ Q



Correct:


¬(P ∧ Q)



Mistake 3:


AND এবং NAND এর Output একই ভাবা।



Difference:


AND:


T,T -> T


NAND:


T,T -> F



Mistake 4:


NAND এর Universal Property না জানা।


"""


# ===========================================================
# 10_Exercises
# ===========================================================

"""
Exercise 1:


Calculate:


True NAND True


Answer:


False



Exercise 2:


True NAND False


Answer:


True



Exercise 3:


Truth Table তৈরি করো:


P ↑ Q



Exercise 4:


Python:


x = False

y = True


result = not(x and y)


Output কী হবে?



Exercise 5:


Explain:


কেন NAND কে Universal Gate বলা হয়?


"""


# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
AI এবং Machine Learning এ NAND Logic এর ব্যবহার:


1. Neural Network Research


XOR Problem সমাধানের জন্য
Multi Layer Network প্রয়োজন হয়।

Logic Gate Simulation এ:

NAND, AND, OR

ব্যবহার করা হয়।



2. Digital AI Hardware


AI Accelerator Chip এবং Processor এ
NAND Gate ভিত্তিক Circuit থাকে।



3. Rule Based System


Example:


NOT(
    fever AND cough
)


এই ধরনের Complex Rule তৈরি করা যায়।



4. Boolean Feature Engineering


Example:


not(
    feature_A and feature_B
)


Feature Combination তৈরি করতে ব্যবহার হয়।



5. Logic Simulation


AI Agent এর Decision Rule
Test করার জন্য NAND ব্যবহার করা হয়।



Conclusion:


NAND হলো Logic এর সবচেয়ে গুরুত্বপূর্ণ
Universal Operator গুলোর একটি।

এটি ব্যবহৃত হয়:

- Computer Hardware
- Digital Circuit
- AI Chip
- Neural Network Research
- Logic Design

কারণ শুধুমাত্র NAND দিয়ে
সম্পূর্ণ Logic System তৈরি করা সম্ভব।
"""


# ===========================================================
# End of NAND Operator
# ===========================================================