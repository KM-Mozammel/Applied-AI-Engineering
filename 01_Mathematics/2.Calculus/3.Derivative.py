# Derivative : কত দ্রুত পরিবর্তন হচ্ছে?
# সমস্যা : "এই মুহূর্তে আপেলটা কত গতিতে নিচে নামছে?"

# Average speed বের করা সহজ: distance / time

# কিন্তু একটা নির্দিষ্ট মুহূর্তে speed? যেমন ঠিক t = 2 second এ? 
# এই প্রশ্ন থেকেই Derivative জন্ম নেয়।

# Derivative = Instantaneous Rate of Change; অর্থাৎ কোন জিনিস কত দ্রুত পরিবর্তিত হচ্ছে

def position(t):
    return t**2

def derivative(t):
    return 2*t

print(derivative(3))

"""
===========================================================
Derivative (অন্তরক / ডেরিভেটিভ)
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
Derivative (অন্তরক) হলো Calculus-এর সবচেয়ে গুরুত্বপূর্ণ ধারণাগুলোর
একটি।

Derivative বলে:

কোনো quantity কত দ্রুত পরিবর্তন হচ্ছে।

সহজ ভাষায়:

"একটি জিনিস পরিবর্তন হলে অন্য জিনিস কত দ্রুত পরিবর্তিত হচ্ছে?"

Derivative মূলত:

Rate of Change

এর mathematical measurement।


Examples:

- গাড়ির instantaneous speed
- Temperature change
- Stock price movement
- Neural Network weight update


Calculus:

1. Limit
2. Continuity
3. Derivative
4. Integral


Derivative তৈরি হয়েছে Limit-এর উপর ভিত্তি করে।
"""


# ===========================================================
# 02_WhyThisConceptExistsInRelationToHistory
# ===========================================================

"""
ইতিহাস:

প্রাচীন গণিতে মানুষ average change বের করতে পারত।

Example:

একটি গাড়ি:

100 km distance
2 hours time


Average speed:

50 km/h


কিন্তু সমস্যা:

একটি নির্দিষ্ট মুহূর্তে গাড়ির speed কত?


এই সমস্যা সমাধানের জন্য
instantaneous rate of change প্রয়োজন হয়।


17th century:

Isaac Newton এবং Gottfried Wilhelm Leibniz
Calculus তৈরি করেন।


Newton এটিকে Fluxion নামে চিন্তা করেছিলেন।

Leibniz derivative notation:

dy/dx

প্রবর্তন করেন।


Derivative এই প্রশ্নের উত্তর দেয়:

"ঠিক এই মুহূর্তে পরিবর্তনের হার কত?"
"""


# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
বাস্তব জীবনের উদাহরণ:


Example 1:

গাড়ির Speed:


Distance:

সময় অনুযায়ী পরিবর্তিত হচ্ছে।


Average speed:

Distance / Time


কিন্তু:

একটি নির্দিষ্ট second-এ speed?


Derivative ব্যবহার করতে হয়।



--------------------------------


Example 2:

Temperature:


সকাল:

20°C

দুপুর:

30°C


Temperature কত দ্রুত বাড়ছে?


Derivative বলে।



--------------------------------


Example 3:

Business:

Profit পরিবর্তন হচ্ছে।

Derivative বলে:

Production বাড়ালে profit কত দ্রুত বাড়বে।
"""


# ===========================================================
# 04_Definition
# ===========================================================

"""
Derivative হলো কোনো function-এর
instantaneous rate of change।


যদি:

y = f(x)


তাহলে derivative:


f'(x)


অথবা:


dy/dx


মানে:

x পরিবর্তনের সাথে y কত পরিবর্তন হচ্ছে।


Geometrically:

Derivative হলো graph-এর একটি point-এর slope।
"""


# ===========================================================
# 05_Formula
# ===========================================================

"""
Derivative-এর মূল Formula:


f'(x)

=

lim(h→0)

[f(x+h)-f(x)] / h



এটি First Principle বা Definition of Derivative।



Meaning:


f(x+h)

=

নতুন value



f(x)

=

পুরাতন value



Difference:

f(x+h)-f(x)


পরিবর্তন



h

=

input-এর ছোট পরিবর্তন



Limit h→0

=

অতি ক্ষুদ্র পরিবর্তন



--------------------------------


Common Derivative Rules:


1. Constant Rule:


d/dx(c)=0



Example:

d/dx(5)=0



--------------------------------


2. Power Rule:


d/dx(xⁿ)=nxⁿ⁻¹



Example:


d/dx(x²)


=2x



--------------------------------


3. Sum Rule:


