# KL Divergence -জন্ম: Cross Entropy তৈরি হওয়ার পরে বিজ্ঞানীরা নতুন প্রশ্ন করলেন। ধরো দুটি Probability Distribution আছে। একটি বাস্তব পৃথিবী। আরেকটি Machine-এর Prediction। দুটো কতটা আলাদা? এখান থেকেই KL Divergence.

# ধারণা: KL Divergence মাপে দুটি Distribution-এর Distance।

# Example: Real Cat = 90% | Dog = 10% 
# Prediction: Cat = 88% | Dog = 12%

# KL -> ছোট। 

# আরেকটি Prediction: Cat = 20%, Dog = 80%; KL -> অনেক বড়।

# Formula: DKL(P∣∣Q) = ∑P(x)log P(x)/Q(x)

import numpy as np

P = np.array([0.9,0.1])

Q = np.array([0.8,0.2])

kl = np.sum(P*np.log(P/Q))

print(kl)

# ML Relation: KL Divergence ব্যবহার হয়

# Variational Autoencoder (VAE)
# Reinforcement Learning
# Knowledge Distillation
# Diffusion Models
# Large Language Models


"""
===========================================================
KL Divergence (Kullback-Leibler Divergence)
Information Theory
===========================================================

Structure:
01_Introduction
02_WhyThisConceptExistsInRealtionTohistory
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
Information Theory-তে শুধুমাত্র একটি Probability Distribution-এর
অনিশ্চয়তা (Entropy) জানলেই সবসময় যথেষ্ট হয় না।

অনেক সময় আমাদের দুটি Probability Distribution
একই রকম নাকি ভিন্ন, তা জানতে হয়।

ঠিক এই পার্থক্য পরিমাপ করার জন্য
KL Divergence (Kullback-Leibler Divergence) ব্যবহার করা হয়।

এটি বলে দেয়—

"বাস্তব Probability Distribution থেকে
Model-এর Probability Distribution
কতটা দূরে রয়েছে।"

Machine Learning-এ এটি অত্যন্ত গুরুত্বপূর্ণ,
কারণ Model-এর Prediction বাস্তব Distribution-এর
কাছাকাছি আনাই মূল লক্ষ্য।
"""

# ===========================================================
# 02_WhyThisConceptExistsInRealtionTohistory
# ===========================================================

"""
১৯৫১ সালে Solomon Kullback এবং Richard Leibler
এই ধারণাটি প্রকাশ করেন।

তাদের উদ্দেশ্য ছিল—

যদি দুটি Probability Distribution থাকে,

একটি বাস্তব (True Distribution)

এবং

একটি অনুমানকৃত (Estimated Distribution),

তাহলে

একটি Distribution দিয়ে অন্যটিকে প্রকাশ করলে
কত অতিরিক্ত Information লাগবে?

এই অতিরিক্ত তথ্যের পরিমাণই
KL Divergence।

বর্তমানে এটি

Machine Learning

Statistics

Bayesian Inference

Information Theory

Deep Learning

সহ অসংখ্য ক্ষেত্রে ব্যবহৃত হয়।
"""

# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
ধরো একজন আবহাওয়াবিদ বললেন—

আগামীকাল বৃষ্টি হওয়ার সম্ভাবনা

90%

কিন্তু বাস্তবে

Probability

50%

অর্থাৎ Prediction বাস্তবতা থেকে
অনেক দূরে।

KL Divergence হবে বড়।

--------------------------------------

আরেকটি ক্ষেত্রে

Prediction

51%

বাস্তব

50%

দুটি প্রায় একই।

KL Divergence হবে খুব ছোট।

অর্থাৎ

দুটি Distribution যত কাছাকাছি,

KL Divergence তত কম।
"""

# ===========================================================
# 04_Definition
# ===========================================================

"""
KL Divergence হলো

একটি Probability Distribution

P

থেকে

আরেকটি Probability Distribution

Q

কতটা ভিন্ন,

তার পরিমাপ।

এটি Distance-এর মতো মনে হলেও
আসলে এটি প্রকৃত Distance নয়।

কারণ

KL(P||Q)

≠

KL(Q||P)

অর্থাৎ

এটি Symmetric নয়।

KL Divergence-এর মান

সবসময়

0 অথবা তার বেশি।

0 মানে

দুটি Distribution সম্পূর্ণ একই।
"""

# ===========================================================
# 05_Formula
# ===========================================================

"""
Discrete KL Divergence

              P(x)
D(P||Q)=Σ P(x) log₂(------)
              Q(x)

যেখানে

P(x)

=

True Probability

Q(x)

=

Predicted Probability

--------------------------------------

Continuous Version

∞
∫ P(x) log(P(x)/Q(x)) dx

--------------------------------------

Relationship

Cross Entropy

=

Entropy

+

KL Divergence

অর্থাৎ

H(P,Q)

=

H(P)

+

