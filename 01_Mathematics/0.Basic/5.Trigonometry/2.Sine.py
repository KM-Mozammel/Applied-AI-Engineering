"""
===========================================================
Sine (সাইন)
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
Unit Circle শেখার পরে
Trigonometry-এর প্রথম Function হলো

Sine (sin)।

Sine আমাদের বলে,

কোনো Right Triangle-এ

একটি নির্দিষ্ট Angle-এর জন্য

Opposite Side

Hypotenuse-এর কত অংশ।

অর্থাৎ,

Sine হলো

একটি Ratio।

পরবর্তীতে,

Cosine,

Tangent,

Wave,

Signal Processing,

Machine Learning,

Computer Graphics

সবকিছুতেই Sine ব্যবহৃত হয়।
"""

# ===========================================================
# 02_WhyThisConceptExistsInRealtionTohistory
# ===========================================================

"""
প্রাচীন ভারতীয় এবং Greek গণিতবিদরা

কোণ (Angle)

এবং

ত্রিভুজ (Triangle)

নিয়ে গবেষণা করতেন।

তারা বুঝতে পারেন,

কোনো নির্দিষ্ট Angle-এর জন্য

Side-এর Ratio

সবসময় একই থাকে।

এই Ratio-গুলোর একটি হলো

Sine।

আজ,

Physics,

Engineering,

Navigation,

Robotics,

Computer Graphics

এবং

AI

সবখানেই Sine ব্যবহৃত হয়।
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

সবসময় একই।

কিন্তু,

Angle পরিবর্তন করলে

উচ্চতা পরিবর্তন হয়।

এই উচ্চতার Ratio-ই

Sine-এর মূল ধারণা।

আরও উদাহরণ—

✔ Building Height

✔ Ramp

✔ Drone Height

✔ Elevator Motion

✔ Ferris Wheel
"""

# ===========================================================
# 04_Definition
# ===========================================================

"""
Right Triangle-এ,

কোনো Angle-এর

Opposite Side

এবং

Hypotenuse

এর Ratio-কে

Sine

বলে।

Unit Circle-এ,

যে কোনো Point

(cosθ,sinθ)

হলে,

Sine হলো

y-coordinate।
"""

# ===========================================================
# 05_Formula
# ===========================================================

# :contentReference[oaicite:0]{index=0}

"""
Right Triangle

sinθ

=

Opposite / Hypotenuse

------------------------------------

Unit Circle

Point

(cosθ,sinθ)

↓

sinθ

=

y-coordinate

------------------------------------

Range

-1 ≤ sinθ ≤ 1
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
        /θ  | Opposite
       /____|
     Adjacent

Hypotenuse

Triangle-এর সবচেয়ে বড় বাহু।

যখন,

Opposite Side

কে

Hypotenuse

দিয়ে ভাগ করি,

একটি নির্দিষ্ট Ratio পাই।

এই Ratio-ই

Sine।

Unit Circle-এ,

Hypotenuse = Radius = 1

তাই,

sinθ

=

Opposite / 1

=

Opposite

=

y-coordinate
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
          /  | y = sinθ
         /θ  |
        /____|
          x

----------------------------

Angle বাড়লে,

Point উপরে ওঠে।

↓

y-coordinate

পরিবর্তিত হয়।

↓

Sine পরিবর্তিত হয়।

------------------------------------

Special Values

0°

sin = 0

90°

sin = 1

180°

sin = 0

270°

sin = -1
"""

# ===========================================================
# 08_Examples
# ===========================================================

import math

print("=" * 60)
print("Example 1")
print("=" * 60)

angle = 30

print("sin(30°) =", round(math.sin(math.radians(angle)), 2))

print()

print("=" * 60)
print("Example 2")
print("=" * 60)

angle = 45

print("sin(45°) =", round(math.sin(math.radians(angle)), 4))

print()

print("=" * 60)
print("Example 3")
print("=" * 60)

angle = 90

print("sin(90°) =", round(math.sin(math.radians(angle)), 2))

print()

print("=" * 60)
print("Example 4")
print("=" * 60)

angle = 270

print("sin(270°) =", round(math.sin(math.radians(angle)), 2))

"""
Output

sin(30°) = 0.5

sin(45°) = 0.7071

sin(90°) = 1.0

sin(270°) = -1.0
"""

# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
❌ ভুল ১

Sine-এর Formula ভুল লেখা।

সঠিক

Opposite / Hypotenuse

------------------------------------

❌ ভুল ২

Degree-এর পরিবর্তে

Radian

না ব্যবহার করে

math.sin()

Call করা।

Python-এর

math.sin()

Radians চায়।

------------------------------------

❌ ভুল ৩

Sine-এর Range

-1 থেকে 1

ভুলে যাওয়া।

------------------------------------

❌ ভুল ৪

Unit Circle-এ

sinθ

হলো

y-coordinate

এটি ভুলে যাওয়া।

------------------------------------

❌ ভুল ৫

Opposite

এবং

Adjacent

গুলিয়ে ফেলা।
"""

# ===========================================================
# 10_Exercises
# ===========================================================

"""
১।

sin(0°)

বের করো।

----------------------------------

২।

sin(30°)

বের করো।

----------------------------------

৩।

sin(45°)

বের করো।

----------------------------------

৪।

sin(60°)

বের করো।

----------------------------------

৫।

sin(90°)

বের করো।

----------------------------------

৬।

Python ব্যবহার করে

0° থেকে 360°

পর্যন্ত

প্রতি 30°

এর জন্য

Sine Value Print করো।

----------------------------------

৭।

User থেকে একটি Angle Input নিয়ে

sinθ

Print করো।
"""

# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
Sine
AI এবং Computer Science-এর
সবচেয়ে বেশি ব্যবহৃত Mathematical Function-গুলোর একটি।

১।

Signal Processing

Audio Wave

----------------------------------

২।

Computer Graphics

Animation

----------------------------------

৩।

Robotics

Robot Motion

----------------------------------

৪।

Game Development

Smooth Movement

----------------------------------

৫।

Machine Learning

Transformer Positional Encoding

Sine Function ব্যবহার করে।

----------------------------------

৬।

Deep Learning

Fourier Features,

Periodic Activation,

Time-Series Encoding

ইত্যাদিতে Sine অত্যন্ত গুরুত্বপূর্ণ।

Sine না বুঝলে,

Cosine,

Wave,

Fourier Transform,

Signal Processing,

Transformer,

Diffusion Model

বোঝা কঠিন হয়ে যায়।
"""

# ===========================================================
# End of File
# ===========================================================