"""
===========================================================
AI Usage in Logic (লজিকে AI এর ব্যবহার)
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
Logic এবং Artificial Intelligence (AI) একে অপরের সাথে
খুব গভীরভাবে সম্পর্কিত।

AI মূলত Decision Making System।

একটি AI System কে সিদ্ধান্ত নিতে হয়:


- True অথবা False
- Yes অথবা No
- 0 অথবা 1


এই Binary Decision নেওয়ার জন্য
Logic ব্যবহার করা হয়।


Logic AI এর ভিত্তি তৈরি করে:


- Rule Based System
- Expert System
- Machine Learning Decision
- Neural Network
- Knowledge Representation


AI এর ভিতরে অনেক Algorithm
Logical Reasoning এর উপর নির্ভর করে।
"""


# ===========================================================
# 02_WhyThisConceptExistsInRelationToHistory
# ===========================================================

"""
AI এর শুরুতে Computer কে মানুষের মতো
যুক্তি দিয়ে চিন্তা করানোর চেষ্টা করা হয়।


1950-1960 সালের দিকে:

Artificial Intelligence Research শুরু হয়।


প্রথম দিকে AI ছিল:

Symbolic AI


যেখানে Computer কে Rule দেওয়া হতো।


Example:


IF:

Human has fever

AND

Human has cough


THEN:


Possible Disease = Flu



এই ধরনের Rule Logic এর উপর ভিত্তি করে তৈরি।


পরবর্তীতে:


Machine Learning

এবং

Deep Learning


আসে, কিন্তু Logic এখনো গুরুত্বপূর্ণ।


"""


# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
মানুষ যেভাবে সিদ্ধান্ত নেয়:


Example:


যদি:

বৃষ্টি হচ্ছে

AND

আকাশ মেঘলা


তাহলে:

ছাতা নেওয়া উচিত।



এই চিন্তা AI তেও ব্যবহার করা হয়।


AI Rule:


rain = True

cloud = True


if rain and cloud:

    take_umbrella = True



এখানে:


AND Logic


ব্যবহার হচ্ছে।



আরেকটি উদাহরণ:


একটি Email Spam কিনা:


যদি:


Unknown Sender

OR

Suspicious Link


তাহলে:


Spam = True



এখানে:


OR Logic


ব্যবহার হচ্ছে।
"""


# ===========================================================
# 04_Definition
# ===========================================================

"""
Definition:


AI Logic হলো এমন একটি পদ্ধতি যেখানে
Logical Rules, Boolean Values এবং Reasoning
ব্যবহার করে Machine সিদ্ধান্ত নেয়।


AI Logic এর মূল উপাদান:


1. Proposition


Statement যার Truth Value আছে।



Example:


"User is Admin"


True / False



2. Boolean Variable


True = 1

False = 0



3. Logical Operator


AND

OR

NOT

XOR



4. Rule


IF condition THEN action


"""


# ===========================================================
# 05_Formula
# ===========================================================

"""
AI Logic এর Mathematical Representation:


------------------------------------------------
1. Boolean Decision
------------------------------------------------


Output = True / False



------------------------------------------------
2. AND Rule
------------------------------------------------


Decision = A ∧ B



Example:


Approved =

Income_OK AND Credit_OK



------------------------------------------------
3. OR Rule
------------------------------------------------


Decision = A ∨ B



Example:


Access =

Admin OR Manager



------------------------------------------------
4. NOT Rule
------------------------------------------------


Decision = ¬A



Example:


Available = NOT Busy



------------------------------------------------
5. Rule Based AI
------------------------------------------------


IF:

Condition


THEN:


Action



Mathematical:


Condition → Action



"""


# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
ধরি একটি AI Loan Approval System।


Requirement:


Loan Approved হবে যদি:


1. Income ভালো হয়

AND

2. Credit Score ভালো হয়



Variables:


A = Income Good


B = Credit Score Good



Logic:


A ∧ B



Truth Table:


A       B       Decision


T       T          T


T       F          F


F       T          F


F       F          F



Meaning:


দুইটি Condition সত্য হলেই
AI Approval দেবে।



এভাবেই Real World Problem কে
Logical Expression এ পরিবর্তন করা হয়।
"""


# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
AI System ভিতরে Logic ব্যবহার করে:


Input

↓

Feature Extraction

↓

Logical Evaluation

↓

Decision


Example:


Email:


Features:


sender_unknown = True

has_link = True



Logic:


sender_unknown OR has_link



