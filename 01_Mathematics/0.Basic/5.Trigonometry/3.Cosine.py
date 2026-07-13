"""
===========================================================
Cosine (কোসাইন)
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
Unit Circle এবং Sine শেখার পরে

পরবর্তী Trigonometric Function হলো

Cosine (cos)।

Cosine আমাদের বলে,

কোনো Right Triangle-এ

একটি নির্দিষ্ট Angle-এর জন্য

Adjacent Side

Hypotenuse-এর কত অংশ।

অর্থাৎ,

Cosine-ও একটি Ratio।

Unit Circle-এ,

Cosine হলো

Point-এর

x-coordinate।

Computer Graphics,
Physics,
Game Development,
Machine Learning

সবখানেই Cosine ব্যবহৃত হয়।
"""

# ===========================================================
# 02_WhyThisConceptExistsInRealtionTohistory
# ===========================================================

"""
প্রাচীন Greek এবং ভারতীয় গণিতবিদরা

ত্রিভুজের বাহু ও কোণের সম্পর্ক
নিয়ে গবেষণা করতেন।

তারা লক্ষ্য করেন,

একটি নির্দিষ্ট Angle-এর জন্য

Adjacent Side

এবং

Hypotenuse

এর Ratio

সবসময় একই থাকে।

এই Ratio-ই

Cosine।

বর্তমানে,

Engineering,

Astronomy,

Robotics,

Signal Processing,

Computer Graphics,

AI

সবখানেই Cosine ব্যবহৃত হয়।
"""

# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
ধরো,

একটি মই দেয়ালে হেলান দিয়ে আছে।

          ●
         /|
        / |
       /  |
      /θ  |
     /____|

মই-এর দৈর্ঘ্য

একই থাকে।

কিন্তু,

Angle পরিবর্তন হলে

দেয়াল থেকে মাটির দূরত্ব

পরিবর্তিত হয়।

এই অনুভূমিক (Horizontal)

দূরত্বের Ratio-ই

Cosine।

আরও উদাহরণ—

✔ Car Moving on Road

✔ Robot Arm

✔ Rotating Wheel

✔ Shadow Length

✔ Game Character Rotation
"""

# ===========================================================
# 04_Definition
# ===========================================================

"""
Right Triangle-এ,

কোনো Angle-এর

Adjacent Side

এবং

Hypotenuse

এর Ratio-কে

Cosine

বলে।

Unit Circle-এ,

যে কোনো Point

(cosθ, sinθ)

হলে,

Cosine হলো

x-coordinate।
"""

# ===========================================================
# 05_Formula
# ===========================================================

"""
Right Triangle

cosθ

=

Adjacent / Hypotenuse

------------------------------------

Unit Circle

Point

(cosθ, sinθ)

↓

cosθ

=

x-coordinate

------------------------------------

Range

-1 ≤ cosθ ≤ 1
"""

# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
ধরি,

একটি Right Triangle আছে।

            ●
           /|
          / |
         /  |
        /θ  |
       /____|
     Adjacent

Hypotenuse

Triangle-এর সবচেয়ে বড় বাহু।

যখন,

Adjacent Side

কে

Hypotenuse

দিয়ে ভাগ করি,

একটি নির্দিষ্ট Ratio পাই।

এই Ratio-ই

Cosine।

Unit Circle-এ,

Hypotenuse = Radius = 1

তাই,

cosθ

=

Adjacent / 1

=

Adjacent

=

x-coordinate
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
          x = cosθ

----------------------------

Angle বাড়লে,

Point

বাম বা ডানে সরে।

↓

x-coordinate

পরিবর্তিত হয়।

↓

Cosine পরিবর্তিত হয়।

------------------------------------

Special Values

0°

cos = 1

90°

cos = 0

180°

cos = -1

270°

cos = 0
"""

# ===========================================================
# 08_Examples
# ===========================================================

import math

print("=" * 60)
print("Example 1")
print("=" * 60)

angle = 0

print("cos(0°) =", round(math.cos(math.radians(angle)), 2))

print()

print("=" * 60)
print("Example 2")
print("=" * 60)

angle = 60

print("cos(60°) =", round(math.cos(math.radians(angle)), 2))

print()

print("=" * 60)
print("Example 3")
print("=" * 60)

angle = 45

print("cos(45°) =", round(math.cos(math.radians(angle)), 4))

print()

print("=" * 60)
print("Example 4")
print("=" * 60)

angle = 180

print("cos(180°) =", round(math.cos(math.radians(angle)), 2))

"""
Output

cos(0°) = 1.0

cos(60°) = 0.5

cos(45°) = 0.7071

cos(180°) = -1.0
"""

# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
❌ ভুল ১

Cosine-এর Formula ভুল লেখা।

সঠিক

Adjacent / Hypotenuse

------------------------------------

❌ ভুল ২

Cosine-কে

Opposite / Hypotenuse

মনে করা।

এটি Sine-এর Formula।

------------------------------------

❌ ভুল ৩

Python-এর

math.cos()

এ Degree সরাসরি পাঠানো।

সঠিক

math.cos(math.radians(angle))

------------------------------------

❌ ভুল ৪

Unit Circle-এ

Cosine হলো

x-coordinate

এটি ভুলে যাওয়া।

------------------------------------

❌ ভুল ৫

Cosine-এর Range

-1 থেকে 1

ভুলে যাওয়া।
"""

# ===========================================================
# 10_Exercises
# ===========================================================

"""
১।

cos(0°)

বের করো।

----------------------------------

২।

cos(30°)

বের করো।

----------------------------------

৩।

cos(45°)

বের করো।

----------------------------------

৪।

cos(60°)

বের করো।

----------------------------------

৫।

cos(90°)

বের করো।

----------------------------------

৬।

Python ব্যবহার করে

0° থেকে 360°

পর্যন্ত

প্রতি 30°

এর জন্য

Cosine Value Print করো।

----------------------------------

৭।

User থেকে একটি Angle Input নিয়ে

cosθ

Print করো।
"""

# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
Cosine
Machine Learning, AI এবং Computer Science-এ
অত্যন্ত গুরুত্বপূর্ণ।

১।

Computer Graphics

2D ও 3D Rotation Matrix

----------------------------------

২।

Game Development

Object Rotation

----------------------------------

৩।

Signal Processing

Cosine Wave

----------------------------------

৪।

Robotics

Robot Arm Position

----------------------------------

৫।

Machine Learning

Transformer Positional Encoding

Sine-এর পাশাপাশি
Cosine ব্যবহার করা হয়।

----------------------------------

৬।

Natural Language Processing (NLP)

Cosine Similarity

দুটি Vector-এর
Similarity Measure করতে ব্যবহৃত হয়।

----------------------------------

৭।

Deep Learning

Fourier Transform,

Frequency Encoding,

Computer Vision,

Image Processing

ইত্যাদিতে Cosine অত্যন্ত গুরুত্বপূর্ণ।

Cosine না বুঝলে,

Rotation Matrix,

Cosine Similarity,

Signal Processing,

Fourier Transform,

Transformer,

Computer Graphics

বোঝা কঠিন হয়ে যায়।
"""

# ===========================================================
# End of File
# ===========================================================