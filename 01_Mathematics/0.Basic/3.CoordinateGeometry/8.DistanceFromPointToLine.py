"""
===========================================================
Distance From Point to Line
(একটি Point থেকে একটি Line-এর দূরত্ব)
===========================================================

Structure:
01_Introduction
02_WhyThisConceptExistsInRealtionTohistory
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
Coordinate Geometry-তে শুধু দুইটি Point-এর Distance
জানলেই সব সমস্যা সমাধান হয় না।

অনেক সময় জানতে হয়—

"একটি নির্দিষ্ট Point একটি Line থেকে
কত দূরে অবস্থিত?"

মনে রাখবে,

এই Distance Line বরাবর মাপা হয় না।

বরং,

Point থেকে Line-এর উপর অঙ্কিত
সবচেয়ে ছোট লম্ব (Perpendicular) দূরত্বই
আসল Distance।

এই ধারণাকেই বলা হয়

Distance From Point to Line।
"""

# ===========================================================
# 02_WhyThisConceptExistsInRealtionTohistory
# ===========================================================

"""
প্রাচীনকাল থেকেই মানুষ

✔ রাস্তা নির্মাণ

✔ সেতু নির্মাণ

✔ জমি জরিপ

✔ দুর্গ নির্মাণ

✔ মানচিত্র তৈরি

ইত্যাদিতে কোনো নির্দিষ্ট বিন্দু
একটি রেখা থেকে কত দূরে আছে
তা নির্ণয় করত।

Coordinate Geometry আবিষ্কারের পরে
গণিতবিদরা এমন একটি সূত্র তৈরি করেন
যা শুধুমাত্র

Point-এর Coordinate

এবং

Line-এর Equation

ব্যবহার করে

Shortest Distance

নির্ণয় করতে পারে।
"""

# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
ধরো,

তুমি একটি রাস্তার পাশে দাঁড়িয়ে আছো।

রাস্তার উপর হাঁটলে
অনেক দূর যেতে হতে পারে।

কিন্তু

রাস্তার দিকে
একদম সোজা (৯০° কোণে)

হাঁটলে

সবচেয়ে কম দূরত্ব অতিক্রম করতে হবে।

এই সবচেয়ে ছোট দূরত্বই

Distance From Point to Line।

আরও উদাহরণ—

✔ GPS Navigation

✔ Drone Landing

✔ Robotics

✔ Computer Graphics

✔ Land Survey

✔ Image Processing
"""

# ===========================================================
# 04_Definition
# ===========================================================

"""
একটি Point থেকে একটি Line-এর

Shortest Perpendicular Distance

-কে

Distance From Point to Line

বলা হয়।

যদি,

Point = (x₀, y₀)

এবং

Line

Ax + By + C = 0

হয়,

তাহলে Distance
একটি নির্দিষ্ট সূত্র দিয়ে বের করা যায়।
"""

# ===========================================================
# 05_Formula
# ===========================================================

"""
Line

Ax + By + C = 0

Point

(x₀, y₀)



                |Ax₀ + By₀ + C|
Distance =
               ------------------
                √(A² + B²)


যেখানে,

A, B, C

হলো Line-এর Coefficients

(x₀,y₀)

হলো Point।
"""

# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
ধরি,

Line

Ax + By + C = 0

এবং

Point

P(x₀,y₀)

Line-এর উপর
একটি লম্ব আঁকা হলো।

Vector Geometry অনুযায়ী,

Line-এর একটি Normal Vector থাকে।

Normal Vector

=

(A,B)

এই Normal Vector-এর সাহায্যে

Point-এর Projection

নির্ণয় করলে,

শেষ পর্যন্ত Distance পাওয়া যায়—

                |Ax₀+By₀+C|
d =
              ----------------
               √(A²+B²)

এই সূত্রটি

Vector Projection

এবং

Analytic Geometry

থেকে এসেছে।
"""

# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
                 y
                 ↑

                 ● P(x₀,y₀)
                 |
                 |
                 |   Shortest Distance
                 |
-----------------●--------------------
              /
            /
          /
        /
      /

        Line


