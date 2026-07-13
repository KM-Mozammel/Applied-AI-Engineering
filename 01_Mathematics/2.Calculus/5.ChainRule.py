# Chain Rule: Function-এর ভিতরে Function হলে?

# Derivative আবিষ্কারের পরে নতুন সমস্যা এল। ধরো Function-এর ভিতরে Function আছে। y = (x² + 1)³

# এখন, নিউটন দেখলেন

# Outer Function: (x²+1)³
# Inner Function: x²+1

# দুটোর পরিবর্তন একসাথে হচ্ছে। এখান থেকে জন্ম নেয় Chain Rule
# Formula: dy / dx = dy / du * du / dx

# Example: y = (x**2 + 1)**3
# Inner: u = x**2 + 1
# Outer: y = u**3
# Derivative: 3u² × 2x


def chain_rule(x):
    return 3*(x**2+1)**2 * (2*x)

print(chain_rule(2))

# Deep Learning-এর পুরো Backpropagation Chain Rule-এর উপর দাঁড়িয়ে।
# Input -> Layer1 -> Layer2 -> Layer3 -> Loss
# প্রতিটি layer এর derivative বের করতে হয়।

"""
===========================================================
Chain Rule (চেইন রুল)
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
Chain Rule হলো Differentiation-এর সবচেয়ে গুরুত্বপূর্ণ
নিয়মগুলোর একটি।

যখন একটি function-এর ভিতরে আরেকটি function থাকে,
তখন derivative বের করার জন্য Chain Rule ব্যবহার করা হয়।


Example:


y = sin(x²)


এখানে:

Outer Function:

sin(u)


Inner Function:

u = x²


একটি function আরেকটির উপর নির্ভর করছে।

এই dependency-এর derivative বের করার পদ্ধতিই Chain Rule।
"""


# ===========================================================
# 02_WhyThisConceptExistsInRelationToHistory
# ===========================================================

"""
ইতিহাস:

Calculus আবিষ্কারের পর mathematicians বুঝতে পারেন
যে বাস্তব জীবনের অনেক function একাধিক ধাপে তৈরি হয়।


Example:

Temperature sensor:


Input:

Time


↓

Temperature Function


↓

Sensor Output


এখানে একটির পরিবর্তন অন্যটির মাধ্যমে ঘটে।


Simple function-এর derivative সহজ ছিল।

কিন্তু:


y = sin(x²)


বা


y = e^(3x²+1)


এর মতো function-এর জন্য নতুন নিয়ম দরকার হয়।


এই সমস্যার সমাধান হিসেবে Chain Rule তৈরি হয়।
"""


# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
বাস্তব জীবনের intuition:


Example 1:

গাড়ি:


Time

↓

Distance

↓

Speed



Time পরিবর্তন করলে:

Distance পরিবর্তন হয়।

Distance পরিবর্তন করলে:

Speed পরিবর্তন হয়।



একটি change আরেকটি change-এর মাধ্যমে আসে।



--------------------------------


Example 2:

Machine Learning:


Input

↓

Hidden Layer 1

↓

Hidden Layer 2

↓

Output



Input-এর ছোট পরিবর্তন
প্রতিটি layer পার হয়ে output পরিবর্তন করে।


এই layered dependency-এর জন্য Chain Rule প্রয়োজন।
"""


# ===========================================================
# 04_Definition
# ===========================================================

"""
Chain Rule বলে:


যদি একটি function অন্য একটি function-এর উপর
নির্ভর করে:


y=f(g(x))


তাহলে derivative:


প্রথমে outer function-এর derivative

তারপর inner function-এর derivative


দুইটি multiply করতে হবে।


সহজ ভাষায়:


"বাইরের পরিবর্তনের হার × ভিতরের পরিবর্তনের হার"
"""


# ===========================================================
# 05_Formula
# ===========================================================

"""
Basic Formula:


যদি:


y=f(g(x))


তাহলে:


dy/dx

=

dy/du × du/dx



অথবা:


(f(g(x)))'

=

f'(g(x)) × g'(x)



--------------------------------


Example:


y=sin(x²)



ধরি:


u=x²



তাহলে:


Outer:

y=sin(u)



Derivative:

dy/du=cos(u)



Inner:

du/dx=2x



Final:


dy/dx

=

cos(x²) × 2x



=

