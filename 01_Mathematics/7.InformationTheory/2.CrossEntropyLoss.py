# Cross Entropy Loss -জন্ম: Machine Learning শুরু হওয়ার পরে বিজ্ঞানীরা নতুন সমস্যায় পড়লেন। ধরো, Cat vs Dog Classifier: Actual: Cat; Model বলছে Cat = 0.60, Dog = 0.40 আরেকটি Model: Cat = 0.99, Dog = 0.01; দুটোই Cat বলছে। কিন্তু দ্বিতীয়টি অনেক ভালো। কীভাবে সেটা Measure করব? এভাবেই Cross Entropy Loss-এর জন্ম। ধারণা: Cross Entropy মাপে Prediction এবং Reality-এর মধ্যে দূরত্ব। যত কম -> তত ভালো। Example: Actual: Cat; Prediction: [0.99,0.01] Loss -> খুব কম। Prediction: [0.51,0.49] Loss -> বেশি।

# Formula: Loss = −∑ylog(y^)

import math
prediction = 0.9
loss = -math.log(prediction)
print(loss)

# Prediction খারাপ:
prediction = 0.1
loss = -math.log(prediction)
print(loss)
# Loss -> অনেক বড়।

# ML Relation: সবচেয়ে বেশি ব্যবহৃত Loss; # Logistic Regression, # CNN, # BERT, # GPT, # Image Classification, # NLP

# ===========================================================
# 01_Introduction
# ===========================================================
"""
Machine Learning-এ Model কতটা ভুল Prediction করছে, তা পরিমাপ করার জন্য একটি Loss Function ব্যবহার করা হয়। Classification সমস্যার জন্য সবচেয়ে জনপ্রিয় Loss Function হলো Cross Entropy Loss। এটি বলে দেয় "Model-এর Predict করা Probability এবং বাস্তব (True) Probability-এর মধ্যে পার্থক্য কত?" Prediction যত সঠিক হবে Cross Entropy Loss তত কম হবে। Prediction যত ভুল হবে Loss তত বেশি হবে।
"""
# ===========================================================
# 02_WhyThisConceptExistsInRealtionTohistory
# ===========================================================
"""
Cross Entropy এসেছে Information Theory থেকে। Claude Shannon Entropy-এর মাধ্যমে তথ্যের অনিশ্চয়তা (Uncertainty) পরিমাপ করেন।
পরবর্তীতে গবেষকরা প্রশ্ন করেন— যদি বাস্তব Probability একরকম হয়, কিন্তু Model অন্যরকম Probability অনুমান করে, তাহলে অতিরিক্ত কত তথ্য (Extra Information) লাগবে? এই অতিরিক্ত তথ্য পরিমাপ করার জন্য Cross Entropy তৈরি হয়। Machine Learning-এ পরে এটিই Classification-এর প্রধান Loss Function হয়ে যায়।
"""
# ===========================================================
# 03_RealLifeIntuition
# ===========================================================
"""
ধরো তুমি একটি পরীক্ষার ফলাফল অনুমান করছ। বাস্তব ফলাফল Pass তুমি Prediction দিলে Pass = 99%, Fail = 1% এটি খুব ভালো Prediction। Loss খুব কম।
--------------------------------------
এখন ধরো, বাস্তব ফলাফল Pass; কিন্তু Prediction দিলে Pass = 5%; Fail = 95% এটি খুব খারাপ Prediction। Loss অনেক বেশি। Cross Entropy ঠিক এই ভুলের পরিমাণ সংখ্যা দিয়ে প্রকাশ করে।
"""

# ===========================================================
# 04_Definition
# ===========================================================

"""
Cross Entropy হলো

বাস্তব Probability Distribution
এবং

Model-এর Predict করা Probability Distribution

এর মধ্যে পার্থক্যের পরিমাপ।

অর্থাৎ

Prediction যত বাস্তবের কাছাকাছি হবে

Loss তত কম হবে।

Prediction যত দূরে হবে

Loss তত বেশি হবে।

Machine Learning-এর লক্ষ্য

Cross Entropy Loss যত সম্ভব কমানো।
"""

# ===========================================================
# 05_Formula
# ===========================================================

"""
সাধারণ Formula

H(P,Q)

=

- Σ P(x) log₂(Q(x))


যেখানে

P(x)

=

True Probability

Q(x)

=

Predicted Probability


--------------------------------------

Binary Cross Entropy

L

=

-(

y log(p)

+

(1-y) log(1-p)

)


যেখানে

y

=

True Label

(0 অথবা 1)

p

=

Model-এর Predict করা Probability


--------------------------------------

Multi-Class Cross Entropy

L

=

- Σ yi log(pi)

যেখানে

yi

=

One-Hot Label

pi

=

Predicted Probability
"""

# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
আমরা জানি

একটি ঘটনার Information

I(x)

=

-log(P(x))

এখন

বাস্তব Distribution

P

কিন্তু Model বিশ্বাস করছে

