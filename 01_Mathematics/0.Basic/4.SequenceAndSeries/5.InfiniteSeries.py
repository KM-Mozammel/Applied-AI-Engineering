"""
===========================================================
Infinite Series (অসীম ধারা)
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
এখন পর্যন্ত আমরা Arithmetic Series এবং
Geometric Series শিখেছি।

সেখানে একটি নির্দিষ্ট সংখ্যক (Finite)
Term ছিল।

কিন্তু যদি Series-এর

শেষই না থাকে?

যেমন,

1 + 1/2 + 1/4 + 1/8 + 1/16 + ...

এখানে Term অনন্ত (Infinite)।

এ ধরনের Series-কে বলা হয়

Infinite Series (অসীম ধারা)।

আশ্চর্যের বিষয়,

সব Infinite Series-এর Sum অসীম হয় না।

কিছু Infinite Series-এর
একটি নির্দিষ্ট Sum থাকে।

এই ধারণা Calculus-এর অন্যতম ভিত্তি।
"""

# ===========================================================
# 02_WhyThisConceptExistsInRealtionTohistory
# ===========================================================

"""
প্রাচীন Greek গণিতবিদরা
Infinite Series নিয়ে গবেষণা শুরু করেন।

পরে,

Isaac Newton,

Gottfried Leibniz,

Leonhard Euler

Infinite Series ব্যবহার করে

✔ Calculus

✔ Trigonometry

✔ Physics

✔ Astronomy

উন্নত করেন।

বর্তমানে,

Computer Science,
Machine Learning,
Signal Processing,
Quantum Physics

সব ক্ষেত্রেই Infinite Series ব্যবহৃত হয়।
"""

# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
ধরো,

তুমি একটি দেয়ালের দিকে হাঁটছো।

প্রথম ধাপে

অর্ধেক পথ গেলে।

পরের ধাপে

বাকি পথের অর্ধেক গেলে।

তারপর আবার
বাকি পথের অর্ধেক।

তুমি কখনো পুরো পথ
এক ধাপে শেষ করছো না।

কিন্তু,

বাস্তবে তুমি
দেয়ালের খুব কাছাকাছি পৌঁছে যাও।

এটাই Infinite Series-এর ধারণা।

আরও উদাহরণ—

✔ Bouncing Ball

✔ Compound Interest

✔ Signal Decay

✔ Zooming Animation

✔ Exponential Decay
"""

# ===========================================================
# 04_Definition
# ===========================================================

"""
Infinite Series হলো

এমন একটি Series,

যেখানে

Term-এর সংখ্যা

অসীম (∞)।

যদি,

Series-এর Partial Sum

একটি নির্দিষ্ট সংখ্যার দিকে যায়,

তাহলে তাকে বলে

Convergent Series।

আর যদি

কোনো নির্দিষ্ট মানে না পৌঁছায়,

তাহলে তাকে বলে

Divergent Series।
"""

# ===========================================================
# 05_Formula
# ===========================================================

"""
Infinite Geometric Series

শুধুমাত্র তখনই Sum থাকে,

যখন,

|r| < 1

হয়।

Formula

          a
S = -------------
        1 - r

যেখানে,

a = First Term

r = Common Ratio

এবং,

|r| < 1

------------------------------------

যদি,

|r| ≥ 1

হয়,

তাহলে

Series Divergent।

কোনো Finite Sum নেই।
"""

# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
Finite Geometric Series

            a(1-rⁿ)
Sₙ = -------------------
           1-r

এখন,

যদি,

|r| < 1

হয়,

তাহলে,

rⁿ

→ 0

যখন,

n → ∞

অতএব,

             a(1-0)
S = -------------------
            1-r

অর্থাৎ,

          a
S = -------------
        1-r

এটাই Infinite Geometric Series-এর Formula।

এটি Calculus-এর Limit ধারণার উপর ভিত্তি করে।
"""

# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
Example

1

+

1/2

+

1/4

+

1/8

+

1/16

+

...

↓

Partial Sum

1

↓

1.5

