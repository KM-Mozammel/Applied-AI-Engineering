"""
===========================================================
NOT Operator (Logical NOT) - Logic
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
NOT (Logical NOT) হলো Logic এর একটি মৌলিক Logical Operator।

NOT কোনো একটি Proposition এর Truth Value কে উল্টে দেয়।

অর্থাৎ:

True  → False

False → True


Symbol:

NOT = ¬


Programming এ:

not


Example:


P = True


NOT P


Result:

False


"""


# ===========================================================
# 02_WhyThisConceptExistsInRelationToHistory
# ===========================================================

"""
মানুষের যুক্তিতে অনেক সময় কোনো বক্তব্যের
বিপরীত অবস্থা বোঝানোর প্রয়োজন হয়।


Example:


Statement:

"আজ বৃষ্টি হচ্ছে।"


এর বিপরীত:


"আজ বৃষ্টি হচ্ছে না।"



এই Negation বা বিপরীত ধারণা প্রকাশ করার জন্য
NOT Logic তৈরি হয়।


George Boole এর Boolean Algebra এ
NOT একটি মৌলিক Operation।


Computer Hardware এ:

NOT Gate

বা Inverter Circuit ব্যবহার করে
এই Logic বাস্তবায়ন করা হয়।


"""


# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
ধরি:


P = দরজা খোলা আছে।


NOT P মানে:


দরজা খোলা নেই।



Situation:


P              NOT P


True           False


False          True



অর্থাৎ:

NOT সবসময় মূল Condition এর বিপরীত Result দেয়।
"""


# ===========================================================
# 04_Definition
# ===========================================================

"""
Definition:


NOT হলো একটি Unary Logical Operator
যা একটি Proposition এর Truth Value পরিবর্তন করে।


Mathematical Representation:


¬P


যেখানে:


P = Proposition



Truth Value:


¬True = False


¬False = True



"""


# ===========================================================
# 05_Formula
# ===========================================================

"""
NOT Formula:


¬P



Truth Table:


P       NOT P


T          F


F          T



Binary Representation:


NOT 1 = 0


NOT 0 = 1



NOT হলো Bit Inversion।

"""


# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
ধরি:


P = "আমি আজ অফিসে যাব।"


এখন:


NOT P


মানে:


"আমি আজ অফিসে যাব না।"



Case 1:


P = True


আমি অফিসে যাব।


NOT P:


False



Case 2:


P = False


আমি অফিসে যাব না।


NOT P:


True



তাই:

NOT Operator সবসময় Statement এর
Opposite Truth Value দেয়।
"""


# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
NOT Gate:


Input ---- NOT ---- Output



Input:

1


NOT Output:


0



Input:

0


NOT Output:


1



Digital Electronics:


High Voltage = 1

Low Voltage  = 0



NOT Gate Input Signal কে Invert করে।



Programming Example:


is_logged_in = False


if not is_logged_in:

    show_login_page()



এখানে:


not False = True


তাই Login Page দেখাবে।

"""


# ===========================================================
# 08_Examples
# ===========================================================

"""
Example 1:


Python:


is_raining = True


not is_raining


Output:


False



Example 2:


Security System:


door_locked = False


if not door_locked:

    alarm()


কারণ:

Door Locked না হলে Alarm চালু হবে।



Example 3:


Machine Learning:


prediction = False


not prediction


Output:


True


"""


# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
Mistake 1:

NOT কে পরিবর্তন না করা।


Wrong:


NOT True = True


Correct:


NOT True = False



Mistake 2:

AND/OR এর সাথে NOT গুলিয়ে ফেলা।


NOT শুধুমাত্র একটি Condition এর
Truth Value পরিবর্তন করে।



Mistake 3:

Programming এ:


not x


এবং


x != True


সবসময় একই নয়।


কারণ:

Different Data Type এর Behaviour আলাদা হতে পারে।



Mistake 4:

Double NOT ভুল বোঝা।


Example:


not not True


Step 1:


not True = False


Step 2:


not False = True


Result:

True


"""


# ===========================================================
# 10_Exercises
# ===========================================================

"""
Exercise 1:


Truth Value বের করো:


NOT True


Answer:


False



Exercise 2:


NOT False


Answer:


True



Exercise 3:


Truth Table তৈরি করো:


¬P



Exercise 4:


বাস্তব উদাহরণ:


P:

"User is Active"


NOT P কী হবে?



Exercise 5:


Python:


is_admin = False


result = not is_admin


Output কী হবে?


"""


# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
AI এবং Machine Learning এ NOT Logic এর ব্যবহার:


1. Data Filtering


Example:


Remove inactive users:


if not user.active:

    delete_user()



2. Classification


Prediction:


is_spam = False


NOT is_spam


মানে:


Email is not spam



3. Rule Based AI


IF:


not available


THEN:


search alternative



4. Feature Engineering


Boolean Feature:


has_error = False


not has_error


Result:


System is healthy



5. Neural Network


Binary Classification এ:


0 ↔ 1


এই ধরনের inversion operation
ব্যবহার করা হয়।



Conclusion:


NOT হলো Logic এর একটি গুরুত্বপূর্ণ Operator।

এটি ব্যবহার হয়:

- Programming
- Digital Circuit
- Database
- Machine Learning
- Artificial Intelligence


যেখানে কোনো Condition এর
Opposite State প্রয়োজন হয়।
"""


# ===========================================================
# End of NOT Operator
# ===========================================================