d/dx(f+g)

=

f' + g'



--------------------------------


4. Product Rule:


(fg)' = f'g + fg'



--------------------------------


5. Chain Rule:


(f(g(x)))'

=

f'(g(x)) × g'(x)
"""


# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
First Principle থেকে derivative বের করি।


ধরি:


f(x)=x²



Formula:


f'(x)

=

lim(h→0)

[(x+h)²-x²]/h



Expand:


(x+h)²

=

x²+2xh+h²



তাহলে:


=

lim(h→0)

[x²+2xh+h²-x²]/h



Cancel:


=

lim(h→0)

[2xh+h²]/h



h বের করি:


=

lim(h→0)

h(2x+h)/h



Cancel h:


=

lim(h→0)

(2x+h)



h → 0 হলে:


=2x



Therefore:


d/dx(x²)=2x



এভাবেই derivative formula আসে।
"""


# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
Graphically:


Derivative = Slope


Positive slope:


       /
      /
     /
----/----------



Derivative positive



--------------------------------



Negative slope:


\
 \
  \
---\----------



Derivative negative



--------------------------------


Flat line:


------------


Derivative = 0



--------------------------------


Computer ভিতরে:


1. Function নেয়

2. দুইটি কাছাকাছি point নেয়

3. Slope calculate করে

4. Distance ছোট করতে থাকে

5. h → 0 হলে exact slope পাওয়া যায়


এটি Limit ব্যবহার করে।
"""


# ===========================================================
# 08_Examples
# ===========================================================

"""
Example 1:


Find derivative:


f(x)=x³



Using power rule:


d/dx(x³)


=3x²



Answer:

3x²



--------------------------------


Example 2:


f(x)=5x²+3x+7



Derivative:


=10x+3



কারণ:


5x² → 10x

3x → 3

7 → 0



--------------------------------


Example 3:


Distance:


s(t)=t²+5t



Velocity:


v(t)=ds/dt



=2t+5


এটি instantaneous speed।
"""


# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
Common Mistakes:


1. Derivative এবং function value এক মনে করা


Derivative হলো change rate,
মূল function নয়।



--------------------------------


2. Constant-এর derivative ভুল করা


Example:


d/dx(10)=0



--------------------------------


3. Power rule ভুল প্রয়োগ:


x³


Derivative:

3x²


x² নয়।



--------------------------------


4. Chain Rule ভুলে যাওয়া


যখন function-এর ভিতরে আরেকটি function থাকে,
chain rule প্রয়োজন।



--------------------------------


5. Derivative সবসময় positive ভাবা


Slope negative হতে পারে।
"""


# ===========================================================
# 10_Exercises
# ===========================================================

"""
Practice Problems:


1.

Find:

d/dx(x⁴)


Answer:

4x³



--------------------------------


2.

Find:

d/dx(3x²+2x+1)


Answer:

6x+2



--------------------------------


3.

Find derivative:

f(x)=sin(x)


Answer:

cos(x)



--------------------------------


4.

Find:

d/dx(eˣ)


Answer:

eˣ



--------------------------------


5.

Explain:

Why derivative depends on limit?
"""


# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
Machine Learning এবং AI-তে Derivative:


1. Gradient Descent


Neural Network training-এর মূল বিষয়।


Model:

Prediction

↓

Loss Calculate

↓

Derivative বের করা

↓

Weight Update



Formula:


New Weight

=

Old Weight

-

Learning Rate × Gradient



--------------------------------


2. Backpropagation


Neural Network-এর ভিতরে:

Error backward direction-এ পাঠানো হয়।


Derivative ব্যবহার করে:

কোন weight কতটা পরিবর্তন হবে
তা নির্ধারণ করা হয়।



--------------------------------


3. Optimization


AI model এমন parameter খোঁজে
যেখানে loss minimum।


Derivative বলে:

কোন দিকে গেলে loss কমবে।



--------------------------------


4. Computer Vision


Image processing-এ:

Edge detection

Gradient calculation

সব derivative-এর উপর ভিত্তি করে।



--------------------------------


5. Physics Simulation AI


Motion prediction:

Position

↓

Velocity

↓

Acceleration


সব derivative সম্পর্কিত।



--------------------------------


Summary:


Derivative শেখায়:

"পরিবর্তন কত দ্রুত হচ্ছে"


এটি প্রয়োজন:


✓ Physics
✓ Engineering
✓ Economics
✓ Machine Learning
✓ Deep Learning
✓ Optimization


Derivative ছাড়া আধুনিক AI সম্ভব নয়।
"""


# ===========================================================
# End of Derivative
# ===========================================================