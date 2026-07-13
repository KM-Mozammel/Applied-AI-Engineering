"""
===========================================================
Optimization (অপ্টিমাইজেশন)
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
Optimization হলো Mathematics এবং Computer Science-এর
একটি গুরুত্বপূর্ণ ধারণা।

Optimization মানে:

কোনো problem-এর সবচেয়ে ভালো solution খুঁজে বের করা।


সাধারণত দুই ধরনের optimization হয়:


1. Minimization:

সবচেয়ে ছোট value খোঁজা।


Example:

Loss কমানো



2. Maximization:

সবচেয়ে বড় value খোঁজা।


Example:

Profit বাড়ানো



Machine Learning-এ:

Goal:

Model-এর error বা loss minimum করা।


Optimization হলো AI learning process-এর মূল ভিত্তি।
"""


# ===========================================================
# 02_WhyThisConceptExistsInRelationToHistory
# ===========================================================

"""
ইতিহাস:

মানুষ সবসময় ভালো সিদ্ধান্ত নেওয়ার চেষ্টা করেছে।


Example:

- কম খরচে বেশি উৎপাদন
- কম সময়ে বেশি কাজ
- বেশি লাভ


প্রাচীন গণিত:

Maximum এবং Minimum problem নিয়ে কাজ করা হতো।


Calculus আবিষ্কারের পরে:

Derivative ব্যবহার করে
কোনো function-এর maximum/minimum খুঁজে বের করা সম্ভব হয়।


Modern era:

Complex optimization problem তৈরি হয়:


- Machine Learning
- Robotics
- Finance
- Engineering


Optimization এখন AI-এর প্রধান mathematical tool।
"""


# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
বাস্তব জীবনের intuition:


Example 1:

ব্যবসা:


Goal:

Profit maximize করা।


Variables:

Price

Production

Marketing


Optimization বলে:

কোন combination সবচেয়ে ভালো।



--------------------------------


Example 2:

GPS Route:


Goal:

Distance minimize করা।


Possible routes:

অনেকগুলো।


Optimization:

সবচেয়ে ছোট পথ নির্বাচন করে।



--------------------------------


Example 3:

Machine Learning:


Model prediction ভুল করছে।


Goal:

Error কমানো।


Optimization algorithm:

Parameter পরিবর্তন করে
best model খুঁজে বের করে।
"""


# ===========================================================
# 04_Definition
# ===========================================================

"""
Optimization হলো:

কোনো objective function-এর
maximum অথবা minimum value খুঁজে বের করার প্রক্রিয়া।


Components:


1. Objective Function


যেটা optimize করতে চাই।



Example:


Loss Function



--------------------------------


2. Variables / Parameters


যেগুলো পরিবর্তন করা যায়।



Example:


Neural Network weights



--------------------------------


3. Constraints


কিছু সীমাবদ্ধতা থাকতে পারে।



Example:


Budget limit
"""


# ===========================================================
# 05_Formula
# ===========================================================

"""
General Optimization:


Minimize:


f(x)



Subject to:


constraints



--------------------------------


Derivative Condition:


Minimum বা Maximum point-এ:


f'(x)=0



কারণ:

সেখানে slope zero হয়।



--------------------------------


Gradient Optimization:


For multiple variables:


∇f(x)=0



--------------------------------


Gradient Descent Formula:


x_new

=

x_old - α∇f(x)



যেখানে:


α = Learning Rate


∇f(x)=Gradient



--------------------------------


Newton Optimization:


x_new

=

x - H⁻¹∇f(x)



যেখানে:


H = Hessian Matrix
"""


# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
Gradient Descent Formula Derivation:


ধরি:

আমাদের goal:

Loss minimize করা।



Function:


J(θ)



Gradient:


∇J(θ)



Gradient বলে:

কোন দিকে function সবচেয়ে দ্রুত বাড়ছে।



তাই minimum পেতে
এর বিপরীত direction-এ যেতে হবে।



Direction:


-∇J(θ)



একটি ছোট step:


α



নিলে:


New parameter:


θ_new

=

θ_old - α∇J(θ)



এটাই Gradient Descent formula।
"""


# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
Optimization visualization:


Loss Surface:


          Loss

           /\

          /  \

---------/----\---------

          ↓

       Minimum



Goal:

উপর থেকে নিচে নামা।



Gradient Descent:


1. Current position নেয়

2. Gradient calculate করে

3. Opposite direction নেয়

4. Parameter update করে

5. আবার repeat করে



Machine Learning pipeline:


Data

↓

Model

↓

Prediction

↓

Loss

↓

Gradient

↓

Optimization

↓

Updated Model
"""


# ===========================================================
# 08_Examples
# ===========================================================

"""
Example 1:


Function:


f(x)=x²



Derivative:


f'(x)=2x



Minimum:


2x=0


x=0



Answer:


Minimum point = 0



--------------------------------


Example 2:


Gradient Descent:


Loss:

J(w)=w²



Gradient:


dJ/dw=2w



Initial:


w=10



Learning rate:


α=0.1



Update:


w_new

=

10-0.1(20)



=

8



Weight কমে যাচ্ছে।



--------------------------------


Example 3:


AI Model:


Loss Function:


L(w,b)



Parameters:


w,b



Optimization:

w,b update করে
loss minimum করা।
"""


# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
Common Mistakes:


1. Optimization মানে শুধু minimum ভাবা


Maximum-ও optimization-এর অংশ।



--------------------------------


2. Gradient direction ভুল ব্যবহার করা


Gradient:

Maximum increase direction


Negative Gradient:

Decrease direction



--------------------------------


3. Learning rate ভুল নির্বাচন করা


Too high:

Overshoot


Too low:

Slow learning



--------------------------------


4. Local minimum এবং global minimum
গোলমাল করা


Local:

একটি ছোট area-এর minimum


Global:

সবচেয়ে ভালো minimum



--------------------------------


5. শুধু derivative zero হলেই minimum ভাবা


Second derivative বা Hessian analysis প্রয়োজন।
"""


# ===========================================================
# 10_Exercises
# ===========================================================

"""
Practice Problems:


1.


Find minimum:


f(x)=x²+4x+4



--------------------------------


2.


Explain:

Why Gradient Descent uses negative gradient?



--------------------------------


3.


What happens if learning rate is too large?



--------------------------------


4.


Difference between:

Gradient Descent

Newton Method



--------------------------------


5.


Why optimization is important in AI?
"""


# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
AI এবং Machine Learning-এ Optimization:


1. Model Training


Neural Network training:


Prediction

↓

Loss Calculation

↓

Optimization

↓

Weight Update



--------------------------------


2. Gradient Descent


সবচেয়ে জনপ্রিয় optimization algorithm।


Used in:


- Linear Regression
- Logistic Regression
- Neural Networks



--------------------------------


3. Deep Learning Optimizers:


Common algorithms:


- SGD
- Momentum
- RMSProp
- Adam



সবগুলো gradient ব্যবহার করে।



--------------------------------


4. Hyperparameter Optimization


Best values খোঁজা:


Learning rate

Batch size

Number of layers



--------------------------------


5. Reinforcement Learning


Goal:


Maximum reward পাওয়া।


Optimization ব্যবহার করে
best policy শেখা হয়।



--------------------------------


6. Computer Vision


Image recognition model train করতে
optimization প্রয়োজন।



--------------------------------


7. Large Language Models


LLM training:


Billions of parameters


Optimization ছাড়া সম্ভব নয়।



--------------------------------


Summary:


Optimization শেখায়:


✓ Best solution খোঁজা
✓ Loss minimize করা
✓ Model train করা
✓ Decision improve করা


AI-এর মূল প্রশ্ন:


"কীভাবে সবচেয়ে ভালো ফলাফল পাওয়া যায়?"


এই প্রশ্নের mathematical উত্তর হলো
Optimization।
"""


# ===========================================================
# End of Optimization
# ===========================================================