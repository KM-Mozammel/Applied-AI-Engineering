"""
===========================================================
Jacobian Matrix (জ্যাকোবিয়ান ম্যাট্রিক্স)
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
Jacobian Matrix হলো Multivariable Calculus-এর একটি গুরুত্বপূর্ণ
ধারণা।

এটি ব্যবহার করা হয়:

একাধিক input-এর পরিবর্তনে
একাধিক output কত পরিবর্তিত হচ্ছে
তা বোঝার জন্য।


সহজ ভাষায়:

"অনেকগুলো variable পরিবর্তন করলে
অনেকগুলো output কীভাবে পরিবর্তন হয়?"


একটি function:


f(x)


যেখানে:

Input → Output


যদি input এবং output একাধিক হয়,
তাহলে derivative একটি matrix আকারে প্রকাশ করা হয়।

এটাই Jacobian Matrix।


Machine Learning, Robotics, Computer Vision,
Deep Learning-এ Jacobian ব্যাপকভাবে ব্যবহৃত হয়।
"""


# ===========================================================
# 02_WhyThisConceptExistsInRelationToHistory
# ===========================================================

"""
ইতিহাস:

প্রথম Calculus ছিল single variable-এর জন্য।


Example:


y=f(x)


এখানে derivative:


dy/dx


একটি সংখ্যা।



কিন্তু বাস্তব সমস্যা:


Input:

(x1,x2,x3)


Output:

(y1,y2,y3)



এখানে প্রতিটি output
প্রতিটি input-এর উপর নির্ভর করে।


প্রশ্ন:

x1 পরিবর্তন করলে y1 কত পরিবর্তন হবে?

x2 পরিবর্তন করলে y3 কত পরিবর্তন হবে?


এই সম্পর্ক প্রকাশ করার জন্য
Jacobian Matrix তৈরি হয়।


19th century mathematician
Carl Gustav Jacob Jacobi-এর নামে
এর নামকরণ করা হয়।
"""


# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
বাস্তব জীবনের intuition:


Example 1:

Robot Arm:


Input:

Joint angles:

θ1, θ2


Output:

Position:

x,y,z



একটি joint angle পরিবর্তন করলে
position কত পরিবর্তন হবে?


Jacobian বলে।



--------------------------------


Example 2:

Weather System:


Inputs:

Temperature

Pressure

Humidity


Outputs:

Wind speed

Rain probability



Input change অনুযায়ী output change
Jacobian দিয়ে বিশ্লেষণ করা যায়।



--------------------------------


Example 3:

Neural Network:


Input vector:

[x1,x2,x3]


Output:

[y1,y2]


প্রতিটি input-এর প্রভাব
প্রতিটি output-এর উপর জানতে
Jacobian ব্যবহার হয়।
"""


# ===========================================================
# 04_Definition
# ===========================================================

"""
Jacobian Matrix হলো:

একাধিক variable function-এর
সব first-order partial derivative দিয়ে তৈরি matrix।


ধরি:


F(x,y)


এর output:

[u,v]


তাহলে:

u এবং v দুইটি function।


প্রতিটি output-এর প্রতি input-এর
partial derivative নিয়ে matrix তৈরি করা হয়।


Jacobian =

Change of outputs
-----------------
Change of inputs
"""


# ===========================================================
# 05_Formula
# ===========================================================

"""
ধরি:


F(x,y)

=

[
f1(x,y),
f2(x,y)
]



তাহলে Jacobian:


J=

[
∂f1/∂x    ∂f1/∂y

∂f2/∂x    ∂f2/∂y
]



--------------------------------


General Formula:


যদি:


F:

Rⁿ → Rᵐ



তাহলে Jacobian:


Jᵢⱼ

=

∂fᵢ/∂xⱼ



যেখানে:


i = output index


j = input index



--------------------------------


Example:


F(x,y,z)


→

(u,v)



Jacobian হবে:


2×3 matrix
"""


# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
Jacobian আসে Partial Derivative থেকে।


ধরি:


Output:


u=x²+y²


v=xy



Input:


(x,y)



Step 1:

u-এর derivative:


∂u/∂x=2x


∂u/∂y=2y



Step 2:

v-এর derivative:


∂v/∂x=y


∂v/∂y=x



Step 3:

Matrix তৈরি:


J=

[
2x  2y

y   x
]



এটাই Jacobian Matrix।
"""


# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
Jacobian একটি local transformation বোঝায়।


Input space:


(x,y)


↓

Function


↓

Output space:


(u,v)



Jacobian বলে:

ছোট input change হলে
output কীভাবে পরিবর্তিত হবে।



Mathematically:


ΔOutput

≈

J × ΔInput



Computer ভিতরে:


1. প্রতিটি output function নেয়

2. সব input-এর প্রতি derivative নেয়

3. Matrix তৈরি করে

4. Transformation calculate করে



Deep Learning framework-এ
computational graph-এর মাধ্যমে
Jacobian ধারণা ব্যবহৃত হয়।
"""


# ===========================================================
# 08_Examples
# ===========================================================

"""
Example 1:


Find Jacobian:


F(x,y)


=

[
x²+y,
xy
]



Step 1:


First function:


f1=x²+y



Derivative:


∂f1/∂x=2x


∂f1/∂y=1



Second function:


f2=xy



Derivative:


∂f2/∂x=y


∂f2/∂y=x



Jacobian:


J=

[
2x  1

y   x
]



--------------------------------


Example 2:


Linear Transformation:


F(x,y)


=

[
2x+y,

x-3y
]



Jacobian:


J=

[
2  1

1 -3
]



--------------------------------


Example 3:


Neural Network:


Input:

x1,x2


Output:

y1,y2,y3



Jacobian:


3×2 Matrix


প্রতিটি output-এর উপর
প্রতিটি input-এর effect।
"""


# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
Common Mistakes:


1. Jacobian এবং Gradient একই ভাবা


Gradient:

একটি scalar function-এর derivative vector।


Jacobian:

Vector function-এর derivative matrix।



--------------------------------


2. Row এবং column order ভুল করা


সাধারণত:


Rows = outputs

Columns = inputs



--------------------------------


3. Partial derivative ভুল করা


Jacobian সম্পূর্ণভাবে
partial derivative-এর উপর নির্ভর করে।



--------------------------------


4. Matrix dimension ভুল করা


যদি:


Input = n


Output = m



Jacobian:

m × n
"""


# ===========================================================
# 10_Exercises
# ===========================================================

"""
Practice Problems:


1.


Find Jacobian:


F(x,y)


=

[
x²,
xy
]



--------------------------------


2.


Find Jacobian:


F(x,y,z)

=

[
x+y+z,
xyz
]



--------------------------------


3.


What is the dimension of Jacobian?


Input:

5 variables

Output:

3 variables



Answer:

3×5



--------------------------------


4.


Difference between:

Gradient and Jacobian



--------------------------------


5.


Why Jacobian is important in Neural Networks?
"""


# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
AI এবং Machine Learning-এ Jacobian:


1. Backpropagation


Neural Network-এ:

একাধিক output এবং parameter-এর
relationship বের করতে Jacobian ব্যবহার করা হয়।



--------------------------------


2. Automatic Differentiation


Framework:

- PyTorch
- TensorFlow


Computational graph থেকে
Jacobian calculate করতে পারে।



--------------------------------


3. Computer Vision


Image transformation:


Input pixels

↓

Transformed pixels



Transformation sensitivity
Jacobian দিয়ে প্রকাশ করা হয়।



--------------------------------


4. Robotics


Robot movement:


Joint angles

↓

Position


Jacobian:

Velocity transformation

এবং

Inverse kinematics-এ ব্যবহৃত হয়।



--------------------------------


5. Optimization


Multiple parameter optimization-এ
gradient এবং Jacobian ব্যবহার হয়।



--------------------------------


6. Neural Network Analysis


একটি layer:


y=f(x)


এর sensitivity:

∂y/∂x


হলো Jacobian।



--------------------------------


Summary:


Jacobian Matrix শেখায়:


✓ Multiple input-output change
✓ Partial derivative organization
✓ Transformation analysis
✓ Neural network sensitivity
✓ Robotics control


Jacobian হলো Multivariable Calculus এবং
AI mathematics-এর একটি গুরুত্বপূর্ণ bridge।
"""


# ===========================================================
# End of Jacobian Matrix
# ===========================================================