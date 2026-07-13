"""
===========================================================
Limits (সীমা)
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
Limit (সীমা) হলো Calculus-এর সবচেয়ে গুরুত্বপূর্ণ ধারণাগুলোর একটি।

Limit দিয়ে আমরা বুঝতে পারি:

কোনো function-এর input একটি নির্দিষ্ট value-এর কাছে গেলে
output কোন value-এর দিকে এগিয়ে যায়।

সহজ ভাষায়:

"কোনো কিছু ঠিক জায়গায় না পৌঁছেও তার কাছাকাছি গেলে
তার আচরণ কেমন হবে?"

Calculus-এর মূল ভিত্তি:

1. Limit
2. Derivative
3. Integral

Derivative এবং Integral দুটোই Limit-এর উপর নির্ভর করে।
"""


# ===========================================================
# 02_WhyThisConceptExistsInRelationToHistory
# ===========================================================

"""
ইতিহাস:

প্রাচীন গণিতে মানুষ পরিবর্তনের হার এবং অসীম ছোট দূরত্ব
নিয়ে চিন্তা করত।

গ্রিক গণিতবিদরা area এবং motion বের করার জন্য
limit-এর মতো ধারণা ব্যবহার করতেন।

কিন্তু Limit-এর আধুনিক ধারণা আসে:

17th century:

Isaac Newton এবং Gottfried Wilhelm Leibniz
Calculus তৈরি করেন।

তারা বুঝতে পারেন:

যদি কোনো পরিবর্তনকে অসীম ছোট অংশে ভাগ করা যায়,
তাহলে continuous change বোঝা সম্ভব।

Limit এই "অসীম ছোট পরিবর্তন" বোঝার mathematical tool।
"""


# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
বাস্তব জীবনের উদাহরণ:

Example 1:

একটি গাড়ি 100 km/h speed-এ চলছে।

কিন্তু speedometer প্রতি মুহূর্তের exact speed দেখায়।

কিভাবে?

সময়কে খুব ছোট ছোট অংশে ভাগ করে।

যেমন:

1 second
0.1 second
0.001 second

যত ছোট interval হবে,
তত accurate instantaneous speed পাওয়া যাবে।

এই ধারণার পেছনে Limit কাজ করে।


Example 2:

একটি বল মাটির দিকে পড়ছে।

সময়:

1 sec
0.5 sec
0.1 sec
0.01 sec

যখন সময় 2 second-এর কাছে যায়,
বল কত দূরত্ব অতিক্রম করবে?

এটি limit দিয়ে বের করা যায়।
"""


# ===========================================================
# 04_Definition
# ===========================================================

"""
Mathematical Definition:

যখন x একটি নির্দিষ্ট সংখ্যা a-এর দিকে এগিয়ে যায়,
তখন function f(x) যে value-এর দিকে যায়,
তাকে limit বলে।

Notation:

lim x→a f(x) = L


এখানে:

lim  = Limit

x→a  = x approaches a

f(x) = Function

L    = Limit value


অর্থ:

x যখন a-এর খুব কাছাকাছি যাবে,
তখন f(x) এর মান L-এর কাছাকাছি যাবে।
"""


# ===========================================================
# 05_Formula
# ===========================================================

"""
Basic Limit Formula:

lim(x→a) f(x) = L


Example:

lim(x→2) x²


এখানে:

x = 2 এর দিকে যাচ্ছে

তাই:

2² = 4


Answer:

lim(x→2) x² = 4


---------------------------------

Important Limit Laws:

1. Constant Rule:

lim(x→a) c = c


Example:

lim(x→5) 10 = 10



2. Identity Rule:

lim(x→a) x = a



3. Addition Rule:

lim(x→a)(f(x)+g(x))

=

lim f(x) + lim g(x)



4. Multiplication Rule:

lim(f(x)g(x))

=

lim f(x) × lim g(x)



5. Division Rule:

lim(f(x)/g(x))

=

lim f(x) / lim g(x)

