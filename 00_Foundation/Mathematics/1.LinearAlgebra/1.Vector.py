# ===========================================================
# 01_Introduction
# ===========================================================
"""
ভেক্টর (Vector) হলো Linear Algebra এর একটি মৌলিক ধারণা। 
সহজভাবে বললে: Vector হলো এমন একটি Mathematical Object যার দুইটি প্রধান বৈশিষ্ট্য থাকে: 
1. Magnitude (মান / দৈর্ঘ্য), 2. Direction (দিক)| 
উদাহরণ: একটি গাড়ি যদি ৫০ km/h গতিতে উত্তর দিকে যায়। 
এখানে: Magnitude = 50 km/h, Direction = North তাই এটি একটি Vector Quantity.

Linear Algebra এ Vector ব্যবহার করা হয়: - Machine Learning, - Computer Graphics, - Physics Simulation, - Robotics, - Data Science, - Deep Learning.

AI এর জগতে: একটি ছবি, শব্দ বা Text কে Vector আকারে প্রকাশ করা হয়।

যেমন: Cat Image: [ 0.23, 0.56, 0.89, 0.12 ] | এই সংখ্যাগুলোই Image এর Vector Representation.
"""

# ===========================================================
# 02_WhyThisConceptExistsInRelationToHistory
# ===========================================================
"""
Vector কেন প্রয়োজন হলো? প্রাচীন গণিতে মূলত Scalar Quantity ব্যবহার করা হতো।
Scalar: শুধু মান প্রকাশ করে। যেমন: Weight = 50 kg, Temperature = 30°C কিন্তু Physics এ সমস্যা দেখা দিল। কারণ কিছু জিনিস শুধু মান দিয়ে প্রকাশ করা যায় না। যেমন: একটি জাহাজকে বলতে হবে: "১০০ km যাও" এটি অসম্পূর্ণ। কারণ জানতে হবে: কোন দিকে যাবে?
তাই Direction + Magnitude প্রকাশ করার জন্য Vector ধারণা তৈরি হয়।

Vector এর উন্নয়ন:
- 1800 সালের দিকে Physics এবং Geometry তে Vector ধারণা জনপ্রিয় হয়।
- William Rowan Hamilton এর Quaternion ধারণা Vector Mathematics এ গুরুত্বপূর্ণ ভূমিকা রাখে।
- Gibbs এবং Heaviside আধুনিক Vector Algebra তৈরি করেন।

বর্তমানে: Computer Science এবং AI তে Vector হলো Data Representation এর মূল ভিত্তি।
"""

# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
Real Life এ Vector:

------------------------------------------------
1. গাড়ির গতি
------------------------------------------------

গাড়ি:

Speed = 60 km/h
Direction = East


এটি Vector.


------------------------------------------------
2. বিমান চলাচল
------------------------------------------------

Airplane:

Velocity = 800 km/h
Direction = South-East


------------------------------------------------
3. Force
------------------------------------------------

Physics এ Force:

Force = Magnitude + Direction


যেমন:

একটি বাক্সকে ডান দিকে ঠেলা।


------------------------------------------------
4. AI Data
------------------------------------------------

একজন মানুষের Height এবং Weight:

Person:

Height = 170
Weight = 65


Vector:

[
170,
65
]


Machine Learning Model এই Vector ব্যবহার করে।
"""


# ===========================================================
# 04_Definition
# ===========================================================

"""
Vector হলো:

একটি ordered list of numbers যা space এর মধ্যে
একটি point বা direction প্রকাশ করে।


Mathematically:

একটি Vector:

v = [x1, x2, x3, .... xn]


যেখানে:

x1, x2, x3 ... xn হলো Vector এর Components.


Example:

2D Vector:

v = [3,4]


3D Vector:

v = [2,5,7]


n-dimensional Vector:

v = [x1,x2,x3,...xn]


Machine Learning এ:

Feature Vector:

X = [
Age,
Height,
Weight,
Salary
]


প্রতিটি value একটি feature।
"""


# ===========================================================
# 05_Formula
# ===========================================================

"""
1. Vector Magnitude:

একটি Vector এর দৈর্ঘ্য:

For 2D:

v = (x,y)


|v| = √(x² + y²)



For 3D:

v = (x,y,z)


|v| = √(x²+y²+z²)



General Formula:


|v| = √(x1²+x2²+...+xn²)



------------------------------------------------


2. Vector Addition:


a = [a1,a2]

b = [b1,b2]


a+b =

[a1+b1,
 a2+b2]


------------------------------------------------


3. Scalar Multiplication:


k × v


যেখানে k হলো সংখ্যা।


Example:

2 × [3,4]

=

[6,8]



------------------------------------------------


4. Dot Product:


a.b =

a1b1 + a2b2 + ... + anbn



Dot Product ব্যবহার হয়:

- Similarity
- Angle calculation
- Machine Learning
"""


# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
Vector Magnitude Derivation:


ধরি একটি 2D Vector:

v = (x,y)


এটি একটি Right Triangle তৈরি করে।


Pythagorean theorem:


c² = a²+b²


এখানে:


c = Vector Length

a = x component

b = y component


তাই:


|v|² = x²+y²


Square root করলে:


|v| = √(x²+y²)



এই ধারণা থেকেই:

n-dimensional Vector এর Formula এসেছে:


|v| = √(Σ xi²)


"""


# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
Computer এর ভিতরে Vector আসলে একটি Array।


Example:

Vector:

[10,20,30]


Memory:

Index 0 -> 10
Index 1 -> 20
Index 2 -> 30



Python:

vector = [10,20,30]


Machine Learning এ:

Input Data:


[
Height,
Weight,
Age
]


Convert হয়:


X = [
170,
65,
25
]


Model এই Vector এর উপর Mathematical Operation চালায়।



Neural Network:

Input Vector

       |
       v

Matrix Multiplication

       |
       v

Output Vector



Deep Learning এর সব Layer Vector এবং Matrix operation এর উপর কাজ করে।
"""


# ===========================================================
# 08_Examples
# ===========================================================


# Example 1: Creating Vector

vector = [3, 4]

print("Vector:", vector)



# Example 2: Vector Magnitude

import math


x = 3
y = 4


magnitude = math.sqrt(x*x + y*y)


print("Magnitude:", magnitude)



# Example 3: Vector Addition


vector1 = [2,3]
vector2 = [4,5]


result = [
    vector1[0]+vector2[0],
    vector1[1]+vector2[1]
]


print("Addition:", result)



# Example 4: AI Feature Vector


person = [
    25,     # Age
    170,    # Height
    65      # Weight
]


print("Feature Vector:", person)



# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
1. Vector এবং Scalar গুলিয়ে ফেলা

ভুল:

Distance = Vector


সঠিক:

Distance = Scalar

Displacement = Vector



------------------------------------------------


2. Direction ভুলে যাওয়া

Vector এ Direction গুরুত্বপূর্ণ।


------------------------------------------------


3. Vector Dimension ভুল বোঝা


[1,2]

এটি 2D Vector


[1,2,3]

এটি 3D Vector



------------------------------------------------


4. Vector Addition এ Dimension mismatch


ভুল:


[1,2] + [3,4,5]


সম্ভব নয়।



------------------------------------------------


5. AI তে Feature Scaling না করা


বড় এবং ছোট সংখ্যার পার্থক্য Model কে প্রভাবিত করতে পারে।
"""


# ===========================================================
# 10_Exercises
# ===========================================================

"""
Beginner:

1.

একটি Vector:

v = [6,8]

এর Magnitude বের করো।



2.

দুটি Vector যোগ করো:


A=[1,2]

B=[3,4]



3.

Scalar multiplication করো:


3 × [2,5]



Intermediate:


4.

একটি 3D Vector:

[2,3,6]

এর Magnitude বের করো।



5.

Dot Product বের করো:


A=[2,3]

B=[4,5]



Advanced:


6.

একটি Student Feature Vector তৈরি করো:


Age
Height
Marks
Attendance


7.

একটি Image কে Vector এ Convert করার ধারণা ব্যাখ্যা করো।
"""


# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
Machine Learning এ Vector হলো সবচেয়ে গুরুত্বপূর্ণ Data Structure.


------------------------------------------------
1. Feature Vector
------------------------------------------------


Machine Learning Model এ Input:

Student:

Age = 20
Height = 170
Marks = 90


Vector:

X = [

20,
170,
90

]



------------------------------------------------
2. Image Processing
------------------------------------------------


একটি Image:

100 x 100 pixels


প্রতিটি pixel value:

0-255


Flatten করলে:


[120,130,140,...]


এটি Image Vector.



------------------------------------------------
3. Natural Language Processing
------------------------------------------------


Text:

"King"


Model এটিকে Vector এ পরিবর্তন করে:


[0.21,0.45,0.76,...]


একে বলা হয়:

Word Embedding.



------------------------------------------------
4. Neural Network
------------------------------------------------


Neural Network:

Input Vector

        |

Matrix Multiplication

        |

Activation Function

        |

Output Vector



------------------------------------------------
5. Similarity Search
------------------------------------------------


RAG AI System এ:


Document Vector

+

Query Vector


তাদের মধ্যে:

Cosine Similarity


ব্যবহার করে সবচেয়ে কাছের তথ্য খুঁজে বের করা হয়।



------------------------------------------------
Summary:

AI = Data → Vector → Mathematical Operations → Prediction


Vector ছাড়া:

Machine Learning,
Deep Learning,
LLM,
Computer Vision

কাজ করা সম্ভব নয়।
"""


# ===========================================================
# End of Vector
# ===========================================================