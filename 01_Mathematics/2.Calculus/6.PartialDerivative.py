# Partial Derivative : অনেক Variable থাকলে একটি Variable-এর প্রভাব কত?
# Newton এর পরে বিজ্ঞানীরা আরও জটিল সমস্যা পেলেন। আগে ছিল: f(x), এখন: f(x,y,z)

# house_price = size + location + age

# এখন প্রশ্ন: size বাড়লে কী হবে? location স্থির রেখে। এখান থেকে জন্ম Partial Derivative

# Example: f(x,y)=x^2+y^2
# x অনুযায়ী: ∂x / ∂f = 2x
# y অনুযায়ী: ∂y / ∂f = 2y

def partial_x(x):
    return 2*x

def partial_y(y):
    return 2*y

# Machine Learning-এ Loss(w1,w2,w3,...) প্রতিটি weight-এর জন্য derivative বের করতে হয়।

"""
===========================================================
Partial Derivative (আংশিক অন্তরক)
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
Partial Derivative (আংশিক অন্তরক) হলো Calculus-এর এমন একটি
ধারণা যেখানে একটি function-এর একাধিক variable থাকে,
এবং আমরা একটি variable পরিবর্তন করে অন্য variable-গুলোকে
constant ধরে derivative বের করি।


Example:


z = x² + y²


এখানে দুইটি variable আছে:

x

y


Partial derivative বের করার সময়:

∂z/∂x

মানে:

শুধু x পরিবর্তন হবে,
y constant থাকবে।


∂z/∂y

মানে:

শুধু y পরিবর্তন হবে,
x constant থাকবে।


Partial derivative multivariable calculus-এর ভিত্তি।
"""


# ===========================================================
# 02_WhyThisConceptExistsInRelationToHistory
# ===========================================================

"""
ইতিহাস:

প্রথম Calculus মূলত single variable-এর জন্য তৈরি হয়েছিল।


Example:

y=f(x)


কিন্তু বাস্তব জগতের অনেক সমস্যা একাধিক variable-এর উপর
নির্ভর করে।


Example:


Temperature:

T = f(latitude, longitude, altitude)


Physics:


Force = f(mass, acceleration)


Machine Learning:


Loss = f(weight1, weight2, weight3,...)



এই ধরনের সমস্যার জন্য
multivariable calculus প্রয়োজন হয়।


Partial Derivative এই সমস্যার সমাধান দেয়।

18th century-তে mathematicians
multivariable function নিয়ে কাজ করার সময়
partial derivative-এর ধারণা তৈরি করেন।
"""


# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
বাস্তব জীবনের intuition:


Example 1:

একটি পাহাড়ের height:


Height = f(x,y)


এখানে:

x = east-west position

y = north-south position


আপনি যদি শুধু x direction-এ হাঁটেন:

∂h/∂x


বলবে:

কত দ্রুত height পরিবর্তন হচ্ছে।



--------------------------------


Example 2:

Room Temperature:


Temperature:

T = f(x,y,z)


যেখানে:

x = width

y = length

z = height


শুধু x পরিবর্তন করলে:

∂T/∂x


Temperature কত পরিবর্তন হচ্ছে
তা পাওয়া যায়।



--------------------------------


Example 3:

AI Model:


Loss depends on:

weight1

weight2

weight3


একটি weight পরিবর্তন করলে
loss কত পরিবর্তন হবে?


Partial derivative ব্যবহার করা হয়।
"""


# ===========================================================
# 04_Definition
# ===========================================================

"""
Partial Derivative হলো:

একাধিক variable থাকা function-এর
একটি নির্দিষ্ট variable-এর প্রতি derivative।


Notation:


∂f/∂x



এখানে:

∂ = Partial symbol


Example:


f(x,y)=x²+y²



Partial with respect to x:


∂f/∂x


এখানে y constant।



Partial with respect to y:


∂f/∂y


এখানে x constant।
"""


# ===========================================================
# 05_Formula
# ===========================================================

"""
Partial Derivative Formula:


যদি:


z=f(x,y)



তাহলে:


∂z/∂x

=

lim(h→0)

[f(x+h,y)-f(x,y)]/h



এখানে:

শুধু x পরিবর্তন হচ্ছে।



--------------------------------


আর:


∂z/∂y

=

lim(h→0)

[f(x,y+h)-f(x,y)]/h



এখানে:

শুধু y পরিবর্তন হচ্ছে।



--------------------------------


Basic Rules:


1. Power Rule:


∂/∂x(xⁿ)=nxⁿ⁻¹



2. Constant Rule:


∂/∂x(c)=0