যদি denominator zero না হয়।
"""


# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
Limit থেকে Formula:

ধরি:

f(x)=x²


আমরা বের করবো:

lim(x→3)x²


x এর কাছাকাছি value নেই:

x = 2.9

f(x)=2.9²=8.41


x = 2.99

f(x)=2.99²=8.9401


x = 2.999

f(x)=2.999²=8.994001


দেখা যাচ্ছে:

x যত 3-এর কাছে যাচ্ছে,

f(x) তত 9-এর কাছে যাচ্ছে।


তাই:

lim(x→3)x² = 9


Limit মূলত approximation-এর ধারণা থেকে এসেছে।
"""


# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
Function:

f(x)=x²


Graph:

        |
    9   |          *
        |
    4   |     *
        |
    1   | *
        |
--------|----------------
        0  1  2  3


যখন x → 3

তখন graph-এর point

(3,9)

এর দিকে এগিয়ে যায়।


Computer ভিতরে:

1. একটি input value নেয়
2. target value-এর কাছাকাছি যায়
3. function calculate করে
4. output pattern observe করে


Example:

x:

3.1
3.01
3.001
3.0001


Output:

9.61
9.0601
9.006001
9.00060001


Output → 9
"""


# ===========================================================
# 08_Examples
# ===========================================================

"""
Example 1:

Find:

lim(x→4) x+5


Solution:

= 4+5

= 9


--------------------------------


Example 2:

Find:

lim(x→2) x²+3x


Solution:

= 2² + 3(2)

= 4+6

=10


--------------------------------


Example 3:

Find:

lim(x→0) sin(x)/x


Important:

Direct substitution দিলে:

0/0

যা undefined


কিন্তু limit:

lim(x→0) sin(x)/x = 1


এটি Calculus-এর গুরুত্বপূর্ণ limit।
"""


# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
Common Mistakes:

1. Limit এবং function value একই মনে করা

Example:

lim(x→2)(x²-4)/(x-2)

Direct substitution:

0/0

কিন্তু limit exist করতে পারে।


--------------------------------


2. Left hand এবং Right hand limit না দেখা


Left:

x → a-


Right:

x → a+


দুটো equal না হলে limit exist করে না।



3. Division rule ভুল ব্যবহার করা

যদি denominator limit = 0 হয়,
তাহলে সরাসরি ভাগ করা যাবে না।



4. Limit মানে exact পৌঁছানো ভাবা

Limit হলো কাছে যাওয়া,
সবসময় পৌঁছানো নয়।
"""


# ===========================================================
# 10_Exercises
# ===========================================================

"""
Practice Problems:

1.

Find:

lim(x→5) x²


Answer:

25



2.

Find:

lim(x→3)(2x+4)


Answer:

10



3.

Find:

lim(x→1)(x³+x²+x)


Answer:

3



4.

Find:

lim(x→0) sin(x)/x


Answer:

1



5.

Explain:

Why limit is important in derivative?
"""


# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
Machine Learning এবং AI-তে Limit-এর ব্যবহার:


1. Gradient Descent

Neural Network training-এর সময়:

Loss function কমানোর জন্য
parameter update করা হয়।

Formula:

θ = θ - α∇J(θ)


এখানে:

gradient বের করতে derivative লাগে।

Derivative-এর ভিত্তি হলো Limit।



--------------------------------


2. Optimization

AI model এমন parameter খোঁজে
যেখানে error minimum হয়।

Continuous optimization-এ
limit গুরুত্বপূর্ণ।



--------------------------------


3. Probability

Machine Learning-এ:

sample সংখ্যা বাড়লে
probability distribution কেমন হবে

এটি limit দিয়ে বোঝানো হয়।



--------------------------------


4. Deep Learning

Neural network:

Input → Hidden Layer → Output


প্রতিটি weight update:

ছোট ছোট পরিবর্তনের মাধ্যমে হয়।

এই continuous change বোঝার জন্য
Limit প্রয়োজন।



--------------------------------


Summary:

Limit হলো Calculus-এর foundation।

Limit বুঝলে:

✓ Derivative বোঝা সহজ হয়
✓ Integral বোঝা সহজ হয়
✓ Optimization বোঝা সহজ হয়
✓ Machine Learning mathematics পরিষ্কার হয়
"""


# ===========================================================
# End of Limits
# ===========================================================