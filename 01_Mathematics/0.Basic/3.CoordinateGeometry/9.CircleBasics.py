"""
===========================================================
Circle Basics (বৃত্তের মৌলিক ধারণা)
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
Coordinate Geometry-তে Line শেখার পরে
পরবর্তী গুরুত্বপূর্ণ Shape হলো Circle (বৃত্ত)।

আমরা প্রতিদিন অসংখ্য বৃত্তাকার জিনিস দেখি—

✔ ঘড়ি

✔ কয়েন

✔ চাকার রিম

✔ প্লেট

✔ CD/DVD

✔ Camera Lens

কিন্তু,

গণিতে Circle শুধুমাত্র একটি গোলাকার আকৃতি নয়।

এটি এমন একটি Shape,
যার প্রতিটি Point একটি নির্দিষ্ট Point
থেকে সমান দূরত্বে থাকে।

এই ধারণাই Circle-এর ভিত্তি।
"""

# ===========================================================
# 02_WhyThisConceptExistsInRealtionTohistory
# ===========================================================

"""
প্রাচীন সভ্যতাগুলো

✔ চাকা তৈরি

✔ স্থাপত্য

✔ জ্যোতির্বিজ্ঞান

✔ সূর্যঘড়ি

✔ কৃষি

ইত্যাদিতে Circle ব্যবহার করত।

পরে Greek গণিতবিদরা
Circle-এর বৈশিষ্ট্য নিয়ে গবেষণা করেন।

Coordinate Geometry আবিষ্কারের পর
Circle-কে Coordinate এবং Equation-এর মাধ্যমে
প্রকাশ করা সম্ভব হয়।

আজকের আধুনিক Geometry,
Computer Graphics,
Robotics এবং AI-এ
Circle একটি মৌলিক Shape।
"""

# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
ধরো,

তুমি একটি খুঁটির সঙ্গে
একটি ৫ মিটার লম্বা দড়ি বেঁধেছো।

দড়ির অন্য প্রান্ত ধরে
চারদিকে হাঁটছো।

তুমি যতই ঘুরো,

দড়ির দৈর্ঘ্য

সবসময়

৫ মিটারই থাকবে।

ফলে তুমি যে পথ তৈরি করবে,
সেটি হবে একটি Circle।

এখানে,

খুঁটি = Center

দড়ির দৈর্ঘ্য = Radius

তোমার চলার পথ = Circle

আরও উদাহরণ—

✔ Ferris Wheel

✔ Satellite Orbit (সরল মডেল)

✔ Radar

✔ Ripple in Water

✔ Robot Rotation
"""

# ===========================================================
# 04_Definition
# ===========================================================

"""
Circle হলো

Plane-এর এমন একটি Point-এর সমষ্টি,

যাদের প্রত্যেকটি

একটি নির্দিষ্ট Point থেকে

সমান দূরত্বে অবস্থিত।

এই নির্দিষ্ট Point-কে

Center

বলা হয়।

এবং

সমান দূরত্বকে

Radius

বলা হয়।
"""

# ===========================================================
# 05_Formula
# ===========================================================

"""
Circle-এর গুরুত্বপূর্ণ অংশ

Center = (h, k)

Radius = r

------------------------------------

Standard Equation

(x - h)² + (y - k)² = r²

------------------------------------

যদি Center হয়

(0,0)

তাহলে,

x² + y² = r²

------------------------------------

Diameter

d = 2r

------------------------------------

Circumference

C = 2πr

------------------------------------

Area

A = πr²
"""

# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
ধরি,

Circle-এর Center

(h,k)

এবং

Circle-এর উপর একটি Point

(x,y)

সংজ্ঞা অনুযায়ী,

Center থেকে Circle-এর
যে কোনো Point-এর Distance

সবসময়

r

হবে।

Distance Formula ব্যবহার করলে,

√((x-h)² + (y-k)²)

=

r

এখন,

উভয় পাশে Square করলে,

(x-h)² + (y-k)²

=

r²

এটাই Circle-এর Standard Equation।

অর্থাৎ,

Circle-এর Equation
Distance Formula থেকেই এসেছে।
"""

# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
                     y
                     ↑

               ● ● ● ● ●

           ●             ●

        ●       C(h,k)     ●
                ●
                │
                │ Radius = r
                │
        ●                   ●

           ●             ●

               ● ● ● ● ●

────────────────────────────────────→ x


Center থেকে
Boundary-এর প্রতিটি Point-এর Distance

সমান।

এই সমান Distance-ই

Radius।

এই কারণেই Shape-টি
Perfect Circle হয়।
"""

# ===========================================================
# 08_Examples
# ===========================================================

import math

print("=" * 60)
print("Example 1")
print("=" * 60)

radius = 5

diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print("Radius =", radius)
print("Diameter =", diameter)
print("Circumference =", circumference)
print("Area =", area)

print()

print("=" * 60)
print("Example 2")
print("=" * 60)

h = 2
k = 3
r = 4

print("Circle Equation")

print(f"(x-{h})² + (y-{k})² = {r*r}")

print()

print("=" * 60)
print("Example 3")
print("=" * 60)

h = 0
k = 0
r = 7

print(f"x² + y² = {r*r}")

"""
Output

Radius = 5

Diameter = 10

Circumference ≈ 31.42

Area ≈ 78.54

-------------------------

(x-2)² + (y-3)² = 16

-------------------------

x² + y² = 49
"""

# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
❌ ভুল ১

Radius

এবং

Diameter

এক মনে করা।

Diameter = 2 × Radius

------------------------------------

❌ ভুল ২

Equation-এ

r

ব্যবহার করা।

সঠিক হলো

r²

------------------------------------

❌ ভুল ৩

Center

(h,k)

এর Sign ভুল লেখা।

যদি Center

(3,5)

হয়,

তাহলে

Equation

(x-3)²+(y-5)²

হবে।

------------------------------------

❌ ভুল ৪

Circle-এর প্রতিটি Point-এর Distance
সমান—এই সংজ্ঞা ভুলে যাওয়া।

------------------------------------

❌ ভুল ৫

Circumference

এবং

Area-এর Formula
গুলিয়ে ফেলা।
"""

# ===========================================================
# 10_Exercises
# ===========================================================

"""
১।

Center

(0,0)

Radius = 8

Equation লেখো।

----------------------------------

২।

Center

(3,-2)

Radius = 5

Equation লেখো।

----------------------------------

৩।

Radius = 9

Diameter,
Circumference,
Area

বের করো।

----------------------------------

৪।

নিজের

circle_area()

Function লেখো।

----------------------------------

৫।

নিজের

circle_circumference()

Function লেখো।

----------------------------------

৬।

User থেকে Radius Input নিয়ে

সব তথ্য Print করো।

----------------------------------

৭।

Center এবং Radius Input নিয়ে

Circle Equation Print করো।
"""

# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
Circle-এর ধারণা AI এবং Computer Science-এ
খুবই গুরুত্বপূর্ণ।

১।

Computer Vision

Circle Detection

(Hough Circle Transform)

----------------------------------

২।

Robotics

Robot-এর Turning Radius

নির্ণয়ে।

----------------------------------

৩।

Game Development

Circular Collision Detection

----------------------------------

৪।

GIS ও GPS

Coverage Area

নির্ণয়ে।

----------------------------------

৫।

Computer Graphics

Circular Objects
আঁকতে।

----------------------------------

৬।

Machine Learning

Clustering,
Spatial Analysis,
Geometric Feature Extraction

ইত্যাদিতে Circle-ভিত্তিক ধারণা ব্যবহৃত হয়।

----------------------------------

Circle হলো
Coordinate Geometry-এর অন্যতম মৌলিক Shape।

পরবর্তীতে Ellipse,
Parabola,
Hyperbola
শেখার ভিত্তি তৈরি করে Circle-এর ধারণা।
"""

# ===========================================================
# End of File
# ===========================================================