Result:


Spam = True



Visualization:


Feature

  |

  v

Boolean Logic

  |

  v

Decision



Modern AI তে Deep Learning থাকলেও
অনেক জায়গায় Logical Layer থাকে।


Example:


Autonomous Vehicle:


Object detected

AND

Danger level high


↓

Emergency Brake


"""


# ===========================================================
# 08_Examples
# ===========================================================

"""
Example 1:

Chatbot


User:


"Reset password"


Logic:


IF:

user_verified = True


THEN:


allow_reset = True



--------------------------------


Example 2:

Medical AI


Features:


fever = True

cough = True



Rule:


fever AND cough



Output:


Possible Infection



--------------------------------


Example 3:

Recommendation System


Condition:


User likes AI

OR

User likes Programming



Recommend:


AI Course



--------------------------------


Example 4:

Security AI


Condition:


Face recognized

AND

Voice matched



Allow Entry


"""


# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
Mistake 1:


AI কে শুধুমাত্র Logic মনে করা।


AI এর মধ্যে রয়েছে:


- Statistics
- Probability
- Optimization
- Neural Network



Logic হলো একটি অংশ।



Mistake 2:


Boolean Logic এবং Machine Learning
একই ভাবা।


Machine Learning:

Data থেকে Pattern শেখে।


Logic:


Explicit Rule Follow করে।



Mistake 3:


AND এবং OR Condition ভুল ব্যবহার করা।



Mistake 4:


False মানে Error ভাবা।


AI তে:


False একটি Valid Decision Value।



Mistake 5:


Logic Rule বেশি তৈরি করা।


অনেক Rule হলে System Complex হয়ে যায়।
"""


# ===========================================================
# 10_Exercises
# ===========================================================

"""
Exercise 1:


একটি AI Rule তৈরি করো:


User Access পাবে যদি:


Username Correct

AND

Password Correct



Logic Expression লেখো।



--------------------------------


Exercise 2:


Spam Detection Rule তৈরি করো:


Unknown Email

OR

Dangerous Link



--------------------------------


Exercise 3:


NOT ব্যবহার করে লেখো:


System Available


যদি:


System Busy না হয়।



--------------------------------


Exercise 4:


Truth Table তৈরি করো:


A AND B



--------------------------------


Exercise 5:


Explain:


Machine Learning এবং Rule Based AI এর
মধ্যে পার্থক্য।


"""


# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
Logic নিজেই AI এর একটি গুরুত্বপূর্ণ অংশ।


AI তে Logic এর ব্যবহার:


===================================================
1. Expert System
===================================================


পুরনো AI System এ:

IF-THEN Rule


ব্যবহার করা হতো।


Example:


IF:

temperature_high

AND

cough


THEN:


Disease = Possible



===================================================
2. Decision Tree
===================================================


Decision Tree এর প্রতিটি Node
একটি Logical Condition।


Example:


Age > 18?


YES / NO



===================================================
3. Feature Engineering
===================================================


Boolean Feature তৈরি করা হয়:


has_account = True


is_active = False



Multiple Feature Combine:


has_account AND is_active



===================================================
4. Neural Network Logic
===================================================


Neural Network সরাসরি Logic Gate নয়,
কিন্তু Boolean Function শেখার জন্য
ব্যবহার করা হয়।


বিশেষ করে:


XOR Problem


Neural Network Development এ
গুরুত্বপূর্ণ ছিল।



===================================================
5. AI Hardware
===================================================


AI Chip:

- GPU
- TPU
- NPU


Logic Circuit এর মাধ্যমে
Binary Operation সম্পন্ন করে।



===================================================
6. Natural Language Processing
===================================================


NLP System এ:


Intent Detection


Example:


User wants:

"Book flight"


Logic Rule:

IF travel_intent

THEN show_flight_option



===================================================
7. Robotics
===================================================


Robot Decision:


Obstacle detected

AND

Distance < threshold


THEN:


Stop movement



===================================================


Conclusion:


Logic হলো AI এর একটি মৌলিক ভিত্তি।

Logic ছাড়া:


- Decision Making
- Rule System
- Computer Hardware
- AI Reasoning


সম্পূর্ণভাবে বোঝা সম্ভব নয়।


Mathematical Logic থেকে শুরু করে
Modern AI System পর্যন্ত
Logic একটি গুরুত্বপূর্ণ ভূমিকা পালন করে।
"""


# ===========================================================
# End of AI Usage in Logic
# ===========================================================