"""
===========================================================
Matrix Factorization (ম্যাট্রিক্স ফ্যাক্টরাইজেশন)
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
Matrix Factorization হলো Linear Algebra এর একটি গুরুত্বপূর্ণ
Technique যেখানে একটি বড় Matrix কে কয়েকটি ছোট Matrix এ
ভেঙে ফেলা হয়।


সহজভাবে:

একটি Matrix:

A


কে ভেঙে:


A = B × C


আকারে প্রকাশ করা হয়।


এটি ব্যবহার করা হয়:


- Data Compression
- Recommendation System
- Machine Learning
- Image Compression
- Feature Extraction


AI এর জগতে:

বড় Dataset Matrix থেকে Hidden Pattern বের করার জন্য
Matrix Factorization ব্যবহার করা হয়।
"""


# ===========================================================
# 02_WhyThisConceptExistsInRelationToHistory
# ===========================================================

"""
Matrix Factorization কেন প্রয়োজন হলো?


বড় Matrix নিয়ে সরাসরি কাজ করা কঠিন।


Example:


একটি Movie Recommendation System এ:


Users × Movies Matrix


হাজার হাজার User এবং Movie থাকতে পারে।


যদি Matrix অনেক বড় হয়:

Memory বেশি লাগে।

Calculation ধীর হয়।



তাই প্রশ্ন আসে:


এই বড় Matrix কে কি ছোট কিছু Matrix দিয়ে প্রকাশ করা যায়?


এই সমস্যার সমাধান:

Matrix Factorization।



History:


- Linear Algebra এর উন্নতির সাথে Matrix Decomposition ধারণা তৈরি হয়।
- Gaussian Elimination, Eigenvalue Analysis থেকে
  Factorization Technique উন্নত হয়।
- Singular Value Decomposition (SVD) আধুনিক Matrix Factorization এর গুরুত্বপূর্ণ অংশ।



বর্তমানে:


Netflix, Spotify, Recommendation System এ
এটি ব্যাপকভাবে ব্যবহৃত হয়।
"""


# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
Real Life Intuition:


------------------------------------------------
1. Movie Recommendation
------------------------------------------------


ধরি:


User-Movie Rating Matrix:


          Movie1 Movie2 Movie3

User1       5      3      ?

User2       4      ?      2



এখানে ? মানে User Rating দেয়নি।



Matrix Factorization বুঝতে পারে:


User Preference

এবং

Movie Feature



তারপর অনুমান করে:

User কোন Movie পছন্দ করবে।



------------------------------------------------
2. Image Compression
------------------------------------------------


একটি Image Matrix:


1000 × 1000


এটি অনেক বড়।


Factorization করে:


ছোট দুটি Matrix:


1000 × k

k × 1000


দিয়ে প্রকাশ করা যায়।



------------------------------------------------
3. Hidden Pattern


একটি Dataset এ:

অনেক Feature থাকে।


Factorization:

Hidden Feature বের করে।
"""


# ===========================================================
# 04_Definition
# ===========================================================

"""
Matrix Factorization হলো:

একটি Matrix কে দুই বা ততোধিক ছোট Matrix এর
গুণফল হিসেবে প্রকাশ করার Process।



General Form:


A = B × C



যেখানে:


A = Original Matrix


B,C = Factor Matrices



Example:


A(m×n)


কে:


U(m×k)

×

V(k×n)


আকারে লেখা হয়।



যেখানে:

k হলো Latent Dimension।



k সাধারণত:

m এবং n থেকে ছোট হয়।
"""


# ===========================================================
# 05_Formula
# ===========================================================

"""
1. Basic Matrix Factorization:


A = BC



------------------------------------------------


2. LU Factorization:


A = LU



যেখানে:


L = Lower Triangular Matrix


U = Upper Triangular Matrix



------------------------------------------------


3. QR Factorization:


A = QR



যেখানে:


Q = Orthogonal Matrix


R = Upper Triangular Matrix



------------------------------------------------


4. Singular Value Decomposition (SVD):


A = UΣVᵀ



যেখানে:


U = Left Singular Vector


Σ = Singular Values


Vᵀ = Right Singular Vector



------------------------------------------------


5. Recommendation System:


R ≈ P × Qᵀ



যেখানে:


R = Rating Matrix


P = User Feature Matrix


Q = Movie Feature Matrix
"""


# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
Matrix Factorization এর মূল ধারণা:


ধরি একটি Matrix:


A



এর মধ্যে অনেক Information আছে।


কিন্তু সব Information প্রয়োজনীয় নয়।



Eigenvalue এবং SVD থেকে জানা যায়:

বড় Matrix এর মধ্যে কিছু গুরুত্বপূর্ণ
Direction থাকে।



এই Important Information ব্যবহার করে:


A কে:


UΣVᵀ


আকারে প্রকাশ করা যায়।



SVD থেকে:


A ≈ Smaller Representation



এটাই Matrix Factorization এর ভিত্তি।
"""


# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
Computer এর ভিতরে:


Original Matrix:


A


ধরি:


10000 × 10000



এটি অনেক বড়।



Factorization:


A = U × Vᵀ



যেখানে:


U:

10000 × 50


V:

10000 × 50



এখন:


দুইটি ছোট Matrix ব্যবহার করে
Original Information Approximate করা যায়।



------------------------------------------------


Recommendation System:


User Matrix:


U


×


Movie Matrix:


V


=

Rating Prediction



Algorithm:


1. Random Factor Matrix তৈরি।

2. Prediction Error বের করা।

3. Gradient Descent দিয়ে Update করা।

4. Error কমানো।



"""


# ===========================================================
# 08_Examples
# ===========================================================


# Example 1: Simple Matrix Factorization Idea


import numpy as np


A = np.array(

[
[2,4],
[3,6]
]

)


B = np.array(

[
[1,2],
[1.5,3]
]

)


print("Original Matrix:")
print(A)



# Example 2: SVD


matrix = np.array(

[
[1,2],
[3,4],
[5,6]
]

)


U, S, VT = np.linalg.svd(matrix)


print("U Matrix:")
print(U)


print("Singular Values:")
print(S)


print("V Transpose:")
print(VT)



# Example 3: Recommendation Idea


user_features = np.array(

[
[5,2],
[4,1]

]

)


movie_features = np.array(

[
[3,4],
[2,5]

]

)


prediction = user_features @ movie_features.T


print("Predicted Ratings:")
print(prediction)



# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
1. Matrix Factorization মানে Matrix Division ভাবা


ভুল।


এটি Matrix কে ছোট Matrix এ ভাঙা।



------------------------------------------------


2. Exact এবং Approximate Factorization গুলিয়ে ফেলা


অনেক সময়:


A = BC


না হয়ে:


A ≈ BC


হয়।



------------------------------------------------


3. সব Matrix একইভাবে Factorize করা যায় ভাবা


Different Matrix এর জন্য:

Different Method লাগে।



------------------------------------------------


4. Latent Feature ভুল বোঝা


Latent Feature সরাসরি দেখা যায় না।

এগুলো Hidden Pattern।



------------------------------------------------


5. Factor সংখ্যা খুব বেশি নেওয়া


বেশি Factor:

Overfitting করতে পারে।
"""


# ===========================================================
# 10_Exercises
# ===========================================================

"""
Beginner:


1.

Matrix Factorization এর সংজ্ঞা লেখো।



2.

A = BC

এর অর্থ কী?



3.

LU এবং SVD এর পূর্ণরূপ লেখো।



Intermediate:


4.

একটি 3×3 Matrix কে ছোট Matrix এ
ভাঙার ধারণা ব্যাখ্যা করো।



5.

Recommendation System এ Matrix Factorization
কেন ব্যবহার হয়?



Advanced:


6.

SVD:

A = UΣVᵀ


ব্যাখ্যা করো।



7.

Gradient Descent দিয়ে Matrix Factorization
কিভাবে শেখানো হয়?
"""


# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
AI এবং Machine Learning এ
Matrix Factorization অত্যন্ত গুরুত্বপূর্ণ।



------------------------------------------------
1. Recommendation System
------------------------------------------------


Netflix:

User-Movie Matrix


Spotify:

User-Song Matrix



Factorization:


User Preference

+

Item Feature


থেকে

Recommendation তৈরি করে।



------------------------------------------------
2. Collaborative Filtering
------------------------------------------------


User Behavior থেকে:

Hidden Feature

শেখে।



Formula:


R ≈ P Qᵀ



------------------------------------------------
3. Dimensionality Reduction


High Dimension Data:


↓

Low Dimension Representation



PCA এবং SVD ব্যবহার করে
Feature কমানো হয়।



------------------------------------------------
4. Image Compression


Image Matrix:


↓

Factorized Matrix


↓

Compressed Image



------------------------------------------------
5. Natural Language Processing


Word Embedding Matrix এ:

Hidden Semantic Pattern

খুঁজে বের করতে
Factorization ব্যবহার হয়।



------------------------------------------------
6. Deep Learning


Embedding Layer এবং
Parameter Compression এ
Matrix Factorization ব্যবহার হয়।



------------------------------------------------
7. LLM Optimization


Large Model এর:

Weight Matrix


Compress এবং Approximate করার জন্য
Low-Rank Matrix Factorization ব্যবহার করা হয়।



------------------------------------------------
Summary:


Matrix Factorization:


Large Matrix

↓

Small Hidden Matrices

↓

Pattern Extraction

↓

Prediction


Modern AI এর:

Recommendation,
Compression,
Embedding,
LLM Optimization

সব জায়গায় Matrix Factorization গুরুত্বপূর্ণ।
"""


# ===========================================================
# End of Matrix Factorization
# ===========================================================