"""
==========================================================
Non-Linear Function (নন-লিনিয়ার ফাংশন)
==========================================================

# 01_Introduction
# 02_WhyThisConceptExistsInRelationToHistory
# 03_RealLifeIntuition
# 04_Definition
# 05_Formula
# 06_Derivation (How the Formula Comes)
# 07_InternalWorking / Visualization
# 08_Examples
# 09_CommonMistakes
# 10_Exercises
# 11_AIUsage (Machine Learning / AI)

==========================================================
01_Introduction
==========================================================

Non-Linear Function হলো এমন Function
যার Graph একটি Straight Line নয়।

Linear Function-এ

Input সমান হারে বাড়লে

Output-ও সমান হারে বাড়ে।

কিন্তু Non-Linear Function-এ

Input পরিবর্তনের সাথে সাথে
Output-এর পরিবর্তনের হারও পরিবর্তিত হয়।

ফলে Graph বাঁকা (Curve) হয়।

==========================================================
02_WhyThisConceptExistsInRelationToHistory
==========================================================

মানুষ প্রথমে ভাবত
বেশিরভাগ সম্পর্কই Linear।

কিন্তু বাস্তবে দেখা গেল—

• বল ছুঁড়লে পথ বাঁকা হয়।
• জনসংখ্যা দ্রুত বৃদ্ধি পায়।
• সুদের টাকা Compound হয়।
• শব্দের তীব্রতা Logarithmic।
• আলো, তাপ, মহাকর্ষ—সবই Linear নয়।

অর্থাৎ

প্রকৃতির অধিকাংশ ঘটনাই
Non-Linear।

এই ধরনের সম্পর্ক প্রকাশ করার জন্য
Non-Linear Function ধারণা এসেছে।

==========================================================
03_RealLifeIntuition
==========================================================

উদাহরণ ১

গাড়ির গতি

তুমি যদি Accelerator ধীরে চাপো,

Speed

0

↓

10

↓

25

↓

45

↓

70

↓

100

প্রতি সেকেন্ডে সমান হারে Speed বাড়ছে না।

এটি Non-Linear।

----------------------------------------------------------

উদাহরণ ২

Population

100

↓

200

↓

400

↓

800

↓

1600

এটি Exponential Growth।

----------------------------------------------------------

উদাহরণ ৩

Ball Throw

বল উপরে উঠবে

↓

থামবে

↓

আবার নিচে নামবে

এটি Quadratic Function।

==========================================================
04_Definition
==========================================================

Non-Linear Function হলো এমন Function

যার Graph

Straight Line নয়।

এবং

Rate of Change

Constant নয়।

==========================================================
05_Formula
==========================================================

Non-Linear Function-এর
একটি নির্দিষ্ট Formula নেই।

কারণ এটি অনেক ধরনের Function-এর সমষ্টি।

উদাহরণ

Quadratic

y=x²

---------------------------------

Cubic

y=x³

---------------------------------

Exponential

y=2^x

---------------------------------

Logarithmic

y=log(x)

---------------------------------

Root

y=√x

---------------------------------

Trigonometric

y=sin(x)

y=cos(x)

==========================================================
06_Derivation (How the Formula Comes)
==========================================================

Linear Function

y=mx+c

এখানে

Slope

সবসময় একই।

ধরো

y=2x

x

1 →2

2→4

3→6

4→8

সবসময়

+2

---------------------------------

এখন

y=x²

1→1

2→4

3→9

4→16

Difference

+3

+5

+7

এখানে Difference পরিবর্তিত হচ্ছে।

অর্থাৎ

Rate of Change

Constant নয়।

এ কারণেই

এটি Non-Linear।

==========================================================
07_InternalWorking / Visualization
==========================================================

Linear

y=x

          /
        /
      /
    /
  /

---------------------------------

Quadratic

y=x²

      ∪

---------------------------------

Exponential

y=2^x

        /
      /
    /
  /
 /

শেষের দিকে
দ্রুত উপরে উঠে যায়।

---------------------------------

Logarithmic

y=log(x)

_____

      \

       \

ধীরে ধীরে বাড়ে।

---------------------------------

Sin Function

~~~~~~

Wave তৈরি করে।

অর্থাৎ

সব Curve-ই

Non-Linear।

==========================================================
08_Examples
==========================================================

Example 1

y=x²

Non-Linear

---------------------------------

Example 2

y=x³

Non-Linear

---------------------------------

Example 3

y=2^x

Non-Linear

---------------------------------

Example 4

y=√x

Non-Linear

---------------------------------

Example 5

y=sin(x)

Non-Linear

==========================================================
09_CommonMistakes
==========================================================

❌ ভুল ১

সব Curve-কে Quadratic ভাবা।

আসলে

Quadratic

Exponential

Logarithmic

Sin

সব আলাদা।

---------------------------------

❌ ভুল ২

x²

এবং

2^x

এক মনে করা।

x²

Quadratic

2^x

Exponential

---------------------------------

❌ ভুল ৩

Graph না দেখে Function বোঝার চেষ্টা করা।

Graph দেখলে
Function-এর ধরন সহজে বোঝা যায়।

==========================================================
10_Exercises
==========================================================

Exercise 1

নিচের কোনগুলো Non-Linear?

1)

y=3x+2

2)

y=x²

3)

y=2^x

4)

y=log(x)

---------------------------------

Exercise 2

Quadratic Function-এর Formula লিখো।

---------------------------------

Exercise 3

Exponential Function-এর Formula লিখো।

---------------------------------

Exercise 4

Logarithmic Function-এর Formula লিখো।

---------------------------------

Exercise 5

নিজের মতো একটি Non-Linear Function লিখো।

==========================================================
11_AIUsage (Machine Learning / AI)
==========================================================

Artificial Intelligence-এর সবচেয়ে গুরুত্বপূর্ণ ধারণাগুলোর
একটি হলো

Non-Linearity।

----------------------------------------------------------

কেন?

ধরো

House Price

শুধু

Area

দিয়ে নির্ধারণ করা যায় না।

কারণ

Location

Bedroom

Age

Road

School

Market

ইত্যাদি অনেক বিষয় একসাথে কাজ করে।

এই সম্পর্ক Linear নয়।

----------------------------------------------------------

Neural Network

প্রথমে

Linear

Calculation করে।

Output

=WX+B

এরপর

Activation Function

ব্যবহার করে।

যেমন

ReLU

f(x)=max(0,x)

---------------------------------

Sigmoid

f(x)=1/(1+e^-x)

---------------------------------

Tanh

---------------------------------

GELU

---------------------------------

Swish

এগুলো সবই

Non-Linear Function।

----------------------------------------------------------

যদি Neural Network-এ

Activation Function

না থাকত,

তাহলে

১০০ Layer

থাকলেও

পুরো Network

একটি মাত্র Linear Function-এ
পরিণত হতো।

ফলে

Image Recognition

Speech Recognition

ChatGPT

Self Driving Car

Medical Diagnosis

কোনোটাই সম্ভব হতো না।

----------------------------------------------------------

Machine Learning-এ

Decision Tree

Random Forest

XGBoost

Deep Learning

সবগুলো Non-Linear Model।

এ কারণেই তারা জটিল Pattern শিখতে পারে।

==========================================================
Summary
==========================================================

✔ Graph Straight Line নয়

✔ Rate of Change পরিবর্তিত হয়

✔ Quadratic

✔ Cubic

✔ Exponential

✔ Logarithmic

✔ Root

✔ Trigonometric

সবই Non-Linear Function

✔ Neural Network-এর শক্তির মূল কারণ হলো
Non-Linearity

✔ Activation Function ছাড়া Deep Learning সম্ভব নয়।

==========================================================
Relationship Between All Functions
==========================================================

                Function
                    │
        ┌───────────┴───────────┐
        │                       │
        ▼                       ▼
 Linear Function         Non-Linear Function
   y = mx + c                 │
                               │
      ┌────────────────────────┼─────────────────────────┐
      │                        │                         │
      ▼                        ▼                         ▼
 Quadratic              Exponential              Logarithmic
  y=x²                     y=a^x                  y=log(x)

      ┌───────────────┬───────────────┬───────────────┐
      ▼               ▼               ▼
    Cubic           Root          Trigonometric
    y=x³            y=√x          sin(x), cos(x)

==========================================================
Final Note
==========================================================

তুমি এখন Function-এর সম্পূর্ণ ভিত্তি শেষ করেছো।

ক্রম অনুযায়ী যা শিখেছো—

✅ Function
    ↓  
✅ Linear Function
    ↓
✅ Quadratic Function
    ↓
✅ Exponential Function
    ↓
✅ Logarithmic Function
    ↓
✅ Non-Linear Function

এখন তুমি সহজেই পরবর্তী অধ্যায়
**Polynomials** শুরু করতে পারবে, কারণ Polynomial
মূলত Linear, Quadratic, Cubic ইত্যাদি Function-এরই
একটি সাধারণ (Generalized) রূপ।
"""