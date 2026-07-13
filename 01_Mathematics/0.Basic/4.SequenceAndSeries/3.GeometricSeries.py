"""
===========================================================
Geometric Series (গুণোত্তর ধারার যোগফল)
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
Geometric Sequence শেখার পরে
পরবর্তী প্রশ্ন আসে—

যদি পুরো Sequence-এর সব Term যোগ করতে চাই,
তাহলে কী করবো?

উদাহরণ,

2, 4, 8, 16, 32

এগুলো একটি Geometric Sequence।

এখন,

2 + 4 + 8 + 16 + 32

=

62

এই যোগফলকে বলা হয়

Geometric Series।

অর্থাৎ,

Geometric Series হলো

Geometric Sequence-এর
সব Term-এর যোগফল।
"""

# ===========================================================
# 02_WhyThisConceptExistsInRealtionTohistory
# ===========================================================

"""
প্রকৃতিতে অনেক কিছু
গুণ (Multiplication) আকারে বৃদ্ধি পায়।

যেমন,

✔ Compound Interest

✔ Population Growth

✔ Virus Spread

✔ Radioactive Decay

✔ Cell Division

এসব ক্ষেত্রে শুধু Sequence জানলেই হয় না।

মোট বৃদ্ধি বা মোট পরিমাণও জানতে হয়।

এই সমস্যার সমাধানই

Geometric Series।

এটি বহু শতাব্দী ধরে
গণিত, অর্থনীতি এবং বিজ্ঞানে ব্যবহৃত হয়ে আসছে।
"""

# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
ধরো,

তুমি একটি ব্যাংকে

1000 টাকা

জমা রাখলে।

প্রতি বছর টাকা

দ্বিগুণ হচ্ছে।

বছর ১

1000

বছর ২

2000

বছর ৩

4000

বছর ৪

8000

এখন প্রশ্ন—

মোট কত টাকা জমা হয়েছে?

এটি Geometric Series-এর সমস্যা।

আরও উদাহরণ—

✔ Compound Interest

✔ Pyramid Scheme Analysis

✔ Bacteria Growth

✔ Investment Return

✔ Computer Memory Growth
"""

# ===========================================================
# 04_Definition
# ===========================================================

"""
Geometric Series হলো

একটি Geometric Sequence-এর
সবগুলো Term-এর যোগফল।

যদি,

a = First Term

r = Common Ratio

n = Number of Terms

হয়,

তাহলে

Series-এর Sum
একটি নির্দিষ্ট সূত্র দিয়ে বের করা যায়।
"""

# ===========================================================
# 05_Formula
# ===========================================================

"""
যদি

r ≠ 1

হয়,

তাহলে,

            a(rⁿ−1)
S = --------------------
          r−1

অথবা,

            a(1-rⁿ)
S = --------------------
           1-r

(দুইটি সূত্র একই,
শুধু লেখার ধরন আলাদা।)

------------------------------------

যদি

r = 1

হয়,

তাহলে,

S = a × n

কারণ সবগুলো Term সমান।
"""

# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
ধরি,

S

=

a + ar + ar² + ... + arⁿ⁻¹

এখন,

পুরো সমীকরণকে

r

দিয়ে গুণ করি।

rS

=

ar + ar² + ar³ + ... + arⁿ

এখন,

দুইটি সমীকরণ বিয়োগ করি।

rS − S

=

arⁿ − a

অর্থাৎ,

S(r−1)

=

a(rⁿ−1)

অতএব,

            a(rⁿ−1)
S = --------------------
          r−1

এটাই Geometric Series-এর সূত্র।
"""

# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
Sequence

2

4

8

16

32

↓

Series

2 + 4 + 8 + 16 + 32

↓

Step

S

=

2 + 4 + 8 + 16 + 32

2S

=

4 + 8 + 16 + 32 + 64

Subtract

↓

2S − S

=

64 − 2

↓

S = 62

এভাবেই Formula তৈরি হয়েছে।
"""

# ===========================================================
# 08_Examples
# ===========================================================

print("=" * 60)
print("Example 1")
print("=" * 60)

a = 2
r = 2
n = 5

S = a * (r ** n - 1) / (r - 1)

print("Sum =", S)

print()

print("=" * 60)
print("Example 2")
print("=" * 60)

a = 3
r = 3
n = 4

S = a * (r ** n - 1) / (r - 1)

print("Sum =", S)

print()

print("=" * 60)
print("Example 3")
print("=" * 60)

a = 5
r = 1
n = 8

if r == 1:
    S = a * n
else:
    S = a * (r ** n - 1) / (r - 1)

print("Sum =", S)

"""
Output

Sum = 62

Sum = 120

Sum = 40
"""

# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
❌ ভুল ১

Geometric Sequence

এবং

Geometric Series

এক মনে করা।

Sequence

→ সংখ্যার তালিকা

Series

→ সংখ্যাগুলোর যোগফল

------------------------------------

❌ ভুল ২

Arithmetic Series-এর Formula
ব্যবহার করা।

------------------------------------

❌ ভুল ৩

r = 1

হলে

Division by Zero

হয়ে যায়।

এই ক্ষেত্রে,

S = an

ব্যবহার করতে হবে।

------------------------------------

❌ ভুল ৪

rⁿ এর পরিবর্তে

rⁿ⁻¹

লেখা।

------------------------------------

❌ ভুল ৫

Negative Ratio-এর ক্ষেত্রে
Sign পরিবর্তন ভুল করা।
"""

# ===========================================================
# 10_Exercises
# ===========================================================

"""
১।

2 + 4 + 8 + 16 + 32

এর যোগফল বের করো।

----------------------------------

২।

First Term = 5

Ratio = 3

Term = 6

Series Sum বের করো।

----------------------------------

৩।

First Term = 100

Ratio = 2

Term = 10

Sum বের করো।

----------------------------------

৪।

নিজের

geometric_series_sum()

Function লেখো।

----------------------------------

৫।

User থেকে

a

r

n

Input নিয়ে

Series Sum বের করো।

----------------------------------

৬।

r = 1

হলে আলাদা Logic ব্যবহার করো।
"""

# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
Geometric Series
Machine Learning এবং Computer Science-এ
খুবই গুরুত্বপূর্ণ।

১।

Discounted Reward

Reinforcement Learning-এ

γ + γ² + γ³ ...

----------------------------------

২।

Learning Rate Decay

ধীরে ধীরে Learning Rate কমাতে।

----------------------------------

৩।

Signal Processing

Repeated Signal Analysis।

----------------------------------

৪।

Computer Graphics

Recursive Rendering।

----------------------------------

৫।

Algorithm Analysis

Divide and Conquer Algorithm-এর
Complexity বিশ্লেষণে।

----------------------------------

৬।

Deep Learning

Exponential Moving Average (EMA)

এবং

Optimization Algorithm

(Adam, RMSProp)

বোঝার জন্য
Geometric Series অত্যন্ত গুরুত্বপূর্ণ।

পরবর্তীতে,

Infinite Series,
Calculus,
Taylor Series,
Probability,
Markov Process

শেখার ভিত্তি তৈরি করে।
"""

# ===========================================================
# End of File
# ===========================================================