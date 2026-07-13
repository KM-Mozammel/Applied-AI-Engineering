"""
===========================================================
Haversine Formula
(পৃথিবীর পৃষ্ঠে দুইটি অবস্থানের মধ্যকার দূরত্ব)
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
এখন পর্যন্ত আমরা যে Distance Formula শিখেছি,
তা সমতল (2D Plane)-এর জন্য।

কিন্তু বাস্তবে পৃথিবী সমতল নয়।

পৃথিবী প্রায় একটি গোলকের (Sphere) মতো।

তাই,

ঢাকা থেকে চট্টগ্রাম,
নিউইয়র্ক থেকে লন্ডন,
অথবা
টোকিও থেকে সিডনি—

এই শহরগুলোর দূরত্ব
সাধারণ Distance Formula দিয়ে
সঠিকভাবে বের করা যায় না।

এই সমস্যার সমাধানের জন্য ব্যবহৃত হয়

Haversine Formula।

এটি পৃথিবীর বাঁকানো পৃষ্ঠ (Curved Surface)
ধরে দুইটি অবস্থানের মধ্যে
Shortest Great-Circle Distance
নির্ণয় করে।
"""

# ===========================================================
# 02_WhyThisConceptExistsInRealtionTohistory
# ===========================================================

"""
সমুদ্রযাত্রা ও জ্যোতির্বিজ্ঞানের যুগে
নাবিকদের পৃথিবীর এক স্থান থেকে
অন্য স্থানের দূরত্ব নির্ণয় করতে হতো।

পৃথিবী গোলাকার হওয়ায়
সাধারণ Plane Geometry যথেষ্ট ছিল না।

১৮শ ও ১৯শ শতাব্দীতে
Navigation-এর জন্য
Haversine Function জনপ্রিয় হয়ে ওঠে।

আজ,

✔ GPS

✔ Google Maps

✔ Aviation

✔ Marine Navigation

✔ Satellite Systems

সবখানেই Haversine Formula
ব্যবহৃত হয়।
"""

# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
ধরো,

একটি ফুটবল হাতে নিয়েছো।

ফুটবলের উপর দুইটি বিন্দু চিহ্নিত করলে,

তাদের মধ্যে সবচেয়ে ছোট পথ
বলটির পৃষ্ঠ বরাবর যাবে।

এটি বলের ভেতর দিয়ে যাবে না।

পৃথিবীর ক্ষেত্রেও একই বিষয়।

ঢাকা থেকে লন্ডনের
সবচেয়ে ছোট পথ

পৃথিবীর পৃষ্ঠ বরাবর,

যাকে বলে

Great Circle Route।

এই Distance-ই
Haversine Formula বের করে।

আরও উদাহরণ—

✔ Flight Route

✔ Ship Navigation

✔ GPS Tracking

✔ Food Delivery

✔ Ride Sharing Apps
"""

# ===========================================================
# 04_Definition
# ===========================================================

"""
Haversine Formula হলো

পৃথিবীর Latitude এবং Longitude ব্যবহার করে

দুইটি Location-এর মধ্যে

Great-Circle Distance

নির্ণয়ের একটি গাণিতিক সূত্র।

এটি ধরে নেয় যে

পৃথিবী একটি Sphere।

যদিও বাস্তবে পৃথিবী পুরোপুরি গোল নয়,
তবুও অধিকাংশ Applications-এর জন্য
এটি যথেষ্ট নির্ভুল।
"""

# ===========================================================
# 05_Formula
# ===========================================================

"""
ধরি,

Latitude₁ = φ₁

Longitude₁ = λ₁

Latitude₂ = φ₂

Longitude₂ = λ₂

Earth Radius

R = 6371 km


Δφ = φ₂ - φ₁

Δλ = λ₂ - λ₁


a = sin²(Δφ/2)
    +
    cos(φ₁) × cos(φ₂)
    × sin²(Δλ/2)


c = 2 × atan2(√a, √(1-a))


Distance

d = R × c

এখানে,

সমস্ত Angle অবশ্যই

