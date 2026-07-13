"""
===========================================================
Directional Derivative (দিকনির্দেশিত অন্তরক)
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
Directional Derivative হলো Multivariable Calculus-এর একটি
গুরুত্বপূর্ণ ধারণা।

এটি বলে:

কোনো function একটি নির্দিষ্ট direction-এ
কত দ্রুত পরিবর্তিত হচ্ছে।


Derivative:

একটি নির্দিষ্ট axis-এর পরিবর্তন দেখে।


Partial Derivative:

একটি variable-এর direction দেখে।


Directional Derivative:

যেকোনো arbitrary direction-এ change measure করে।


Example:


একটি পাহাড়ের উপর দাঁড়িয়ে আছেন।

আপনি উত্তর দিকে হাঁটলে height কত দ্রুত বাড়বে?

পূর্ব দিকে হাঁটলে height কত দ্রুত বাড়বে?


এই প্রশ্নের উত্তর দেয়
Directional Derivative।
"""


# ===========================================================
# 02_WhyThisConceptExistsInRelationToHistory
# ===========================================================

"""
ইতিহাস:

প্রথম Calculus single variable-এর জন্য তৈরি হয়েছিল।


Example:


y=f(x)


এখানে শুধু একটি direction ছিল।


কিন্তু বাস্তব জগতে:

Temperature:

T(x,y,z)


Mountain height:

H(x,y)


Electric field:

E(x,y,z)


এগুলোতে অসংখ্য direction থাকতে পারে।


Partial derivative শুধু x, y, z axis-এর পরিবর্তন দেয়।


কিন্তু arbitrary direction-এর পরিবর্তন জানতে
Directional Derivative প্রয়োজন হয়।


Gradient এবং Directional Derivative একসাথে
multivariable change বোঝার শক্তিশালী tool।
"""


# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
বাস্তব জীবনের intuition:


Example 1:

পাহাড়ের ঢাল:


আপনি পাহাড়ে দাঁড়িয়ে আছেন।

চারদিকে অনেক রাস্তা আছে।


একটি রাস্তা বেছে নিলেন।

এই direction-এ height কত দ্রুত বাড়ছে?


Directional Derivative এটি বলে।



--------------------------------


Example 2:

Weather Map:


Temperature:

T(x,y)


আপনি একটি নির্দিষ্ট direction-এ হাঁটছেন।


সেই পথে temperature change:


Directional Derivative



--------------------------------


Example 3:

Robot Movement:


একটি robot coordinate plane-এ চলছে।


Robot একটি নির্দিষ্ট direction-এ move করলে
environment value কত পরিবর্তন হবে?


Directional derivative ব্যবহার করা যায়।
"""


# ===========================================================
# 04_Definition
# ===========================================================

"""
Directional Derivative হলো:

কোনো scalar function-এর
একটি নির্দিষ্ট direction বরাবর
rate of change।


যদি:


f(x,y)


এবং direction vector:


u


থাকে,


তাহলে:

Dᵤf


মানে:

u direction-এ f-এর derivative।


এটি Gradient-এর সাথে সম্পর্কিত।
"""


# ===========================================================
# 05_Formula
# ===========================================================

"""
Directional Derivative Formula:


Dᵤf

=

∇f · u



যেখানে:


∇f

=

Gradient Vector



u

=

Unit Direction Vector



·

=

Dot Product



--------------------------------


Gradient:


∇f

=

[
∂f/∂x,
∂f/∂y
]



Direction Vector:


v=[a,b]



Unit Vector:


u

=

v / |v|



--------------------------------


Final:


Dᵤf

=

|∇f||u|cosθ



কারণ:

u unit vector হওয়ায়:


Dᵤf

=

|∇f|cosθ
"""


# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
Directional Derivative আসে Gradient থেকে।


ধরি:


f(x,y)


একটি ছোট displacement:


Δr


হলো।


Function change:


Δf


Gradient অনুযায়ী:


Δf ≈ ∇f · Δr



যদি direction vector:

u


হয়:


Δr = hu



তাহলে:


Δf ≈ ∇f · hu



Divide করি h দিয়ে:


Δf/h ≈ ∇f · u



যখন:

h → 0


তখন:


Dᵤf = ∇f · u



এটাই Directional Derivative formula।
"""


# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
Visualization:


Surface:


             z
             |
          /\ 
        /    \
      /        \
----------------
       x,y



একটি point-এ:

Gradient:

↑

সবচেয়ে দ্রুত বৃদ্ধির direction



Directional Derivative:

যেকোনো নির্বাচিত direction-এ
gradient-এর projection।



যদি:


Direction = Gradient direction


তাহলে:

Maximum increase



যদি:


Direction opposite হয়:


Maximum decrease



যদি:


90 degree হয়:


Change = 0



Computer ভিতরে:


1. Gradient calculate করে

2. Direction vector normalize করে

3. Dot product নেয়

4. Change rate বের করে
"""


# ===========================================================
# 08_Examples
# ===========================================================

"""
Example 1:


Find directional derivative:


f(x,y)=x²+y²


Point:

(1,2)



Step 1:

Gradient:


∇f=[2x,2y]


At (1,2):


∇f=[2,4]



--------------------------------


Direction:


v=[3,4]



Magnitude:


|v|=5



Unit vector:


u=[3/5,4/5]



--------------------------------


Directional derivative:


Dᵤf

=

[2,4] · [3/5,4/5]


=

6/5+16/5


=

22/5



Answer:

22/5



--------------------------------


Example 2:


Direction যদি gradient-এর দিকে হয়:


Dᵤf=maximum



কারণ:

cos(0)=1
"""


# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
Common Mistakes:


1. Direction vector normalize না করা


Formula-তে:

u অবশ্যই unit vector হতে হবে।



--------------------------------


2. Gradient এবং Directional Derivative
একই মনে করা


Gradient:

সব direction-এর information দেয়।


Directional Derivative:

একটি নির্দিষ্ট direction-এর change দেয়।



--------------------------------


3. Dot product ভুল করা


Gradient · Direction


হতে হবে।



--------------------------------


4. Direction negative হলে ভুল বোঝা


Negative value মানে:

এই direction-এ function কমছে।
"""


# ===========================================================
# 10_Exercises
# ===========================================================

"""
Practice Problems:


1.


Find directional derivative:


f(x,y)=x²+y²


at (2,1)

direction:

[1,0]



--------------------------------


2.


Find:


Gradient of:

f(x,y)=xy



Answer:


[y,x]



--------------------------------


3.


Why unit vector is needed?



--------------------------------


4.


When directional derivative becomes zero?



--------------------------------


5.


Explain relation:

Gradient and Directional Derivative
"""


# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
AI এবং Machine Learning-এ Directional Derivative:


1. Optimization


Machine Learning-এ parameter space অনেক বড়।


একটি নির্দিষ্ট direction-এ loss কত পরিবর্তন হচ্ছে
তা জানা প্রয়োজন।



--------------------------------


2. Gradient Descent


Gradient descent মূলত:

Negative gradient direction


অনুসরণ করে।


কারণ:

এই direction-এ loss সবচেয়ে দ্রুত কমে।



--------------------------------


3. Neural Network Optimization


Weights অনেক dimension-এর vector।


একটি update direction-এ:

Loss change


Directional derivative দিয়ে বোঝা যায়।



--------------------------------


4. Adversarial Machine Learning


Input-এর নির্দিষ্ট direction পরিবর্তন করে
model output কত পরিবর্তিত হয়
তা বিশ্লেষণ করা হয়।



--------------------------------


5. Reinforcement Learning


Policy parameter-এর direction change
evaluate করতে ব্যবহার করা হয়।



--------------------------------


Summary:


Directional Derivative শেখায়:


✓ নির্দিষ্ট direction-এ change
✓ Gradient-এর ব্যবহার
✓ Optimization বোঝা
✓ AI parameter update বুঝতে


Gradient + Directional Derivative
modern AI mathematics-এর গুরুত্বপূর্ণ অংশ।
"""


# ===========================================================
# End of Directional Derivative
# ===========================================================