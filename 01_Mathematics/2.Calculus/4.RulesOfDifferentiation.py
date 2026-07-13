"""
===========================================================
Rules of Differentiation (ডিফারেনশিয়েশনের নিয়মসমূহ)
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
Rules of Differentiation হলো derivative দ্রুত এবং সহজে
বের করার mathematical rules।

Derivative-এর মূল formula:

f'(x)=lim(h→0)[f(x+h)-f(x)]/h


কিন্তু বড় function-এর ক্ষেত্রে প্রতিবার
first principle ব্যবহার করা কঠিন।

তাই mathematicians বিভিন্ন shortcut rule তৈরি করেন।


প্রধান differentiation rules:

1. Constant Rule
2. Power Rule
3. Constant Multiple Rule
4. Sum Rule
5. Difference Rule
6. Product Rule
7. Quotient Rule
8. Chain Rule


এই rules ব্যবহার করে জটিল function-এর derivative
সহজে বের করা যায়।
"""


# ===========================================================
# 02_WhyThisConceptExistsInRelationToHistory
# ===========================================================

"""
ইতিহাস:

Newton এবং Leibniz যখন Calculus তৈরি করেন,
তখন তারা derivative বের করার জন্য limit definition ব্যবহার করতেন।


কিন্তু সমস্যা:

Complex function যেমন:

(x²+3x)(sin x)

বা

sin(x²)

এর derivative বের করতে অনেক সময় লাগত।


তাই বিভিন্ন pattern খুঁজে বের করা হয়।

এই pattern থেকেই differentiation rules তৈরি হয়।


Rules of Differentiation:

Derivative calculation-কে দ্রুত,
নির্ভুল এবং scalable করে।
"""


# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
বাস্তব জীবনের intuition:


Example 1:

একটি গাড়ির position:

s(t)=t²+5t+10


Velocity বের করতে derivative লাগে।


যদি function ছোট হয়:

First principle ব্যবহার করা যায়।


কিন্তু যদি:


s(t)=t³+5t²+sin(t)+e^t


তাহলে rule ব্যবহার করতে হবে।



--------------------------------


Example 2:

Machine Learning:

একটি neural network-এ হাজার হাজার parameter থাকে।

প্রতিটি parameter-এর derivative বের করতে
first principle ব্যবহার করলে অসম্ভব ধীর হবে।


Chain Rule এবং Product Rule ব্যবহার করে
backpropagation করা হয়।
"""


# ===========================================================
# 04_Definition
# ===========================================================

"""
Rules of Differentiation হলো কিছু mathematical rule
যার মাধ্যমে derivative বের করার shortcut পাওয়া যায়।


যদি:

y=f(x)


তাহলে:

Derivative:

dy/dx


বিভিন্ন function-এর pattern অনুযায়ী
বিভিন্ন rule প্রয়োগ করা হয়।


Example:


x² এর derivative:


Power Rule:

2x


sin(x) এর derivative:


Trigonometric Rule:

cos(x)
"""


# ===========================================================
# 05_Formula
# ===========================================================

"""
===========================================================
1. Constant Rule
===========================================================


যদি:

f(x)=c


তাহলে:


d/dx(c)=0



Example:


d/dx(10)=0



কারণ:

Constant পরিবর্তন হয় না।



===========================================================
2. Power Rule
===========================================================


Formula:


d/dx(xⁿ)=nxⁿ⁻¹



Example:


d/dx(x⁴)


=4x³



===========================================================
3. Constant Multiple Rule
===========================================================


Formula:


d/dx(cf(x))

=

c f'(x)



Example:


d/dx(5x²)


=5(2x)


=10x



===========================================================
4. Sum Rule
===========================================================


Formula:


d/dx(f+g)

=

f'+g'



Example:


d/dx(x²+x)


=

2x+1



===========================================================
5. Difference Rule
===========================================================


Formula:


d/dx(f-g)

=

f'-g'



Example:


d/dx(x²-x)


=

2x-1



===========================================================
6. Product Rule
===========================================================


যদি:


y=f(x)g(x)



Formula:


(fg)'=f'g+fg'



===========================================================
7. Quotient Rule
===========================================================


যদি:


y=f/g



Formula:


(f/g)'=

(gf'-fg')/g²



===========================================================
8. Chain Rule
===========================================================


যদি:


y=f(g(x))


Formula:


