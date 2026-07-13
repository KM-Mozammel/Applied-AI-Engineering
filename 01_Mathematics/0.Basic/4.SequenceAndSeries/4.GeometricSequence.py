"""
===========================================================
Geometric Sequence (গুণোত্তর ধারা)
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
Arithmetic Sequence-এ প্রতিটি সংখ্যা
একটি নির্দিষ্ট সংখ্যা (Difference) যোগ করে বাড়ে।

যেমন,

2, 4, 6, 8, 10

এখানে প্রতিবার +2 যোগ হচ্ছে।

কিন্তু সব Sequence এমন নয়।

কিছু Sequence-এ প্রতিবার
একটি নির্দিষ্ট সংখ্যা দিয়ে গুণ করা হয়।

যেমন,

2, 4, 8, 16, 32

এখানে,

2 × 2 = 4

4 × 2 = 8

8 × 2 = 16

16 × 2 = 32

এ ধরনের Sequence-কে বলা হয়

Geometric Sequence (গুণোত্তর ধারা)।
"""

# ===========================================================
# 02_WhyThisConceptExistsInRealtionTohistory
# ===========================================================

"""
Geometric Sequence বহু শতাব্দী ধরে ব্যবহৃত হচ্ছে।

প্রাচীন গণিতবিদরা লক্ষ্য করেছিলেন,

অনেক ঘটনা

যোগ (Addition)

দিয়ে নয়,

বরং

গুণ (Multiplication)

দিয়ে বৃদ্ধি পায়।

যেমন,

✔ Population Growth

✔ Compound Interest

✔ Bacteria Growth

✔ Radioactive Decay

✔ Tree Branching

এসব বুঝতেই Geometric Sequence-এর ধারণা আসে।
"""

# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
ধরো,

তুমি একটি ভিডিও YouTube-এ আপলোড করলে।

প্রথম দিন

100 View

প্রতিদিন View দ্বিগুণ হচ্ছে।

দিন ১

100

দিন ২

200

দিন ৩

400

দিন ৪

800

দিন ৫

1600

এটি একটি Geometric Sequence।

আরও উদাহরণ—

✔ Compound Interest

✔ Virus Spread

✔ Social Media Growth

✔ Rabbit Population

✔ Cell Division
"""

# ===========================================================
# 04_Definition
# ===========================================================

"""
Geometric Sequence হলো

এমন একটি Sequence,

যেখানে

প্রতিটি পরবর্তী Term

আগের Term-কে

একটি নির্দিষ্ট সংখ্যা দিয়ে

গুণ করলে পাওয়া যায়।

এই নির্দিষ্ট সংখ্যাকে বলে

Common Ratio (r)।
"""

# ===========================================================
# 05_Formula
# ===========================================================

"""
First Term = a

Common Ratio = r

------------------------------------

Second Term

a × r

------------------------------------

Third Term

a × r²

------------------------------------

Fourth Term

a × r³

------------------------------------

n-th Term

aₙ = arⁿ⁻¹

যেখানে,

a = First Term

r = Common Ratio

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

ar

Third Term

arr

=

ar²

Fourth Term

ar³

...

প্রতিবার

একবার করে

r

দিয়ে গুণ হচ্ছে।

সুতরাং,

n-th Term পর্যন্ত

মোট

(n−1)

বার

r

দিয়ে গুণ করা হবে।

অতএব,

aₙ = arⁿ⁻¹

এটাই Geometric Sequence-এর সূত্র।
"""

# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
Example

2

↓

2×2

↓

4

↓

4×2

↓

8

↓

8×2

↓

16

↓

16×2

↓

32

Difference

❌ সমান নয়

Ratio

✔ সবসময় সমান

4 / 2 = 2

8 / 4 = 2

16 / 8 = 2

32 / 16 = 2

এটাই Common Ratio।
"""

# ===========================================================
# 08_Examples
# ===========================================================

print("=" * 60)
print("Example 1")
print("=" * 60)

a = 2
r = 2

for n in range(1, 6):
    term = a * (r ** (n - 1))
    print(f"Term {n} = {term}")

print()

print("=" * 60)
print("Example 2")
print("=" * 60)

a = 5
r = 3

for n in range(1, 6):
    term = a * (r ** (n - 1))
    print(f"Term {n} = {term}")

print()

print("=" * 60)
print("Example 3")
print("=" * 60)

a = 81
r = 1/3

for n in range(1, 6):
    term = a * (r ** (n - 1))
    print(f"Term {n} = {term}")

"""
Output

Term 1 = 2
Term 2 = 4
Term 3 = 8
Term 4 = 16
Term 5 = 32

-----------------------

Term 1 = 5
Term 2 = 15
Term 3 = 45
Term 4 = 135
Term 5 = 405

-----------------------

Term 1 = 81
Term 2 = 27
Term 3 = 9
Term 4 = 3
Term 5 = 1
"""

# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
❌ ভুল ১

Difference এবং Ratio
একই মনে করা।

Arithmetic → Difference

Geometric → Ratio

------------------------------------

❌ ভুল ২

a × rⁿ

লেখা।

সঠিক হলো

arⁿ⁻¹

------------------------------------

❌ ভুল ৩

r = 0

হলে সব Term কী হবে
তা না বোঝা।

------------------------------------

❌ ভুল ৪

Negative Ratio

(-2)

এর ক্ষেত্রে
Sign পরিবর্তন ভুল করা।

------------------------------------

❌ ভুল ৫

Sequence এবং Series
গুলিয়ে ফেলা।
"""

# ===========================================================
# 10_Exercises
# ===========================================================

"""
১।

3, 6, 12, 24,...

এর Common Ratio বের করো।

----------------------------------

২।

First Term = 5

Ratio = 3

১০ম Term বের করো।

----------------------------------

৩।

First Term = 81

Ratio = 1/3

৬ষ্ঠ Term বের করো।

----------------------------------

৪।

নিজের

geometric_term()

Function লেখো।

----------------------------------

৫।

User থেকে

a

r

n

Input নিয়ে

n-th Term বের করো।

----------------------------------

৬।

একটি Geometric Sequence-এর
প্রথম ১০টি Term Print করো।
"""

# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
Geometric Sequence
Machine Learning ও Computer Science-এ
খুবই গুরুত্বপূর্ণ।

১।

Compound Growth

ডেটার দ্রুত বৃদ্ধি বোঝাতে।

----------------------------------

২।

Learning Rate Decay

Deep Learning-এ
Learning Rate ধীরে ধীরে কমানো।

----------------------------------

৩।

Population Modeling

Simulation-এ।

----------------------------------

৪।

Binary Tree

প্রতিটি Level-এ Node সংখ্যা।

----------------------------------

৫।

Computer Graphics

Mipmaps
এবং
Image Scaling।

----------------------------------

৬।

Machine Learning

Exponential Growth,
Exponential Decay,
Probability,
Neural Network Mathematics

বোঝার ভিত্তি তৈরি করে।

Geometric Sequence
পরবর্তীতে Geometric Series,
Exponential Function,
Logarithm
এবং Deep Learning Mathematics
বোঝার জন্য অত্যন্ত গুরুত্বপূর্ণ।
"""

# ===========================================================
# End of File
# ===========================================================