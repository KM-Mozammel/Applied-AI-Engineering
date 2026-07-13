"""
===========================================================
polynomials.py
Algebra Essentials - Chapter 05
Language: Bengali
===========================================================

Polynomial হলো এমন একটি Algebraic Expression
যেখানে Variable-এর Exponent (Power)
শুধুমাত্র 0 বা ধনাত্মক পূর্ণসংখ্যা (0, 1, 2, 3, ...)
হতে পারে।

Examples

5

x

2x + 3

x² + 3x + 2

4x³ - 2x² + 7x - 5

সবগুলোই Polynomial।
"""

# ===========================================================
# 01_Introduction
# ===========================================================

"""
এখন পর্যন্ত আমরা শিখেছি

Variable

↓

Expression

↓

Equation

↓

Factorization

এখন আমরা শিখব Polynomial।

Polynomial হলো Algebra-এর সবচেয়ে বেশি ব্যবহৃত
Expression-এর একটি ধরন।

Machine Learning, Physics,
Computer Graphics,
Signal Processing,
Optimization—

সবখানেই Polynomial ব্যবহৃত হয়।
"""

# ===========================================================
# 02_WhyThisConceptExists
# ===========================================================

"""
সব Expression এক ধরনের নয়।

Examples

x + 5

x² + 3x + 2

3x³ + x² + 8

এগুলো সুন্দরভাবে কাজ করে।

কিন্তু

1/x

√x

x⁻¹

এগুলো অন্য ধরনের Expression।

তাই Mathematics এমন Expression-গুলোর
একটি বিশেষ Category তৈরি করেছে।

তার নাম

Polynomial।
"""

# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
ধরো,

একটি Building তৈরি হচ্ছে।

Building তৈরি হয়

Floor 0

Floor 1

Floor 2

Floor 3

...

Negative Floor নেই।

Half Floor নেই।

Polynomial-ও ঠিক এমন।

Power হবে

0

1

2

3

4

...

Allowed

কিন্তু

-1

1/2

√

Allowed নয়।

--------------------------------

Polynomial মানে

Legal Power

Illegal Power নয়।
"""

# ===========================================================
# 04_Definition
# ===========================================================

"""
Definition

Polynomial হলো এমন একটি Algebraic Expression
যেখানে

Coefficient

×

Variable

^

Non-negative Integer

থাকে।

General Form

aₙxⁿ + aₙ₋₁xⁿ⁻¹ + ...

+

a₂x²

+

a₁x

+

a₀

যেখানে

a = Coefficient

x = Variable

n = Non-negative Integer
"""

# ===========================================================
# 05_Formula
# ===========================================================

"""
General Polynomial

P(x)

=

aₙxⁿ

+

aₙ₋₁xⁿ⁻¹

+

...

+

a₁x

+

a₀

--------------------------------

Degree

Highest Power

--------------------------------

Constant Polynomial

5

--------------------------------

Linear Polynomial

2x + 1

--------------------------------

Quadratic Polynomial

x² + 5x + 6

--------------------------------

Cubic Polynomial

x³ + 2x² + x + 7
"""

# ===========================================================
# 06_Derivation
# ===========================================================

"""
ধরো,

আমরা বিভিন্ন Power ব্যবহার করছি।

x⁰

x¹

x²

x³

...

এগুলোকে Coefficient দিয়ে গুণ করি।

5x³

+

2x²

+

7x

+

1

এখন এগুলো যোগ করি।

5x³ + 2x² + 7x + 1

এটাই Polynomial।

--------------------------------

যদি

√x

অথবা

1/x

ব্যবহার করি

তাহলে এটি আর Polynomial থাকবে না।
"""

# ===========================================================
# 07_InternalWorking
# ===========================================================

"""
Polynomial

4x³ + 2x² + 5x + 8

↓

Terms

---------------------

4x³

↓

Degree = 3

---------------------

2x²

↓

Degree = 2

---------------------

5x

↓

Degree = 1

---------------------

8

↓

Degree = 0

--------------------------------

Highest Degree

↓

3

Polynomial Degree = 3
"""

# ===========================================================
# 08_Examples
# ===========================================================

"""
Example 1

5

Polynomial

Degree = 0

----------------------------

Example 2

3x + 2

Polynomial

Degree = 1

----------------------------

Example 3

x² + 5x + 6

Polynomial

Degree = 2

----------------------------

Example 4

2x³ + 4x² - x + 8

Polynomial

Degree = 3

----------------------------

Example 5

7x⁵ + x² + 10

Polynomial

Degree = 5
"""

# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
Mistake 1

1/x

Polynomial

Wrong

কারণ

Power = -1

----------------------------

Mistake 2

√x

Polynomial

Wrong

কারণ

Power = 1/2

----------------------------

Mistake 3

x⁻²

Polynomial

Wrong

Negative Power

----------------------------

Mistake 4

2ˣ

Polynomial

Wrong

Variable Exponent-এ আছে।

Polynomial-এ

Exponent অবশ্যই Constant হবে।

----------------------------

Mistake 5

Degree বের করার সময়

Coefficient দেখা।

Wrong

Degree নির্ভর করে

Highest Power-এর উপর।
"""

# ===========================================================
# 10_Exercises
# ===========================================================

"""
Level 1

বল Polynomial কি না।

1)

5

----------------------------

2)

x + 2

----------------------------

3)

x² + 7

----------------------------

4)

1/x

============================

Level 2

Degree বের করো।

1)

2x² + 7x + 3

----------------------------

2)

5x⁴ + 3x² + 8

----------------------------

3)

9

----------------------------

4)

7x⁶ + 5x + 2

============================

Challenge

নিজে

১টি Linear

১টি Quadratic

১টি Cubic

Polynomial লিখো।
"""

# ===========================================================
# 11_AIUsage
# ===========================================================

"""
Polynomial AI-এ খুব গুরুত্বপূর্ণ।

Polynomial Regression

y

=

a₀

+

a₁x

+

a₂x²

+

a₃x³

...

এটি Non-linear Relationship শেখে।

--------------------------------

Computer Graphics

Bezier Curve

Polynomial ব্যবহার করে।

--------------------------------

Optimization

Polynomial Cost Function

ব্যবহার হয়।

--------------------------------

Taylor Series

Complex Function-কে

Polynomial দিয়ে Approximate করে।

Deep Learning-এ Activation Function-এর
Approximation করতেও Polynomial ব্যবহৃত হয়।
"""

# ===========================================================
# Summary
# ===========================================================

"""
✔ Polynomial হলো একটি বিশেষ ধরনের Expression।

✔ Power অবশ্যই

0, 1, 2, 3 ...

হতে হবে।

✔ Negative Power বা Fractional Power
থাকলে Polynomial নয়।

✔ Degree = Highest Power।

✔ Polynomial হলো
Calculus,
Linear Algebra,
Machine Learning,
Computer Graphics,
Scientific Computing-এর
মৌলিক ভিত্তিগুলোর একটি।

Next Chapter

functions.py
"""