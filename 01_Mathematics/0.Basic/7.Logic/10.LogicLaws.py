"""
===========================================================
Logic Laws (যুক্তির সূত্রসমূহ) - Logic
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
Logic Laws হলো কিছু নির্দিষ্ট নিয়ম
যেগুলো ব্যবহার করে Logical Expression
সরল (Simplify) করা যায়।

যেমন:

Mathematics এ:

x + 0 = x


তেমনি Logic এ:


P AND True = P


Logic Laws ব্যবহার করে:

- Complex Logic সহজ করা
- Circuit Design করা
- Programming Condition Optimize করা

যায়।


প্রধান Logic Laws:


1. Identity Law

2. Null Law

3. Idempotent Law

4. Complement Law

5. Double Negation Law

6. Commutative Law

7. Associative Law

8. Distributive Law

9. Absorption Law

10. De Morgan's Law


"""


# ===========================================================
# 02_WhyThisConceptExistsInRelationToHistory
# ===========================================================

"""
Logic Expression বড় হলে মানুষের জন্য
সরাসরি বিশ্লেষণ করা কঠিন হয়ে যায়।


Example:


(A AND B) OR (A AND NOT B)


এই ধরনের Expression সহজ করার জন্য
Logic Laws প্রয়োজন হয়।


George Boole এর Boolean Algebra থেকে
এই Law গুলো তৈরি হয়।


পরবর্তীতে:

- Digital Circuit Optimization
- Computer Architecture
- Programming Compiler

এ Logic Laws ব্যবহার শুরু হয়।


আজকের Computer Hardware এর
Circuit Simplification এ Logic Laws
অত্যন্ত গুরুত্বপূর্ণ।


"""


# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
বাস্তব উদাহরণ:


ধরি:


একজন User Access পাবে যদি:


Admin হয়

OR

Manager হয়



Expression:


Admin OR Manager



যদি একই Condition বারবার থাকে:


(Admin OR Manager) AND Admin


এটি Logic Law ব্যবহার করে
সহজ করা যায়।


যেমন Mathematics এ
একই মানের Expression সহজ করি,
তেমনি Logic Expression সহজ করি।
"""


# ===========================================================
# 04_Definition
# ===========================================================

"""
Definition:


Logic Laws হলো এমন কিছু Mathematical Rule
যেগুলো Logical Expression পরিবর্তন না করে
তার সরল রূপ বের করতে সাহায্য করে।


অর্থাৎ:


Original Expression


=

Equivalent Expression



যেখানে দুইটির Truth Value একই থাকে।



"""


# ===========================================================
# 05_Formula
# ===========================================================

"""
===========================================================
1. Identity Law
===========================================================


P OR False


P ∨ 0 = P



P AND True


P ∧ 1 = P



Example:


A + 0 = A


A · 1 = A



===========================================================
2. Null Law
===========================================================


P OR True


P ∨ 1 = 1



P AND False


P ∧ 0 = 0



===========================================================
3. Idempotent Law
===========================================================


P OR P


P ∨ P = P



P AND P


P ∧ P = P



===========================================================
4. Complement Law
===========================================================


P OR NOT P


P ∨ ¬P = 1



P AND NOT P


P ∧ ¬P = 0



===========================================================
5. Double Negation Law
===========================================================


¬(¬P) = P



===========================================================
6. Commutative Law
===========================================================


P ∨ Q = Q ∨ P


P ∧ Q = Q ∧ P



===========================================================
7. Associative Law
===========================================================


(P ∨ Q) ∨ R

=

P ∨ (Q ∨ R)



(P ∧ Q) ∧ R

=

P ∧ (Q ∧ R)



===========================================================
8. Distributive Law
===========================================================


P ∧ (Q ∨ R)


=

(P ∧ Q) ∨ (P ∧ R)



P ∨ (Q ∧ R)


=

(P ∨ Q) ∧ (P ∨ R)



===========================================================
9. Absorption Law
===========================================================


P ∨ (P ∧ Q)


=

P



P ∧ (P ∨ Q)


=

P



===========================================================
10. De Morgan's Law
===========================================================


NOT(P AND Q)


=