Radians-এ হতে হবে।
"""

# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
Haversine Formula-এর ভিত্তি হলো

Spherical Geometry।

Plane Geometry-তে

Pythagoras ব্যবহার করা যায়।

কিন্তু Sphere-এর ক্ষেত্রে

Great Circle
এবং
Central Angle

ব্যবহার করতে হয়।

প্রথমে,

দুইটি Location-এর মধ্যে

Central Angle (c)

বের করা হয়।

তারপর,

Arc Length-এর সূত্র ব্যবহার করা হয়।

Arc Length

=

Radius × Angle

অর্থাৎ,

Distance

=

R × c

এইভাবেই

Haversine Formula তৈরি হয়েছে।

সম্পূর্ণ Derivation
Trigonometry
এবং
Spherical Geometry-এর উপর ভিত্তি করে।
"""

# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
                     North Pole
                          ●
                       .-''''-.
                    .-'        '-.
                  .'              '.
                 /                  \
                |        🌍          |
                |      ●──────●      |
                |   Great Circle     |
                 \                  /
                  '.              .'
                    '-.        .-'
                       '-.__.-'

     Location A          Location B


Plane Distance

❌ সঠিক নয়

-----------------------------

Great Circle Distance

✔ সঠিক

কারণ,

পৃথিবী সমতল নয়,
বরং গোলাকার।
"""

# ===========================================================
# 08_Examples
# ===========================================================

import math

print("=" * 60)
print("Example : Dhaka → Chattogram")
print("=" * 60)

# Latitude এবং Longitude (Degrees)

lat1 = 23.8103
lon1 = 90.4125

lat2 = 22.3569
lon2 = 91.7832

# Degree → Radian

lat1 = math.radians(lat1)
lon1 = math.radians(lon1)

lat2 = math.radians(lat2)
lon2 = math.radians(lon2)

# Earth Radius

R = 6371

dlat = lat2 - lat1
dlon = lon2 - lon1

a = (
    math.sin(dlat / 2) ** 2
    + math.cos(lat1)
    * math.cos(lat2)
    * math.sin(dlon / 2) ** 2
)

c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

distance = R * c

print(f"Distance ≈ {distance:.2f} km")

"""
Output

Distance ≈ 194 km
(প্রায়)
"""

# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
❌ ভুল ১

Latitude এবং Longitude-কে

Radians-এ রূপান্তর না করা।

------------------------------------

❌ ভুল ২

Earth Radius

6371 km

ব্যবহার না করা
(যদি ফলাফল কিলোমিটারে চাই।)

------------------------------------

❌ ভুল ৩

Plane Distance Formula
ব্যবহার করা।

------------------------------------

❌ ভুল ৪

Latitude এবং Longitude
অদলবদল করা।

------------------------------------

❌ ভুল ৫

Degree এবং Radian
মিশিয়ে ফেলা।
"""

# ===========================================================
# 10_Exercises
# ===========================================================

"""
১।

ঢাকা এবং খুলনার
Latitude ও Longitude নিয়ে
Distance বের করো।

----------------------------------

২।

ঢাকা এবং রাজশাহীর
Distance বের করো।

----------------------------------

৩।

নিজের বর্তমান Location
এবং একটি বন্ধুর Location-এর
Distance বের করো।

----------------------------------

৪।

নিজের

haversine()

Function তৈরি করো।

----------------------------------

৫।

User থেকে

Latitude

এবং

Longitude

Input নিয়ে

Distance বের করো।

----------------------------------

৬।

Earth Radius

6371 km

এর পরিবর্তে

3959 miles

ব্যবহার করে
Distance মাইলে বের করো।
"""

# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
Haversine Formula
AI, Data Science এবং GIS-এ
অত্যন্ত গুরুত্বপূর্ণ।

১।

GPS Navigation

বর্তমান অবস্থান থেকে
গন্তব্যের Distance নির্ণয়।

----------------------------------

২।

Ride Sharing Apps

যেমন,

Uber,
Pathao,
InDrive

নিকটতম Driver নির্বাচন করতে।

----------------------------------

৩।

Food Delivery

নিকটতম Restaurant
নির্বাচন করতে।

----------------------------------

৪।

Location-Based Recommendation

নিকটবর্তী Hotel,
ATM,
Hospital
খুঁজে বের করতে।

----------------------------------

৫।

Geospatial Machine Learning

Location Feature
বিশ্লেষণ করতে।

----------------------------------

৬।

Clustering

Geographical Data-এর
Distance Measure হিসেবে।

----------------------------------

Haversine Formula
Location Intelligence,
GIS,
Satellite Tracking,
Autonomous Navigation
এবং
Geospatial AI-এর
একটি মৌলিক ভিত্তি।
"""

# ===========================================================
# End of File
# ===========================================================