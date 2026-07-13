"""
===========================================================
Matrix (ম্যাট্রিক্স)
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
Matrix (ম্যাট্রিক্স) হলো Linear Algebra এর সবচেয়ে গুরুত্বপূর্ণ
ধারণাগুলোর একটি।

সহজভাবে:

Matrix হলো সংখ্যাগুলোর একটি rectangular arrangement
যেখানে সংখ্যা Row এবং Column আকারে সাজানো থাকে।


Example:


A =

[
 [1, 2, 3],
 [4, 5, 6]
]


এখানে:

Rows = 2

Columns = 3


Matrix কে সাধারণত ব্যবহার করা হয়:

- Data Representation
- Linear Transformation
- Computer Graphics
- Machine Learning
- Deep Learning
- Image Processing


AI এর ভিতরে:

Neural Network এর Weight, Image Pixel,
Embedding সব Matrix আকারে থাকে।
"""


# ===========================================================
# 02_WhyThisConceptExistsInRelationToHistory
# ===========================================================

"""
Matrix কেন প্রয়োজন হলো?


প্রথমে গণিতে শুধু Equation সমাধান করা হতো।

যেমন:


2x + 3y = 10

4x + 5y = 20



যখন অনেকগুলো Variable এবং Equation নিয়ে কাজ করা শুরু হলো,
তখন এগুলোকে সুন্দরভাবে Organize করার প্রয়োজন হলো।


Matrix সেই সমস্যার সমাধান দেয়।



History:

- 1800 সালের দিকে Matrix ধারণা তৈরি হয়।
- Arthur Cayley Matrix Algebra উন্নয়নে গুরুত্বপূর্ণ ভূমিকা রাখেন।
- Matrix Linear Equation এবং Transformation এর মূল ভিত্তি হয়ে ওঠে।


বর্তমানে:

Computer Science এ Matrix ব্যবহার হয়:

- Graphics Rotation
- Neural Network
- Image Processing
- Scientific Computing
"""


# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
Real Life এ Matrix:


------------------------------------------------
1. Spreadsheet
------------------------------------------------


Excel Table:


Name | Age | Salary

Rahim | 25 | 30000

Karim | 30 | 40000



এটি একটি Matrix এর মতো।



------------------------------------------------
2. Image
------------------------------------------------


একটি Black & White Image:


[
 [0,255,0],
 [255,0,255],
 [0,255,0]
]


প্রতিটি সংখ্যা Pixel Value প্রকাশ করে।



------------------------------------------------
3. Computer Graphics
------------------------------------------------


একটি 3D Object কে:

Rotate

Scale

Move

করার জন্য Matrix ব্যবহার হয়।



------------------------------------------------
4. Machine Learning Data
------------------------------------------------


একটি Dataset:


[
 [Age, Height, Weight],
 [20,170,60],
 [25,180,75]
]


এটি একটি Data Matrix।
"""


# ===========================================================
# 04_Definition
# ===========================================================

"""
Matrix হলো:

সংখ্যা বা Mathematical Element এর
Row এবং Column আকারে সাজানো একটি Array।


General Form:


A =


[
a11 a12 a13
a21 a22 a23
a31 a32 a33
]



এখানে:


a = Element


প্রথম index = Row

দ্বিতীয় index = Column



Example:


A =

[
[1,2],
[3,4]
]


এটি:

2 × 2 Matrix



Dimension:


Rows × Columns
"""


# ===========================================================
# 05_Formula
# ===========================================================

"""
1. Matrix Addition:


A + B = C


শর্ত:

দুই Matrix এর Dimension একই হতে হবে।


Example:


A=

[1 2]

[3 4]


B=

[5 6]

[7 8]


A+B=


[6 8]

[10 12]



------------------------------------------------


2. Matrix Multiplication:


A(m×n) × B(n×p)


Result:

m×p Matrix



Condition:

প্রথম Matrix এর Column

=

দ্বিতীয় Matrix এর Row



------------------------------------------------


3. Transpose:


Rows কে Column এ পরিবর্তন করা।



A:


[1 2 3]



Transpose:


[1]

[2]

[3]



Symbol:

Aᵀ



------------------------------------------------


4. Identity Matrix:


I =


[1 0]

[0 1]



যেখানে:

A × I = A
"""


# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
Matrix Multiplication কেন এমন হয়?


ধরি:


A =

[a b]

[c d]



B =

[x y]

[z w]



Matrix multiplication এ:

প্রথম Row

এবং

প্রথম Column

এর Dot Product করা হয়।



Result:


(a*x)+(b*z)



অর্থাৎ:

Matrix Multiplication আসলে
অনেকগুলো Dot Product এর সমষ্টি।



তাই:


Matrix × Matrix

=

Multiple Vector Dot Products
"""


# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
Computer এর ভিতরে Matrix আসলে
Nested Array হিসেবে থাকে।



Example:


Matrix:


[
[1,2],
[3,4]
]



Memory:


Row 0:

Index 0 -> 1

Index 1 -> 2



Row 1:

Index 0 -> 3

Index 1 -> 4



Python:


matrix = [
    [1,2],
    [3,4]
]



Machine Learning এ:


Input Matrix:


X


Weight Matrix:


W



Operation:


X × W


↓

New Representation



Neural Network এর প্রতিটি Layer
Matrix Multiplication ব্যবহার করে।
"""


# ===========================================================
# 08_Examples
# ===========================================================


# Example 1: Creating Matrix


matrix = [
    [1,2,3],
    [4,5,6]
]


print("Matrix:")
print(matrix)



# Example 2: Matrix Addition


A = [
    [1,2],
    [3,4]
]


B = [
    [5,6],
    [7,8]
]


C = [
    [
        A[0][0]+B[0][0],
        A[0][1]+B[0][1]
    ],
    [
        A[1][0]+B[1][0],
        A[1][1]+B[1][1]
    ]
]


print("Addition:")
print(C)



# Example 3: Matrix Multiplication


A = [
    [1,2],
    [3,4]
]


B = [
    [5,6],
    [7,8]
]


result = [
    [
        A[0][0]*B[0][0] + A[0][1]*B[1][0],
        A[0][0]*B[0][1] + A[0][1]*B[1][1]
    ],
    [
        A[1][0]*B[0][0] + A[1][1]*B[1][0],
        A[1][0]*B[0][1] + A[1][1]*B[1][1]
    ]
]


print("Multiplication:")
print(result)



# Example 4: Image Matrix


image = [

[0,255,0],

[255,0,255],

[0,255,0]

]


print("Image Matrix:")
print(image)



# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
1. Matrix Dimension ভুল করা


A(2×3)

B(4×2)


Multiplication সম্ভব নয়।



------------------------------------------------


2. Matrix এবং Array একই মনে করা


Array শুধু Data রাখে।

Matrix এর Mathematical Rules আছে।



------------------------------------------------


3. Multiplication এ Element-wise ভুল করা


Matrix multiplication:

Row × Column



------------------------------------------------


4. Addition এ Different Dimension ব্যবহার করা


2×2 Matrix

+

2×3 Matrix

অসম্ভব।



------------------------------------------------


5. Row এবং Column গুলিয়ে ফেলা।
"""


# ===========================================================
# 10_Exercises
# ===========================================================

"""
Beginner:


1.

একটি 3×3 Matrix তৈরি করো।



2.

দুইটি Matrix যোগ করো:


A=[1 2]

  [3 4]


B=[5 6]

  [7 8]



3.

একটি Matrix এর Transpose বের করো।



Intermediate:


4.

দুইটি 2×2 Matrix Multiply করো।



5.

Identity Matrix তৈরি করো।



Advanced:


6.

একটি Image কে Matrix হিসেবে Represent করো।



7.

একটি Neural Network Layer এর Matrix Operation
ব্যাখ্যা করো।
"""


# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
Machine Learning এবং AI সম্পূর্ণভাবে Matrix এর উপর নির্ভরশীল।



------------------------------------------------
1. Dataset Representation
------------------------------------------------


Dataset:


[
Feature1 Feature2 Feature3

10       20       30

15       25       35

]


এটি একটি Matrix।



------------------------------------------------
2. Linear Regression
------------------------------------------------


Formula:


Y = XW + b



যেখানে:


X = Input Matrix

W = Weight Matrix

b = Bias



------------------------------------------------
3. Neural Network
------------------------------------------------


একটি Layer:


Output = XW + b



Input Matrix

×

Weight Matrix

=

Output Matrix



------------------------------------------------
4. Image Processing
------------------------------------------------


Image:


Pixel Matrix


CNN Model এই Matrix এর উপর কাজ করে।



------------------------------------------------
5. Transformer / LLM
------------------------------------------------


Large Language Model এ:


Query Matrix

Key Matrix

Value Matrix


Matrix Multiplication এর মাধ্যমে

Attention তৈরি করে।



------------------------------------------------
Summary:


Modern AI:

Data

↓

Vector

↓

Matrix

↓

Matrix Multiplication

↓

Prediction



Matrix ছাড়া:

Machine Learning,
Deep Learning,
Computer Vision,
LLM

অসম্ভব।
"""


# ===========================================================
# End of Matrix
# ===========================================================