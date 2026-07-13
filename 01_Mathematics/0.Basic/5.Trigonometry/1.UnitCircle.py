"""
===========================================================
Unit Circle (একক বৃত্ত)
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
Trigonometry-এর পুরো ভিত্তি দাঁড়িয়ে আছে একটি ছোট কিন্তু অত্যন্ত গুরুত্বপূর্ণ ধারণার উপর। সেটি হলো Unit Circle। তুমি যদি Unit Circle ভালোভাবে বুঝতে পারো, তাহলে

✔ Sine
✔ Cosine
✔ Tangent
✔ Trigonometric Identities
✔ Rotation
✔ Complex Numbers
✔ Fourier Transform

সবকিছু অনেক সহজ হয়ে যাবে। তাই Trigonometry শেখার প্রথম ধাপই হলো Unit Circle।
"""

# ===========================================================
# 02_WhyThisConceptExistsInRealtionTohistory
# ===========================================================

"""
প্রাচীন Babylon ও Greek গণিতবিদরা
বৃত্ত এবং কোণ (Angle) নিয়ে গবেষণা করতেন।

পরে,

Hipparchus,
Ptolemy,
Euler

এবং আরও অনেক গণিতবিদ বুঝতে পারেন,

যদি Radius সবসময়

1

ধরা হয়,

তাহলে Trigonometry অনেক সহজ হয়ে যায়।

এভাবেই

Unit Circle

ধারণার জন্ম হয়।

বর্তমানে,

Physics,
Computer Graphics,
AI,
Robotics,
Signal Processing

সবখানেই এটি ব্যবহৃত হয়।
"""

# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
ধরো,

একটি ঘড়ির কাঁটা ঘুরছে।

ঘড়ির কেন্দ্র থেকে

কাঁটার দৈর্ঘ্য

সবসময় একই থাকে।

কিন্তু,

কোণ পরিবর্তন হলে

কাঁটার মাথার অবস্থান পরিবর্তন হয়।

এই পথটি একটি Circle।

যদি,

কাঁটার দৈর্ঘ্য

1

হয়,

তাহলে সেটিই Unit Circle।

আরও উদাহরণ—

✔ Ferris Wheel

✔ Ceiling Fan

✔ Car Tire

✔ Clock

✔ Robot Arm Rotation
"""

# ===========================================================
# 04_Definition
# ===========================================================

"""
Unit Circle হলো

এমন একটি Circle,

যার

Radius = 1

এবং

Center = (0,0)

অর্থাৎ,

Origin-কে কেন্দ্র করে
১ একক Radius-এর Circle।

Unit Circle-এর প্রতিটি Point

(x,y)

আসলে

(cosθ,sinθ)

প্রকাশ করে।
"""

# ===========================================================
# 05_Formula
# ===========================================================

"""
Center

(0,0)

------------------------------------

Radius

r = 1

------------------------------------

Equation

x² + y² = 1

------------------------------------

Point on Circle

(x,y)

=

(cosθ,sinθ)

------------------------------------

tanθ

=

sinθ / cosθ

=

y / x
"""

# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
Circle-এর সাধারণ Equation

x² + y² = r²

Unit Circle-এ,

r = 1

তাই,

x² + y² = 1²

=

1

এখন,

একটি Radius
Positive x-axis-এর সাথে

θ

কোণ তৈরি করলে,

Triangle থেকে পাই,

Adjacent

=

cosθ

Opposite

=

sinθ

এবং

Hypotenuse

=

1

অতএব,

Circle-এর Point

=

(cosθ,sinθ)

এটাই Unit Circle-এর মূল ধারণা।
"""

# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
                     y
                     ↑

                 (0,1)
                   ●
                .-' '-.
             .-'       '-.
(-1,0) ●----(0,0)------● (1,0)
             '-.       .-'
                '-. .-'
                   ●
                (0,-1)

                     →
                     x

Radius = 1

------------------------------------

যদি,

θ = 0°

