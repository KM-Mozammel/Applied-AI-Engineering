"""
===========================================================
Parallel and Perpendicular Lines
(সমান্তরাল ও লম্ব রেখা)
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
Coordinate Geometry-তে অনেকগুলো Line একসাথে থাকতে পারে।

কিছু Line কখনো একে অপরকে ছেদ (Intersect) করে না।

আবার কিছু Line একে অপরকে ৯০° কোণে ছেদ করে।

এই দুই ধরনের Line-কে বলা হয়—

১. Parallel Lines (সমান্তরাল রেখা)

২. Perpendicular Lines (লম্ব রেখা)

Slope ব্যবহার করেই খুব সহজে বোঝা যায়
দুইটি Line Parallel নাকি Perpendicular।
"""

# ===========================================================
# 02_WhyThisConceptExistsInRealtionTohistory
# ===========================================================

"""
প্রাচীনকাল থেকেই মানুষ

✔ রাস্তা নির্মাণ

✔ ভবন নির্মাণ

✔ সেতু নির্মাণ

✔ কৃষিজমি ভাগ করা

✔ মানচিত্র তৈরি

ইত্যাদি কাজে Parallel এবং Perpendicular
রেখা ব্যবহার করে আসছে।

Coordinate Geometry আবিষ্কারের পরে
গণিতবিদরা বুঝতে পারলেন,

শুধুমাত্র Slope ব্যবহার করেই
দুইটি Line-এর সম্পর্ক নির্ণয় করা যায়।

এভাবে Parallel ও Perpendicular Line-এর
গাণিতিক নিয়ম তৈরি হয়।
"""

# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
Parallel Lines

দুটি রেললাইন কল্পনা করো।

========================

========================

তারা পাশাপাশি চলে,
কিন্তু কখনো মিলিত হয় না।

এগুলো Parallel।

------------------------------------

Perpendicular Lines

একটি রাস্তা আরেকটি রাস্তাকে

ঠিক ৯০° কোণে কাটছে।

      |
      |
------|-------
      |
      |

এগুলো Perpendicular।

আরও উদাহরণ—

✔ Window Frame

✔ Graph Paper

✔ Building Design

✔ Floor Tiles

✔ Chess Board
"""

# ===========================================================
# 04_Definition
# ===========================================================

"""
Parallel Lines

দুটি Line-এর Slope সমান হলে

তারা Parallel হয়।

তারা কখনো একে অপরকে ছেদ করে না।

------------------------------------

Perpendicular Lines

দুটি Line-এর Slope-এর গুণফল

-1

হলে

তারা Perpendicular হয়।

অর্থাৎ,

তারা ৯০° কোণে মিলিত হয়।
"""

# ===========================================================
# 05_Formula
# ===========================================================

"""
Parallel Lines

m₁ = m₂

------------------------------------

Perpendicular Lines

m₁ × m₂ = -1

------------------------------------

Perpendicular Slope

যদি

m = 2

হয়,

তাহলে

Perpendicular Slope

= -1/2

অর্থাৎ,

Negative Reciprocal।
"""

# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
Parallel Lines

দুইটি Line যদি একই হারে উপরে ওঠে
অথবা নিচে নামে,

তাহলে তাদের ঢাল (Slope)

একই হবে।

তাই,

m₁ = m₂

------------------------------------

Perpendicular Lines

ধরি,

একটি Line-এর Slope

m = 2

এখন,

৯০° ঘুরলে

নতুন Line-এর Slope হবে

-1/2

কারণ,

2 × (-1/2)

=

-1

সাধারণভাবে,

m₁ × m₂ = -1

এটাই Perpendicular Line-এর নিয়ম।

এই ধারণাটি বিশ্লেষণাত্মক জ্যামিতি
এবং Trigonometry-এর উপর ভিত্তি করে এসেছে।
"""

# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
Parallel Lines


      /
     /
    /
   /
  /

----------------------------

      /
     /
    /
   /
  /


Slope

m₁ = m₂

------------------------------------

Perpendicular Lines


        |
        |
--------+---------
        |
        |


Slope

m₁ × m₂ = -1

------------------------------------

উদাহরণ

Line 1

y = 2x + 3

Slope = 2

Line 2

y = 2x - 5

Slope = 2

দুইটি Line Parallel।

