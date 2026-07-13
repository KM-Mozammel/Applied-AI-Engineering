"""
===========================================================
Matrix Transpose (ম্যাট্রিক্স ট্রান্সপোজ)
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
Matrix Transpose হলো Linear Algebra এর একটি গুরুত্বপূর্ণ
Operation যেখানে Matrix এর Row এবং Column একে অপরের
সাথে পরিবর্তন হয়।


সহজভাবে:

Original Matrix এর:

Row → Column

Column → Row


হয়ে যায়।


Example:


A =

[
[1,2,3],
[4,5,6]
]


Transpose:


Aᵀ =

[
[1,4],
[2,5],
[3,6]
]


এখানে:

Original:

2 Rows × 3 Columns


Transpose:

3 Rows × 2 Columns



Matrix Transpose ব্যবহার হয়:

- Matrix Multiplication
- Neural Network
- Data Transformation
- Statistics
- Computer Graphics
"""


# ===========================================================
# 02_WhyThisConceptExistsInRelationToHistory
# ===========================================================

"""
Matrix Transpose কেন প্রয়োজন হলো?


Linear Algebra এ কাজ করার সময় দেখা যায়:

অনেক সময় Row আকারে থাকা Data কে Column আকারে
প্রয়োজন হয়।


Example:

Feature Data:


Student:

[Age, Height, Weight]


কিন্তু Mathematical Operation এর জন্য দরকার:


[
Age
Height
Weight
]


এই পরিবর্তনের জন্য Transpose ব্যবহার করা হয়।



History:

Matrix Algebra এর উন্নতির সাথে Transpose ধারণা তৈরি হয়।

Matrix এর Structure পরিবর্তন না করে
শুধু Data Arrangement পরিবর্তনের জন্য এটি তৈরি করা হয়।


বর্তমানে:

Statistics,
Machine Learning,
Deep Learning

সব জায়গায় Transpose ব্যবহৃত হয়।
"""


# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
Real Life Intuition:


------------------------------------------------
1. Table Rotation
------------------------------------------------


Original Table:


Name | Age | Salary

Rahim | 25 | 30000



Transpose করলে:


Name

Age

Salary



অর্থাৎ:

Horizontal Data

থেকে

Vertical Data



------------------------------------------------
2. Excel Sheet
------------------------------------------------


একটি বড় Table কে Column ভিত্তিক
Analysis করার জন্য Transpose করা হয়।



------------------------------------------------
3. AI Dataset
------------------------------------------------


Feature:


Height Weight Age


Transpose করলে:


Height

Weight

Age


Machine Learning Model এর Input Format
পরিবর্তন করা যায়।



------------------------------------------------
4. Neural Network
------------------------------------------------


Weight Matrix এর Dimension Match করার জন্য
Transpose ব্যবহার করা হয়।
"""


# ===========================================================
# 04_Definition
# ===========================================================

"""
Matrix Transpose হলো:

একটি Matrix এর element গুলোর Row এবং Column
position পরিবর্তন করার Process।



যদি:


A = [aij]


তাহলে:


Aᵀ = [aji]



অর্থাৎ:


Original Matrix এর

element (i,j)

Transpose এ হয়ে যায়:

(j,i)



Example:


A =


[
1 2
3 4
]


Aᵀ =


[
1 3
2 4
]



Symbol:

Aᵀ

পড়া হয়:

"A Transpose"
"""


# ===========================================================
# 05_Formula
# ===========================================================

"""
General Formula:


যদি Matrix:

A = [aij]

তাহলে:


(Aᵀ)ij = Aji



Meaning:


Row index এবং Column index swap হবে।



------------------------------------------------


Example:


A:


[
a b c
d e f
]



Transpose:


[
a d
b e
c f
]



------------------------------------------------


Important Properties:


1.


(Aᵀ)ᵀ = A



অর্থাৎ:

দুইবার Transpose করলে
আবার Original Matrix পাওয়া যায়।



------------------------------------------------


2.


(A+B)ᵀ = Aᵀ+Bᵀ



------------------------------------------------


3.


(AB)ᵀ = BᵀAᵀ



Matrix Multiplication এ
Order Reverse হয়।
"""


# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
Transpose Formula Derivation:


ধরি:


A =


[
1 2 3
4 5 6
]



এখানে:


A[0][1] = 2


মানে:

Row 0

Column 1



Transpose এ:


Aᵀ[1][0] = 2



অর্থাৎ:


A[i][j]

পরিবর্তন হয়:


Aᵀ[j][i]



তাই:


(Aᵀ)ij = Aji



এটাই Transpose এর মূল নিয়ম।
"""


# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
Computer এর ভিতরে Matrix Transpose:


Original Matrix:


[
[1,2,3],
[4,5,6]
]



Memory:


Row 0:

1 2 3


Row 1:

4 5 6



Transpose Algorithm:


Step 1:

Column 0 সংগ্রহ:

1,4


Step 2:

Column 1 সংগ্রহ:

2,5


Step 3:

Column 2 সংগ্রহ:

3,6



Result:


[
[1,4],
[2,5],
[3,6]
]



Python এ:

Nested Loop ব্যবহার করে করা যায়।
"""


# ===========================================================
# 08_Examples
# ===========================================================


# Example 1: Basic Transpose


matrix = [

[1,2,3],

[4,5,6]

]


transpose = []


for i in range(len(matrix[0])):

    row = []

    for j in range(len(matrix)):

        row.append(matrix[j][i])

    transpose.append(row)



print("Original Matrix:")
print(matrix)


print("Transpose:")
print(transpose)



# Example 2: Square Matrix


A = [

[1,2],

[3,4]

]


result = [

[A[0][0], A[1][0]],

[A[0][1], A[1][1]]

]


print("Square Matrix Transpose:")
print(result)



# Example 3: Feature Vector


features = [

[10,20,30]

]


feature_transpose = [

[10],

[20],

[30]

]


print("Feature Transpose:")
print(feature_transpose)



# Example 4: Using Zip


matrix = [

[1,2,3],

[4,5,6]

]


transpose = list(zip(*matrix))


print("Using Zip:")
print(transpose)



# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
1. শুধু Matrix এর Shape পরিবর্তন মনে করা


Transpose শুধু Shape পরিবর্তন করে না,

Element Position পরিবর্তন করে।



------------------------------------------------


2. Row এবং Column ভুল পরিবর্তন করা


সঠিক:


(i,j)

হবে:

(j,i)



------------------------------------------------


3. Square Matrix ছাড়া Transpose হয় না ভাবা


ভুল।


যেকোনো Matrix Transpose করা যায়।



------------------------------------------------


4. Matrix Multiplication এ Order ভুল করা


(AB)ᵀ


=

BᵀAᵀ



AᵀBᵀ নয়।
"""


# ===========================================================
# 10_Exercises
# ===========================================================

"""
Beginner:


1.

Matrix:


[
1 2
3 4
]


এর Transpose বের করো।



2.

3×2 Matrix তৈরি করে Transpose করো।



3.

প্রমাণ করো:


(Aᵀ)ᵀ = A



Intermediate:


4.

একটি Dataset Matrix Transpose করো।



5.

দুটি Matrix এর:


(A+B)ᵀ


প্রমাণ করো।



Advanced:


6.

Matrix Multiplication এ কেন:


(AB)ᵀ = BᵀAᵀ


তা ব্যাখ্যা করো।



7.

Neural Network এ Weight Matrix Transpose
কেন প্রয়োজন হয় লিখো।
"""


# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
Machine Learning এবং AI তে Matrix Transpose
খুব গুরুত্বপূর্ণ।



------------------------------------------------
1. Linear Regression
------------------------------------------------


Formula:


W = (XᵀX)⁻¹XᵀY



এখানে:


Xᵀ

ব্যবহার করে Matrix Dimension ঠিক করা হয়।



------------------------------------------------
2. Neural Network
------------------------------------------------


Forward Pass:


Output = XW



Backward Pass এ:


Weight Update এর সময়:

Xᵀ

ব্যবহার করা হয়।



------------------------------------------------
3. Deep Learning Gradient Calculation
------------------------------------------------


Backpropagation এ:

Gradient বের করার সময়

Matrix Transpose প্রয়োজন হয়।



------------------------------------------------
4. Computer Vision
------------------------------------------------


Image Matrix:

Height × Width


Transpose করলে:

Width × Height


হতে পারে।



------------------------------------------------
5. Data Science


Feature Matrix:


Rows = Samples

Columns = Features



অনেক Algorithm এ

Feature Orientation পরিবর্তনের জন্য

Transpose ব্যবহার হয়।



------------------------------------------------
Summary:


Transpose হলো:

Matrix এর Row এবং Column পরিবর্তনের
একটি Fundamental Operation।


AI Pipeline:


Data Matrix

↓

Transpose

↓

Matrix Multiplication

↓

Learning


Matrix Transpose ছাড়া
Modern AI Mathematics সম্পূর্ণ হয় না।
"""


# ===========================================================
# End of Matrix Transpose
# ===========================================================