↓

1.75

↓

1.875

↓

1.9375

↓

1.96875

↓

...

↓

2

Series-এর Sum

2-এর দিকে এগিয়ে যাচ্ছে।

এটিকে বলে

Convergence।

------------------------------------

Example

1 + 2 + 4 + 8 + 16 + ...

↓

1

↓

3

↓

7

↓

15

↓

31

↓

63

↓

...

↓

∞

এটি কখনো
কোনো নির্দিষ্ট সংখ্যায় পৌঁছায় না।

এটিকে বলে

Divergence।
"""

# ===========================================================
# 08_Examples
# ===========================================================

print("=" * 60)
print("Example 1 : Convergent Series")
print("=" * 60)

a = 1
r = 0.5

S = a / (1 - r)

print("Infinite Sum =", S)

print()

print("=" * 60)
print("Example 2 : Divergent Series")
print("=" * 60)

a = 2
r = 2

if abs(r) < 1:
    S = a / (1 - r)
    print("Infinite Sum =", S)
else:
    print("Series is Divergent")

print()

print("=" * 60)
print("Example 3 : Partial Sum")
print("=" * 60)

a = 1
r = 0.5

partial_sum = 0

for i in range(10):
    partial_sum += a * (r ** i)
    print(f"After {i+1} Terms = {partial_sum:.6f}")

"""
Output

Infinite Sum = 2.0

Series is Divergent

After 1 Terms = 1.000000
After 2 Terms = 1.500000
After 3 Terms = 1.750000
...
After 10 Terms = 1.998047
"""

# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
❌ ভুল ১

সব Infinite Series-এর
Finite Sum আছে ভাবা।

আসলে,

শুধুমাত্র কিছু Series
Convergent।

------------------------------------

❌ ভুল ২

|r| < 1

শর্ত ভুলে যাওয়া।

------------------------------------

❌ ভুল ৩

Finite Geometric Series-এর Formula
Infinite Series-এ ব্যবহার করা।

------------------------------------

❌ ভুল ৪

Convergent

এবং

Divergent

গুলিয়ে ফেলা।

------------------------------------

❌ ভুল ৫

Partial Sum

এবং

Infinite Sum

একই মনে করা।
"""

# ===========================================================
# 10_Exercises
# ===========================================================

"""
১।

1 + 1/3 + 1/9 + 1/27 + ...

এর Infinite Sum বের করো।

----------------------------------

২।

5 + 2.5 + 1.25 + ...

এর Infinite Sum বের করো।

----------------------------------

৩।

2 + 4 + 8 + 16 + ...

Convergent না Divergent?

----------------------------------

৪।

নিজের

infinite_geometric_sum()

Function লেখো।

----------------------------------

৫।

User থেকে

a

এবং

r

Input নিয়ে

Infinite Sum বের করো।

----------------------------------

৬।

প্রথম ১৫টি Partial Sum Print করো।
"""

# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
Infinite Series
Machine Learning, AI এবং Computer Science-এর
একটি অত্যন্ত গুরুত্বপূর্ণ ভিত্তি।

১।

Gradient Descent

Repeated Update বিশ্লেষণে।

----------------------------------

২।

Reinforcement Learning

Discounted Future Reward

R = r + γr + γ²r + ...

----------------------------------

৩।

Deep Learning

Exponential Moving Average (EMA)

----------------------------------

৪।

Signal Processing

Infinite Impulse Response (IIR) Filter

----------------------------------

৫।

Probability

Markov Chain

এবং

Stochastic Process

----------------------------------

৬।

Calculus

Taylor Series,

Maclaurin Series,

Fourier Series

সবই Infinite Series-এর উপর ভিত্তি করে।

Infinite Series না বুঝলে,

Calculus,
Optimization,
Deep Learning,
Scientific Computing

সম্পূর্ণভাবে বোঝা কঠিন।

এটি উচ্চতর গণিতের অন্যতম গুরুত্বপূর্ণ ভিত্তি।
"""

# ===========================================================
# End of File
# ===========================================================