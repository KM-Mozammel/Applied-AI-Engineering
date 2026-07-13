"""
===========================================================
Logic Circuit (লজিক সার্কিট) - Logic
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
Logic Circuit হলো এমন একটি Digital Circuit
যেখানে Logical Operation ব্যবহার করে
Input Signal থেকে Output তৈরি করা হয়।


Logic Circuit এর মূল Building Block:


- AND Gate
- OR Gate
- NOT Gate
- XOR Gate
- NAND Gate
- NOR Gate



Computer এর ভিতরের সব Digital System:

- CPU
- Memory
- Processor
- AI Chip


Logic Circuit এর উপর ভিত্তি করে তৈরি।



Logic Circuit কাজ করে:


Binary Value দিয়ে:


0 = False = OFF


1 = True = ON


"""


# ===========================================================
# 02_WhyThisConceptExistsInRelationToHistory
# ===========================================================

"""
প্রাচীন সময়ে Logic শুধুমাত্র Mathematical
Theory হিসেবে ব্যবহৃত হতো।


George Boole:

Boolean Algebra তৈরি করেন।


তারপর Claude Shannon দেখান:


Boolean Algebra + Electrical Circuit


মিলিয়ে Digital Circuit তৈরি করা সম্ভব।



এর ফলে তৈরি হয়:


- Digital Computer
- Microprocessor
- Integrated Circuit


আজকের Computer এর প্রতিটি Transistor
একটি ছোট Logic Circuit এর মতো কাজ করে।
"""


# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
বাস্তব উদাহরণ:


Automatic Door System:


Condition:


A = Person Detected


B = Safety Check Passed



Door Open হবে যদি:


A AND B



Logic Circuit:


Person Sensor
       |
       |
       AND Gate ---- Door Motor



যদি:


A = 1

B = 1


Output:

1


Door Open হবে।


"""


# ===========================================================
# 04_Definition
# ===========================================================

"""
Definition:


Logic Circuit হলো এমন একটি Digital Circuit
যেখানে Logic Gate ব্যবহার করে
Boolean Expression বাস্তবায়ন করা হয়।



Components:


1. Input


যেখানে Binary Signal দেওয়া হয়।



2. Logic Gate


যেখানে Logical Operation হয়।



3. Output


যেখানে Final Result পাওয়া যায়।



Example:


A ----\
       AND ---- Output
B ----/


Expression:


A ∧ B


"""


# ===========================================================
# 05_Formula
# ===========================================================

"""
Logic Circuit এর Formula
Boolean Expression হিসেবে লেখা হয়।



Common Logic Gates:



================================================
AND Gate
================================================


Expression:


A · B


Truth:


A B | Output

1 1 | 1

1 0 | 0

0 1 | 0

0 0 | 0



================================================
OR Gate
================================================


Expression:


A + B


Truth:


A B | Output

1 1 | 1

1 0 | 1

0 1 | 1

0 0 | 0



================================================
NOT Gate
================================================


Expression:


A'


Truth:


A | Output

1 | 0

0 | 1



================================================
XOR Gate
================================================


Expression:


A ⊕

B


Truth:


A B | Output

1 1 | 0

1 0 | 1

0 1 | 1

0 0 | 0



================================================
NAND Gate
================================================


Expression:


(A · B)'



================================================
NOR Gate
================================================


Expression:


(A + B)'



"""


# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
ধরি:


একটি Security System তৈরি করতে হবে।


Requirement:


Alarm চালু হবে যদি:


Door Open

AND

Window Open



Variable:


A = Door Open

B = Window Open



Boolean Expression:


A · B



Truth Table:


A   B    Output


1   1      1


1   0      0


0   1      0


0   0      0



Circuit:


Door Sensor
      |
      |
      AND Gate ---- Alarm


Window Sensor
      |


এইভাবেই Real Problem থেকে
Logic Circuit তৈরি হয়।
"""


# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
Logic Circuit ভিতরে কীভাবে কাজ করে:


Step 1:

Input Signal আসে।


Example:


A = 1

B = 0



Step 2:

Signal Logic Gate এ যায়।



Step 3:

Gate Boolean Rule অনুসারে
Output তৈরি করে।



Example:


AND Gate:


1 AND 0


=

0



Step 4:

Output পরবর্তী Circuit এ যায়।



Computer Chip এ:


Millions of Logic Gate
একসাথে কাজ করে
Complex Operation সম্পন্ন করে।



Example:


CPU:


Input Data

↓

Logic Circuit

↓

Arithmetic Operation

↓

Output


"""


# ===========================================================
# 08_Examples
# ===========================================================

"""
Example 1:

Half Adder Circuit


Binary Addition করতে
XOR এবং AND Gate ব্যবহার হয়।


Sum:


A XOR B



Carry:


A AND B




Example 2:


Traffic Light System:


Condition:


Sensor Active

AND

Timer Finished



Output:


Green Light ON




Example 3:


Programming Logic:


if age >= 18 and has_ticket:

    allow_entry



এটি একটি Logic Circuit এর মতো কাজ করে।



"""


# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
Mistake 1:


Logic Circuit কে সাধারণ Electrical Circuit
ভাবা।


Logic Circuit:

Binary Signal নিয়ে কাজ করে।



Mistake 2:


AND এবং OR Gate গুলিয়ে ফেলা।



AND:

সব Input True হলে Output True।



OR:

একটি Input True হলেই Output True।



Mistake 3:


NAND এবং NOR এর Difference ভুল করা।



NAND:

NOT(AND)



NOR:

NOT(OR)



Mistake 4:


Boolean Expression না বুঝে
Circuit আঁকা।


"""


# ===========================================================
# 10_Exercises
# ===========================================================

"""
Exercise 1:


AND Gate এর Truth Table তৈরি করো।



Exercise 2:


একটি Circuit তৈরি করো:


A OR B



Exercise 3:


Expression তৈরি করো:


A AND (B OR C)



Exercise 4:


Half Adder Circuit ব্যাখ্যা করো।



Exercise 5:


নিচের Expression এর Circuit আঁকো:


(A AND B) OR C


"""


# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
AI এবং Machine Learning এ Logic Circuit এর ব্যবহার:


1. AI Hardware


AI Processor:

- GPU
- TPU
- Neural Processing Unit


Logic Circuit দিয়ে তৈরি।



2. Neural Network Accelerator


Matrix Calculation করার জন্য
Digital Circuit ব্যবহার করা হয়।



3. Binary Classification


Output:


0 অথবা 1


Logic Circuit এর Binary Output এর মতো।



4. Edge AI Device


কম Power এ AI Model চালাতে
Special Logic Circuit ব্যবহার হয়।



5. Computer Architecture


AI System এর:


Memory

Processor

Control Unit


সব Logic Circuit এর উপর নির্ভর করে।



Conclusion:


Logic Circuit হলো Computer এর
মৌলিক Hardware Foundation।

এটি বুঝলে বোঝা যায়:


- Computer কীভাবে চিন্তা করে
- CPU কীভাবে কাজ করে
- AI Hardware কীভাবে তৈরি হয়


"""


# ===========================================================
# End of Logic Circuit
# ===========================================================