# region Series Basic
# Pandas Series: প্রথমে একটা প্রশ্ন,তুমি Python-এ List জানো। numbers = [10, 20, 30, 40]

# এখন প্রশ্ন—এটার মধ্যে কি আছে?: 
# 0 → 10, 1 → 20, 2 → 30, 3 → 40 মানে প্রত্যেকটি ভ্যালুর একটি Position (Index) আছে।

# Pandas Series আসলে কী? Series = Supercharged List অথবা Series হলো Index সহ একটি একমাত্রিক (1D) Data Structure। ভাবো এটা এমন—

# Python List: 10 20 30 40

# কিন্তু Series,
# Index      Value
# 0  ------> 10
# 1  ------> 20
# 2  ------> 30
# 3  ------> 40
# অর্থাৎ, প্রতিটি Value-এর সাথে Index থাকে।

# কেন Pandas নিজের List বানালো? কারণ AI/ML-এ আমরা শুধু ৪টা সংখ্যা নিয়ে কাজ করি না। আমরা কাজ করি, ১ কোটি মানুষের বয়স - ৫০ লাখ ছবির নাম - ১০ লাখ Sensor Data = Stock Price - Temperature - Text. Python List এত বড় ডেটার জন্য তৈরি নয়। তাই Pandas Series এসেছে।

import pandas as pd
ages = pd.Series([20, 25, 30, 35])
print(ages)

# Output:
# 0    20
# 1    25
# 2    30
# 3    35
# dtype: int64

# এখন Output দেখে ভয় পেও না। এটা ভেঙে দেখি। 
# 0    20 মানে Index = 0 | Value = 20
# 1    25 মানে Index = 1 Value = 25
# শেষের লাইন dtype: int64 মানে Series-এর Data Type হলো Integer (64 bit)
# Visual:
# ages

#       +----------------+
# 0 --->| 20             |
# 1 --->| 25             |
# 2 --->| 30             |
# 3 --->| 35             |
#       +----------------+

# Value Access
import pandas as pd
ages = pd.Series([20,25,30,35])
print(ages[0])
print(ages.values)

# Index Access
print(ages.index)

# Length:
print(len(ages))

# Custom Index
ages = pd.Series(
    [20, 24, 30],
    index=["Rahim", "karim", "Sakib"]
)

print(ages)
print(ages["karim"])

# Dictionary - to - Series
student = {
    "Rahim":20,
    "Karim":22,
    "Sakib":24
}

ages = pd.Series(student)
print("Dictionaly to Series", ages)
# Dictionary-এর Key হয়ে গেল Index, আর Value হয়ে গেল Series-এর Value।

# endregion

# region Operations

# Series-এর সবচেয়ে বড় সুবিধা হল একসাথে সব Value-এর উপর Operation করা যায়। ধরো তোমার কাছে ৫ জন ছাত্রের নম্বর আছে। প্রতিটি নম্বরের সাথে ৫ যোগ করো Python List হলে,

# ADD
marks = [50, 60, 70, 80, 90]
new = []

for i in marks:
    new.append(i + 5)
    
# Loop লাগল। কিন্তু Series marks + 5 দেখো। এক লাইনে পুরো কাজ।

import pandas as pd
marks = pd.Series([50, 60, 70, 80, 90])
print("Addition on series marks+5: ", marks + 5)

# কেন এমন হলো? মনে করো 50 60 70 80 90 Pandas ভেতরে ভেতরে করছে 50 + 5 60 + 5 70 + 5 80 + 5 90 + 5 তোমাকে Loop লিখতে হচ্ছে না।

# MULTIPLICATION
print("Multiplication on marks * 2: ", marks * 2)
# output: 100 120 140 160 180

#POWERE
print("Power: marks ** 2", marks ** 2)
# output: 2500 3600 4900 6400 8100

#দুইটি Series যোগঃ 
math = pd.Series([80,90,70])
english = pd.Series([10,5,20])
total = math + english
print("Adding 2 Series: ", total)
# output:
# 0    90
# 1    95
# 2    90

# ভেতরে কী হলো? 80+10 90+5 70+20

# যদি Index আলাদা হয়?

s1 = pd.Series(
    [10,20],
    index=["Rahim","Karim"]
)

s2 = pd.Series(
    [30,40],
    index=["Karim","Rahim"]
)

print(s1+s2)

# Output:
# Karim    50
# Rahim    50

# খেয়াল করো। Pandas Position দেখে যোগ করেনি। নাম দেখে যোগ করেছে। এটাই Series-এর অসাধারণ শক্তি।

# Visual:
# Rahim -----> 10
# Karim -----> 20
#       +
# Karim -----> 30
# Rahim -----> 40
#       ↓
# Rahim -----> 50
# Karim -----> 50

# এজন্য Data Analysis এত সহজ হয়।

#endregion

# region Filtering

# আমি শুধু ৬০-এর বেশি নম্বর চাই। এটাকে বলে Boolean Mask।
marks = pd.Series([40,55,70,85,95])
print(marks > 60)

# Output:
# 0    False
# 1    False
# 2    True
# 3    True
# 4    True

# Get Only true value
print(marks[marks > 60])
# Output:
# 2    70
# 3    85
# 4    95
# AI-তে এটা প্রতিদিন ব্যবহার হবে।
# salary[salary > 50000]
# age[age >= 18]
# probability[probability > 0.90]

# একাধিক condition
print(marks[(marks>50) & (marks<90)])
# Output: 55 70 85

# OR Condition
print(marks[(marks<50) | (marks>90)])


# endregion

# region Missing Value
# Missing Value বাস্তব Dataset কখনোই Perfect হয় না।

import numpy as np
ages = pd.Series([20,25,np.nan,30])

# Output:
# 20
# 25
# NaN
# 30
# NaN মানে Data নেই।

# Missing Check: 
print(ages.isnull())
# Output:
# False
# False
# True
# False

# Missing Count
print(ages.isnull().sum())
# output : 1

# endregion

# region Statistics

marks = pd.Series([50,60,70,80,90])
Sum = marks.sum()
# Output: 350

Mean = marks.mean()
# Output: 70

Maximum = marks.max()
# Output: 90

Minimum = marks.min()
# Output: 50

Count = marks.count()
# Output: 5

StandardDeviation = marks.std()

# endregion

# ধরো একটি AI Model Prediction করেছে।
prediction = pd.Series([
    0.95,
    0.87,
    0.30,
    0.99,
    0.65
])
# আমি শুধু ৯০% Confidence-এর Prediction চাই।
prediction[prediction > 0.90]
# Output:
# 0    0.95
# 3    0.99
# এভাবে Object Detection, NLP, Medical AI—সব জায়গায় Confidence Threshold ব্যবহার করা হয়।

