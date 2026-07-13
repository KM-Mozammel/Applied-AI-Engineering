"""
===========================================================
Distance Between Two Points (দুটি বিন্দুর মধ্যবর্তী দূরত্ব)
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
যখন Coordinate Geometry শেখা শুরু করি, তখন প্রথম প্রশ্ন আসে—

"দুটি Point-এর মধ্যে কত দূরত্ব?"

যেমন,

A = (2, 3)
B = (7, 9)

চোখে দেখলে বোঝা যায় B, A থেকে দূরে আছে।
কিন্তু ঠিক কত দূরে?

এই প্রশ্নের উত্তর দেয়
Distance Between Two Points।

এটি Coordinate Geometry-এর সবচেয়ে গুরুত্বপূর্ণ সূত্রগুলোর একটি।
"""

# ===========================================================
# 02_WhyThisConceptExistsInRealtionTohistory
# ===========================================================

"""
প্রাচীনকালে মানুষ দূরত্ব মাপতো দড়ি, কাঠি অথবা হাঁটার ধাপ গুনে।

কিন্তু Coordinate System আবিষ্কারের পরে
René Descartes দেখালেন যে,

প্রত্যেক Point-কে সংখ্যা দিয়ে প্রকাশ করা যায়।

এরপর প্রশ্ন হলো—

যদি দুইটি Point-এর Coordinate জানা থাকে,
তাহলে তাদের দূরত্ব কীভাবে বের করবো?

এই সমস্যার সমাধান আসে
Pythagoras Theorem থেকে।

আজকের Distance Formula
আসলে Pythagoras-এর সরাসরি ব্যবহার।
"""

# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
ধরো তুমি Google Maps ব্যবহার করছো।

তোমার অবস্থান:
(3, 2)

বন্ধুর অবস্থান:
(9, 7)

Maps জানে তোমাদের Coordinate।

এখন Maps বের করে—

তোমাদের মধ্যে সরলরেখার দূরত্ব কত?

এটাই Distance Between Two Points।

আরও উদাহরণ—

✔ GPS Navigation
✔ Game Development
✔ Drone Navigation
✔ Robot Movement
✔ Image Processing
✔ Machine Learning
"""

# ===========================================================
# 04_Definition
# ===========================================================

"""
Distance Between Two Points হলো

Coordinate Plane-এ
দুটি Point-এর মধ্যকার
সবচেয়ে ছোট সরলরেখার দূরত্ব।

যদি

A(x₁, y₁)

এবং

B(x₂, y₂)

হয়,

তাহলে তাদের Distance নির্ণয় করা যায়
Distance Formula দিয়ে।
"""

# ===========================================================
# 05_Formula
# ===========================================================

"""

             __________________________
d = √((x₂-x₁)² + (y₂-y₁)²)

যেখানে,

d  = Distance

x₁ = প্রথম Point-এর x

y₁ = প্রথম Point-এর y

x₂ = দ্বিতীয় Point-এর x

y₂ = দ্বিতীয় Point-এর y

মনে রাখো—

Distance কখনো Negative হয় না।
"""

# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
ধরি,

A(2,3)

B(8,7)

Coordinate Plane-এ দুইটি Point যুক্ত করলে
একটি Right Triangle তৈরি করা যায়।

Vertical Difference

Δy = y₂ - y₁

Horizontal Difference

Δx = x₂ - x₁

Triangle অনুযায়ী,

Hypotenuse = Distance

Pythagoras Theorem বলে—

Hypotenuse² =
Base² + Height²

অর্থাৎ,

d² = (Δx)² + (Δy)²

Square Root নিলে,

             ________________________
d = √((Δx)² + (Δy)²)

এখন,

Δx = x₂-x₁

Δy = y₂-y₁

সুতরাং,

             __________________________
d = √((x₂-x₁)² + (y₂-y₁)²)

এটাই Distance Formula।
"""

# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
উদাহরণ

A(2,3)

B(7,9)


            y
            ↑

9                 ● B(7,9)
                  |
                  |
                  |  Δy = 6
                  |
3       ● A(2,3)
        ───────────────
          Δx = 5

────────────────────────────→ x


Right Triangle তৈরি হলো।

Base = 5

Height = 6

Distance

= √(5² + 6²)

= √61

≈ 7.81

Distance হলো Triangle-এর Hypotenuse।
"""

# ===========================================================
# 08_Examples
# ===========================================================

print("=" * 60)
print("Example 1")
print("=" * 60)

x1, y1 = 1, 2
x2, y2 = 4, 6

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(f"A = ({x1}, {y1})")
print(f"B = ({x2}, {y2})")
print("Distance =", distance)

print()

print("=" * 60)
print("Example 2")
print("=" * 60)

x1, y1 = -2, 5
x2, y2 = 3, 1

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(f"A = ({x1}, {y1})")
print(f"B = ({x2}, {y2})")
print("Distance =", distance)

print()

print("=" * 60)
print("Example 3 (Same Point)")
print("=" * 60)

x1, y1 = 4, 7
x2, y2 = 4, 7

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print("Distance =", distance)

"""
Output

Distance = 5.0

Distance = 6.403...

Distance = 0
"""

# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
❌ ভুল ১

(x₂-x₁)² + (y₂-y₁)²

এর Square Root নিতে ভুলে যাওয়া।

----------------------------------

❌ ভুল ২

(x₂+x₁)

লেখা।

সঠিক হলো

(x₂-x₁)

----------------------------------

❌ ভুল ৩

Square না করা।

----------------------------------

❌ ভুল ৪

Negative Distance আশা করা।

Distance সবসময় Positive অথবা Zero।

----------------------------------

❌ ভুল ৫

x এবং y অদলবদল করা।
"""

# ===========================================================
# 10_Exercises
# ===========================================================

"""
১।

A(2,3)

B(6,7)

Distance বের করো।

----------------------------------

২।

A(-1,-2)

B(4,6)

Distance বের করো।

----------------------------------

৩।

A(0,0)

B(8,15)

Distance বের করো।

----------------------------------

৪।

নিজের distance() Function লেখো।

----------------------------------

৫।

User থেকে দুইটি Point Input নিয়ে Distance বের করো।

----------------------------------

৬।

একটি List-এ একাধিক Point রেখে
প্রতিটি consecutive Point-এর Distance বের করো।
"""

# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
Distance Formula Machine Learning-এর অন্যতম
সবচেয়ে বেশি ব্যবহৃত ধারণাগুলোর একটি।

১।
K-Nearest Neighbors (KNN)

দুইটি Data Point-এর Distance বের করতে।

----------------------------------

২।
Clustering (K-Means)

নিকটতম Centroid নির্ণয় করতে।

----------------------------------

৩।
Computer Vision

দুইটি Feature Point-এর Distance নির্ণয় করতে।

----------------------------------

৪।
Robotics

Robot-এর বর্তমান অবস্থান এবং Target-এর
মধ্যকার Distance বের করতে।

----------------------------------

৫।
GPS Navigation

Current Location থেকে Destination-এর
Distance বের করতে।

----------------------------------

৬।
Recommendation System

User Similarity বা Item Similarity
পরিমাপ করতে বিভিন্ন ধরনের Distance ব্যবহৃত হয়।

----------------------------------

Distance Formula হলো
Euclidean Distance-এর ভিত্তি।

Machine Learning-এ Data-কে বহু-মাত্রিক (Multi-dimensional)
Space-এর Point হিসেবে ধরা হয়।

তারপর বিভিন্ন Point-এর মধ্যে Distance হিসাব করে
Prediction, Classification এবং Clustering করা হয়।
"""

# ===========================================================
# End of File
# ===========================================================