Point

(1,0)

------------------------------------

θ = 90°

Point

(0,1)

------------------------------------

θ = 180°

Point

(-1,0)

------------------------------------

θ = 270°

Point

(0,-1)

------------------------------------

যে কোনো Angle-এর জন্য,

Point

=

(cosθ,sinθ)
"""

# ===========================================================
# 08_Examples
# ===========================================================

import math

print("=" * 60)
print("Example 1")
print("=" * 60)

angle = 0

x = math.cos(math.radians(angle))
y = math.sin(math.radians(angle))

print("Angle =", angle)
print("Point =", (x, y))

print()

print("=" * 60)
print("Example 2")
print("=" * 60)

angle = 90

x = math.cos(math.radians(angle))
y = math.sin(math.radians(angle))

print("Angle =", angle)
print("Point =", (round(x, 2), round(y, 2)))

print()

print("=" * 60)
print("Example 3")
print("=" * 60)

angle = 45

x = math.cos(math.radians(angle))
y = math.sin(math.radians(angle))

print("Angle =", angle)
print("cos =", round(x, 4))
print("sin =", round(y, 4))

print()

print("=" * 60)
print("Example 4")
print("=" * 60)

angle = 180

x = math.cos(math.radians(angle))
y = math.sin(math.radians(angle))

print("Point =", (round(x, 2), round(y, 2)))

"""
Output

Angle = 0
Point = (1.0, 0.0)

-------------------------

Angle = 90
Point = (0.0, 1.0)

-------------------------

Angle = 45
cos = 0.7071
sin = 0.7071

-------------------------

Point = (-1.0, 0.0)
"""

# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
❌ ভুল ১

Radius = 1

ভুলে যাওয়া।

------------------------------------

❌ ভুল ২

Point

(sinθ, cosθ)

লেখা।

সঠিক

(cosθ,sinθ)

------------------------------------

❌ ভুল ৩

Degree এবং Radian
মিশিয়ে ফেলা।

------------------------------------

❌ ভুল ৪

Circle-এর Equation

x²+y²=r²

এর পরিবর্তে

x+y=1

লেখা।

------------------------------------

❌ ভুল ৫

tanθ

=

x/y

ভাবা।

সঠিক

y/x

=

sinθ/cosθ
"""

# ===========================================================
# 10_Exercises
# ===========================================================

"""
১।

Unit Circle-এর Equation লেখো।

----------------------------------

২।

45°

এর Coordinate বের করো।

----------------------------------

৩।

180°

এর Coordinate বের করো।

----------------------------------

৪।

নিজের

unit_circle_point()

Function লেখো।

----------------------------------

৫।

User থেকে Angle Input নিয়ে

(cosθ,sinθ)

Print করো।

----------------------------------

৬।

0°,90°,180°,270°

এর Coordinates Print করো।
"""

# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
Unit Circle
AI, Computer Science এবং Engineering-এর
সবচেয়ে গুরুত্বপূর্ণ Mathematical Tools-এর একটি।

১।

Computer Graphics

2D Rotation

----------------------------------

২।

Game Development

Character Rotation

----------------------------------

৩।

Robotics

Robot Arm Rotation

----------------------------------

৪।

Signal Processing

Sine ও Cosine Wave

----------------------------------

৫।

Machine Learning

Positional Encoding
(Transformer Model)

----------------------------------

৬।

Deep Learning

Fourier Features,

Periodic Activation Functions,

Frequency Encoding

----------------------------------

৭।

Computer Vision

Image Rotation

----------------------------------

Unit Circle না বুঝলে,

Rotation Matrix,

Complex Numbers,

Fourier Transform,

Signal Processing,

Robotics,

Computer Graphics,

Transformer Positional Encoding

বোঝা অনেক কঠিন হয়ে যায়।

এটি Trigonometry-এর সবচেয়ে গুরুত্বপূর্ণ ভিত্তি।
"""

# ===========================================================
# End of File
# ===========================================================