NOT P OR NOT Q



¬(P ∧ Q)


=

¬P ∨ ¬Q



NOT(P OR Q)


=

NOT P AND NOT Q



¬(P ∨ Q)


=

¬P ∧ ¬Q


"""


# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
Example:

Prove:


P ∨ (P ∧ Q) = P



Case 1:


P = True


Left Side:


True OR (True AND Q)



True AND Q:


Q



True OR Q:


True



Right Side:


P = True



Both Equal.



Case 2:


P = False


Left Side:


False OR (False AND Q)



False AND Q:


False



False OR False:


False



Right Side:


P = False



দুই ক্ষেত্রেই Result একই।

তাই:


P ∨ (P ∧ Q)


=

P


এটি Absorption Law।
"""


# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
Computer Logic Circuit এ
Logic Laws ব্যবহার করে Circuit ছোট করা হয়।


Before:


A ----\
       AND ----\
B ----/         OR ---- Output
               /
A ------------/



এখানে অনেক Gate প্রয়োজন।


Logic Simplification করার পর:


A ---- Output



কম Gate মানে:


- কম Hardware
- কম Power Consumption
- দ্রুত Processing


Compiler এবং Hardware Optimizer
এই ধরনের Simplification ব্যবহার করে।
"""


# ===========================================================
# 08_Examples
# ===========================================================

"""
Example 1:


Simplify:


A AND True



Solution:


A ∧ 1


Identity Law:


= A



--------------------------------


Example 2:


Simplify:


A OR NOT A



Solution:


A ∨ ¬A


Complement Law:


= 1



--------------------------------


Example 3:


Simplify:


NOT(NOT A)



Solution:


¬(¬A)


Double Negation:


= A



--------------------------------


Example 4:


Programming:


if True and condition:


এটি simplify হয়ে:


if condition:


হয়।
"""


# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
Mistake 1:


Boolean Algebra এর নিয়ম
সাধারণ Algebra এর মতো ভাবা।


Example:


Boolean:


1 + 1 = 1



সাধারণ Math:


1 + 1 = 2



Mistake 2:


AND এবং OR Law গুলিয়ে ফেলা।



Mistake 3:


De Morgan's Law ভুল প্রয়োগ করা।


Wrong:


¬(A AND B)


=

¬A AND ¬B



Correct:


¬A OR ¬B



Mistake 4:


Expression Simplify করার সময়
Operator Priority না মানা।


"""


# ===========================================================
# 10_Exercises
# ===========================================================

"""
Exercise 1:


Simplify:


A OR 0



Answer:


A



Exercise 2:


Simplify:


A AND 1



Answer:


A



Exercise 3:


Simplify:


A OR A



Answer:


A



Exercise 4:


Simplify:


A AND NOT A



Answer:


0



Exercise 5:


Apply De Morgan:


NOT(A OR B)



Answer:


NOT A AND NOT B



Exercise 6:


Simplify:


A OR (A AND B)



"""


# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
AI এবং Machine Learning এ Logic Laws এর ব্যবহার:


1. Decision Rule Optimization


AI Rule:


(A AND B) OR (A AND NOT B)


Simplify করলে:


A


হতে পারে।


কম Rule মানে:

দ্রুত Decision।



2. Decision Tree Optimization


অপ্রয়োজনীয় Condition বাদ দিতে
Logic Law ব্যবহার করা হয়।



3. Neural Network Logic Research


XOR Problem এবং Boolean Function
বোঝার জন্য Logic Laws ব্যবহার করা হয়।



4. Feature Engineering


Complex Boolean Feature
Simplify করা হয়।



5. Hardware Optimization


AI Processor এবং Neural Chip
কম Circuit এ তৈরি করতে Logic Law ব্যবহার করা হয়।



Conclusion:


Logic Laws হলো Logical Reasoning এর
Mathematical Foundation।

এগুলো ব্যবহার হয়:


- Programming
- Digital Electronics
- Compiler Optimization
- Machine Learning
- Artificial Intelligence


Complex Logic কে সহজ এবং কার্যকর করার জন্য।
"""


# ===========================================================
# End of Logic Laws
# ===========================================================