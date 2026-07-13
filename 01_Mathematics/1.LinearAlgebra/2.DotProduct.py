"""
===========================================================
Dot Product (ডট প্রোডাক্ট)
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
Dot Product (Scalar Product) হলো Linear Algebra এর একটি
গুরুত্বপূর্ণ Vector Operation।

Dot Product দুইটি Vector এর মধ্যে সম্পর্ক বের করে।

এটি আমাদের বলে:

- দুইটি Vector কতটা একই দিকে আছে
- দুইটি Vector এর Similarity কত
- একটি Vector অন্য Vector এর দিকে কতটা প্রভাব ফেলছে


Dot Product এর Result সবসময় একটি Scalar Number হয়।

Example:

A = [2,3]

B = [4,5]


A · B = 23


এখানে Result Vector নয়, একটি সংখ্যা।
"""


# ===========================================================
# 02_WhyThisConceptExistsInRelationToHistory
# ===========================================================

"""
Dot Product কেন প্রয়োজন হলো?


Geometry এবং Physics এ একটি সমস্যা ছিল:

দুইটি Direction এর মধ্যে সম্পর্ক কীভাবে বের করা যায়?


Example:

দুইটি Force:

Force A → East

Force B → North


তারা কি একই দিকে কাজ করছে?


এই সম্পর্ক বোঝানোর জন্য Dot Product তৈরি হয়।


Dot Product এর মাধ্যমে:

- Angle between vectors
- Projection
- Work done by force

সহজে বের করা যায়।



History:

- Vector Algebra এর উন্নতির সাথে Dot Product তৈরি হয়।
- Josiah Willard Gibbs এবং Oliver Heaviside Vector Calculus উন্নয়নে গুরুত্বপূর্ণ ভূমিকা রাখেন।


বর্তমানে:

Dot Product হলো Machine Learning এর ভিত্তি।
"""


# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
Real Life Intuition:


------------------------------------------------
1. Force এবং Movement
------------------------------------------------


ধরি:

একটি বাক্সকে ১০ Newton Force দিয়ে ঠেলা হচ্ছে।

কিন্তু বাক্সটি যে দিকে যাচ্ছে,
Force সেই দিকেই না হলে সব Force কাজে লাগবে না।


Dot Product বলে:

কতটুকু Force কার্যকর হয়েছে।



------------------------------------------------
2. দুইজন মানুষের Similarity
------------------------------------------------


Person A:

[Height, Weight, Age]


Person B:

[Height, Weight, Age]


Dot Product ব্যবহার করে বোঝা যায়
তাদের Feature কতটা কাছাকাছি।



------------------------------------------------
3. AI Recommendation System
------------------------------------------------


তোমার পছন্দের Vector:

User Vector


একটি Movie Vector


Dot Product দিয়ে বের করা হয়:

Movie কতটা তোমার পছন্দের সাথে মিলে।
"""


# ===========================================================
# 04_Definition
# ===========================================================

"""
Dot Product হলো:

দুইটি সমান Dimension এর Vector এর
corresponding element গুলোকে multiply করে
সবগুলো যোগ করা।


ধরি:


A = [a1,a2,a3]

B = [b1,b2,b3]


তাহলে:


A · B =

(a1*b1) + (a2*b2) + (a3*b3)



Result:

একটি Scalar Number



শর্ত:

দুইটি Vector এর Dimension একই হতে হবে।
"""


# ===========================================================
# 05_Formula
# ===========================================================

"""
Algebraic Formula:


A · B = Σ(ai × bi)



2D Vector:


A = [a1,a2]

B = [b1,b2]


A · B = a1b1 + a2b2



3D Vector:


A · B =

a1b1 + a2b2 + a3b3



-----------------------------------------------


Geometric Formula:


A · B = |A| |B| cosθ



যেখানে:


|A| = Vector A এর Magnitude

|B| = Vector B এর Magnitude

θ = দুই Vector এর মাঝের Angle



যদি:


θ = 0°

তাহলে:

cos(0)=1

Maximum Dot Product



θ = 90°

তাহলে:

cos(90)=0

Dot Product = 0



θ = 180°

তাহলে:

cos(180)=-1

Negative Dot Product
"""


# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
Derivation:


ধরি দুইটি Vector:


A = (a1,a2)

B = (b1,b2)



Geometry থেকে:


Vector Difference:

|A-B|²


Pythagorean theorem ব্যবহার করি:


|A-B|² = |A|² + |B|² - 2|A||B|cosθ



আবার Algebra অনুযায়ী:


(A-B)·(A-B)


=

A·A - 2(A·B) + B·B



যেহেতু:


A·A = |A|²

B·B = |B|²



তাই:


A·B = |A||B|cosθ



এটাই Dot Product এর Geometric Formula।
"""


# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
Computer এর ভিতরে Dot Product খুব সহজ।


Example:


A = [2,3]

B = [4,5]



Memory:


A:

Index 0 -> 2
Index 1 -> 3



B:

Index 0 -> 4
Index 1 -> 5



Operation:


Index 0:

2 * 4 = 8


Index 1:

3 * 5 = 15



সব যোগ:


8 + 15 = 23



Result:

23



Machine Learning এ:


Input Vector:

[x1,x2,x3]


Weights:

[w1,w2,w3]


Dot Product:


x1w1+x2w2+x3w3



এটি Neural Network এর মূল Operation।
"""


# ===========================================================
# 08_Examples
# ===========================================================


# Example 1: Basic Dot Product

A = [2,3]
B = [4,5]


result = (A[0]*B[0]) + (A[1]*B[1])


print("Dot Product:", result)



# Example 2: Three Dimension


A = [1,2,3]
B = [4,5,6]


result = (
    A[0]*B[0] +
    A[1]*B[1] +
    A[2]*B[2]
)


print("3D Dot Product:", result)



# Example 3: Using Loop


A = [2,4,6]
B = [1,3,5]


dot = 0


for i in range(len(A)):
    dot += A[i] * B[i]


print("Using Loop:", dot)



# Example 4: Machine Learning Weight Calculation


features = [10,20,30]

weights = [0.5,0.2,0.1]


prediction = 0


for i in range(len(features)):
    prediction += features[i] * weights[i]


print("Prediction:", prediction)



# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
1. Dimension mismatch


ভুল:


A = [1,2]

B = [3,4,5]


Dot Product সম্ভব নয়।



------------------------------------------------


2. Dot Product এবং Cross Product গুলিয়ে ফেলা


Dot Product:

Result = Scalar


Cross Product:

Result = Vector



------------------------------------------------


3. Multiplication এর পরে যোগ করতে ভুল করা


ভুল:

(2+4)*(3+5)


সঠিক:

(2*3)+(4*5)



------------------------------------------------


4. Angle Formula ভুল ব্যবহার করা


A·B = |A||B|cosθ


এখানে θ অবশ্যই দুই Vector এর মধ্যকার Angle।
"""


# ===========================================================
# 10_Exercises
# ===========================================================

"""
Beginner:


1.

A=[2,3]

B=[4,5]

Dot Product বের করো।



2.

A=[1,2,3]

B=[4,5,6]

Dot Product বের করো।



3.

দুইটি Vector:

[5,5]

[2,2]

এর Dot Product বের করো।



Intermediate:


4.

যদি:

A·B = 0


তাহলে Vector দুটি সম্পর্কে কী বলা যায়?



5.

দুটি Vector এর Angle বের করার Formula লেখো।



Advanced:


6.

একটি Neural Network এর Weighted Sum
Dot Product দিয়ে Implement করো।



7.

Cosine Similarity কেন Dot Product ব্যবহার করে ব্যাখ্যা করো।
"""


# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
Machine Learning এ Dot Product সবচেয়ে বেশি ব্যবহৃত হয়।



------------------------------------------------
1. Linear Regression
------------------------------------------------


Formula:


Prediction = X · W + b



যেখানে:


X = Feature Vector

W = Weight Vector

b = Bias



Example:


Input:

[Age,Salary]


Weight:

[w1,w2]



Prediction:


Age*w1 + Salary*w2



------------------------------------------------
2. Neural Network
------------------------------------------------


Neuron:


Output = Activation(X · W + b)



প্রতিটি Neuron:

Input Vector

এর সাথে

Weight Vector

এর Dot Product করে।



------------------------------------------------
3. Cosine Similarity
------------------------------------------------


Text Embedding:


Document Vector

Query Vector



Similarity:


(A·B)/(|A||B|)



RAG AI System এ:

User Query

↓

Vector

↓

Dot Product

↓

Relevant Document Search



------------------------------------------------
4. Recommendation System
------------------------------------------------


User Vector

·

Product Vector


বেশি Dot Product মানে:

বেশি Similarity



------------------------------------------------
5. Large Language Model (LLM)
------------------------------------------------


Transformer Architecture এ:


Query

Key


এর মধ্যে Dot Product দিয়ে

Attention Score তৈরি করা হয়।



Summary:


Dot Product হলো:

Vector এর ভাষায় similarity এবং interaction measure করার
সবচেয়ে গুরুত্বপূর্ণ Operation।


AI = Vector + Dot Product + Matrix Operations
"""


# ===========================================================
# End of Dot Product
# ===========================================================