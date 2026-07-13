"""
===========================================================
XOR Operator (Exclusive OR) - Logic
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
XOR (Exclusive OR) হলো Logic এর একটি গুরুত্বপূর্ণ
Logical Operator।

XOR এর পূর্ণরূপ:

Exclusive OR


মূল নিয়ম:

শুধুমাত্র একটি Condition True হলে Result True হবে।

অর্থাৎ:

একটি True এবং অন্যটি False হলে True।

কিন্তু:

দুইটিই True হলে False।


Symbol:

⊕

Programming এ:

^


Example:


P XOR Q


যদি:


P = True

Q = False


তাহলে:


P ⊕ Q = True


"""


# ===========================================================
# 02_WhyThisConceptExistsInRelationToHistory
# ===========================================================

"""
সাধারণ OR Logic এ:

দুইটি Condition True হলেও Result True হয়।


Example:

A অথবা B


A = True

B = True


OR Result:

True



কিন্তু অনেক ক্ষেত্রে প্রয়োজন হয়:


"শুধুমাত্র একটি হবে"


এই ধরনের Exclusive Decision এর জন্য
XOR তৈরি করা হয়।


Claude Shannon এবং Digital Logic Design এ
XOR Circuit গুরুত্বপূর্ণ ভূমিকা রাখে।


Computer:

- Addition Circuit
- Error Detection
- Encryption

এ XOR ব্যাপকভাবে ব্যবহার করে।


"""


# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
ধরি:


একটি প্রশ্ন:


"তুমি কি Tea অথবা Coffee নেবে?"

কিন্তু শুধুমাত্র একটি নির্বাচন করা যাবে।


Tea     Coffee      Result


Yes     No          True


No      Yes         True


Yes     Yes         False


No      No          False



কারণ:

একসাথে দুইটি নির্বাচন করা যাবে না।


এটাই Exclusive OR।
"""


# ===========================================================
# 04_Definition
# ===========================================================

"""
Definition:


XOR হলো একটি Logical Operator যেখানে
দুইটি Input আলাদা হলে Output True হয়
এবং একই হলে Output False হয়।


Mathematical Representation:


P ⊕ Q


Truth Value:


True XOR False = True


False XOR True = True


True XOR True = False


False XOR False = False



"""


# ===========================================================
# 05_Formula
# ===========================================================

"""
XOR Formula:


P ⊕ Q


Equivalent Formula:


(P ∨ Q) ∧ ¬(P ∧ Q)



অর্থ:


প্রথমে:

P অথবা Q


কিন্তু:

দুইটিই True হওয়া যাবে না।



Truth Table:


P       Q       P ⊕ Q


T       T          F


T       F          T


F       T          T


F       F          F



Binary:


1 XOR 1 = 0


1 XOR 0 = 1


0 XOR 1 = 1


0 XOR 0 = 0


"""


# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
ধরি:


P = Switch A ON

Q = Switch B ON



আমরা চাই:

শুধুমাত্র একটি Switch ON হলে Light জ্বলবে।



Case 1:


P = True

Q = False


একটি ON


Result:

True



Case 2:


P = False

Q = True


একটি ON


Result:

True



Case 3:


P = True

Q = True


দুইটি ON


Exclusive Rule ভেঙে যায়।


Result:

False



Case 4:


P = False

Q = False


কোনোটিই ON নয়।


Result:

False



তাই:

Different Input = True

Same Input = False


"""


# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
XOR Gate:


P ----\
       XOR ---- Output
Q ----/



Input:


P     Q      Output


1     1         0


1     0         1


0     1         1


0     0         0



Computer ভিতরে:


XOR Bit Comparison হিসেবে কাজ করে।



Example:


A = 1010

B = 1100


A XOR B:


1010

1100

----

0110



যেখানে:

Same Bit = 0

Different Bit = 1



"""


# ===========================================================
# 08_Examples
# ===========================================================

"""
Example 1:


Password Verification:


Old Password XOR New Password


যদি দুইটি আলাদা হয়:

True



Example 2:


Python:


a = True

b = False


result = a ^ b


Output:


True



Example 3:


Network:


Data Transmission এ
Error Detection এর জন্য XOR ব্যবহার হয়।



Example 4:


Digital Addition:


Binary Addition এ:


1 XOR 1 = 0


Carry আলাদা Handle করা হয়।


"""


# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
Mistake 1:

XOR কে OR মনে করা।


OR:


True OR True = True


XOR:


True XOR True = False



Mistake 2:

XOR কে AND এর মতো ভাবা।


AND:


শুধু দুইটি True হলে True


XOR:


আলাদা হলে True



Mistake 3:

Python এ:


^


কে Power Operator মনে করা।


Python:


2 ** 3 = Power


2 ^ 3 = Bitwise XOR



Mistake 4:

Exclusive শব্দের অর্থ না বোঝা।


Exclusive:

শুধুমাত্র একটি।


"""


# ===========================================================
# 10_Exercises
# ===========================================================

"""
Exercise 1:


Calculate:


True XOR False


Answer:


True



Exercise 2:


True XOR True


Answer:


False



Exercise 3:


False XOR False


Answer:


False



Exercise 4:


Truth Table তৈরি করো:


P ⊕ Q



Exercise 5:


Python:


x = 10

y = 5


result = x ^ y


কী Result হবে?


"""


# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
AI এবং Machine Learning এ XOR এর ব্যবহার:


1. Neural Network History


XOR Problem:

Single Layer Perceptron XOR Solve করতে পারে না।


এই সমস্যা থেকেই:

Multi Layer Neural Network

এর প্রয়োজনীয়তা বোঝা যায়।



2. Feature Comparison


Example:


Feature A

Feature B


Different হলে:

New Pattern Detect



3. Error Detection


Communication System:


Data XOR Check Bit


ব্যবহার করে Error Detect করা হয়।



4. Cryptography


XOR Encryption এর একটি
মূল ভিত্তি।


Example:


Message XOR Key

=

Encrypted Data



5. Computer Vision


Image Processing এ:

Pixel Difference Detection

এ XOR ব্যবহার করা হয়।



Conclusion:


XOR হলো Logic এর একটি গুরুত্বপূর্ণ Operator।

এটি ব্যবহৃত হয়:

- Neural Network
- Encryption
- Digital Circuit
- Error Detection
- Machine Learning

এবং যেখানে দুইটি Input এর
Difference খুঁজে বের করতে হয়।
"""


# ===========================================================
# End of XOR Operator
# ===========================================================