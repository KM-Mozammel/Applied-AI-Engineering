"""
===========================================================
Rotating Objects (ত্রিকোণমিতি ব্যবহার করে বস্তু ঘোরানো)
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
এখন পর্যন্ত আমরা শিখেছি

✔ Unit Circle

✔ Sine

✔ Cosine

✔ Tangent

এখন প্রশ্ন হলো,

যদি একটি Object-কে

ঘোরাতে (Rotate)

চাই,

তাহলে তার নতুন Position
কীভাবে বের করবো?

যেমন,

✔ Game Character

✔ Car Wheel

✔ Robot Arm

✔ Satellite

✔ Fan Blade

সবক্ষেত্রেই Rotation দরকার।

Rotation-এর পুরো গণিত
Sine এবং Cosine-এর উপর ভিত্তি করে।
"""

# ===========================================================
# 02_WhyThisConceptExistsInRealtionTohistory
# ===========================================================

"""
প্রাচীনকাল থেকেই

মানুষ

চাকা,

গিয়ার,

জ্যোতির্বিজ্ঞান

এবং

গ্রহের গতিবিধি

নিয়ে গবেষণা করত।

পরে,

Euler

এবং

Rotation Matrix

ধারণার মাধ্যমে

যেকোনো Point-কে

গাণিতিকভাবে ঘোরানোর

পদ্ধতি তৈরি হয়।

বর্তমানে,

✔ Robotics

✔ Animation

✔ Computer Graphics

✔ CAD Software

✔ AI

সবখানেই এটি ব্যবহৃত হয়।
"""

# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
ধরো,

একটি Ceiling Fan ঘুরছে।

Fan-এর প্রতিটি Blade

একটি Circle-এর উপর চলাচল করছে।

আবার,

একটি Game Character

বামে বা ডানে ঘুরছে।

আবার,

একটি Robot Arm

নির্দিষ্ট Angle-এ ঘুরছে।

সবক্ষেত্রেই

একই Rotation Formula

ব্যবহৃত হয়।

Rotation মানে

Distance পরিবর্তন না করে

Direction পরিবর্তন করা।
"""

# ===========================================================
# 04_Definition
# ===========================================================

"""
Rotation হলো

কোনো Point বা Object-কে

একটি নির্দিষ্ট Center-এর চারপাশে

একটি নির্দিষ্ট Angle

দিয়ে ঘোরানো।

2D Graphics-এ

সাধারণত Origin

(0,0)

কে কেন্দ্র ধরে Rotation করা হয়।

Rotation-এর পরে

Point-এর Distance

Center থেকে

একই থাকে।

শুধু Position পরিবর্তিত হয়।
"""

# ===========================================================
# 05_Formula
# ===========================================================

"""
ধরি,

পুরনো Point

(x, y)

Rotation Angle

θ

তাহলে,

নতুন Point হবে,

x'

=

x cosθ

−

y sinθ

-------------------------------

y'

=

x sinθ

+

y cosθ

--------------------------------

এটিই

2D Rotation Formula।

এই Formula-কে

Rotation Matrix

দিয়েও প্রকাশ করা যায়।

| cosθ  -sinθ |

| sinθ   cosθ |
"""

# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
Unit Circle থেকে,

যে কোনো Point

কে Polar Coordinate-এ

লেখা যায়।

ধরি,

Point-এর

Distance = r

Angle = α

তাহলে,

x = r cosα

y = r sinα

এখন যদি,

θ

Angle দ্বারা Rotate করি,

নতুন Angle হবে,

α + θ

অতএব,

x'

=

r cos(α+θ)

y'

=

r sin(α+θ)

এখন,

Cosine Addition Formula

এবং

Sine Addition Formula

ব্যবহার করলে,

x'

=

x cosθ − y sinθ

y'

=

x sinθ + y cosθ

এই Rotation Formula পাওয়া যায়।
"""

# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
Before Rotation

            y
            ↑
            |
        ● (x,y)
       /
      /
-----O----------------→ x

Rotate

90°

↓

            y
            ↑
      ●
      |
      |
      O--------------→ x

New Point

(x',y')

------------------------------------

Rotation

Distance

✔ একই থাকে

Angle

✔ পরিবর্তিত হয়