2x cos(x²)
"""


# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
Chain Rule আসে derivative definition থেকে।


ধরি:


y=f(u)

এবং:


u=g(x)



Derivative:


dy/dx


আমরা লিখতে পারি:


dy/dx

=

(dy/du) × (du/dx)



কারণ:


dy পরিবর্তন হচ্ছে u-এর মাধ্যমে

এবং

u পরিবর্তন হচ্ছে x-এর মাধ্যমে।



Mathematically:


dy/dx

=

dy
--
du


×

du
--
dx



এখানে du cancel হয়ে যায়:


dy/dx



তাই:


dy/dx = dy/du × du/dx



এটাই Chain Rule।
"""


# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
Chain Rule ভিতরে যেভাবে কাজ করে:


Function:


y=sin(x²)


Step 1:

Function ভাঙে:


x²

↓

sin(u)



Step 2:

প্রতিটি অংশের derivative বের করে:


Inner:

x² → 2x



Outer:

sin(u) → cos(u)



Step 3:

Multiply:


2x × cos(x²)



Final:

2xcos(x²)



Visualization:


Input x

 |

 | derivative

 ↓

Inner Function

 |

 | derivative

 ↓

Outer Function

 |

 ↓

Final Gradient



Computer Algebra System এবং AI framework
এইভাবে function graph তৈরি করে।
"""


# ===========================================================
# 08_Examples
# ===========================================================

"""
Example 1:


Find:


y=(x²+1)³



Step 1:


Inner:


u=x²+1



Outer:


y=u³



Step 2:


Outer derivative:


dy/du=3u²



Inner derivative:


du/dx=2x



Step 3:


Multiply:


dy/dx

=

3(x²+1)² × 2x



Answer:


6x(x²+1)²



--------------------------------


Example 2:


y=e^(x²)



Inner:


u=x²



Outer:


e^u



Derivative:


e^u × 2x



Answer:


2xe^(x²)



--------------------------------


Example 3:


y=log(x³)



Inner:


u=x³



Outer:


log(u)



Derivative:


1/u × 3x²



Answer:


3x²/x³


=

3/x
"""


# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
Common Mistakes:


1. শুধু outer derivative নেওয়া


Example:


sin(x²)


ভুল:


cos(x²)


সঠিক:


2xcos(x²)



--------------------------------


2. Inner derivative ভুলে যাওয়া


Chain Rule-এ সবসময় ভিতরের function
multiply করতে হয়।



--------------------------------


3. Function identify না করা


প্রথমে বুঝতে হবে:


Outer function কোনটি?

Inner function কোনটি?



--------------------------------


4. Multiple layer function-এ
একাধিক Chain Rule প্রয়োজন।


Example:


sin(e^(x²))


এখানে কয়েকবার Chain Rule লাগবে।
"""


# ===========================================================
# 10_Exercises
# ===========================================================

"""
Practice Problems:


1.


Find:


d/dx(sin(x³))


Answer:


3x²cos(x³)



--------------------------------


2.


Find:


d/dx((2x+5)⁴)


Answer:


8(2x+5)³



--------------------------------


3.


Find:


d/dx(e^(3x))


Answer:


3e^(3x)



--------------------------------


4.


Find:


d/dx(cos(x²))


Answer:


-2xsin(x²)



--------------------------------


5.


Explain:

Why Chain Rule is important for neural networks?
"""


# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
Machine Learning এবং AI-তে Chain Rule:


1. Backpropagation


Neural Network:


Input

↓

Layer 1

↓

Layer 2

↓

Output


Loss function থেকে
প্রতিটি weight-এর gradient বের করতে
Chain Rule ব্যবহার হয়।



--------------------------------


2. Neural Network Gradient


ধরি:


Output:

y=f(g(x))


তাহলে:


dy/dx

=

dy/dg × dg/dx



এক layer থেকে আরেক layer পর্যন্ত
gradient propagate হয়।



--------------------------------


3. Deep Learning


Deep Neural Network-এ:


Input → Hidden1 → Hidden2 → Output


অনেকগুলো function chain আকারে থাকে।


Chain Rule ছাড়া
deep learning training সম্ভব নয়।



--------------------------------


4. Automatic Differentiation


Framework:


- PyTorch
- TensorFlow


Computational graph তৈরি করে।

তারপর Chain Rule ব্যবহার করে
gradient calculate করে।



--------------------------------


5. Optimization


Gradient Descent:


Weight update করতে
Chain Rule থেকে পাওয়া gradient ব্যবহার করে।



--------------------------------


Summary:


Chain Rule শেখায়:


✓ Nested function-এর derivative
✓ Dependency বোঝা
✓ Backpropagation
✓ Deep Learning training


Modern AI-এর mathematical engine-এর
একটি প্রধান ভিত্তি হলো Chain Rule।
"""


# ===========================================================
# End of Chain Rule
# ===========================================================