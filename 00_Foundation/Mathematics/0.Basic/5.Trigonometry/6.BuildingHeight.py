"""
===========================================================
Building Height using Trigonometry
(ত্রিকোণমিতি ব্যবহার করে ভবনের উচ্চতা নির্ণয়)
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
আমরা ইতোমধ্যে শিখেছি

✔ Sine

✔ Cosine

✔ Tangent

এখন প্রশ্ন হলো,

যদি কোনো ভবনের
উচ্চতা সরাসরি মাপা না যায়,

তাহলে কীভাবে বের করবো?

যেমন,

✔ Eiffel Tower

✔ Mobile Tower

✔ Mountain

✔ Tree

এগুলোর উচ্চতা

মই বা দড়ি ছাড়াই

Trigonometry ব্যবহার করে বের করা যায়।

এই অধ্যায়ে
সেটিই শিখবো।
"""

# ===========================================================
# 02_WhyThisConceptExistsInRealtionTohistory
# ===========================================================

"""
প্রাচীন Egypt-এ

Pyramid-এর উচ্চতা মাপতে

Trigonometry ব্যবহার করা হতো।

পরে,

Greek গণিতবিদরা

Angle Measurement

এবং

Triangle

ব্যবহার করে

অজানা উচ্চতা বের করার পদ্ধতি তৈরি করেন।

বর্তমানে,

✔ Surveying

✔ Civil Engineering

✔ Construction

✔ Drone Mapping

✔ Satellite Measurement

সবখানেই এই ধারণা ব্যবহৃত হয়।
"""

# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
ধরো,

তুমি একটি ভবনের সামনে দাঁড়িয়ে আছো।

তুমি জানো,

✔ ভবন থেকে তোমার দূরত্ব

✔ ভবনের চূড়ার দিকে তাকানোর Angle

এখন,

এই দুইটি তথ্য ব্যবহার করেই

পুরো ভবনের উচ্চতা বের করা সম্ভব।

এটাই Trigonometry-এর
সবচেয়ে জনপ্রিয় ব্যবহারগুলোর একটি।

আরও উদাহরণ—

✔ Tree Height

✔ Electric Pole

✔ Mountain Height

✔ Tower Height

✔ Drone Altitude
"""

# ===========================================================
# 04_Definition
# ===========================================================

"""
যদি,

Observer

এবং

Building

মিলে একটি Right Triangle তৈরি করে,

তাহলে,

Tangent Formula ব্যবহার করে

Building-এর Height

বের করা যায়।

কারণ,

tanθ

=

Opposite / Adjacent

এখানে,

Opposite

=

Building Height

Adjacent

=

Observer থেকে Building-এর Distance
"""

# ===========================================================
# 05_Formula
# ===========================================================

"""
মূল সূত্র

tanθ

=

Height / Distance

------------------------------------

Height

=

Distance × tanθ

------------------------------------

যদি,

Observer-এর Height

h

হয়,

তাহলে,

Actual Building Height

=

Distance × tanθ + h
"""

# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
Right Triangle

          Building
             ●
             |
             | Height
             |
             |
             |
-------------●-------------
             \
              \
               \
                \
                 👤

Distance

=

Adjacent

Height

=

Opposite

Angle

=

θ

আমরা জানি,

tanθ

=

Opposite / Adjacent

অর্থাৎ,

tanθ

=

Height / Distance

দুই পাশে

Distance

দিয়ে গুণ করলে,

Height

=

Distance × tanθ

এইভাবেই
Building Height-এর Formula
পাওয়া যায়।
"""

# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
                  Building
                     ●
                     |
                     | Height
                     |
                     |
                     |
---------------------●-------------------
                    /
                   /
                  / θ
                 /
                👤

Observer

Distance = d

----------------------------

tanθ

=

Height / Distance

↓

Height

=

d × tanθ

যদি Observer-এর চোখ
মাটি থেকে ১.৬ মিটার উপরে হয়,

তাহলে,

Final Height

=

d × tanθ + 1.6
"""

# ===========================================================
# 08_Examples
# ===========================================================

import math

print("=" * 60)
print("Example 1")
print("=" * 60)

distance = 20      # meter
angle = 45         # degree

height = distance * math.tan(math.radians(angle))

print("Building Height =", round(height, 2), "meter")

print()

print("=" * 60)
print("Example 2")
print("=" * 60)

distance = 30
angle = 60

height = distance * math.tan(math.radians(angle))

print("Building Height =", round(height, 2), "meter")

print()

print("=" * 60)
print("Example 3 (Observer Height Included)")
print("=" * 60)

distance = 25
angle = 50
observer_height = 1.7

height = distance * math.tan(math.radians(angle))
total_height = height + observer_height

print("Actual Building Height =", round(total_height, 2), "meter")

"""
Output

Building Height = 20.0 meter

Building Height = 51.96 meter

Actual Building Height = 31.49 meter
"""

# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
❌ ভুল ১

sin

ব্যবহার করা।

এখানে,

tan

ব্যবহার করতে হবে।

------------------------------------

❌ ভুল ২

Distance

এবং

Height

অদলবদল করা।

------------------------------------

❌ ভুল ৩

Degree-কে

math.tan()

এ সরাসরি পাঠানো।

Python-এ,

math.tan()

Radians ব্যবহার করে।

------------------------------------

❌ ভুল ৪

Observer-এর Height
যোগ করতে ভুলে যাওয়া।

------------------------------------

❌ ভুল ৫

Angle of Elevation

এবং

Angle of Depression

গুলিয়ে ফেলা।
"""

# ===========================================================
# 10_Exercises
# ===========================================================

"""
১।

Distance = 10 meter

Angle = 45°

Height বের করো।

----------------------------------

২।

Distance = 25 meter

Angle = 60°

Height বের করো।

----------------------------------

৩।

Distance = 40 meter

Angle = 35°

Height বের করো।

----------------------------------

৪।

Observer Height = 1.8 meter

যোগ করে Actual Height বের করো।

----------------------------------

৫।

নিজের

building_height()

Function লেখো।

----------------------------------

৬।

User থেকে

Distance

এবং

Angle

Input নিয়ে

Height বের করো।
"""

# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
Building Height নির্ণয়ের ধারণা
AI এবং Engineering-এ
অত্যন্ত গুরুত্বপূর্ণ।

১।

Computer Vision

Single Image থেকে

Building Height Estimation।

----------------------------------

২।

Autonomous Vehicles

Obstacle Height Measurement।

----------------------------------

৩।

Drone Mapping

Ground থেকে Structure Height নির্ণয়।

----------------------------------

৪।

Satellite Image Analysis

Building ও Mountain-এর Height নির্ণয়।

----------------------------------

৫।

Robotics

Camera Angle ব্যবহার করে
Object-এর উচ্চতা নির্ণয়।

----------------------------------

৬।

Machine Learning

3D Reconstruction,

SLAM (Simultaneous Localization and Mapping),

Depth Estimation,

Augmented Reality (AR),

Digital Twin

ইত্যাদিতে এই Trigonometric ধারণা
ব্যাপকভাবে ব্যবহৃত হয়।

Building Height সমস্যা
Trigonometry-এর একটি বাস্তব এবং
সবচেয়ে জনপ্রিয় Application।
"""

# ===========================================================
# End of File
# ===========================================================