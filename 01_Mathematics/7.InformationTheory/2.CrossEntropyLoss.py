# Cross Entropy Loss -জন্ম: Machine Learning শুরু হওয়ার পরে বিজ্ঞানীরা নতুন সমস্যায় পড়লেন।

# ধরো, Cat vs Dog Classifier:

# Actual: Cat
# Model বলছে Cat = 0.60, Dog = 0.40
# আরেকটি Model: Cat = 0.99, Dog = 0.01

# দুটোই Cat বলছে। কিন্তু দ্বিতীয়টি অনেক ভালো। কীভাবে সেটা Measure করব? এভাবেই Cross Entropy Loss-এর জন্ম।

# ধারণা: Cross Entropy মাপে Prediction এবং Reality-এর মধ্যে দূরত্ব। যত কম -> তত ভালো।

# Example: Actual: Cat

# Prediction: [0.99,0.01] Loss -> খুব কম।
# Prediction: [0.51,0.49] Loss -> বেশি।
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

# ML Relation: সবচেয়ে বেশি ব্যবহৃত Loss

# Logistic Regression
# CNN
# BERT
# GPT
# Image Classification
# NLP