------------------------------------

Line 3

y = -1/2 x + 7

Slope = -1/2

2 × (-1/2)

=

-1

অতএব,

Line 1 এবং Line 3

Perpendicular।
"""

# ===========================================================
# 08_Examples
# ===========================================================

print("=" * 60)
print("Example 1 : Parallel")
print("=" * 60)

m1 = 3
m2 = 3

if m1 == m2:
    print("Lines are Parallel")
else:
    print("Lines are NOT Parallel")

print()

print("=" * 60)
print("Example 2 : Perpendicular")
print("=" * 60)

m1 = 2
m2 = -0.5

if m1 * m2 == -1:
    print("Lines are Perpendicular")
else:
    print("Lines are NOT Perpendicular")

print()

print("=" * 60)
print("Example 3")
print("=" * 60)

m1 = -4
m2 = 0.25

if m1 * m2 == -1:
    print("Perpendicular")
else:
    print("Not Perpendicular")

print()

print("=" * 60)
print("Example 4")
print("=" * 60)

m1 = 5
m2 = 5

print("Parallel :", m1 == m2)

"""
Output

Lines are Parallel

Lines are Perpendicular

Perpendicular

Parallel : True
"""

# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
❌ ভুল ১

Parallel-এর জন্য

m₁ = -m₂

ভাবা।

সঠিক হলো

m₁ = m₂

------------------------------------

❌ ভুল ২

Perpendicular-এর জন্য

Slope সমান ভাবা।

আসলে

Negative Reciprocal।

------------------------------------

❌ ভুল ৩

m₁ + m₂ = -1

মনে করা।

সঠিক হলো

m₁ × m₂ = -1

------------------------------------

❌ ভুল ৪

Vertical ও Horizontal Line
বিশেষ ক্ষেত্রে ভুলে যাওয়া।

Horizontal Line-এর

Slope = 0

Vertical Line-এর

Slope Undefined

এবং

Horizontal ও Vertical Line
পরস্পর Perpendicular।

------------------------------------

❌ ভুল ৫

Floating Point Number তুলনা করতে
== ব্যবহার করলে অনেক সময় সমস্যা হতে পারে।

বাস্তব প্রোগ্রামে
Tolerance ব্যবহার করা ভালো।
"""

# ===========================================================
# 10_Exercises
# ===========================================================

"""
১।

Slope 4 এবং 4

Parallel কি না নির্ণয় করো।

----------------------------------

২।

Slope 3 এবং -1/3

Perpendicular কি না নির্ণয় করো।

----------------------------------

৩।

Slope -5 হলে

Perpendicular Slope বের করো।

----------------------------------

৪।

একটি Function লেখো

is_parallel(m1, m2)

----------------------------------

৫।

একটি Function লেখো

is_perpendicular(m1, m2)

----------------------------------

৬।

User থেকে দুইটি Slope নিয়ে

Parallel না Perpendicular

তা নির্ণয় করো।

----------------------------------

৭।

Horizontal Line এবং Vertical Line-এর
সম্পর্ক ব্যাখ্যা করো।
"""

# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
Parallel এবং Perpendicular ধারণা
AI ও Computer Science-এর বিভিন্ন ক্ষেত্রে ব্যবহৃত হয়।

১।

Computer Graphics

Object Alignment

----------------------------------

২।

Computer Vision

Edge Detection

এবং

Image Geometry

----------------------------------

৩।

Robotics

Robot-এর Movement Direction

এবং

Obstacle Avoidance

----------------------------------

৪।

CAD Software

Building ও Mechanical Design

----------------------------------

৫।

3D Graphics

Surface Orientation

----------------------------------

৬।

Machine Learning

যদিও সরাসরি Parallel বা Perpendicular Line
খুব বেশি ব্যবহৃত হয় না,

তবে

Vectors,

Linear Algebra,

Hyperplane,

Decision Boundary,

Principal Component Analysis (PCA)

ইত্যাদি বিষয় বুঝতে
এই ধারণাগুলো গুরুত্বপূর্ণ ভিত্তি তৈরি করে।

বিশেষ করে Support Vector Machine (SVM)-এ
Hyperplane-এর সাথে Perpendicular Vector
(Normal Vector) একটি মৌলিক ধারণা।
"""

# ===========================================================
# End of File
# ===========================================================