"""
===========================================================
OR Operator (Logical OR) - Logic
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
OR (Logical OR) হলো Logic এর একটি মৌলিক Logical Operator।

OR ব্যবহার করে দুই বা তার বেশি Proposition এর
মধ্যে সম্পর্ক নির্ধারণ করা হয়।

OR এর মূল নিয়ম:

যেকোনো একটি Condition True হলেই Result True হবে।

Symbol:

OR = ∨

Programming এ:

or


Example:

P OR Q


যদি:

P = True

Q = False


তাহলে:

P ∨ Q = True


"""


# ===========================================================
# 02_WhyThisConceptExistsInRelationToHistory
# ===========================================================

"""
বাস্তব জীবনে অনেক সময় একাধিক বিকল্পের
মধ্যে যেকোনো একটি পূরণ হলেই সিদ্ধান্ত নেওয়া হয়।


Example:

"আমি ভ্রমণে যাব যদি:

- বাস পাওয়া যায়

OR

- ট্রেন পাওয়া যায়"


এখানে যেকোনো একটি Option কাজ করলেই
সিদ্ধান্ত True হবে।


George Boole এর Boolean Algebra এ
OR একটি মৌলিক Logical Operation।


Computer Hardware এ:

OR Gate

এই Logic বাস্তবায়ন করে।


"""


# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
ধরি:


P = আমার কাছে Cash আছে

Q = আমার কাছে Card আছে


আমি Payment করতে পারবো যদি:


Cash OR Card থাকে।


Situation:


Cash     Card       Payment


True     True       Yes

True     False      Yes

False    True       Yes

False    False      No



কারণ:

কমপক্ষে একটি Payment Method থাকলেই হবে।
"""


# ===========================================================
# 04_Definition
# ===========================================================

"""
Definition:

OR হলো একটি Logical Operator যা
যেকোনো একটি বা একাধিক Proposition True হলে
True Return করে।


Mathematical Representation:


P ∨ Q


যেখানে:


P = First Proposition

Q = Second Proposition


Truth Value:


True  ∨ True  = True

True  ∨ False = True

False ∨ True  = True

False ∨ False = False


"""


# ===========================================================
# 05_Formula
# ===========================================================

"""
OR Formula:


P ∨ Q



Truth Table:


P       Q       P ∨ Q


T       T          T

T       F          T

F       T          T

F       F          F



Binary Representation:


1 OR 1 = 1

1 OR 0 = 1

0 OR 1 = 1

0 OR 0 = 0



"""


# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
ধরি:


P = আজ ছুটি

Q = আজ শুক্রবার


Statement:


"আজ ছুটি অথবা শুক্রবার"


Case 1:


P = True

Q = True


একটি Condition True,

Result = True



Case 2:


P = True

Q = False


ছুটি আছে,

Result = True



Case 3:


P = False

Q = True


শুক্রবার,

Result = True



Case 4:


P = False

Q = False


কোনোটিই সত্য নয়,

Result = False



তাই OR এর নিয়ম:


কমপক্ষে একটি Input True হলে Output True।
"""


# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
OR Gate:


P ----\
       OR ---- Output
Q ----/


Input:


P = 1

Q = 0


Output:

1



কারণ:

একটি Input High (1)


সব Combination:


1 OR 1 = 1

1 OR 0 = 1

0 OR 1 = 1

0 OR 0 = 0



Digital Circuit এ:


HIGH Signal = True = 1

LOW Signal  = False = 0


OR Gate যেকোনো একটি High Signal পেলেই
Output High দেয়।


Programming Example:


has_email = True

has_phone = False


if has_email or has_phone:

    contact_available = True


"""


# ===========================================================
# 08_Examples
# ===========================================================

"""
Example 1:


Login System:


User can login using:


Google Account

OR

Email Password



google_login = True

email_login = False


google_login or email_login


Output:

True



Example 2:


Machine Learning:


Customer is potential buyer if:


visited_website

OR

clicked_ad



Example 3:


Python:


is_admin = False

is_staff = True


is_admin or is_staff


Output:

True


"""


# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
Mistake 1:

OR কে AND মনে করা।


Wrong:

সব Condition True হতে হবে।


Correct:

যেকোনো একটি True হলেই True।



Mistake 2:

False OR False এর Result ভুল করা।


False OR False = False



Mistake 3:

Python এ:


or

এবং


|

একই মনে করা।


or:

Logical Operator


|:

Bitwise OR



Mistake 4:

Inclusive OR এবং Exclusive OR
এর পার্থক্য না বোঝা।


OR:

দুইটিই True হতে পারে।


"""


# ===========================================================
# 10_Exercises
# ===========================================================

"""
Exercise 1:


Truth Value বের করো:


True OR False


Answer:

True



Exercise 2:


False OR False


Answer:

False



Exercise 3:


Truth Table তৈরি করো:


P ∨ Q



Exercise 4:


বাস্তব উদাহরণ:


একজন User Access পাবে যদি:


Admin = True

OR

Manager = True


কখন Access পাওয়া যাবে?



Exercise 5:


Python:


has_wifi = False

has_mobile_data = True


result = has_wifi or has_mobile_data


Output কী হবে?


"""


# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
AI এবং Machine Learning এ OR Logic এর ব্যবহার:


1. Feature Selection


Example:


Customer Interested যদি:


Viewed Product

OR

Added To Cart



2. Rule Based AI


IF:


weather_rainy

OR

weather_cloudy


THEN:


carry_umbrella



3. Search System


Query Matching:


keyword_found

OR

semantic_match



4. Database Filtering


SQL:


SELECT *

FROM products

WHERE category='AI'

OR

category='ML';



5. Classification System


Multiple Conditions এর মধ্যে
যেকোনো একটি পূরণ হলে
একটি Class নির্বাচন করা হয়।



Conclusion:


OR হলো Logic এর একটি গুরুত্বপূর্ণ Operator।

এটি ব্যবহৃত হয়:

- Programming Conditions
- Computer Hardware
- Database Query
- Decision System
- Machine Learning
- Artificial Intelligence

এবং যেকোনো জায়গায় যেখানে
Multiple Alternative এর মধ্যে
একটি পূরণ হলেই সিদ্ধান্ত নেওয়া হয়।
"""


# ===========================================================
# End of OR Operator
# ===========================================================