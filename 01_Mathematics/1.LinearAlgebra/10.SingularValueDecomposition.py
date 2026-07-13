"""
===========================================================
Singular Value Decomposition (SVD)
সিঙ্গুলার ভ্যালু ডিকম্পোজিশন
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
Singular Value Decomposition (SVD) হলো Linear Algebra এর
সবচেয়ে শক্তিশালী Matrix Decomposition Technique গুলোর একটি।


সহজভাবে:

একটি বড় Matrix কে তিনটি ছোট Matrix এ ভেঙে ফেলার
পদ্ধতি হলো SVD।



Formula:


A = UΣVᵀ



যেখানে:


A = Original Matrix

U = Left Singular Vector Matrix

Σ = Singular Value Matrix

Vᵀ = Right Singular Vector Matrix



SVD ব্যবহার করা হয়:


- Data Compression
- Dimensionality Reduction
- Image Compression
- Recommendation System
- Machine Learning
- Natural Language Processing



AI এর জগতে:

SVD হলো Hidden Pattern বের করার
একটি গুরুত্বপূর্ণ Mathematical Tool।
"""


# ===========================================================
# 02_WhyThisConceptExistsInRelationToHistory
# ===========================================================

"""
SVD কেন প্রয়োজন হলো?


অনেক বড় Matrix নিয়ে কাজ করার সময় সমস্যা হয়:


- Storage বেশি লাগে
- Calculation ধীর হয়
- সব Information সমান গুরুত্বপূর্ণ নয়


তখন প্রশ্ন আসে:


একটি বড় Matrix এর মধ্যে থাকা
সবচেয়ে গুরুত্বপূর্ণ Information কিভাবে বের করা যায়?


এই সমস্যার সমাধান:

Singular Value Decomposition।



History:


- Eigenvalue এবং Eigenvector Analysis থেকে SVD এর ধারণা আসে।
- Eugenio Beltrami এবং Camille Jordan SVD এর প্রথম ধারণা দেন।
- পরবর্তীতে Eckart এবং Young Approximation Theory উন্নত করেন।



বর্তমানে:


SVD হলো Machine Learning এবং Data Science এর
সবচেয়ে গুরুত্বপূর্ণ Matrix Technique গুলোর একটি।
"""


# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
Real Life Intuition:


------------------------------------------------
1. Image Compression
------------------------------------------------


একটি Image:


1000 × 1000 Pixel


মানে:

10 লক্ষ Data Point।


কিন্তু সব Pixel সমান গুরুত্বপূর্ণ নয়।


SVD ব্যবহার করে:

Important Pattern রাখা হয়।

অপ্রয়োজনীয় Information বাদ দেওয়া হয়।



Result:

ছোট Size এর Image Representation।



------------------------------------------------
2. Recommendation System
------------------------------------------------


User-Movie Rating Matrix:


        Movie1 Movie2 Movie3

User1      5      3      ?

User2      4      ?      2



SVD খুঁজে বের করে:


User Hidden Preference

এবং

Movie Hidden Feature।



------------------------------------------------
3. Data Compression


Original Data:

High Dimension


↓

SVD


↓

Low Dimension Representation



------------------------------------------------
4. Noise Removal


Image বা Signal থেকে Noise কমানোর জন্য
Small Singular Value বাদ দেওয়া হয়।
"""


# ===========================================================
# 04_Definition
# ===========================================================

"""
Singular Value Decomposition হলো:


একটি Matrix A কে তিনটি Matrix এর
গুণফল হিসেবে প্রকাশ করার পদ্ধতি।



Formula:


A = UΣVᵀ



যেখানে:


A:

m × n Matrix



U:

m × m Orthogonal Matrix



Σ:

m × n Diagonal Matrix



Vᵀ:

n × n Orthogonal Matrix



এখানে:


Σ এর Diagonal Element গুলো হলো:

Singular Values



"""


# ===========================================================
# 05_Formula
# ===========================================================

"""
Main Formula:


A = UΣVᵀ



------------------------------------------------


Singular Values বের করার Formula:


AᵀA এর Eigenvalues:


λ1, λ2, λ3 ...


তাহলে:


Singular Values:


σ = √λ



------------------------------------------------


Properties:


1.


UᵀU = I



2.


VᵀV = I



3.


Σ এর diagonal value:

σ1 ≥ σ2 ≥ σ3...



সবচেয়ে বড় Singular Value:

সবচেয়ে বেশি Information ধারণ করে।
"""


# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
SVD Derivation:


ধরি:

A একটি Matrix।



প্রথমে:


AᵀA


বের করা হয়।



AᵀA একটি Square Matrix।



তার Eigenvalues বের করি:


λ1, λ2,...λn



তারপর:


Singular Values:


σi = √λi



এই Singular Values দিয়ে:


Σ Matrix তৈরি হয়।



Eigenvectors থেকে:

V Matrix তৈরি হয়।



তারপর:


U = AVΣ⁻¹



পাওয়া যায়।



শেষে:


A = UΣVᵀ


"""


# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
Computer এর ভিতরে SVD:


ধরি:


A = Image Matrix



Step 1:

AᵀA Calculate করা হয়।



Step 2:

Eigenvalue বের করা হয়।



Step 3:

Singular Value পাওয়া যায়।



Step 4:

U, Σ, V Matrix তৈরি হয়।



Step 5:


A = UΣVᵀ



------------------------------------------------


Image Compression:


Original:


A = UΣVᵀ



সব Singular Value রাখা হয় না।



শুধু বড় Singular Value রাখা হয়:


A ≈ UΣkVᵀ



যেখানে k ছোট।



এতে:

Size কমে যায়,

কিন্তু গুরুত্বপূর্ণ Information থাকে।
"""


# ===========================================================
# 08_Examples
# ===========================================================


# Example 1: Using NumPy SVD


import numpy as np


A = np.array(

[
[1,2],
[3,4],
[5,6]

]

)


U, S, VT = np.linalg.svd(A)



print("U Matrix:")
print(U)



print("Singular Values:")
print(S)



print("V Transpose:")
print(VT)



# Example 2: Image Compression Concept


singular_values = [

10,
5,
1,
0.1,
0.01

]


print("Original Singular Values:")
print(singular_values)



important_values = singular_values[:3]


print("Keep Important Values:")
print(important_values)



# Example 3: Low Rank Approximation


U = np.array(

[
[1,0],
[0,1]

]

)


S = np.array(

[
5,0
]

)


print("Important Components:")
print(S)



# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
1. SVD এবং Eigenvalue একই মনে করা


দুটো সম্পর্কিত হলেও একই নয়।



Eigenvalue:

Square Matrix এর জন্য বেশি ব্যবহৃত।



SVD:

যেকোনো Matrix এর জন্য কাজ করে।



------------------------------------------------


2. Singular Value কে Eigenvalue ভাবা


Singular Value:


√Eigenvalue



------------------------------------------------


3. সব Singular Value সমান গুরুত্বপূর্ণ ভাবা


বড় Singular Value বেশি Information বহন করে।



------------------------------------------------


4. V এবং Vᵀ এর পার্থক্য ভুল করা


Formula:


A = UΣVᵀ



V নয়,

V Transpose লাগে।



------------------------------------------------


5. SVD শুধু Compression এর জন্য মনে করা


এটি:

PCA,
Recommendation,
Optimization

এও ব্যবহৃত হয়।
"""


# ===========================================================
# 10_Exercises
# ===========================================================

"""
Beginner:


1.

SVD Formula লেখো।



2.

U, Σ, Vᵀ এর কাজ কী?



3.

Singular Value কী?



Intermediate:


4.

কেন বড় Singular Value বেশি গুরুত্বপূর্ণ?



5.

Image Compression এ SVD কিভাবে কাজ করে?



Advanced:


6.

প্রমাণ করো:


A = UΣVᵀ



7.

PCA এবং SVD এর সম্পর্ক ব্যাখ্যা করো।



8.

Low Rank Approximation কেন কাজ করে?
"""


# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
Machine Learning এবং AI তে SVD অত্যন্ত গুরুত্বপূর্ণ।



------------------------------------------------
1. Principal Component Analysis (PCA)
------------------------------------------------


PCA সাধারণত:


Covariance Matrix


এর SVD ব্যবহার করে।



Steps:


Data Matrix

↓

Center Data

↓

SVD

↓

Important Components Select



------------------------------------------------
2. Recommendation System
------------------------------------------------


Netflix, Spotify এর মতো System এ:


User-Item Matrix


কে:


UΣVᵀ


আকারে ভাঙা হয়।



এতে পাওয়া যায়:


User Hidden Features

+

Item Hidden Features



------------------------------------------------
3. Image Compression
------------------------------------------------


Image Matrix:


↓

SVD


↓

Top Singular Values রাখা


↓

Compressed Image



------------------------------------------------
4. Noise Reduction


Small Singular Value বাদ দিলে:

Noise কমে যায়।



------------------------------------------------
5. Natural Language Processing


Text Embedding Matrix:

SVD দিয়ে

Hidden Semantic Structure

খুঁজে বের করা যায়।



------------------------------------------------
6. Deep Learning


Large Neural Network Weight Matrix:

Compress করার জন্য

Low Rank SVD ব্যবহার করা হয়।



------------------------------------------------
7. LLM Optimization


Large Language Model এর:

Weight Compression

Memory Reduction

Inference Speed Improvement


এর জন্য SVD-based Technique ব্যবহার করা হয়।



------------------------------------------------
Summary:


SVD:


Large Matrix

↓

UΣVᵀ

↓

Important Hidden Information

↓

Compression + Understanding



Modern AI এর:

PCA,
Recommendation,
Computer Vision,
LLM Optimization

সব জায়গায় SVD একটি Fundamental Tool।
"""


# ===========================================================
# End of Singular Value Decomposition
# ===========================================================