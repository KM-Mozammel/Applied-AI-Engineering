"""
===========================================================
Cross Product (ক্রস প্রোডাক্ট)
===========================================================

Structure:
01_Introduction
02_WhyThisConceptExistsInRelationToHistory
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
Cross Product (Vector Product) হলো Linear Algebra এবং
Vector Mathematics এর একটি গুরুত্বপূর্ণ Operation।

সহজভাবে:

Cross Product দুইটি Vector থেকে একটি নতুন Vector তৈরি করে।


এই নতুন Vector:

1. দুইটি Input Vector এর সাথে Perpendicular হয়।
2. এর Magnitude দুই Vector দ্বারা তৈরি Area প্রকাশ করে।


Example:


A × B = C


যেখানে:


A এবং B হলো Input Vector

C হলো নতুন Vector



Cross Product মূলত 3D Space এ ব্যবহৃত হয়।


ব্যবহার:

- Physics
- Computer Graphics
- Robotics
- 3D Game Development
- Engineering


"""


# ===========================================================
# 02_WhyThisConceptExistsInRelationToHistory
# ===========================================================

"""
Cross Product কেন প্রয়োজন হলো?


Physics এবং Geometry তে একটি সমস্যা ছিল:


দুইটি Vector দেওয়া আছে।

তাদের দ্বারা তৈরি Plane এর
Perpendicular Direction কিভাবে বের করা যাবে?


Example:


একটি Plane Surface:

তার Normal Direction প্রয়োজন।


এই সমস্যার সমাধানের জন্য Cross Product তৈরি হয়।



History:

- Vector Algebra এর উন্নতির সাথে Cross Product তৈরি হয়।
- Josiah Willard Gibbs এবং Oliver Heaviside Vector Calculus উন্নত করেন।
- Cross Product 3D Geometry এবং Physics এ গুরুত্বপূর্ণ হয়ে ওঠে।



বর্তমানে:

Computer Graphics এ Object এর Surface Normal,
Lighting Calculation,
Rotation

এর জন্য Cross Product ব্যবহৃত হয়।
"""


# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
Real Life Intuition:


------------------------------------------------
1. Surface Normal
------------------------------------------------


একটি দেয়ালের Surface আছে।


Light কোন দিকে Reflect করবে জানতে
Surface এর Normal Direction দরকার।


Cross Product সেই Direction বের করে।



------------------------------------------------
2. Torque (বল ঘূর্ণন)
------------------------------------------------


Physics এ:


Torque = Force × Distance



একটি দরজা কোথায় চাপ দিলে
সবচেয়ে বেশি ঘুরবে তা Cross Product দিয়ে
বের করা যায়।



------------------------------------------------
3. 3D Graphics
------------------------------------------------


একটি Triangle:


Point A

Point B

Point C



এই Triangle এর Surface কোন দিকে মুখ করে
তা Cross Product দিয়ে জানা যায়।



------------------------------------------------
4. Robotics
------------------------------------------------


Robot Arm এর Rotation এবং Direction
নির্ণয়ে Cross Product ব্যবহৃত হয়।
"""


# ===========================================================
# 04_Definition
# ===========================================================

"""
Cross Product হলো:

দুইটি 3-dimensional Vector এর মধ্যে
একটি Operation যা একটি নতুন Vector তৈরি করে।



ধরি:


A = (a1,a2,a3)


B = (b1,b2,b3)



তাহলে:


A × B = C



যেখানে C:

A এবং B উভয়ের সাথে Perpendicular।



Cross Product শুধুমাত্র:

3D Vector এর জন্য সংজ্ঞায়িত।



Result:

Vector

(Scalar নয়)
"""


# ===========================================================
# 05_Formula
# ===========================================================

"""
Cross Product Formula:


A × B =


| i    j    k |
| a1   a2   a3|
| b1   b2   b3|



Expand করলে:


C =


i(a2b3 - a3b2)

-

j(a1b3 - a3b1)

+

k(a1b2 - a2b1)



Result:


C =

[
a2b3 - a3b2,

a3b1 - a1b3,

a1b2 - a2b1
]



------------------------------------------------


Magnitude Formula:


|A × B| = |A||B|sinθ



যেখানে:


θ = দুই Vector এর মধ্যকার Angle



যদি:


θ = 90°

তাহলে:

sin(90)=1


Maximum Area পাওয়া যায়।
"""


# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
Cross Product Formula Determination:


ধরি:

A এবং B দুইটি Vector।


আমরা এমন একটি Vector C চাই:

যেটি A এবং B উভয়ের সাথে Perpendicular।



Perpendicular হওয়ার শর্ত:


A · C = 0

B · C = 0



এই দুইটি Equation Solve করলে:


C এর Component পাওয়া যায়:


C1 = a2b3 - a3b2


C2 = a3b1 - a1b3


C3 = a1b2 - a2b1



তাই:


A × B =


[
a2b3-a3b2,
a3b1-a1b3,
a1b2-a2b1
]


"""


# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
Computer এর ভিতরে Cross Product:


Input:


A = [a1,a2,a3]

B = [b1,b2,b3]



Step 1:

প্রথম Component:


a2*b3 - a3*b2



Step 2:

দ্বিতীয় Component:


a3*b1 - a1*b3



Step 3:

তৃতীয় Component:


a1*b2 - a2*b1



Result:


[C1,C2,C3]



Computer Graphics এ:


Triangle Points:


A

B

C


দুটি Edge Vector তৈরি করা হয়:


AB

AC


তারপর:


AB × AC


দিয়ে Surface Normal পাওয়া যায়।
"""


# ===========================================================
# 08_Examples
# ===========================================================


# Example 1: Basic Cross Product


A = [1,2,3]

B = [4,5,6]


cross = [

A[1]*B[2] - A[2]*B[1],

A[2]*B[0] - A[0]*B[2],

A[0]*B[1] - A[1]*B[0]

]


print("Cross Product:")
print(cross)



# Example 2: Perpendicular Vectors


A = [1,0,0]

B = [0,1,0]


result = [

A[1]*B[2] - A[2]*B[1],

A[2]*B[0] - A[0]*B[2],

A[0]*B[1] - A[1]*B[0]

]


print("X Axis × Y Axis:")
print(result)



# Example 3: Surface Normal


pointA = [0,0,0]

pointB = [1,0,0]

pointC = [0,1,0]


AB = [

pointB[0]-pointA[0],

pointB[1]-pointA[1],

pointB[2]-pointA[2]

]


AC = [

pointC[0]-pointA[0],

pointC[1]-pointA[1],

pointC[2]-pointA[2]

]


normal = [

AB[1]*AC[2]-AB[2]*AC[1],

AB[2]*AC[0]-AB[0]*AC[2],

AB[0]*AC[1]-AB[1]*AC[0]

]


print("Surface Normal:")
print(normal)



# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
1. Dot Product এবং Cross Product গুলিয়ে ফেলা


Dot Product:

Result = Scalar


Cross Product:

Result = Vector



------------------------------------------------


2. 2D Vector এ Cross Product ব্যবহার করা


Cross Product মূলত 3D Vector এর জন্য।



------------------------------------------------


3. Order ভুল করা


A × B


≠


B × A



কারণ:


B × A = -(A × B)



------------------------------------------------


4. Formula এর Sign ভুল করা


দ্বিতীয় Component এর Sign Negative হয়।



------------------------------------------------


5. Result Vector এর Direction ভুল বোঝা


Cross Product এর Result:

দুই Input Vector এর Perpendicular Direction।
"""


# ===========================================================
# 10_Exercises
# ===========================================================

"""
Beginner:


1.

A=[1,0,0]

B=[0,1,0]


Cross Product বের করো।



2.

A=[2,3,4]

B=[5,6,7]


Cross Product বের করো।



3.

Cross Product এবং Dot Product এর পার্থক্য লেখো।



Intermediate:


4.

প্রমাণ করো:


A × B = -(B × A)



5.

দুইটি Triangle Point থেকে Surface Normal বের করো।



Advanced:


6.

Game Engine এ Cross Product কেন প্রয়োজন ব্যাখ্যা করো।



7.

Torque Formula:

τ = r × F


ব্যাখ্যা করো।
"""


# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
Machine Learning এ Cross Product এর ব্যবহার
Dot Product এর তুলনায় কম হলেও
Computer Vision এবং Robotics এ গুরুত্বপূর্ণ।



------------------------------------------------
1. Computer Vision
------------------------------------------------


3D Image Processing এ:


Surface Normal

Orientation

Depth


নির্ণয়ের জন্য Cross Product ব্যবহৃত হয়।



------------------------------------------------
2. Robotics
------------------------------------------------


Robot Arm এর:

Rotation Axis

Movement Direction


নির্ণয়ে Cross Product ব্যবহার হয়।



------------------------------------------------
3. Computer Graphics
------------------------------------------------


3D Object:


Triangle Surface


দুটি Edge Vector:


AB

AC



Normal:


AB × AC



Lighting এবং Shadow Calculation এ
Normal প্রয়োজন।



------------------------------------------------
4. Physics Simulation
------------------------------------------------


Torque:


τ = r × F



Object কতটা ঘুরবে
তা নির্ণয় করতে ব্যবহৃত হয়।



------------------------------------------------
5. AI + 3D Models
------------------------------------------------


Autonomous Robot,

Self Driving Car,

3D Vision System


এ Cross Product গুরুত্বপূর্ণ।



------------------------------------------------
Summary:


Dot Product:

Similarity / Projection


Cross Product:

Perpendicular Direction / Area


AI ও Graphics এ:

Vector Mathematics

↓

Cross Product

↓

3D Understanding
"""


# ===========================================================
# End of Cross Product
# ===========================================================