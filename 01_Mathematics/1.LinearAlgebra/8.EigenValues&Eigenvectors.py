"""
===========================================================
Eigenvalues and Eigenvectors (Eigenvalue এবং Eigenvector)
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
Eigenvalues এবং Eigenvectors হলো Linear Algebra এর
সবচেয়ে গুরুত্বপূর্ণ এবং Advanced Concept গুলোর একটি।


সহজভাবে:

যখন একটি Matrix কোনো Vector এর উপর কাজ করে,
তখন বেশিরভাগ Vector এর Direction পরিবর্তন হয়।

কিন্তু কিছু বিশেষ Vector আছে যাদের Direction পরিবর্তন হয় না।

এই বিশেষ Vector হলো:

Eigenvector


এবং Matrix সেই Vector কে কত গুণ পরিবর্তন করে
তা হলো:

Eigenvalue



Example:


A × v = λ × v



যেখানে:


A = Matrix

v = Eigenvector

λ = Eigenvalue



ব্যবহার:

- Machine Learning
- Deep Learning
- PCA
- Computer Vision
- Physics Simulation
- Data Compression
"""


# ===========================================================
# 02_WhyThisConceptExistsInRelationToHistory
# ===========================================================

"""
Eigenvalue এবং Eigenvector কেন প্রয়োজন হলো?


Linear Transformation বোঝার জন্য।


একটি Matrix যখন একটি Vector এর উপর কাজ করে:

কখনো Direction পরিবর্তন করে।

কখনো শুধু Scale পরিবর্তন করে।


প্রশ্ন ছিল:

কোন Vector আছে যাদের Direction অপরিবর্তিত থাকে?


এই প্রশ্নের উত্তর:

Eigenvector



History:


- 1700-1800 সালের দিকে Differential Equation এবং
  Linear Transformation গবেষণায় এই ধারণা আসে।
- Euler, Lagrange, Cauchy এবং Hilbert এই ক্ষেত্রে
  গুরুত্বপূর্ণ অবদান রাখেন।
- "Eigen" শব্দটি German, যার অর্থ "নিজস্ব" বা "নিজের"।


বর্তমানে:


Machine Learning এ Data এর গুরুত্বপূর্ণ Direction
খুঁজে বের করতে Eigenvalue এবং Eigenvector ব্যবহার হয়।
"""


# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
Real Life Intuition:


------------------------------------------------
1. Stretching Rubber Sheet
------------------------------------------------


একটি Rubber Sheet কে Stretch করলে:


কিছু Direction এ বেশি Stretch হয়।

কিছু Direction এ কম।


যে Direction পরিবর্তন হয় না:

Eigenvector


Stretching Amount:

Eigenvalue



------------------------------------------------
2. Image Compression
------------------------------------------------


একটি Image এ অনেক Data থাকে।


কিন্তু কিছু Direction এ বেশি Information থাকে।


PCA ব্যবহার করে:

Important Direction

খুঁজে বের করা হয়।



------------------------------------------------
3. Earthquake Analysis
------------------------------------------------


Building এর বিভিন্ন Natural Frequency থাকে।


Eigenvalue এবং Eigenvector দিয়ে
Vibration Mode বের করা হয়।



------------------------------------------------
4. Google PageRank
------------------------------------------------


Web Page এর Relationship Matrix থেকে
Important Page বের করতে Eigenvector ধারণা ব্যবহৃত হয়।
"""


# ===========================================================
# 04_Definition
# ===========================================================

"""
Eigenvector:

একটি Non-zero Vector যা Matrix Transformation এর পরে
নিজের Direction পরিবর্তন করে না।



Mathematically:


A v = λv



যেখানে:


A = Matrix

v = Eigenvector

λ = Eigenvalue



Eigenvalue:

Matrix দ্বারা Eigenvector কত গুণ
Scale হয়েছে তার পরিমাণ।



Example:


যদি:


A v = 3v


তাহলে:


Eigenvalue = 3



Meaning:

Vector তিন গুণ বড় হয়েছে।
"""


# ===========================================================
# 05_Formula
# ===========================================================

"""
Main Formula:


A v = λ v



Rearrange:


A v - λv = 0



Common factor:


(A - λI)v = 0



যেখানে:


I = Identity Matrix



Non-zero solution পাওয়ার জন্য:


det(A - λI)=0



এটাই Characteristic Equation।



Steps:


1. Matrix A নেওয়া।

2. A - λI বের করা।

3. Determinant বের করা।

4. Equation solve করে λ বের করা।

5. প্রতিটি λ এর জন্য Eigenvector বের করা।
"""


# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
Derivation:


মূল সম্পর্ক:


A v = λv



সব Term এক পাশে:


Av - λv = 0



λv কে Matrix আকারে লিখলে:


Av - λIv = 0



Common v বের করলে:


(A-λI)v = 0



এখন:

v যেন Zero না হয়,

তাই Matrix এর Determinant Zero হতে হবে।



সুতরাং:


det(A-λI)=0



এই Equation থেকে:

Eigenvalues পাওয়া যায়।
"""


# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
Computer এর ভিতরে:


ধরি:


A =


[
2 0
0 3
]



Vector:


v1 = [1,0]


Transformation:


A × v1


=

[2,0]



Direction একই:

[1,0]

থেকে

[2,0]


শুধু Scale হয়েছে।


তাই:


Eigenvector = [1,0]


Eigenvalue = 2



------------------------------------------------


Algorithm:


1. Characteristic Polynomial তৈরি।

2. Polynomial Solve।

3. Eigenvalues বের।

4. Linear Equation Solve করে
   Eigenvectors বের।



Python Library:

NumPy:

numpy.linalg.eig()

ব্যবহার করে করা যায়।
"""


# ===========================================================
# 08_Examples
# ===========================================================


# Example 1: Simple Eigenvalue Concept


matrix = [

[2,0],

[0,3]

]


vector = [

[1],

[0]

]


result = [

[2*vector[0][0]],

[3*vector[1][0]]

]


print("Matrix Result:")
print(result)



# Example 2: Using NumPy


import numpy as np


A = np.array(

[
[2,0],
[0,3]
]

)


eigenvalues, eigenvectors = np.linalg.eig(A)


print("Eigenvalues:")
print(eigenvalues)


print("Eigenvectors:")
print(eigenvectors)



# Example 3: Scaling Interpretation


eigenvalue = 5


vector = [2,3]


scaled_vector = [

eigenvalue * vector[0],

eigenvalue * vector[1]

]


print("Scaled Vector:")
print(scaled_vector)



# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
1. Zero Vector কে Eigenvector মনে করা


Eigenvector অবশ্যই:

Non-zero Vector হতে হবে।



------------------------------------------------


2. সব Vector Eigenvector মনে করা


শুধু কিছু বিশেষ Vector Eigenvector হয়।



------------------------------------------------


3. Eigenvalue এবং Eigenvector গুলিয়ে ফেলা


Eigenvector:

Direction


Eigenvalue:

Scaling Amount



------------------------------------------------


4. Non-square Matrix এ Eigenvalue বের করা


সাধারণত:

Square Matrix এর জন্য Eigenvalue সংজ্ঞায়িত।



------------------------------------------------


5. Eigenvector এর Length গুরুত্বপূর্ণ ভাবা


Eigenvector এর Direction গুরুত্বপূর্ণ,
Magnitude নয়।
"""


# ===========================================================
# 10_Exercises
# ===========================================================

"""
Beginner:


1.

Eigenvalue এবং Eigenvector এর পার্থক্য লেখো।



2.

Formula লেখো:


Av = λv



3.

Identity Matrix এর Eigenvalue কী?



Intermediate:


4.

Matrix:


[
2 0
0 3
]


এর Eigenvalues বের করো।



5.

একটি Matrix এর Eigenvector কেন গুরুত্বপূর্ণ?



Advanced:


6.

Characteristic Equation:

det(A-λI)=0


ব্যাখ্যা করো।



7.

PCA তে Eigenvector কেন ব্যবহার হয়?
"""


# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
Machine Learning এবং AI তে
Eigenvalues এবং Eigenvectors অত্যন্ত গুরুত্বপূর্ণ।



------------------------------------------------
1. Principal Component Analysis (PCA)
------------------------------------------------


PCA হলো:

Dimension Reduction Technique



Steps:


Dataset Matrix

↓

Covariance Matrix

↓

Eigenvalues & Eigenvectors

↓

Important Features Select



সবচেয়ে বড় Eigenvalue এর
Eigenvector হলো:

Principal Component



------------------------------------------------
2. Feature Reduction


অনেক Feature থেকে:

Important Direction

নির্বাচন করতে Eigenvector ব্যবহার হয়।



------------------------------------------------
3. Computer Vision


Image Processing এ:

Image Pattern

Feature Extraction


এর জন্য ব্যবহার হয়।



------------------------------------------------
4. Deep Learning


Neural Network Weight Matrix Analysis এ
Eigenvalue ব্যবহার করা হয়।



------------------------------------------------
5. Recommendation System


User-Item Matrix থেকে

Hidden Pattern

খুঁজে বের করতে
Matrix Factorization এ Eigen ধারণা ব্যবহৃত হয়।



------------------------------------------------
6. LLM এবং Embedding


High-dimensional Vector Space এ:

Important Directions

এবং

Semantic Structure


বোঝার জন্য Eigen Analysis ব্যবহার করা হয়।



------------------------------------------------
Summary:


Matrix

↓

Transformation

↓

Eigenvector = Important Direction

↓

Eigenvalue = Importance / Scale



AI এর ক্ষেত্রে:

Eigenvalues এবং Eigenvectors
Data এর Hidden Structure খুঁজে বের করার
একটি শক্তিশালী Mathematical Tool।
"""


# ===========================================================
# End of Eigenvalues and Eigenvectors
# ===========================================================