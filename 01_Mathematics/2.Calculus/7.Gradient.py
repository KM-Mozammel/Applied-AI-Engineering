# Gradient : সবচেয়ে দ্রুত উপরে ওঠার দিক কোনটি?

# Partial Derivative পাওয়ার পরে বিজ্ঞানীরা নতুন প্রশ্ন করলেন। ধরি তুমি পাহাড়ের উপর দাঁড়িয়ে আছো। কোন দিকে গেলে সবচেয়ে দ্রুত উপরে উঠব?

# Partial derivative শুধু বলে: x দিকে ঢাল কত? y দিকে ঢাল কত?
# Gradient বলে: সবচেয়ে খাড়া উপরের দিক কোনটা?

# Example : f(x,y)=x^2 + y^2
# Gradient: ∇f=(2x,2y)

def gradient(x,y):
    return (2*x,2*y)

print(gradient(3,4))

# Output: (6,8)

# Visualization: ধরি

# x direction slope = 6
# y direction slope = 8

# Gradient vector: (6,8). এটাই steepest ascent direction।

"""
===========================================================
Gradient (গ্রেডিয়েন্ট)
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
Gradient হলো Multivariable Calculus-এর একটি গুরুত্বপূর্ণ ধারণা।

Gradient বলে:

কোনো multivariable function কোন direction-এ
সবচেয়ে দ্রুত বৃদ্ধি পাচ্ছে এবং কত দ্রুত বৃদ্ধি পাচ্ছে।


সহজ ভাষায়:

"একটি surface-এর সবচেয়ে খাড়া উপরের দিক কোনটি?"


Gradient তৈরি হয়:

Partial Derivative

থেকে।


Example:


একটি পাহাড়ের height:


h(x,y)


Gradient বলে:

কোন দিকে হাঁটলে সবচেয়ে দ্রুত উপরে উঠবেন।


Machine Learning-এ:

Gradient বলে:

Loss কমানোর জন্য কোন দিকে parameter পরিবর্তন করতে হবে।
"""


# ===========================================================
# 02_WhyThisConceptExistsInRelationToHistory
# ===========================================================

"""
ইতিহাস:

Single variable calculus-এ:

y=f(x)


শুধু একটি direction থাকে।

তাই derivative যথেষ্ট ছিল।


কিন্তু বাস্তব জগতে:

Temperature:

T(x,y,z)


Height:

H(x,y)


Physics:

Energy:

E(x,y,z)



এগুলোতে অনেকগুলো direction থাকে।


তাই শুধু derivative যথেষ্ট নয়।


Mathematicians gradient ধারণা তৈরি করেন
যাতে:

একাধিক variable-এর পরিবর্তন একসাথে বোঝা যায়।


Gradient multivariable calculus-এর
directional change বোঝার মাধ্যম।
"""


# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
বাস্তব জীবনের intuition:


Example 1:

পাহাড়ের উপর দাঁড়িয়ে আছেন।


আপনার চারপাশে অনেক direction আছে।


কোন দিকে গেলে সবচেয়ে দ্রুত উপরে উঠবেন?


Gradient সেই direction দেখায়।



--------------------------------


Example 2:

Temperature Map:


একটি শহরের temperature:


T(x,y)


Gradient বলে:

কোন দিকে temperature সবচেয়ে দ্রুত বাড়ছে।



--------------------------------


Example 3:

Machine Learning:


Loss function:


L(weight)


Gradient বলে:

কোন দিকে গেলে loss সবচেয়ে বেশি বাড়ে।


তাই বিপরীত দিকে গেলে:

Loss কমে।
"""


# ===========================================================
# 04_Definition
# ===========================================================

"""
Gradient হলো একটি vector যা
একটি scalar function-এর সব partial derivative নিয়ে তৈরি হয়।


যদি:


f(x,y)



তাহলে Gradient:


∇f


পড়া হয়:

"del f" অথবা "nabla f"



Gradient হলো:

একটি vector


যার:

Magnitude = পরিবর্তনের হার

Direction = সবচেয়ে দ্রুত বৃদ্ধির দিক
"""


# ===========================================================
# 05_Formula
# ===========================================================

"""
দুই variable-এর জন্য:


f(x,y)



Gradient:


∇f

=

[
∂f/∂x,
∂f/∂y
]



--------------------------------


তিন variable-এর জন্য:


f(x,y,z)



Gradient:


∇f

=

[
∂f/∂x,
∂f/∂y,
∂f/∂z
]



--------------------------------


Example:


f(x,y)=x²+y²