Direction

✔ পরিবর্তিত হয়
"""

# ===========================================================
# 08_Examples
# ===========================================================

import math

print("=" * 60)
print("Example 1 : Rotate (1,0) by 90°")
print("=" * 60)

x = 1
y = 0
angle = 90

theta = math.radians(angle)

new_x = x * math.cos(theta) - y * math.sin(theta)
new_y = x * math.sin(theta) + y * math.cos(theta)

print("New Point =", (round(new_x, 2), round(new_y, 2)))

print()

print("=" * 60)
print("Example 2 : Rotate (2,3) by 45°")
print("=" * 60)

x = 2
y = 3
angle = 45

theta = math.radians(angle)

new_x = x * math.cos(theta) - y * math.sin(theta)
new_y = x * math.sin(theta) + y * math.cos(theta)

print("New Point =", (round(new_x, 2), round(new_y, 2)))

print()

print("=" * 60)
print("Example 3 : Rotate (5,0) by 180°")
print("=" * 60)

x = 5
y = 0
angle = 180

theta = math.radians(angle)

new_x = x * math.cos(theta) - y * math.sin(theta)
new_y = x * math.sin(theta) + y * math.cos(theta)

print("New Point =", (round(new_x, 2), round(new_y, 2)))

"""
Output

New Point = (0.0, 1.0)

New Point = (-0.71, 3.54)

New Point = (-5.0, 0.0)
"""

# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
❌ ভুল ১

Degree-কে

math.sin()

এবং

math.cos()

এ সরাসরি পাঠানো।

সঠিক

math.radians()

ব্যবহার করা।

------------------------------------

❌ ভুল ২

Rotation Formula-তে

Plus

এবং

Minus

উল্টো লেখা।

------------------------------------

❌ ভুল ৩

Rotation-এর পরে

Distance

পরিবর্তিত হয় ভাবা।

আসলে,

Distance অপরিবর্তিত থাকে।

------------------------------------

❌ ভুল ৪

Clockwise

এবং

Counter-Clockwise

Rotation গুলিয়ে ফেলা।

------------------------------------

❌ ভুল ৫

Origin

ছাড়া অন্য Center-এর চারপাশে Rotation
করতে গেলে

প্রথমে Translate

তারপর Rotate

তারপর আবার Translate Back

করতে হয়।

এটি ভুলে যাওয়া।
"""

# ===========================================================
# 10_Exercises
# ===========================================================

"""
১।

Point

(3,0)

কে

90°

Rotate করো।

----------------------------------

২।

Point

(2,5)

কে

180°

Rotate করো।

----------------------------------

৩।

Point

(4,1)

কে

45°

Rotate করো।

----------------------------------

৪।

নিজের

rotate_point()

Function লেখো।

----------------------------------

৫।

User থেকে

x

y

angle

Input নিয়ে

নতুন Point বের করো।

----------------------------------

৬।

একটি Square-এর
চারটি Corner

90°

Rotate করো।
"""

# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
Rotation
AI এবং Computer Science-এর
অত্যন্ত গুরুত্বপূর্ণ বিষয়।

১।

Computer Graphics

2D ও 3D Object Rotation।

----------------------------------

২।

Game Development

Character Rotation

Camera Rotation

----------------------------------

৩।

Computer Vision

Image Rotation,

Data Augmentation

----------------------------------

৪।

Robotics

Robot Arm Movement,

Forward Kinematics

----------------------------------

৫।

Machine Learning

Image Augmentation

Rotation-based Training

----------------------------------

৬।

Deep Learning

CNN,

Vision Transformer (ViT),

Object Detection,

Pose Estimation,

Autonomous Driving

ইত্যাদিতে Rotation
অত্যন্ত গুরুত্বপূর্ণ।

----------------------------------

৭।

AR/VR

Virtual Object Rotation।

----------------------------------

Rotation Formula না বুঝলে,

Rotation Matrix,

Affine Transformation,

3D Graphics,

Computer Vision,

Robotics,

Game Engine,

Machine Learning

এবং

Deep Learning-এর
অনেক গুরুত্বপূর্ণ বিষয় বোঝা কঠিন হয়ে যায়।
"""

# ===========================================================
# End of File
# ===========================================================