Q

তাহলে Average Information হবে

Σ P(x)

×

(-log(Q(x)))

=

-Σ P(x)log(Q(x))

এটিই Cross Entropy।

--------------------------------------

Binary Classification-এর ক্ষেত্রে

শুধু দুটি Class থাকে।

Positive

Negative

যদি

y=1

তাহলে

Loss

=

-log(p)

আর যদি

y=0

তাহলে

Loss

=

-log(1-p)

দুইটি একত্র করলে

L

=

-(

y log(p)

+

(1-y)log(1-p)

)
"""

# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
বাস্তব Label

Cat


Model Prediction

Cat : 0.95

Dog : 0.03

Bird : 0.02

Loss

↓

খুব কম


--------------------------------------

আরেকটি ক্ষেত্রে

Cat : 0.05

Dog : 0.90

Bird : 0.05

বাস্তব উত্তর

Cat

Loss

↓

অনেক বেশি


Cross Entropy
Prediction ভুল হলে
দ্রুত বড় হয়ে যায়।

এ কারণেই এটি Model-কে
সঠিক Probability শেখায়।
"""

# ===========================================================
# 08_Examples
# ===========================================================

"""
উদাহরণ ১

True Label

1

Prediction

0.99

Loss

=

-log(0.99)

≈

0.01

অর্থাৎ খুব ভালো Prediction।


--------------------------------------

উদাহরণ ২

True Label

1

Prediction

0.50

Loss

=

-log(0.50)

≈

0.693

Loss বেড়েছে।


--------------------------------------

উদাহরণ ৩

True Label

1

Prediction

0.01

Loss

=

-log(0.01)

≈

4.605

খুব বড় Loss।

কারণ Prediction সম্পূর্ণ ভুল।
"""

# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
❌ ভুল ১

Cross Entropy শুধুই Binary Classification-এর জন্য।

ভুল।

এটি Multi-Class Classification-এও ব্যবহৃত হয়।

--------------------------------------

❌ ভুল ২

Prediction Label দিলেই হবে।

ভুল।

Cross Entropy Probability ব্যবহার করে,
শুধু Class Label নয়।

--------------------------------------

❌ ভুল ৩

Loss Negative হতে পারে।

ভুল।

Cross Entropy Loss কখনো Negative হয় না।

Minimum

=

0

--------------------------------------

❌ ভুল ৪

Cross Entropy এবং Entropy একই জিনিস।

না।

Entropy

=

একটি Distribution-এর অনিশ্চয়তা।

Cross Entropy

=

দুটি Distribution-এর পার্থক্য।
"""

# ===========================================================
# 10_Exercises
# ===========================================================

"""
১।

True Label

1

Prediction

0.9

Loss বের কর।

--------------------------------------

২।

Prediction

0.2

True Label

1

Loss হিসাব কর।

--------------------------------------

৩।

কোন Prediction-এর Loss কম?

(A)

0.95

(B)

0.60

--------------------------------------

৪।

Cross Entropy কেন Mean Squared Error-এর
চেয়ে Classification-এ বেশি ব্যবহৃত হয়?

--------------------------------------

৫।

Binary Cross Entropy Formula নিজে
Derive করার চেষ্টা কর।
"""

# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
Cross Entropy Loss আধুনিক AI-এর অন্যতম
সবচেয়ে গুরুত্বপূর্ণ Loss Function।

১।

Logistic Regression

Binary Classification-এর জন্য
Binary Cross Entropy ব্যবহার করে।

--------------------------------------

২।

Neural Network

শেষ Layer-এর Prediction
Cross Entropy দিয়ে Evaluate করা হয়।

--------------------------------------

৩।

CNN (Convolutional Neural Network)

Image Classification-এ
Cross Entropy সবচেয়ে বেশি ব্যবহৃত হয়।

--------------------------------------

৪।

Transformer

প্রতিটি Token Prediction-এর জন্য
Cross Entropy Loss ব্যবহার করা হয়।

--------------------------------------

৫।

Large Language Model (LLM)

যেমন

GPT

LLaMA

Gemini

Claude

সবগুলোই

Next Token Prediction-এর সময়
Cross Entropy Loss কমানোর চেষ্টা করে।

--------------------------------------

৬।

Speech Recognition

সঠিক শব্দ Predict করার জন্য
Cross Entropy ব্যবহার করা হয়।

--------------------------------------

৭।

Natural Language Processing

Sentiment Analysis

Spam Detection

Text Classification

সব ক্ষেত্রেই
Cross Entropy একটি Standard Loss Function।

--------------------------------------

৮।

Training Process

Input

↓

Neural Network

↓

Predicted Probability

↓

Cross Entropy Loss

↓

Backpropagation

↓

Gradient Descent

↓

Weights Update

↓

Better Prediction

এই পুরো Learning Process-এর কেন্দ্রবিন্দুতে
Cross Entropy Loss কাজ করে।
"""