D(P||Q)
"""

# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
আমরা জানি

Entropy

H(P)

=

-ΣP(x)log(P(x))

এবং

Cross Entropy

H(P,Q)

=

-ΣP(x)log(Q(x))

এখন

Cross Entropy

-

Entropy

=

-ΣP(x)log(Q)

+

ΣP(x)log(P)

=

ΣP(x)

(

log(P)

-

log(Q)

)

Log-এর নিয়ম অনুযায়ী

log(a)-log(b)

=

log(a/b)

অতএব

KL

=

ΣP(x)

log(P/Q)

এটাই

KL Divergence-এর Formula।

অর্থাৎ

Cross Entropy-এর অতিরিক্ত অংশই
KL Divergence।
"""

# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
বাস্তব Distribution

P

Cat

0.80

Dog

0.20


Model Distribution

Q

Cat

0.78

Dog

0.22

দুটি প্রায় একই।

KL খুব ছোট।

--------------------------------------

আরেকটি ক্ষেত্রে

P

Cat

0.80

Dog

0.20


Q

Cat

0.10

Dog

0.90

Prediction সম্পূর্ণ আলাদা।

KL অনেক বড়।

অর্থাৎ

Distribution যত আলাদা হবে,

KL তত বাড়বে।
"""

# ===========================================================
# 08_Examples
# ===========================================================

"""
উদাহরণ ১

P

0.5

0.5

Q

0.5

0.5

KL

=

0

কারণ

দুটি একই।

--------------------------------------

উদাহরণ ২

P

0.9

0.1

Q

0.8

0.2

KL

=

খুব ছোট

কারণ

দুটি কাছাকাছি।

--------------------------------------

উদাহরণ ৩

P

0.9

0.1

Q

0.1

0.9

KL

=

অনেক বড়

কারণ

Prediction বাস্তবতা থেকে
অনেক দূরে।
"""

# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
❌ ভুল ১

KL Divergence একটি Distance।

ভুল।

এটি Distance Metric নয়।

--------------------------------------

❌ ভুল ২

KL(P||Q)

=

KL(Q||P)

ভুল।

KL Symmetric নয়।

--------------------------------------

❌ ভুল ৩

KL Negative হতে পারে।

ভুল।

KL সবসময়

≥ 0

--------------------------------------

❌ ভুল ৪

KL = Cross Entropy

ভুল।

Cross Entropy

=

Entropy

+

KL Divergence

--------------------------------------

❌ ভুল ৫

KL যত বড় তত ভালো।

ভুল।

Machine Learning-এ

KL যত কম,

Prediction তত ভালো।
"""

# ===========================================================
# 10_Exercises
# ===========================================================

"""
১।

KL Divergence কী?

নিজের ভাষায় ব্যাখ্যা কর।

--------------------------------------

২।

কখন

KL = 0

হয়?

--------------------------------------

৩।

কেন

KL(P||Q)

এবং

KL(Q||P)

সমান নয়?

--------------------------------------

৪।

Cross Entropy এবং KL Divergence-এর
সম্পর্ক লিখ।

--------------------------------------

৫।

কেন Machine Learning-এ
KL কমানো গুরুত্বপূর্ণ?
"""

# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
KL Divergence আধুনিক AI-এর অন্যতম
গুরুত্বপূর্ণ ধারণা।

১।

Variational Autoencoder (VAE)

Encoder-এর Learned Distribution-কে

Standard Normal Distribution-এর
কাছাকাছি রাখতে

KL Divergence ব্যবহার করা হয়।

--------------------------------------

২।

Knowledge Distillation

Teacher Model

↓

Student Model

Teacher-এর Probability Distribution
অনুসরণ করতে

KL Loss ব্যবহার করা হয়।

--------------------------------------

৩।

Large Language Model (LLM)

Fine-Tuning-এর সময়

নতুন Model যেন
মূল Model থেকে
অতিরিক্ত বিচ্যুত না হয়,

সেজন্য KL Penalty ব্যবহার করা হয়।

--------------------------------------

৪।

Reinforcement Learning

PPO (Proximal Policy Optimization)

নতুন Policy

এবং

পুরনো Policy

এর পার্থক্য সীমিত রাখতে
KL Divergence ব্যবহৃত হয়।

--------------------------------------

৫।

Bayesian Machine Learning

Posterior Distribution

এবং

Prior Distribution

এর পার্থক্য মাপতে
KL ব্যবহার করা হয়।

--------------------------------------

৬।

Generative AI

Diffusion Model

VAE

Normalizing Flow

সবগুলোতেই KL গুরুত্বপূর্ণ ভূমিকা পালন করে।

--------------------------------------

৭।

Anomaly Detection

যদি কোনো নতুন Data-এর Distribution
স্বাভাবিক Distribution থেকে
অনেক আলাদা হয়,

তাহলে KL Divergence বেশি হবে,

এবং সেটিকে
Anomaly হিসেবে শনাক্ত করা যেতে পারে।
"""