3. Variable constant হলে:


∂/∂x(y)=0


কারণ y এখানে constant।
"""


# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
ধরি:


f(x,y)=x²+y²



আমরা বের করবো:


∂f/∂x



Step 1:

x-এর প্রতি derivative নিতে হবে।


তাই:

x পরিবর্তন হবে

y constant থাকবে।



Function:


x²+y²



Derivative:


x² → 2x


y² → 0



কারণ y constant।



তাই:


∂f/∂x=2x



--------------------------------


এখন:


∂f/∂y



x constant:


x² → 0


y² → 2y



তাই:


∂f/∂y=2y
"""


# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
Multivariable function:


z=f(x,y)



একটি surface তৈরি করে।



        z
        |
        |
       /\
      /  \
     /    \
----------------
     x,y



Partial derivative:

Surface-এর একটি direction-এর slope।



Example:


∂z/∂x


মানে:

x direction-এর slope



∂z/∂y


মানে:

y direction-এর slope



Computer ভিতরে:


1. Variable select করে

2. অন্য variable constant রাখে

3. Normal derivative rule apply করে

4. Gradient তৈরি করে
"""


# ===========================================================
# 08_Examples
# ===========================================================

"""
Example 1:


Find:


f(x,y)=x²y+3y²



∂f/∂x



x-এর প্রতি derivative:


x²y → 2xy


3y² → 0



Answer:


∂f/∂x=2xy



--------------------------------


∂f/∂y:



x²y → x²


3y² → 6y



Answer:


∂f/∂y=x²+6y



--------------------------------


Example 2:


f(x,y,z)=x²+y²+z²



Partial derivatives:


∂f/∂x=2x


∂f/∂y=2y


∂f/∂z=2z



--------------------------------


Example 3:


Loss Function:


L(w1,w2)


Gradient:


∂L/∂w1


বলবে:

w1 পরিবর্তন করলে loss কত পরিবর্তন হবে।
"""


# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
Common Mistakes:


1. অন্য variable constant ভুলে যাওয়া


Example:


∂/∂x(y²)


Answer:

0


না:

2y



--------------------------------


2. Normal derivative এবং partial derivative
একই মনে করা


Single variable:

dy/dx


Multiple variable:

∂f/∂x



--------------------------------


3. সব variable একসাথে পরিবর্তন করা


Partial derivative-এ:

একটি variable change হয়।



--------------------------------


4. Gradient এবং partial derivative গুলিয়ে ফেলা


Gradient তৈরি হয় অনেকগুলো partial derivative দিয়ে।
"""


# ===========================================================
# 10_Exercises
# ===========================================================

"""
Practice Problems:


1.


Find:


f(x,y)=x³+y³



∂f/∂x


Answer:

3x²



--------------------------------


2.


Find:


f(x,y)=xy+x²



∂f/∂y


Answer:

x



--------------------------------


3.


Find:


f(x,y,z)=x²yz



∂f/∂x


Answer:

2xyz



--------------------------------


4.


Explain:


Why partial derivative is needed in Machine Learning?



--------------------------------


5.


Find gradient of:


f(x,y)=x²+y²
"""


# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
Machine Learning এবং AI-তে Partial Derivative:


1. Gradient Descent


Machine Learning model-এ:


Loss Function:

L(w1,w2,w3,...)



প্রতিটি weight-এর জন্য:

∂L/∂w1

∂L/∂w2

∂L/∂w3



বের করা হয়।



--------------------------------


2. Gradient Vector


অনেকগুলো partial derivative একসাথে:


∇L


Gradient তৈরি করে।


Example:


∇L =

[
∂L/∂w1,
∂L/∂w2
]



--------------------------------


3. Neural Network Training


প্রতিটি weight এবং bias-এর
প্রভাব জানতে partial derivative ব্যবহার হয়।



--------------------------------


4. Backpropagation


Output error থেকে:

প্রতিটি layer-এর parameter পর্যন্ত
gradient পাঠানো হয়।


এখানে partial derivative গুরুত্বপূর্ণ।



--------------------------------


5. Computer Vision


Image function:


I(x,y)


Pixel intensity পরিবর্তন:


∂I/∂x

∂I/∂y


Edge detection-এ ব্যবহার হয়।



--------------------------------


Summary:


Partial Derivative শেখায়:


✓ Multivariable change বোঝা
✓ Gradient তৈরি করা
✓ Optimization করা
✓ Neural Network train করা


Modern AI mathematics-এর একটি মূল ভিত্তি হলো
Partial Derivative।
"""


# ===========================================================
# End of Partial Derivative
# ===========================================================