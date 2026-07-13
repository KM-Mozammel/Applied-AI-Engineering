# Gradient Descent: সবচেয়ে দ্রুত নিচে নামার দিক কোনটি?
# ধরি পাহাড়ের চূড়ায় দাঁড়িয়ে আছো। তুমি নিচে নামতে চাও।
# Gradient দেখাচ্ছে: উপরে যাওয়ার দিক। তাহলে? উল্টো দিকে হাঁটো। এটাই Gradient Descent

# Formula: Xnew​ = Xold​−learning rate×gradient
# Loss Funcation: L(x)=x^2
# Derivative: L′(x)=2x

x = 8

learning_rate = 0.1

for i in range(10):

    gradient = 2*x

    x = x - learning_rate * gradient

    print(x)
    
    
"""
===========================================================
Gradient Descent (গ্রেডিয়েন্ট ডিসেন্ট)
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
Gradient Descent হলো Machine Learning এবং Optimization-এর
সবচেয়ে গুরুত্বপূর্ণ algorithm-গুলোর একটি।


এটি ব্যবহার করা হয়:

কোনো function-এর minimum value খুঁজে বের করতে।


Machine Learning-এ:

Goal:

Loss Function minimize করা।


Model যখন ভুল prediction করে:

Loss বেশি হয়।

Gradient Descent ধীরে ধীরে parameter পরিবর্তন করে
loss কমিয়ে optimal value খুঁজে বের করে।


মূল ধারণা:


Gradient:

কোন দিকে loss বাড়ছে


Negative Gradient:

কোন দিকে loss কমবে



Gradient Descent:

"Loss কমানোর দিকে ছোট ছোট step নেওয়া"
"""


# ===========================================================
# 02_WhyThisConceptExistsInRelationToHistory
# ===========================================================

"""
ইতিহাস:

Calculus আবিষ্কারের পরে
Derivative ব্যবহার করে
minimum এবং maximum খোঁজা সম্ভব হয়।


কিন্তু সমস্যা:

Modern problem অনেক complex:


- হাজার হাজার parameter
- কোটি কোটি data point


Analytical solution সবসময় সম্ভব নয়।


তাই iterative method প্রয়োজন হয়।


Gradient Descent তৈরি হয়
যেখানে:


1. একটি starting point নেওয়া হয়

2. Gradient বের করা হয়

3. Opposite direction-এ move করা হয়

4. Repeat করা হয়



Machine Learning-এর বড় model training
এই ধারণার উপর ভিত্তি করে।
"""


# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
বাস্তব জীবনের intuition:


Example 1:

একটি পাহাড়ে আছেন।


আপনার লক্ষ্য:

সবচেয়ে নিচু জায়গায় যাওয়া।


কিন্তু চারপাশ দেখা যাচ্ছে না।


আপনি কী করবেন?


1. চারপাশের slope অনুভব করবেন

2. যেদিকে নিচে নামা যায় সেদিকে যাবেন

3. আবার slope দেখবেন


এটাই Gradient Descent।



--------------------------------


Example 2:

Machine Learning:


Model prediction:

ভুল বেশি


↓

Loss calculate


↓

Gradient বলে:

কোন parameter পরিবর্তন করলে
ভুল কমবে


↓

Weight update



--------------------------------


Example 3:

Tuning:


একটি radio station ঠিক frequency খুঁজছে।


বারবার adjust করে
best signal খুঁজে বের করা।


এটিও optimization।
"""


# ===========================================================
# 04_Definition
# ===========================================================

"""
Gradient Descent হলো:

একটি iterative optimization algorithm
যা gradient-এর বিপরীত direction অনুসরণ করে
objective function-এর minimum খুঁজে বের করে।


Components:


1. Function:

যেটা minimize করতে হবে



2. Parameter:

যেগুলো update হবে



3. Gradient:

পরিবর্তনের direction



4. Learning Rate:

কত বড় step নেওয়া হবে



Machine Learning-এ:


Objective Function:

Loss Function
"""


# ===========================================================
# 05_Formula
# ===========================================================

"""
Basic Formula:


θ_new

=

θ_old - α∇J(θ)



যেখানে:


θ

=

Parameter / Weight



α

=

Learning Rate



∇J(θ)

=

Gradient of Loss Function



--------------------------------


Single Variable:


x_new

=

x_old - α f'(x)



--------------------------------


Multiple Variable:


θ=[w1,w2,...]


Gradient:


∇J(θ)



Update:


θ = θ - α∇J(θ)
"""


# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
Gradient Descent Formula আসে
Taylor Expansion থেকে।


ধরি:


Function:


J(x)



ছোট পরিবর্তনের জন্য:


J(x+Δx)

≈

J(x)+J'(x)Δx



আমরা চাই:

J কমুক।



যদি:

J'(x)

positive হয়,


তাহলে:

x কমাতে হবে।



যদি:

J'(x)

negative হয়,


তাহলে:

x বাড়াতে হবে।



দুই ক্ষেত্রেই direction:


-J'(x)



Step size:


α



তাই:


Δx=-αJ'(x)



New value:


x_new

=

x_old-αJ'(x)



Multiple variable হলে:


x_new

=

x_old-α∇J(x)



এটাই Gradient Descent।
"""


# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
Gradient Descent Process:


Loss Surface:


        Loss

          *
         / \
        /   \
-------/-----\-------

        ↓
     Minimum



Algorithm:


Step 1:

Initial parameter choose


Example:

w=10



Step 2:

Gradient calculate


Gradient বলে:

কোন দিকে loss বাড়ছে



Step 3:

Negative direction-এ move


w=w-αgradient



Step 4:

Repeat



শেষে:

Minimum point পাওয়া যায়।



Machine Learning Pipeline:


Data

↓

Model

↓

Prediction

↓

Loss

↓

Gradient Calculation

↓

Weight Update

↓

Better Model
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



Initial:


x=5



Learning rate:


α=0.1



Update:


x_new

=

5-0.1(10)



=

4



Next:


x=4


Gradient:

8



x_new:

3.2



ধীরে ধীরে:


5 → 4 → 3.2 → ... → 0



Minimum পাওয়া যাবে।



--------------------------------


Example 2:


Linear Regression:


Prediction:


y=wx+b



Loss:


MSE



Gradient:


∂Loss/∂w


∂Loss/∂b



Update:


w=w-α∂Loss/∂w


b=b-α∂Loss/∂b



--------------------------------


Example 3:


Neural Network:


Weight:

w


Gradient:


∂L/∂w



Update:


w_new=w_old-α∂L/∂w
"""


# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
Common Mistakes:


1. Positive gradient ব্যবহার করা


ভুল:


θ=θ+α∇J


সঠিক:


θ=θ-α∇J



--------------------------------


2. Learning rate ভুল নির্বাচন:


Too high:


Minimum পার হয়ে যাবে।



Too low:


Training ধীর হবে।



--------------------------------


3. Local minimum-এ আটকে যাওয়া


Complex function-এ হতে পারে।



--------------------------------


4. Gradient zero মানেই সবসময় ভালো নয়


Saddle point হতে পারে।



--------------------------------


5. Feature scaling না করা


Large scale feature হলে
gradient descent ধীরে converge করতে পারে।
"""


# ===========================================================
# 10_Exercises
# ===========================================================

"""
Practice Problems:


1.


Apply gradient descent:


f(x)=x²


Starting point:

x=10

Learning rate:

0.1



--------------------------------


2.


Explain:

Why negative gradient is used?



--------------------------------


3.


What happens if learning rate increases?



--------------------------------


4.


Difference between:


Batch Gradient Descent

Stochastic Gradient Descent



--------------------------------


5.


Why neural networks need optimization?
"""


# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
AI এবং Machine Learning-এ Gradient Descent:


1. Linear Regression


Cost function minimize করতে
Gradient Descent ব্যবহার হয়।



--------------------------------


2. Logistic Regression


Classification boundary শেখার জন্য
parameter update করা হয়।



--------------------------------


3. Neural Networks


Deep Learning-এর মূল training algorithm।


Process:


Forward Pass

↓

Loss

↓

Backpropagation

↓

Gradient Descent

↓

Weight Update



--------------------------------


4. Large Language Models (LLM)


GPT-এর মতো model train করতে:

Billions of parameters optimize করা হয়।



--------------------------------


5. Optimizers:


Gradient Descent-এর উন্নত version:


- SGD
- Momentum
- RMSProp
- Adam



--------------------------------


6. Reinforcement Learning


Policy এবং value function optimize করতে
Gradient-based methods ব্যবহার হয়।



--------------------------------


Summary:


Gradient Descent শেখায়:


✓ Loss কমানো
✓ Parameter update
✓ Model training
✓ Optimization


Machine Learning-এর শেখার process-এর
মূল algorithm হলো Gradient Descent।
"""


# ===========================================================
# End of Gradient Descent
# ===========================================================