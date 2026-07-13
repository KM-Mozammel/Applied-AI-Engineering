"""
===========================================================
Matrix Multiplication (ম্যাট্রিক্স গুণ)
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
Matrix Multiplication হলো Linear Algebra এর সবচেয়ে গুরুত্বপূর্ণ
Operation গুলোর একটি।

সহজভাবে:

একটি Matrix এর তথ্যকে অন্য একটি Matrix এর সাথে Combine করে
নতুন একটি Matrix তৈরি করার Process হলো Matrix Multiplication।


Example:


A =

[
[1,2],
[3,4]
]


B =

[
[5,6],
[7,8]
]


A × B =


[
[19,22],
[43,50]
]


Matrix Multiplication ব্যবহার হয়:

- Machine Learning
- Neural Network
- Computer Graphics
- Physics Simulation
- Data Transformation


AI এর ভিতরে:

প্রায় প্রতিটি Neural Network Layer এ
Matrix Multiplication ব্যবহার হয়।
"""


# ===========================================================
# 02_WhyThisConceptExistsInRelationToHistory
# ===========================================================

"""
Matrix Multiplication কেন প্রয়োজন হলো?


Linear Algebra এর শুরুতে মানুষ Linear Equation
সমাধান করতো।


Example:


2x + 3y = 10

4x + 5y = 20



অনেকগুলো Equation এবং Variable নিয়ে কাজ করার সময়
এগুলোকে একটি Structure এ রাখার প্রয়োজন হয়।


Matrix তৈরি হলো।

কিন্তু শুধু Matrix রাখলে হবে না,
Matrix এর মাধ্যমে Equation Transform করার প্রয়োজন হলো।


সেখান থেকেই Matrix Multiplication তৈরি হয়।



History:

- Matrix Algebra এর উন্নতির সাথে Matrix Multiplication তৈরি হয়।
- Arthur Cayley Matrix Algebra এর ভিত্তি তৈরি করেন।


বর্তমানে:

Computer Graphics থেকে শুরু করে
Artificial Intelligence পর্যন্ত
সব জায়গায় Matrix Multiplication ব্যবহৃত হয়।
"""


# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
Real Life Intuition:


------------------------------------------------
1. Image Transformation
------------------------------------------------


একটি ছবি:

Pixel Matrix


Rotation Matrix এর সাথে Multiply করলে:

নতুন Rotated Image পাওয়া যায়।



------------------------------------------------
2. Google Search
------------------------------------------------


Web Page Data:

Vector


Query:

Vector


Matrix Operation এর মাধ্যমে
Relevant Result বের করা হয়।



------------------------------------------------
3. Neural Network
------------------------------------------------


Input:


[
Feature1,
Feature2,
Feature3
]


Weight:


[
w1,
w2,
w3
]


Matrix Multiplication করে
Neuron Output তৈরি হয়।



------------------------------------------------
4. Multiple Transformations
------------------------------------------------


একটি Object কে:

Scale

Rotate

Move


করার জন্য বিভিন্ন Matrix Multiply করা হয়।
"""


# ===========================================================
# 04_Definition
# ===========================================================

"""
Matrix Multiplication হলো:

দুইটি Matrix এর Row এবং Column এর
Dot Product এর মাধ্যমে নতুন Matrix তৈরি করা।



ধরি:


A = m × n Matrix


B = n × p Matrix



তাহলে:


A × B = m × p Matrix



শর্ত:


প্রথম Matrix এর Column সংখ্যা

=

দ্বিতীয় Matrix এর Row সংখ্যা



Example:


A:

2 × 3


B:

3 × 4



তাহলে:


A × B হবে:


2 × 4 Matrix
"""


# ===========================================================
# 05_Formula
# ===========================================================

"""
General Formula:


C = A × B



যেখানে:


Cij =

A এর i-th Row

এবং

B এর j-th Column

এর Dot Product



Formula:


Cij = Σ(Aik × Bkj)



Example:


A:


[
a b
c d
]


B:


[
e f
g h
]



C:


[
(ae+bg)   (af+bh)

(ce+dg)   (cf+dh)

]



প্রতিটি নতুন Element:

Row × Column
"""


# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
Matrix Multiplication এর Formula আসে
Vector Dot Product থেকে।



ধরি:


A এর একটি Row:


[a,b]



B এর একটি Column:


[
x
y
]



এদের Dot Product:


(a*x)+(b*y)



এটাই Result Matrix এর একটি Element।



যেহেতু:

প্রতিটি Row

প্রতিটি Column এর সাথে Multiply হয়,


তাই:


Cij = Σ(Aik × Bkj)



Matrix Multiplication আসলে
অনেকগুলো Dot Product এর সমষ্টি।
"""


# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
Computer এর ভিতরে Matrix Multiplication:


A:


[
1 2
3 4
]



B:


[
5 6
7 8
]



Step 1:


A এর প্রথম Row:


[1,2]



B এর প্রথম Column:


[
5
7
]



Dot Product:


1*5 + 2*7


= 19



এটি C[0][0]



------------------------------------------------


Step 2:


প্রথম Row × দ্বিতীয় Column:


1*6 + 2*8


=22



C[0][1]



এভাবে সব Row এবং Column
Multiply করা হয়।



Python এ:

Nested Loop ব্যবহার করে
Matrix Multiplication করা হয়।
"""


# ===========================================================
# 08_Examples
# ===========================================================


# Example 1: Basic Matrix Multiplication


A = [

[1,2],

[3,4]

]


B = [

[5,6],

[7,8]

]


result = [

[0,0],

[0,0]

]


for i in range(len(A)):

    for j in range(len(B[0])):

        for k in range(len(B)):

            result[i][j] += A[i][k] * B[k][j]


print("Matrix Multiplication:")
print(result)



# Example 2: Different Dimension


A = [

[1,2,3],

[4,5,6]

]


B = [

[7,8],

[9,10],

[11,12]

]


result = [

[0,0],

[0,0]

]


for i in range(len(A)):

    for j in range(len(B[0])):

        for k in range(len(B)):

            result[i][j] += A[i][k] * B[k][j]


print("2x3 × 3x2:")
print(result)



# Example 3: Neural Network Style


input_vector = [

[2,3,4]

]


weight_matrix = [

[0.5],

[0.2],

[0.1]

]


output = 0


for i in range(3):

    output += input_vector[0][i] * weight_matrix[i][0]


print("Neuron Output:")
print(output)



# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
1. Dimension Rule ভুল করা


A(2×3)

B(2×2)


Multiply করা যাবে না।



কারণ:

3 != 2



------------------------------------------------


2. Element-wise Multiplication মনে করা


ভুল:


A[i][j] × B[i][j]



এটি Matrix Multiplication নয়।



------------------------------------------------


3. Order ভুল করা


সাধারণত:


A × B


≠


B × A



Matrix Multiplication Commutative নয়।



------------------------------------------------


4. Row × Row করা


সঠিক নিয়ম:


Row × Column



------------------------------------------------


5. Result Matrix Dimension ভুল করা


A(m×n)

B(n×p)


Result:

m×p
"""


# ===========================================================
# 10_Exercises
# ===========================================================

"""
Beginner:


1.

Multiply:


A=

[1 2]

[3 4]


B=

[5 6]

[7 8]



2.

2×3 এবং 3×2 Matrix Multiply করো।



3.

Matrix Multiplication এর Dimension Rule লিখো।



Intermediate:


4.

নিজে Nested Loop দিয়ে Matrix Multiplication
Implement করো।



5.

কেন:

A×B ≠ B×A

ব্যাখ্যা করো।



Advanced:


6.

একটি Image Rotation Matrix কিভাবে
Image পরিবর্তন করে ব্যাখ্যা করো।



7.

Neural Network এ Matrix Multiplication এর ভূমিকা
ব্যাখ্যা করো।
"""


# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
Machine Learning এবং AI এর মূল ভিত্তি হলো
Matrix Multiplication।



------------------------------------------------
1. Linear Regression
------------------------------------------------


Formula:


Y = XW + b



এখানে:


X = Input Matrix

W = Weight Matrix



X × W

দিয়ে Prediction তৈরি হয়।



------------------------------------------------
2. Neural Network
------------------------------------------------


প্রতিটি Layer:


Output = XW + b



Example:


Input Features


×

Weights


=

Neuron Output



------------------------------------------------
3. Deep Learning


একটি Neural Network এ:

Millions of Parameters


সবগুলো Matrix আকারে থাকে।



GPU বিশেষভাবে Matrix Multiplication
দ্রুত করার জন্য তৈরি।



------------------------------------------------
4. Transformer / LLM
------------------------------------------------


Large Language Model এ:


Query Matrix

×

Key Matrix


দিয়ে Attention Score তৈরি হয়।



GPT Model এর ভিতরে:

প্রতি Token এর জন্য
বহু Matrix Multiplication হয়।



------------------------------------------------
5. Computer Vision
------------------------------------------------


Image Matrix

×

Filter Matrix


দিয়ে Feature Extraction করা হয়।



------------------------------------------------
Summary:


AI Pipeline:


Data

↓

Vector

↓

Matrix

↓

Matrix Multiplication

↓

Prediction



Matrix Multiplication ছাড়া:

Neural Network,
Deep Learning,
LLM

কাজ করতে পারে না।
"""


# ===========================================================
# End of Matrix Multiplication
# ===========================================================