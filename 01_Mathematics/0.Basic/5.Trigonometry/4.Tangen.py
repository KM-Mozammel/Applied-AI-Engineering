"""
===========================================================
Tangent (ট্যানজেন্ট)
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
Unit Circle, Sine এবং Cosine শেখার পরে

তৃতীয় গুরুত্বপূর্ণ Trigonometric Function হলো

Tangent (tan)।

Sine আমাদের Vertical Ratio বলে।

Cosine আমাদের Horizontal Ratio বলে।

কিন্তু,

Tangent আমাদের বলে,

একটি রেখা (Line)

কতটা খাড়া (Steep)

অথবা

কতটা ঢালু (Slope)

তা।

এ কারণেই

Tangent

Geometry,

Physics,

Computer Graphics,

Machine Learning,

Robotics

এ অত্যন্ত গুরুত্বপূর্ণ।
"""

# ===========================================================
# 02_WhyThisConceptExistsInRealtionTohistory
# ===========================================================

"""
"Tangent" শব্দটি এসেছে

Latin শব্দ

"Tangere"

থেকে,

যার অর্থ

"স্পর্শ করা" (To Touch)।

প্রাচীন জ্যোতির্বিজ্ঞানীরা

সূর্য,

চাঁদ,

তারকা

এর অবস্থান নির্ণয়ের জন্য

Tangent ব্যবহার করতেন।

বর্তমানে,

✔ Surveying

✔ Civil Engineering

✔ Navigation

✔ Computer Graphics

✔ Robotics

✔ AI

সবখানেই Tangent ব্যবহৃত হয়।
"""

# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
ধরো,

তুমি একটি পাহাড়ে উঠছো।

যদি পাহাড় খুব খাড়া হয়,

তাহলে

Tangent-এর মান বড় হবে।

যদি রাস্তা সমতল হয়,

তাহলে

Tangent-এর মান ছোট হবে।

আরও উদাহরণ—

✔ Ramp

✔ Road Slope

✔ Building Height

✔ Wheel Rotation

✔ Camera Angle
"""

# ===========================================================
# 04_Definition
# ===========================================================

"""
Right Triangle-এ,

কোনো Angle-এর

Opposite Side

এবং

Adjacent Side

এর Ratio-কে

Tangent

বলে।

Unit Circle-এ,

tanθ

=

sinθ / cosθ

=

y / x

অর্থাৎ,

Tangent হলো

Vertical Distance

এবং

Horizontal Distance

এর Ratio।
"""

# ===========================================================
# 05_Formula
# ===========================================================

"""
Right Triangle

tanθ

=

Opposite / Adjacent

------------------------------------

Unit Circle

tanθ

=

sinθ / cosθ

=

y / x

------------------------------------

Slope

m

=

tanθ

------------------------------------

Range

∞ থেকে -∞

------------------------------------

Undefined

যখন,

cosθ = 0

অর্থাৎ,

90°

270°

...
"""

# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
আমরা জানি,

sinθ

=

Opposite / Hypotenuse

এবং,

cosθ

=

Adjacent / Hypotenuse

এখন,

sinθ / cosθ

=

(Opposite/Hypotenuse)

/

(Adjacent/Hypotenuse)

=

Opposite / Adjacent

অর্থাৎ,

tanθ

=

sinθ / cosθ

=

Opposite / Adjacent

Unit Circle-এ,

Point

=

(cosθ,sinθ)

তাই,

tanθ

=

y / x
"""

# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
                 y
                 ↑

             ● (x,y)
            /|
           / |
          /  |
         /θ  |
        /____|
           x

------------------------------

sinθ

=

Vertical

------------------------------

cosθ

=

Horizontal

------------------------------

tanθ

=

Vertical / Horizontal

=

Slope

--------------------------------

Special Values

0°

tan = 0

45°

tan = 1

90°

Undefined

180°

tan = 0

270°

Undefined
"""

# ===========================================================
# 08_Examples
# ===========================================================

import math

print("=" * 60)
print("Example 1")
print("=" * 60)

angle = 45

print("tan(45°) =", round(math.tan(math.radians(angle)), 2))

print()

print("=" * 60)
print("Example 2")
print("=" * 60)

angle = 30

print("tan(30°) =", round(math.tan(math.radians(angle)), 4))

print()

print("=" * 60)
print("Example 3")
print("=" * 60)

angle = 60

print("tan(60°) =", round(math.tan(math.radians(angle)), 4))

print()

print("=" * 60)
print("Example 4")
print("=" * 60)

angle = 90

try:
    value = math.tan(math.radians(angle))
    print("tan(90°) ≈", value)
except:
    print("Undefined")

"""
Output

tan(45°) = 1.0

tan(30°) = 0.5774

tan(60°) = 1.7321

tan(90°)

Python-এ একটি খুব বড় সংখ্যা
দেখাতে পারে,

কারণ Floating Point Approximation
ব্যবহার করা হয়।

গাণিতিকভাবে,

tan(90°)

Undefined।
"""

# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
❌ ভুল ১

tanθ

=

Adjacent / Opposite

লেখা।

সঠিক

Opposite / Adjacent

------------------------------------

❌ ভুল ২

tanθ

=

sinθ × cosθ

ভাবা।

সঠিক

sinθ / cosθ

------------------------------------

❌ ভুল ৩

tan(90°)

এর মান অসীম (∞)

মনে করা।

সঠিকভাবে,

এটি

Undefined।

------------------------------------

❌ ভুল ৪

Degree-কে

math.tan()

এ সরাসরি পাঠানো।

Python-এর

math.tan()

Radians চায়।

------------------------------------

❌ ভুল ৫

Slope

এবং

Tangent

এর সম্পর্ক না বোঝা।

Slope

=

tanθ
"""

# ===========================================================
# 10_Exercises
# ===========================================================

"""
১।

tan(0°)

বের করো।

----------------------------------

২।

tan(30°)

বের করো।

----------------------------------

৩।

tan(45°)

বের করো।

----------------------------------

৪।

tan(60°)

বের করো।

----------------------------------

৫।

কেন

tan(90°)

Undefined

তা ব্যাখ্যা করো।

----------------------------------

৬।

Python ব্যবহার করে

0°

থেকে

360°

পর্যন্ত

প্রতি 30°

এর জন্য

Tangent Value Print করো।

----------------------------------

৭।

User থেকে একটি Angle Input নিয়ে

tanθ

Print করো।
"""

# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
Tangent
AI, Computer Science এবং Engineering-এ
খুব গুরুত্বপূর্ণ।

১।

Computer Graphics

Object Rotation

এবং

Slope Calculation।

----------------------------------

২।

Computer Vision

Line Detection

Edge Detection

----------------------------------

৩।

Robotics

Robot Movement

Direction Calculation।

----------------------------------

৪।

Game Development

Camera Rotation

Character Movement

----------------------------------

৫।

Machine Learning

Feature Engineering-এ

Slope

এবং

Angle

বিশ্লেষণে।

----------------------------------

৬।

Linear Regression

Slope (m)

বোঝার ভিত্তি।

m = tanθ

----------------------------------

৭।

Signal Processing

Wave Analysis

এবং

Phase Angle

বিশ্লেষণে।

Tangent না বুঝলে,

Slope,

Linear Function,

Rotation,

Computer Graphics,

Computer Vision,

Robotics

এবং

Machine Learning Mathematics

বোঝা অনেক কঠিন হয়ে যায়।
"""

# ===========================================================
# End of File
# ===========================================================