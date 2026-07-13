"""
===========================================================
Arithmetic Sequence (সমানুত্তর ধারা)
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
গণিতে অনেক সময় এমন সংখ্যার তালিকা দেখা যায়,
যেখানে প্রতিটি সংখ্যা একটি নির্দিষ্ট পরিমাণ করে বাড়ে
অথবা কমে।

যেমন,

2, 5, 8, 11, 14, ...

এখানে প্রতিটি নতুন সংখ্যা
আগের সংখ্যার সাথে 3 যোগ করে তৈরি হয়েছে।

আবার,

20, 16, 12, 8, 4, ...

এখানে প্রতিবার 4 বিয়োগ করা হয়েছে।

এ ধরনের সংখ্যার ধারাকে বলা হয়

Arithmetic Sequence (সমানুত্তর ধারা)।

এটি Sequence-এর সবচেয়ে মৌলিক ধরনের একটি।
"""

# ===========================================================
# 02_WhyThisConceptExistsInRealtionTohistory
# ===========================================================

"""
প্রাচীনকাল থেকেই মানুষ

✔ দিন গণনা

✔ ধাপ (Steps)

✔ সিঁড়ির সংখ্যা

✔ সৈন্যদের সারি

✔ জমির পরিমাপ

ইত্যাদিতে সমান ব্যবধানের সংখ্যা ব্যবহার করত।

পরে গণিতবিদরা লক্ষ্য করলেন,

যেসব সংখ্যার মধ্যে
Difference সবসময় একই থাকে,

সেগুলোকে একটি আলাদা শ্রেণিতে রাখা যায়।

এভাবেই Arithmetic Sequence-এর ধারণা তৈরি হয়।

পরবর্তীতে এটি Algebra,
Calculus,
Computer Science
এবং Machine Learning-এর ভিত্তি হয়ে ওঠে।
"""

# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
ধরো,

তুমি প্রতিদিন 5 কিলোমিটার করে হাঁটো।

Day 1

5 km

Day 2

10 km

Day 3

15 km

Day 4

20 km

Day 5

25 km

প্রতিদিনই

5 km

করে বাড়ছে।

এটি একটি Arithmetic Sequence।

আরও উদাহরণ—

✔ Salary Increment

✔ Stair Steps

✔ Classroom Roll Number

✔ House Numbers

✔ Calendar Dates
"""

# ===========================================================
# 04_Definition
# ===========================================================

"""
Arithmetic Sequence হলো

এমন একটি সংখ্যার ধারা,

যেখানে

পরপর দুইটি সংখ্যার পার্থক্য

সবসময় সমান থাকে।

এই নির্দিষ্ট পার্থক্যকে বলা হয়

Common Difference (d)।

যদি,

a = First Term

d = Common Difference

হয়,

তাহলে পুরো Sequence
একটি সূত্র দিয়ে প্রকাশ করা যায়।
"""

# ===========================================================
# 05_Formula
# ===========================================================

"""
First Term

a

------------------------------------

Second Term

a + d

------------------------------------

Third Term

a + 2d

------------------------------------

Fourth Term

a + 3d

------------------------------------

n-th Term

aₙ = a + (n−1)d

যেখানে,

a = First Term

d = Common Difference

n = Term Number
"""

# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
ধরি,

First Term

a

Second Term

a + d

Third Term

a + d + d

=

a + 2d

Fourth Term

a + 3d

...

প্রথম Term থেকে

n-th Term পর্যন্ত যেতে হলে

মোট

(n−1)

বার

d

যোগ করতে হবে।

অতএব,

aₙ = a + (n−1)d

এটাই Arithmetic Sequence-এর সূত্র।
"""

# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
Example

2

↓

+3

↓

5

↓

+3

↓

8

↓

+3

↓

11

↓

+3

↓

14

প্রতিবার

একই Difference

(+3)

যোগ হচ্ছে।

এটাই Arithmetic Sequence-এর
সবচেয়ে গুরুত্বপূর্ণ বৈশিষ্ট্য।
"""

# ===========================================================
# 08_Examples
# ===========================================================

print("=" * 60)
print("Example 1")
print("=" * 60)

a = 2
d = 3

for n in range(1, 6):
    term = a + (n - 1) * d
    print(f"Term {n} = {term}")

print()

print("=" * 60)
print("Example 2")
print("=" * 60)

a = 20
d = -4

for n in range(1, 6):
    term = a + (n - 1) * d
    print(f"Term {n} = {term}")

print()

print("=" * 60)
print("Example 3")
print("=" * 60)

a = 100
d = 50

for n in range(1, 8):
    term = a + (n - 1) * d
    print(f"Term {n} = {term}")

"""
Output

Term 1 = 2
Term 2 = 5
Term 3 = 8
Term 4 = 11
Term 5 = 14

-----------------------

Term 1 = 20
Term 2 = 16
Term 3 = 12
Term 4 = 8
Term 5 = 4

-----------------------

Term 1 = 100
Term 2 = 150
Term 3 = 200
...
"""

# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
❌ ভুল ১

Common Difference ভুল বের করা।

Difference = Current Term − Previous Term

------------------------------------

❌ ভুল ২

n এর পরিবর্তে

n−1

ব্যবহার করতে ভুলে যাওয়া।

সঠিক সূত্র

aₙ = a + (n−1)d

------------------------------------

❌ ভুল ৩

Arithmetic Sequence

এবং

Geometric Sequence

গুলিয়ে ফেলা।

Arithmetic

→ যোগ বা বিয়োগ

Geometric

→ গুণ বা ভাগ

------------------------------------

❌ ভুল ৪

First Term ভুল ধরা।

------------------------------------

❌ ভুল ৫

Negative Difference থাকলে
Sequence Arithmetic নয় ভাবা।

Negative Difference হলেও
এটি Arithmetic Sequence হতে পারে।
"""

# ===========================================================
# 10_Exercises
# ===========================================================

"""
১।

3, 7, 11, 15,...

এর Common Difference বের করো।

----------------------------------

২।

First Term = 5

Difference = 4

১০ম Term বের করো।

----------------------------------

৩।

First Term = 50

Difference = -5

১৫তম Term বের করো।

----------------------------------

৪।

নিজের

arithmetic_term()

Function লেখো।

----------------------------------

৫।

User থেকে

a

d

n

Input নিয়ে

n-th Term বের করো।

----------------------------------

৬।

একটি Arithmetic Sequence-এর
প্রথম ২০টি Term Print করো।
"""

# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
Arithmetic Sequence
Machine Learning-এ সরাসরি Model হিসেবে
ব্যবহৃত না হলেও,

এর ধারণা অনেক জায়গায় ব্যবহৃত হয়।

১।

Loop Iteration

সমান ধাপে Counter বৃদ্ধি।

----------------------------------

২।

Index Generation

Array ও Dataset Traversal।

----------------------------------

৩।

Learning Schedule

সমান হারে Parameter পরিবর্তন।

----------------------------------

৪।

Data Sampling

সমান Interval-এ Data নেওয়া।

----------------------------------

৫।

Computer Graphics

সমান দূরত্বে Object Placement।

----------------------------------

৬।

Machine Learning Mathematics

Arithmetic Sequence
পরবর্তীতে

Arithmetic Series,
Sigma Notation (Σ),
Linear Function,
Linear Regression

এবং

Discrete Mathematics

বোঝার ভিত্তি তৈরি করে।
"""

# ===========================================================
# End of File
# ===========================================================