Partial derivative:


∂f/∂x=2x


∂f/∂y=2y



Therefore:


∇f=[2x,2y]
"""


# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
Gradient আসে Partial Derivative থেকে।


ধরি:


f(x,y)=x²+y²



Step 1:

x direction change:


∂f/∂x=2x



Step 2:

y direction change:


∂f/∂y=2y



Step 3:

দুটিকে একসাথে vector বানাই:


∇f=[2x,2y]



এখন এই vector বলে:

Surface কোন direction-এ সবচেয়ে দ্রুত
বাড়ছে।



Mathematically:

Directional change = Gradient-এর projection।
"""


# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
একটি surface:


             z
             |
          /-----
        /
      /
----------------
        x,y



প্রতিটি point-এ gradient vector থাকে।



Gradient:

↑

সবচেয়ে steep upward direction



Negative Gradient:

↓

সবচেয়ে দ্রুত নিচে যাওয়ার direction।



Machine ভিতরে:


1. Function নেয়

2. সব variable-এর partial derivative বের করে

3. Vector তৈরি করে

4. Direction এবং magnitude calculate করে



Machine Learning-এ:


Gradient

↓

Weight update direction
"""


# ===========================================================
# 08_Examples
# ===========================================================

"""
Example 1:


Find gradient:


f(x,y)=x²+y²



Solution:


∂f/∂x=2x


∂f/∂y=2y



Gradient:


∇f=[2x,2y]



--------------------------------


Example 2:


f(x,y)=3x²+4y²



Partial:


∂f/∂x=6x


∂f/∂y=8y



Gradient:


∇f=[6x,8y]



--------------------------------


Example 3:


Machine Learning:


Loss:


L(w1,w2)



Gradient:


∇L=

[
∂L/∂w1,
∂L/∂w2
]



Weight update:


w_new

=

w_old - α∇L
"""


# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
Common Mistakes:


1. Gradient এবং derivative একই মনে করা


Derivative:

একটি variable


Gradient:

একাধিক variable-এর derivative vector



--------------------------------


2. Partial derivative ভুল করা


Gradient তৈরির আগে
প্রতিটি partial derivative সঠিক হতে হবে।



--------------------------------


3. Direction ভুল বোঝা


Gradient:

Maximum increase direction



Negative Gradient:

Decrease direction



--------------------------------


4. Magnitude এবং direction আলাদা না করা


Gradient vector-এর দুইটি অংশ:

Direction

Magnitude
"""


# ===========================================================
# 10_Exercises
# ===========================================================

"""
Practice Problems:


1.


Find gradient:


f(x,y)=x²+3y²



Answer:


[2x,6y]



--------------------------------


2.


Find gradient:


f(x,y,z)=x²+y²+z²



Answer:


[2x,2y,2z]



--------------------------------


3.


Calculate:


∇f


for:


f(x,y)=xy



Answer:


[y,x]



--------------------------------


4.


Explain:

Why gradient is used in Gradient Descent?



--------------------------------


5.


Difference between:

Derivative

and

Gradient
"""


# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
AI এবং Machine Learning-এ Gradient:


1. Gradient Descent


সবচেয়ে গুরুত্বপূর্ণ ব্যবহার।


Goal:

Loss Function minimize করা।



Formula:


θ_new

=

θ_old - α∇J(θ)



এখানে:


∇J(θ)

=

Gradient



--------------------------------


2. Neural Network Training


Network-এর:

Weights

Biases


update করতে gradient ব্যবহার হয়।



--------------------------------


3. Backpropagation


Output error থেকে
প্রতিটি parameter-এর gradient বের করা হয়।


Chain Rule + Gradient

মিলে backpropagation তৈরি করে।



--------------------------------


4. Optimization Algorithms


সব modern optimizer:


- SGD
- Adam
- RMSProp


Gradient ব্যবহার করে।



--------------------------------


5. Computer Vision


Image:


I(x,y)


Gradient বের করে:


Edges

Shapes

Patterns


detect করা হয়।



--------------------------------


6. Reinforcement Learning


Policy improvement এবং value function optimization-এ
gradient ব্যবহার করা হয়।



--------------------------------


Summary:


Gradient শেখায়:


✓ কোন direction-এ change হচ্ছে
✓ কত দ্রুত change হচ্ছে
✓ Optimization কীভাবে করতে হয়
✓ AI model কীভাবে শেখে


Gradient হলো Machine Learning-এর
optimization engine।
"""


# ===========================================================
# End of Gradient
# ===========================================================