Point থেকে Line-এর উপর

যে লম্ব আঁকা হয়েছে,

সেই অংশটিই

Shortest Distance।

Line বরাবর কোনো Distance
এখানে গণনা করা হয় না।
"""

# ===========================================================
# 08_Examples
# ===========================================================

import math

print("=" * 60)
print("Example 1")
print("=" * 60)

# Line : 3x + 4y - 10 = 0

A = 3
B = 4
C = -10

# Point

x0 = 2
y0 = 1

distance = abs(A*x0 + B*y0 + C) / math.sqrt(A*A + B*B)

print("Distance =", distance)

print()

print("=" * 60)
print("Example 2")
print("=" * 60)

# Line : x - y + 2 = 0

A = 1
B = -1
C = 2

x0 = 3
y0 = 5

distance = abs(A*x0 + B*y0 + C) / math.sqrt(A*A + B*B)

print("Distance =", distance)

print()

print("=" * 60)
print("Example 3")
print("=" * 60)

# Line : 2x + y - 8 = 0

A = 2
B = 1
C = -8

x0 = 4
y0 = 2

distance = abs(A*x0 + B*y0 + C) / math.sqrt(A*A + B*B)

print("Distance =", distance)

"""
Output

Distance = 0.0

Distance = 0.0

Distance ≈ 0.89
"""

# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
❌ ভুল ১

Absolute Value

|Ax₀+By₀+C|

ব্যবহার না করা।

Distance কখনো Negative হয় না।

------------------------------------

❌ ভুল ২

Denominator-এ

√(A²+B²)

লিখতে ভুলে যাওয়া।

------------------------------------

❌ ভুল ৩

Line-কে

Ax+By+C=0

রূপে না এনে
সরাসরি Formula ব্যবহার করা।

------------------------------------

❌ ভুল ৪

Distance Between Two Points-এর
Formula ব্যবহার করা।

এটি সম্পূর্ণ ভিন্ন Formula।

------------------------------------

❌ ভুল ৫

Shortest Distance-এর পরিবর্তে

Line বরাবর Distance
ভাবা।
"""

# ===========================================================
# 10_Exercises
# ===========================================================

"""
১।

Point

(2,3)

Line

x+y-5=0

Distance বের করো।

----------------------------------

২।

Point

(4,-1)

Line

2x+3y-6=0

Distance বের করো।

----------------------------------

৩।

Point

(0,0)

Line

5x+12y-13=0

Distance বের করো।

----------------------------------

৪।

নিজের

distance_point_to_line()

Function তৈরি করো।

----------------------------------

৫।

User থেকে

A,B,C

এবং

Point Input নিয়ে

Distance বের করো।

----------------------------------

৬।

Distance শূন্য হলে
Point কি Line-এর উপর আছে?

যাচাই করো।
"""

# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
Point থেকে Line-এর Distance
Machine Learning এবং AI-এ
অত্যন্ত গুরুত্বপূর্ণ।

১।

Support Vector Machine (SVM)

Hyperplane থেকে Data Point-এর
Distance নির্ণয় করতে।

----------------------------------

২।

Computer Vision

Edge Detection

এবং

Feature Matching।

----------------------------------

৩।

Robotics

Robot কত দূরে
Boundary থেকে আছে
তা নির্ণয় করতে।

----------------------------------

৪।

Autonomous Vehicles

Lane Detection

এবং

Road Following।

----------------------------------

৫।

Computer Graphics

Collision Detection

এবং

Object Alignment।

----------------------------------

৬।

Optimization

Minimum Distance Problem

সমাধানে।

----------------------------------

বিশেষভাবে,

SVM-এ

Margin

হলো

Data Point থেকে
Decision Boundary (Hyperplane)-এর
Perpendicular Distance-এর উপর ভিত্তি করে নির্ধারিত।

তাই এই ধারণাটি
Machine Learning-এর Linear Models
বোঝার জন্য অত্যন্ত গুরুত্বপূর্ণ।
"""

# ===========================================================
# End of File
# ===========================================================