dy/dx=f'(g(x))×g'(x)
"""


# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
Product Rule Derivation:


ধরি:


y=f(x)g(x)



Derivative definition:


dy/dx

=

lim(h→0)

[f(x+h)g(x+h)-f(x)g(x)]/h



এখন যোগ করি এবং বিয়োগ করি:


f(x+h)g(x)


তাহলে:


=

lim(h→0)

[
f(x+h)g(x+h)-f(x+h)g(x)
+
f(x+h)g(x)-f(x)g(x)
]/h



Factor:


=

lim(h→0)

[
f(x+h)(g(x+h)-g(x))
+
g(x)(f(x+h)-f(x))
]/h



Limit প্রয়োগ করলে:


=

f(x)g'(x)+g(x)f'(x)



Therefore:


(fg)'=f'g+fg'
"""


# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
Computer ভিতরে differentiation:


Example:


f(x)=x²sin(x)


Step 1:

Function structure identify করে।


Step 2:

এটি Product Rule বুঝে:


(x²)'sin(x)+x²(sin(x))'


Step 3:

Individual derivative বের করে।


Step 4:

Combine করে।



Visualization:


Complex Function

        |
        |
   Break into parts
        |
        |
Apply Rules
        |
        |
Derivative


Compiler/AI symbolic systems এই ধরনের
rule-based transformation ব্যবহার করে।
"""


# ===========================================================
# 08_Examples
# ===========================================================

"""
Example 1:

Find:


d/dx(3x⁴)


Solution:


Constant Multiple Rule:


=3(4x³)


=12x³



--------------------------------


Example 2:


Find:


d/dx(x²+x³)


Solution:


Sum Rule:


=2x+3x²



--------------------------------


Example 3:


Find:


d/dx(x²sinx)



Product Rule:


=(2x)sinx+x²cosx



--------------------------------


Example 4:


Find:


d/dx(sin(x²))


Chain Rule:


=cos(x²)×2x


=2x cos(x²)
"""


# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
Common Mistakes:


1. Product Rule ভুল করা


ভুল:


(fg)'=f'g'


সঠিক:


(fg)'=f'g+fg'



--------------------------------


2. Chain Rule ভুলে যাওয়া


Example:


sin(x²)


শুধু cos(x²) নয়।


সঠিক:


2xcos(x²)



--------------------------------


3. Quotient Rule-এর sign ভুল করা


Formula:

(gf'-fg')/g²



--------------------------------


4. Constant-এর derivative ভুল করা


d/dx(100)=0



--------------------------------


5. Power Rule ভুল:


x⁵


Derivative:


5x⁴

না যে:

x⁴
"""


# ===========================================================
# 10_Exercises
# ===========================================================

"""
Practice Problems:


1.

Find:

d/dx(x⁶)


Answer:

6x⁵



--------------------------------


2.

Find:

d/dx(4x³+2x²)


Answer:

12x²+4x



--------------------------------


3.

Find:


d/dx(x sinx)


Answer:


sinx+xcosx



--------------------------------


4.

Find:


d/dx(cos(x²))


Answer:


-2xsin(x²)



--------------------------------


5.

Explain:

Why Chain Rule is important in Deep Learning?
"""


# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
AI এবং Machine Learning-এ Differentiation Rules:


1. Backpropagation


Neural Network:

Input

↓

Layers

↓

Prediction

↓

Loss


Loss থেকে weight পর্যন্ত gradient পাঠাতে
Chain Rule ব্যবহার হয়।



--------------------------------


2. Gradient Descent


Formula:


θ_new = θ_old - α∇J(θ)



এখানে:

∇J(θ)

হলো derivative।



--------------------------------


3. Automatic Differentiation


Framework:


- PyTorch
- TensorFlow


নিজে থেকে differentiation rules apply করে।



Example:


torch.autograd


Chain Rule ব্যবহার করে gradient বের করে।



--------------------------------


4. Deep Neural Networks


একটি network-এ:

f(g(h(x)))


এর derivative বের করতে
বারবার Chain Rule ব্যবহার হয়।



--------------------------------


5. Optimization Algorithms


Adam

RMSProp

SGD


সব derivative-এর উপর নির্ভরশীল।



--------------------------------


Summary:


Differentiation Rules শেখায়:


✓ দ্রুত derivative বের করা
✓ Complex function handle করা
✓ Neural network train করা
✓ Optimization করা


Modern AI mathematics-এর মূল ভিত্তির একটি হলো
Differentiation Rules।
"""


# ===========================================================
# End of Rules of Differentiation
# ===========================================================