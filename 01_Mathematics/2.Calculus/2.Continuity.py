"""
===========================================================
Continuity (ধারাবাহিকতা)
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
Continuity (ধারাবাহিকতা) হলো Calculus-এর একটি গুরুত্বপূর্ণ ধারণা।

এটি বলে:

কোনো function-এর graph বা behavior কি কোনো জায়গায়
ভাঙা ছাড়াই চলতে পারে?

সহজ ভাষায়:

একটি function যদি কোনো point-এ হঠাৎ jump,
break বা gap তৈরি না করে,
তাহলে function-টি সেই point-এ continuous।

Calculus-এ:

Limit → Continuity → Derivative → Integral

Continuity হলো Limit-এর উপর ভিত্তি করে তৈরি।
"""


# ===========================================================
# 02_WhyThisConceptExistsInRelationToHistory
# ===========================================================

"""
ইতিহাস:

প্রাচীন গণিতবিদরা continuous shape এবং motion
বোঝার চেষ্টা করতেন।

কিন্তু সমস্যা ছিল:

বাস্তব জগতের অনেক ঘটনা smooth ভাবে পরিবর্তিত হয়।

যেমন:

- গাড়ির গতি
- গ্রহের motion
- পানির প্রবাহ

17th century-তে Newton এবং Leibniz যখন Calculus
তৈরি করেন, তখন continuous change বোঝার প্রয়োজন হয়।

Continuity ধারণা তৈরি হয় বোঝার জন্য:

"কোনো quantity কি হঠাৎ পরিবর্তন হচ্ছে,
নাকি smooth ভাবে পরিবর্তিত হচ্ছে?"
"""


# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
বাস্তব জীবনের উদাহরণ:


Example 1:

একটি গাড়ি চলছে।

Speed:

0 km/h

তারপর:

10 km/h
20 km/h
30 km/h


গতি ধীরে ধীরে বাড়ছে।

এখানে speed change continuous।



--------------------------------


Example 2:

একটি পাহাড়ের রাস্তা।

আপনি হাঁটছেন।

রাস্তার height:

100m
101m
102m
103m


হঠাৎ:

100m থেকে 500m হয়ে যায় না।

তাই এটি continuous।



--------------------------------


Example 3:

বয়স:

20 বছর

20 বছর 1 দিন

20 বছর 2 দিন


বয়স continuous ভাবে বৃদ্ধি পাচ্ছে।
"""


# ===========================================================
# 04_Definition
# ===========================================================

"""
একটি function f(x), x=a point-এ continuous হবে যদি
তিনটি condition পূরণ করে।


Condition 1:

Function value থাকতে হবে:

f(a) exists


Condition 2:

Limit থাকতে হবে:

lim(x→a) f(x) exists


Condition 3:

Limit এবং function value সমান হতে হবে:


lim(x→a) f(x) = f(a)



তাহলে:

f(x) is continuous at x=a
"""


# ===========================================================
# 05_Formula
# ===========================================================

"""
Continuity Formula:


A function f(x) is continuous at x=a if:


lim(x→a) f(x) = f(a)



Meaning:


Approaching value
        =
Actual value



--------------------------------


Example:


f(x)=x²


Check at x=2:


Step 1:

f(2)=2²

=4



Step 2:

lim(x→2)x²

=4



Therefore:


lim(x→2)x² = f(2)


Function is continuous.
"""


# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
Continuity formula আসে Limit থেকে।


ধরি:

f(x)=x²


Point:

x=3


Function value:


f(3)=3²

=9



এখন x এর কাছাকাছি value নেই:


x=2.9

f(x)=8.41


x=2.99

f(x)=8.9401


x=2.999

f(x)=8.994001



x যত 3 এর কাছে যাচ্ছে,

output তত 9 এর কাছে যাচ্ছে।


অর্থাৎ:


lim(x→3)f(x)=f(3)



তাই function continuous।
"""


# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
Graphically:


Continuous Function:


       *
      *
     *
    *
---*----------------


Graph-এর মধ্যে কোনো break নেই।



--------------------------------


Discontinuous Function:


       *
      *


              *


Graph-এ gap আছে।



Computer ভিতরে:

1. Input value নেয়
2. Nearby points calculate করে
3. Output change observe করে
4. Check করে কোনো sudden jump আছে কিনা


যদি smooth হয়:

continuous


যদি jump থাকে:

discontinuous
"""


# ===========================================================
# 08_Examples
# ===========================================================

"""
Example 1:


f(x)=x+5


Check x=2:


f(2)=7


lim(x→2)(x+5)=7


Therefore:

Continuous



--------------------------------


Example 2:


f(x)=1/x


Check x=0:


f(0) undefined


তাই:

x=0 এ continuous নয়।



--------------------------------


Example 3:


Piecewise Function:


f(x)=

x²     x<1

2x     x>=1



x=1 এ:


Left limit:

1²=1


Right limit:

2(1)=2


Left ≠ Right


Therefore:

Discontinuous
"""


# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
Common Mistakes:


1. শুধু limit থাকলেই continuous মনে করা

ভুল।

Function value এবং limit equal হতে হবে।



--------------------------------


2. Graph না দেখে সিদ্ধান্ত নেওয়া


কিছু discontinuity algebra দিয়ে লুকানো থাকতে পারে।



--------------------------------


3. Division by zero ভুল করা


Example:

f(x)=1/(x-2)


x=2 এ:

denominator = 0


তাই discontinuous।



--------------------------------


4. Continuous মানে constant ভাবা


Continuous মানে constant নয়।

একটি function continuously change করতে পারে।
"""


# ===========================================================
# 10_Exercises
# ===========================================================

"""
Practice Problems:


1.

Check continuity:

f(x)=x²+2x


at x=1



Answer:

Continuous



--------------------------------


2.

Check:

f(x)=1/(x-5)


at x=5



Answer:

Discontinuous



--------------------------------


3.

Find whether:


f(x)=sin(x)


is continuous or not.



Answer:

Continuous everywhere



--------------------------------


4.

Explain:

Why derivative requires continuity?
"""


# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
Machine Learning এবং AI-তে Continuity:


1. Loss Function


Neural network training-এ:

Loss function সাধারণত continuous হয়।


কারণ:

Small input change

↓

Small output change



এতে optimization সহজ হয়।



--------------------------------


2. Gradient Descent


Gradient descent ধরে নেয়:

Function smooth এবং continuous।


কারণ:

Derivative ব্যবহার করে minimum খোঁজা হয়।



--------------------------------


3. Neural Network Activation


অনেক activation function:

- Sigmoid
- Tanh
- ReLU (mostly)


এগুলো model training-এর behavior
control করে।



--------------------------------


4. Computer Vision


Image pixel value পরিবর্তন:

এক pixel থেকে অন্য pixel-এ smooth variation

continuous mathematical model দিয়ে analyze করা হয়।



--------------------------------


5. Reinforcement Learning


State change এবং reward function
continuous হলে agent ভালোভাবে optimize করতে পারে।



--------------------------------


Summary:


Continuity শেখায়:

"একটি mathematical system কি smooth ভাবে পরিবর্তিত হচ্ছে?"


এটি গুরুত্বপূর্ণ কারণ:

✓ Limit বুঝতে সাহায্য করে
✓ Derivative-এর ভিত্তি তৈরি করে
✓ Optimization সহজ করে
✓ AI model training বোঝার foundation দেয়
"""


# ===========================================================
# End of Continuity
# ===========================================================