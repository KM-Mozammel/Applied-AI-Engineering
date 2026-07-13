"""
==========================================================
Function (ফাংশন)
==========================================================

# 01_Introduction
# 02_WhyThisConceptExistsInRelationToHistory
# 03_RealLifeIntuition
# 04_Definition
# 05_Formula
# 06_Derivation (How the formula comes)
# 07_InternalWorking / Visualization
# 08_Examples
# 09_CommonMistakes
# 10_Exercises
# 11_AIUsage (Machine Learning / AI)

==========================================================
01_Introduction
==========================================================

গণিতে Function হলো এমন একটি নিয়ম (Rule) যা একটি Input গ্রহণ করে
এবং সেই Input-এর জন্য ঠিক একটি Output প্রদান করে।

অর্থাৎ,

Input  ----->  Function Rule  -----> Output

Function হলো Mathematics-এর সবচেয়ে গুরুত্বপূর্ণ ধারণাগুলোর একটি।
Algebra, Calculus, Statistics, Machine Learning, Artificial Intelligence
— সবকিছুর ভিত্তি Function।

==========================================================
02_WhyThisConceptExistsInRelationToHistory
==========================================================

প্রাচীন মানুষ বিভিন্ন জিনিসের মধ্যে সম্পর্ক (Relationship) খুঁজে বের করার
চেষ্টা করত।

উদাহরণ:

• সময় বাড়লে সূর্যের অবস্থান বদলায়।
• বয়স বাড়লে উচ্চতা পরিবর্তন হয়।
• টাকা বেশি হলে পণ্য বেশি কেনা যায়।
• দূরত্ব বাড়লে ভ্রমণের সময় বাড়ে।

তারা বুঝতে পারল—

একটি Quantity পরিবর্তন হলে আরেকটি Quantity-ও পরিবর্তিত হয়।

এই সম্পর্কগুলো প্রকাশ করার জন্যই Function ধারণার জন্ম।

পরে René Descartes Coordinate Plane আবিষ্কার করেন।
এরপর Leonhard Euler f(x) notation জনপ্রিয় করেন।

আজকে Physics, Engineering, Economics, Computer Science,
AI—সব জায়গায় Function ব্যবহার করা হয়।

==========================================================
03_RealLifeIntuition
==========================================================

ধরো একটি Juice Machine আছে।

তুমি Machine-এ একটি Orange দিলে,

Orange ------> Juice Machine ------> Orange Juice

Apple দিলে,

Apple ------> Juice Machine ------> Apple Juice

Machine একই Rule অনুসরণ করছে।

ঠিক তেমনি Function-ও একটি Rule।

Input পরিবর্তন হলে Output পরিবর্তিত হয়।

আরেকটি উদাহরণ—

Vending Machine

১০ টাকা দিলে একটি Chocolate

২০ টাকা দিলে দুটি Chocolate

Input = টাকা
Output = Chocolate

==========================================================
04_Definition
==========================================================

Function হলো এমন একটি Rule যেখানে

প্রতিটি Input-এর জন্য
ঠিক একটি Output থাকবে।

Mathematically,

For every x
there exists exactly one y.

একটি Input কখনো দুইটি ভিন্ন Output দিতে পারবে না।

==========================================================
05_Formula
==========================================================

Function সাধারণত লেখা হয়

f(x)

এখানে

f = Function-এর নাম

x = Input

আর Output লেখা হয়

y = f(x)

উদাহরণ

f(x) = 2x + 3

যদি

x = 5

তাহলে

f(5)

= 2(5)+3

=13

==========================================================
06_Derivation (How the Formula Comes)
==========================================================

ধরো তুমি এমন একটি Rule বানাতে চাও—

Input যত হবে,
Output হবে তার দ্বিগুণের সাথে ৩ যোগ।

Input = x

দ্বিগুণ

2x

তারপর ৩ যোগ

2x + 3

এটাই Function

f(x)=2x+3

অর্থাৎ Function Formula আসলে
বাস্তব জীবনের কোনো Rule-কে Mathematical আকারে প্রকাশ করে।

==========================================================
07_InternalWorking / Visualization
==========================================================

Function ভিতরে কী ঘটে?

            Input
              │
              ▼
      +----------------+
      |   Function     |
      |   Rule Apply   |
      +----------------+
              │
              ▼
            Output

উদাহরণ

f(x)=2x+3

Input

5

Step 1

5 × 2

=10

Step 2

10+3

=13

Output

13

আরও উদাহরণ

          x
          │
          ▼
      +----------+
      | ×2 + 3   |
      +----------+
          │
          ▼
         y

==========================================================
08_Examples
==========================================================

Example 1

f(x)=x+5

x=3

f(3)=8

----------------------

Example 2

f(x)=x²

x=4

f(4)=16

----------------------

Example 3

f(x)=10x

x=7

f(7)=70

----------------------

Example 4

f(x)=100-x

x=40

f(40)=60

==========================================================
09_CommonMistakes
==========================================================

❌ ভুল ১

f(x)=2x+3

x=5

অনেকে লেখে

2x+3=8

সঠিক হবে

2(5)+3=13

----------------------

❌ ভুল ২

Function notation বুঝতে না পারা

f(5)

মানে

f × 5

না।

এটি Function-এর মধ্যে 5 পাঠানো বোঝায়।

----------------------

❌ ভুল ৩

একটি Input-এর জন্য দুইটি Output দেওয়া।

এটি Function নয়।

==========================================================
10_Exercises
==========================================================

Exercise 1

f(x)=3x+2

x=4

Output কত?

----------------------

Exercise 2

f(x)=x²

x=8

Output কত?

----------------------

Exercise 3

f(x)=5x−7

x=10

Output কত?

----------------------

Exercise 4

নিজে একটি Function তৈরি করো
যেখানে Input-এর তিনগুণের সাথে ১০ যোগ হবে।

----------------------

Exercise 5

f(x)=100−2x

x=25

Output কত?

==========================================================
11_AIUsage (Machine Learning / AI)
==========================================================

Artificial Intelligence সম্পূর্ণ Function-এর উপর ভিত্তি করে।

উদাহরণ

Input (Image)

↓

Neural Network (Function)

↓

Output (Cat)

অর্থাৎ

Image

↓

f(x)

↓

Prediction

Machine Learning-এ

Linear Function

Quadratic Function

Polynomial Function

Exponential Function

Sigmoid Function

ReLU Function

Softmax Function

সবই বিভিন্ন ধরনের Function।

Neural Network আসলে লক্ষ লক্ষ Function-এর সমন্বয়।

যখন AI শেখে,

তখন মূলত Function-এর Parameters পরিবর্তন করে
যাতে Output আরও সঠিক হয়।

এই কারণেই Function শেখা Algebra-এর সবচেয়ে গুরুত্বপূর্ণ অধ্যায়গুলোর একটি।

==========================================================
Summary
==========================================================

✔ Function একটি Rule

✔ একটি Input-এর জন্য ঠিক একটি Output

✔ f(x) হলো Function notation

✔ Function বাস্তব জীবনের Relationship প্রকাশ করে

✔ AI এবং Machine Learning সম্পূর্ণ Function-এর উপর ভিত্তি করে।
"""