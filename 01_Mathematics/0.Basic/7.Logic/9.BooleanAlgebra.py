"""
===========================================================
Boolean Algebra (বুলিয়ান অ্যালজেব্রা) - Logic
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
Boolean Algebra হলো এমন একটি Mathematical System
যেখানে Variable এর Value শুধুমাত্র দুইটি হতে পারে:


True  (1)

False (0)



এটি সাধারণ Algebra থেকে আলাদা।

সাধারণ Algebra:

x = 5

y = 10



Boolean Algebra:


A = True

B = False



Boolean Algebra ব্যবহার করা হয়:


- Computer Logic
- Digital Circuit
- Programming Condition
- Database Query
- Artificial Intelligence


এর ভিত্তি হলো:

Logic এবং Binary System।
"""


# ===========================================================
# 02_WhyThisConceptExistsInRelationToHistory
# ===========================================================

"""
1800 সালের দিকে Mathematics এ Logic কে
Formal System হিসেবে তৈরি করার প্রয়োজন হয়।


George Boole (1815-1864)

Boolean Algebra তৈরি করেন।


তার কাজের মূল ধারণা ছিল:


Logical Statement কে Mathematical Expression
হিসেবে প্রকাশ করা।



পরবর্তীতে:

Claude Shannon দেখান যে Boolean Algebra ব্যবহার করে
Electrical Circuit Design করা সম্ভব।


এর ফলে তৈরি হয়:


- Computer Processor
- Memory Circuit
- Digital Electronics


আজকের Computer এর ভিতরের Logic
Boolean Algebra এর উপর ভিত্তি করে কাজ করে।
"""


# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
আমাদের বাস্তব জীবনে অনেক সিদ্ধান্ত
দুইটি অবস্থার উপর নির্ভর করে।


Example:


Light Switch:


ON  = 1

OFF = 0



Door:


Open  = True

Close = False



Security System:


Door Open

AND

Password Correct



এই Condition গুলো Boolean Algebra দিয়ে
প্রকাশ করা যায়।


Example:


door_open = True

password_correct = True


access = door_open AND password_correct


"""


# ===========================================================
# 04_Definition
# ===========================================================

"""
Definition:


Boolean Algebra হলো এমন একটি Algebraic System
যেখানে Variable এর মান শুধুমাত্র:


0 অথবা 1


হয় এবং Logical Operation ব্যবহার করে
Expression তৈরি করা হয়।


Main Boolean Operators:


1. AND

Symbol:

·


Example:

A · B



2. OR

Symbol:

+


Example:

A + B



3. NOT

Symbol:

'


Example:


A'


"""


# ===========================================================
# 05_Formula
# ===========================================================

"""
Boolean Algebra এর প্রধান সূত্র:


-------------------------------
1. Identity Law
-------------------------------


A + 0 = A


A · 1 = A



-------------------------------
2. Null Law
-------------------------------


A + 1 = 1


A · 0 = 0



-------------------------------
3. Idempotent Law
-------------------------------


A + A = A


A · A = A



-------------------------------
4. Complement Law
-------------------------------


A + A' = 1


A · A' = 0



-------------------------------
5. Double Negation Law
-------------------------------


(A')' = A



-------------------------------
6. Commutative Law
-------------------------------


A + B = B + A


A · B = B · A



-------------------------------
7. Associative Law
-------------------------------


A + (B + C)

=

(A + B) + C



A · (B · C)

=

(A · B) · C



-------------------------------
8. Distributive Law
-------------------------------


A(B + C)

=

AB + AC



A + BC

=

(A+B)(A+C)


"""


# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
Example:


Prove:


A + A' = 1



Case 1:


A = 1



A' = 0



A + A'


=

1 + 0


=

1



Case 2:


A = 0



A' = 1



A + A'


=

0 + 1


=

1



তাই:


A + A' = 1



অর্থাৎ:

একটি Boolean Variable এবং তার বিপরীত
সবসময় True দেয়।
"""


# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
Computer ভিতরে Boolean Algebra
Binary Signal হিসেবে কাজ করে।


Example:


A = 1

B = 0



AND:


A · B


1 · 0


=

0



OR:


A + B


1 + 0


=

1



NOT:


A'


1'


=

0



Digital Circuit:


AND Gate

OR Gate

NOT Gate


সব Boolean Algebra অনুসরণ করে।



CPU এর ভিতরের কোটি কোটি Transistor
এই Boolean Logic ব্যবহার করে।
"""


# ===========================================================
# 08_Examples
# ===========================================================

"""
Example 1:


Login System:


A = Username Correct


B = Password Correct



Login:


A · B



দুইটি True হলে Login হবে।



Example 2:


Search System:


A = Keyword Match


B = Category Match



Search Result:


A + B



Example 3:


Python:


is_admin = True

is_staff = False



access = is_admin or is_staff



Boolean Expression:


A + B


"""


# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
Mistake 1:


Boolean Algebra কে সাধারণ Algebra ভাবা।


Boolean এ:


1 + 1 = 1


কিন্তু সাধারণ Algebra এ:


1 + 1 = 2



Mistake 2:


AND এবং OR এর Symbol গুলিয়ে ফেলা।



AND:

·


OR:

+



Mistake 3:


Complement ভুল করা।


A + A' = 1


A · A' = 0



Mistake 4:


Binary Value এবং Boolean Value
একইভাবে না বোঝা।


True = 1


False = 0


"""


# ===========================================================
# 10_Exercises
# ===========================================================

"""
Exercise 1:


Simplify:


A + 0



Answer:


A



Exercise 2:


Simplify:


A · 1



Answer:


A



Exercise 3:


Simplify:


A + A'



Answer:


1



Exercise 4:


Simplify:


A · A'



Answer:


0



Exercise 5:


Boolean Expression তৈরি করো:


একজন User Access পাবে যদি:


Logged In

AND

Verified


"""


# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
AI এবং Machine Learning এ Boolean Algebra এর ব্যবহার:


1. Feature Engineering


Binary Feature:


is_student = 1

has_job = 0



Features Combine:


is_student AND has_job



2. Decision Tree


Decision Tree এর Condition:


age > 18

AND

income > threshold



Boolean Rule হিসেবে কাজ করে।



3. Neural Network


Activation Function এর Output
অনেক সময়:


0 অথবা 1


হিসেবে দেখা হয়।



4. Digital AI Hardware


AI Chip এবং GPU Circuit
Boolean Logic এর উপর ভিত্তি করে তৈরি।



5. Rule Based AI


Example:


IF:


(A AND B) OR C


THEN:


Decision



Conclusion:


Boolean Algebra হলো:

- Computer Science
- Programming
- Digital Electronics
- Machine Learning
- Artificial Intelligence


এর একটি মৌলিক ভিত্তি।

Computer এর Binary World বোঝার জন্য
Boolean Algebra অপরিহার্য।
"""


# ===========================================================
# End of Boolean Algebra
# ===========================================================