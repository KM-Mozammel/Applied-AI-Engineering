"""
===========================================================
Pythagorean Identity (পিথাগোরাসীয় পরিচিতি)
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
আমরা ইতোমধ্যে শিখেছি—

✔ Unit Circle

✔ Sine

✔ Cosine

✔ Tangent

এখন প্রশ্ন আসে,

Sine এবং Cosine-এর মধ্যে
কোনো সম্পর্ক আছে কি?

উত্তর হলো—

হ্যাঁ।

তাদের মধ্যে একটি অত্যন্ত গুরুত্বপূর্ণ সম্পর্ক রয়েছে।

সেটি হলো

Pythagorean Identity।

এই একটি সূত্র থেকেই

Trigonometry-এর
অনেক Formula তৈরি হয়েছে।

এটি Calculus,
Physics,
Computer Graphics,
Machine Learning

সবখানেই ব্যবহৃত হয়।
"""

# ===========================================================
# 02_WhyThisConceptExistsInRealtionTohistory
# ===========================================================

"""
প্রাচীন Greek গণিতবিদ

Pythagoras

Right Triangle-এর জন্য

একটি বিখ্যাত সূত্র দেন।

a² + b² = c²

পরে গণিতবিদরা লক্ষ্য করেন,

যদি Triangle-টি
Unit Circle-এর উপর হয়,

তাহলে

Hypotenuse = 1

হয়ে যায়।

সেখান থেকেই

Pythagorean Identity

উৎপন্ন হয়।

এই Identity
Trigonometry-এর
সবচেয়ে গুরুত্বপূর্ণ Identity।
"""

# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
ধরো,

একটি Robot Arm

ঘুরছে।

Arm-এর দৈর্ঘ্য

সবসময়

1

(Unit Length)

থাকে।

কিন্তু,

Horizontal Distance

এবং

Vertical Distance

পরিবর্তিত হয়।

তবুও,

তাদের Square-এর যোগফল

সবসময়

1

থাকে।

এটাই

Pythagorean Identity।

আরও উদাহরণ—

✔ Clock Hand

✔ Ferris Wheel

✔ Rotating Fan

✔ Satellite Rotation

✔ Drone Rotation
"""

# ===========================================================
# 04_Definition
# ===========================================================

"""
Pythagorean Identity হলো

Sine

এবং

Cosine

এর মধ্যে

একটি মৌলিক সম্পর্ক।

যে কোনো Angle-এর জন্য,

sin²θ + cos²θ

সবসময়

1

হয়।

এটি Unit Circle-এর
প্রতিটি Point-এর জন্য সত্য।
"""

# ===========================================================
# 05_Formula
# ===========================================================

"""
মূল সূত্র

sin²θ + cos²θ = 1

------------------------------------

এখান থেকে পাই,

sin²θ = 1 − cos²θ

------------------------------------

এবং,

cos²θ = 1 − sin²θ

------------------------------------

আরও একটি সম্পর্ক,

tanθ = sinθ / cosθ
"""

# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
Unit Circle-এর Equation

x² + y² = 1

আমরা জানি,

x = cosθ

এবং,

y = sinθ

এখন,

x² + y² = 1

এ বসাই,

(cosθ)² + (sinθ)² = 1

অর্থাৎ,

cos²θ + sin²θ = 1

একইভাবে লিখলে,

sin²θ + cos²θ = 1

এটাই

Pythagorean Identity।

অর্থাৎ,

এই Identity
সরাসরি

Unit Circle-এর Equation

থেকে এসেছে।
"""

# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
                 y
                 ↑

             ● (cosθ,sinθ)
            /|
           / |
          /  |
         /θ  |
        /____|
          x

----------------------------

Horizontal

=

cosθ

Vertical

=

sinθ

Radius

=

1

------------------------------------

Pythagoras

x² + y² = 1²

↓

cos²θ + sin²θ = 1

↓

sin²θ + cos²θ = 1

সব Angle-এর জন্য
এই Identity সত্য।
"""

# ===========================================================
# 08_Examples
# ===========================================================

import math

print("=" * 60)
print("Example 1 : 30°")
print("=" * 60)

angle = 30

sin_value = math.sin(math.radians(angle))
cos_value = math.cos(math.radians(angle))

result = sin_value ** 2 + cos_value ** 2

print("sin² + cos² =", round(result, 10))

print()

print("=" * 60)
print("Example 2 : 45°")
print("=" * 60)

angle = 45

sin_value = math.sin(math.radians(angle))
cos_value = math.cos(math.radians(angle))

result = sin_value ** 2 + cos_value ** 2

print("sin² + cos² =", round(result, 10))

print()

print("=" * 60)
print("Example 3 : 120°")
print("=" * 60)

angle = 120

sin_value = math.sin(math.radians(angle))
cos_value = math.cos(math.radians(angle))

result = sin_value ** 2 + cos_value ** 2

print("sin² + cos² =", round(result, 10))

"""
Output

sin² + cos² = 1.0

sin² + cos² = 1.0

sin² + cos² = 1.0
"""

# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
❌ ভুল ১

sin²θ + cos²θ

=

2

ভাবা।

সঠিক

=

1

------------------------------------

❌ ভুল ২

sin²θ

মানে

sin(θ²)

ভাবা।

সঠিক

(sinθ)²

------------------------------------

❌ ভুল ৩

Identity

এবং

Equation

একই মনে করা।

Identity

সব Angle-এর জন্য সত্য।

Equation

শুধু নির্দিষ্ট Angle-এর জন্য সত্য হতে পারে।

------------------------------------

❌ ভুল ৪

Degree এবং Radian
মিশিয়ে ফেলা।

------------------------------------

❌ ভুল ৫

Unit Circle-এর Equation

x²+y²=1

এবং

sin²θ+cos²θ=1

এর সম্পর্ক না বোঝা।
"""

# ===========================================================
# 10_Exercises
# ===========================================================

"""
১।

30° এর জন্য

sin²θ + cos²θ

যাচাই করো।

----------------------------------

২।

60° এর জন্য

Identity যাচাই করো।

----------------------------------

৩।

135° এর জন্য

Identity যাচাই করো।

----------------------------------

৪।

নিজের

verify_identity()

Function লেখো।

----------------------------------

৫।

User থেকে একটি Angle Input নিয়ে

sin²θ + cos²θ

Print করো।

----------------------------------

৬।

0° থেকে 360°

পর্যন্ত

প্রতি 15°

এর জন্য

Identity যাচাই করো।
"""

# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
Pythagorean Identity
AI এবং Computer Science-এর
অনেক ক্ষেত্রে গুরুত্বপূর্ণ।

১।

Computer Graphics

Rotation Matrix

যাচাই করতে।

----------------------------------

২।

Robotics

Robot Arm-এর
নির্দিষ্ট দৈর্ঘ্য বজায় রাখতে।

----------------------------------

৩।

Computer Vision

Image Rotation

এবং

Geometric Transformation।

----------------------------------

৪।

Signal Processing

Sine ও Cosine Wave-এর
Power Analysis।

----------------------------------

৫।

Machine Learning

Positional Encoding

(Fourier Features)

এ

sin² + cos² = 1

সম্পর্কটি গুরুত্বপূর্ণ।

----------------------------------

৬।

Deep Learning

Rotation-Invariant Features,

3D Graphics,

Physics Simulation,

Game Engine

ইত্যাদিতে এই Identity
প্রচুর ব্যবহৃত হয়।

Pythagorean Identity না বুঝলে,

Rotation Matrix,

Fourier Transform,

Complex Numbers,

Signal Processing,

Computer Graphics,

Robotics

এবং

Advanced AI Mathematics

বোঝা কঠিন হয়ে যায়।
"""

# ===========================================================
# End of File
# ===========================================================