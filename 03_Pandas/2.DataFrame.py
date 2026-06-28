# region DataFrame Part-1 ***********
# Series + Series + Series = DataFrame
# DataFrame: আমরা Series-এ কী শিখেছিলাম? ages = pd.Series([20,25,30])

# Visual:
# Index   Value

# 0 ------>20
# 1 ------>25
# 2 ------>30

# এখানে একটি মাত্র Column আছে। এখন ভাবো, যদি একজন Student-এর শুধু Age না থেকে আরও তথ্য থাকে?

# Name, Age, City, CGPA. তখন কি Series যথেষ্ট? না। কারণ Series-এ একটি Column-ই রাখা যায়। তখন আসে DataFrame DataFrame = অনেকগুলো Series একসাথে।

# Visual: DataFrame
# +----------------------------------+
# | Name    Age    City      CGPA    |
# |----------------------------------|
# | Rahim   20     Dhaka     3.80    |
# | Karim   22     Tangail   3.50    |
# | Sakib   24     Rajshahi  3.95    |
# +----------------------------------+
# আরেকভাবে ভাবো

#            DataFrame

#            Columns
#      ----------------------
# Rows | Name | Age | City
# --------------------------
# 0    |Rahim|20   |Dhaka
# 1    |Karim|22   |Tangail
# 2    |Sakib|24   |Rajshahi

# সবচেয়ে গুরুত্বপূর্ণ ধারণা, DataFrame-এর প্রতিটি Column নিজেই একটি Series।

# DataFrame
# Name Column  -----> Series
# Age Column   -----> Series
# City Column  -----> Series
# CGPA Column  -----> Series

# এটাই Pandas-এর মূল ডিজাইন। 
# বাস্তব উদাহরণ, ধরো তুমি একটি AI Project করছো। 
# তোমার Dataset
# Name     Age     Salary     City
# Rahim     20      25000     Dhaka
# Karim     22      30000     Tangail
# Sakib     24      45000     Rajshahi

# এটাই DataFrame। DataFrame তৈরি করা। সবচেয়ে সহজ উপায় হলো Dictionary ব্যবহার করা।

import pandas as pd

students = {
    "Name": ["Rahim", "Karim", "Sakib"],
    "Age": [20, 22, 24],
    "City": ["Dhaka", "Tangail", "Rajshahi"]
}

df = pd.DataFrame(students)

print(df)

# Output:
#     Name    Age      City
# 0  Rahim    20      Dhaka
# 1  Karim    22    Tangail
# 2  Sakib    24   Rajshahi

# ভেতরে কী হলো? Dictionary:

students = {
    "Name": ["Rahim", "Karim", "Sakib"],
    "Age": [20,22,24],
    "City": ["Dhaka","Tangail","Rajshahi"]
}

# DataFrame
#             Columns

#         Name    Age     City
# 0       Rahim   20     Dhaka
# 1       Karim   22     Tangail
# 2       Sakib   24     Rajshahi


# DataFrame-এর Anatomy:
#              Columns
#         -----------------------
# Index | Name | Age | City

# 0     |Rahim|20|Dhaka

# 1     |Karim|22|Tangail

# 2     |Sakib|24|Rajshahi

# এখানে তিনটি গুরুত্বপূর্ণ জিনিস আছে:

# Index (Row Number)
# Columns (Field Name)
# Values (Actual Data)



# DataFrame-এর Type:  
print(type(df))
# Output: <class 'pandas.core.frame.DataFrame'>

# একটি Column বের করা:
print(df["Name"])

# Output: 
# 0    Rahim
# 1    Karim
# 2    Sakib
# খেয়াল করো। এটা DataFrame নয়। এটা একটি Series।

print(type(df["Name"]))

# Output
# <class 'pandas.core.series.Series'>

# এটাই প্রমাণ করে—একটি DataFrame-এর প্রতিটি Column একটি Series।

# একাধিক Column বের করা:
print(df[["Name", "Age"]])

# Output
#     Name   Age
# 0  Rahim   20
# 1  Karim   22
# 2  Sakib   24

# এবার Result-এর Type:
print(type(df[["Name", "Age"]]))

# Output
# <class 'pandas.core.frame.DataFrame'>
# কারণ এখানে দুইটি Series একসাথে আছে।

# DataFrame-এর Shape:
print(df.shape)
# Output: (3,3) মানে ৩টি Row ৩টি Column

# Column Names:
print(df.columns)
# Output: Index(['Name', 'Age', 'City'])

# Index:
print(df.index)
# Output: RangeIndex(start=0, stop=3, step=1)

# Data Types:
print(df.dtypes)

# Output:
# Name    object
# Age      int64
# City    object

# DataFrame Information:
print(df.info())

# Output (সরলভাবে)
# Rows : 3
# Columns : 3
# Memory Usage
# Data Types
# Missing Values
# এটি AI Engineer-দের সবচেয়ে বেশি ব্যবহৃত কমান্ডগুলোর একটি।

# প্রথম ৫টি Row:
print(df.head())
# যদি Dataset-এ ১০ লক্ষ Row থাকে, তবুও এটি শুধু প্রথম ৫টি দেখাবে।

# শেষ ৫টি Row:
print(df.tail())

import pandas as pd

students = {
    "Name": ["Rahim", "Karim", "Sakib"],
    "Age": [20, 22, 24],
    "City": ["Dhaka", "Tangail", "Rajshahi"]
}

df = pd.DataFrame(students)

print("=== Full DataFrame ===")
print(df)

print("\n=== Shape ===")
print(df.shape)

print("\n=== Columns ===")
print(df.columns)

print("\n=== Index ===")
print(df.index)

print("\n=== Data Types ===")
print(df.dtypes)

print("\n=== Information ===")
print(df.info())

print("\n=== Name Column ===")
print(df["Name"])

print("\n=== Name & Age Columns ===")
print(df[["Name", "Age"]])

print("\n=== First 5 Rows ===")
print(df.head())

print("\n=== Last 5 Rows ===")
print(df.tail())

# endregion

# region Dataframe Part-2

import pandas as pd
students = {
    "Name": ["Rahim", "Karim", "Sakib", "Nusrat"],
    "Age": [20, 22, 24, 21],
    "City": ["Dhaka", "Tangail", "Rajshahi", "Khulna"],
    "CGPA": [3.80, 3.50, 3.95, 3.70]
}
df = pd.DataFrame(students)
print(df)

# Output: 
#      Name  Age       City  CGPA
# 0   Rahim   20     Dhaka  3.80
# 1   Karim   22   Tangail  3.50
# 2   Sakib   24  Rajshahi  3.95
# 3  Nusrat   21    Khulna  3.70

# Row Selection: আগে আমরা Column বের করেছি।

df["Name"]

# এখন যদি প্রথম Row চাই? iloc[] - iloc মানে Integer Location অর্থাৎ Row Number দিয়ে Data বের করবে। প্রথম Row
print(df.iloc[0])

# Output:
# Name      Rahim
# Age          20
# City      Dhaka
# CGPA        3.8
# খেয়াল করো Result কিন্তু DataFrame না। এটা একটি Series। কারণ একটি Row-ও আসলে একটি Series।

# দ্বিতীয় Row:
# print(df.iloc[1])

# Output:
# Name      Karim
# Age          22
# City   Tangail
# CGPA        3.5


# Multiple Rows:
print(df.iloc[0:3])

# Output:
#      Name  Age       City  CGPA
# 0   Rahim   20     Dhaka  3.80
# 1   Karim   22   Tangail  3.50
# 2   Sakib   24  Rajshahi  3.95

# এটা Slice। Python List-এর মতোই। 0:3 মানে 0 1 2

# loc[]: loc মানে Location by Label এটি Index Label ব্যবহার করে। আমাদের Index 0 1 2 3 তাই
print(df.loc[0])

# Output:
# Name      Rahim
# Age          20
# City      Dhaka
# CGPA        3.8

# এখন প্রশ্ন আসতে পারে— তাহলে loc আর iloc-এর পার্থক্য কী? এখন না বুঝলেও সমস্যা নেই। একটি উদাহরণ দেখি।

# Custom Index:
df = df.set_index("Name")
print(df)

# Output:
#         Age       City  CGPA
# Name
# Rahim   20     Dhaka   3.80
# Karim   22   Tangail   3.50
# Sakib   24  Rajshahi   3.95
# Nusrat  21    Khulna   3.70

# এখন Index আর সংখ্যা নেই। Index হলো Name।

# এখন df.loc["Rahim"]

# Output:
# Age         20
# City     Dhaka
# CGPA       3.8

# কিন্তু df.iloc[0]

# Output:
# Age         20
# City     Dhaka
# CGPA       3.8

# দুটোর Output একই হলেও কাজ করার পদ্ধতি আলাদা।

# মনে রাখার সহজ নিয়ম
# iloc -> Integer -> Position -> 0 -> 1 -> 2 -> 3 -> 
# loc -> Label
# Rahim
# Karim
# Sakib
# নির্দিষ্ট Row এবং Column ধরো Rahim-এর City দরকার।

df.loc["Rahim", "City"]

# Output: Dhaka অথবা Index Number দিয়ে

df.iloc[0, 1]

# Output: Dhaka . কারণ Row = 0, Column = 1

# Multiple Columns: 
df.loc[:, ["City", "CGPA"]]

# Output:
#             City  CGPA
# Name
# Rahim     Dhaka  3.80
# Karim   Tangail  3.50
# Sakib  Rajshahi  3.95
# Nusrat    Khulna 3.70

# এখানে : মানে সব Row।

# Multiple Rows and Columns: 
df.iloc[0:2, 0:2]

# Output:
#         Age      City
# Name
# Rahim   20     Dhaka
# Karim   22   Tangail

# Visual: 
#         Age      City     CGPA
# Rahim   20     Dhaka    3.80
# Karim   22   Tangail   3.50
# Sakib   24  Rajshahi   3.95

# আমরা নিচের অংশটি নিয়েছি।

#         +----------------------+
# Rahim   |20     Dhaka          |
# Karim   |22   Tangail          |
#         +----------------------+
        
# AI Engineer Example: ধরো একটি Dataset আছে।
# Name Age Salary Department Experience 
# তুমি শুধু Age Experience দিয়ে Model Train করবে।
# তখন,
X = df[["Age", "Experience"]]
# আর Target,
y = df["Salary"]

# এভাবেই Machine Learning-এর Feature (X) এবং Target (y) আলাদা করা হয়।

import pandas as pd

students = {
    "Name": ["Rahim", "Karim", "Sakib", "Nusrat"],
    "Age": [20, 22, 24, 21],
    "City": ["Dhaka", "Tangail", "Rajshahi", "Khulna"],
    "CGPA": [3.80, 3.50, 3.95, 3.70]
}

df = pd.DataFrame(students)

print("=== Original Data ===")
print(df)
print("\n=== First Row ===")
print(df.iloc[0])
print("\n=== First Three Rows ===")
print(df.iloc[0:3])
df = df.set_index("Name")
print("\n=== Custom Index ===")
print(df)
print("\n=== Rahim Data ===")
print(df.loc["Rahim"])
print("\n=== Rahim City ===")
print(df.loc["Rahim", "City"])
print("\n=== First Row, Second Column ===")
print(df.iloc[0, 1])
print("\n=== City and CGPA Columns ===")
print(df.loc[:, ["City", "CGPA"]])
print("\n=== First Two Rows, First Two Columns ===")
print(df.iloc[0:2, 0:2])

# শুধু এই চারটি বিষয় মনে রাখো:
# Method	কী ব্যবহার করে?	উদাহরণ
# iloc[]	Position (সংখ্যা)	df.iloc[0]
# loc[]	Label (নাম/ইনডেক্স)	df.loc["Rahim"]
# df["Age"]	একটি Column	Series
# df[["Age","City"]]	একাধিক Column	DataFrame



# endregion

# region Dataframe Part - 3

# প্রথমে DataFrame তৈরি করি:
import pandas as pd
students = {
    "Name": ["Rahim", "Karim", "Sakib", "Nusrat"],
    "Age": [20, 22, 24, 21],
    "CGPA": [3.80, 3.50, 3.95, 3.70]
}
df = pd.DataFrame(students)
print(df)

# Output:
#      Name  Age  CGPA
# 0   Rahim   20  3.80
# 1   Karim   22  3.50
# 2   Sakib   24  3.95
# 3  Nusrat   21  3.70

# Part 1 : নতুন Column যোগ করা: 
# ধরো, আমরা প্রতিটি Student-এর Department যোগ করতে চাই।
df["Department"] = [
    "CSE",
    "EEE",
    "BBA",
    "CSE"
]
print(df)
# Output:
#      Name  Age  CGPA Department
# 0   Rahim   20  3.80      CSE
# 1   Karim   22  3.50      EEE
# 2   Sakib   24  3.95      BBA
# 3  Nusrat   21  3.70      CSE
# কী হলো? আগে Name Age CGPA এখন Name Age CGPA Department নতুন একটি Column তৈরি হয়েছে।

# Part 2 : একই Value সব Row-তে: ধরো, সবাই Bangladesh-এর Student।

df["Country"] = "Bangladesh"
print(df)
# Output:
# Country
# Bangladesh
# Bangladesh
# Bangladesh
# Bangladesh
# Pandas নিজেই সব Row-তে Value কপি করে দেয়।

# Part 3 : Existing Column Update: সব Student-এর Age ১ বছর বাড়াতে চাই।
df["Age"] = df["Age"] + 1
# অথবা
df["Age"] += 1
# Output: 21 23 25 22

# Visual: আগে 20 22 24 21 -> 21 23 25 22


# Part 4 : নতুন Column Calculation দিয়ে: এটাই Feature Engineering-এর শুরু। ধরো একটি Bonus Score তৈরি করব।

df["Bonus"] = df["CGPA"] * 10

# Output:
# CGPA   Bonus
# 3.80    38
# 3.50    35
# 3.95    39.5
# 3.70    37

# কেন এটা গুরুত্বপূর্ণ? বাস্তব AI Project-এ

# Salary
# ↓
# Tax
# ↓
# Net Salary

# অথবা
# Height
# Weight
# ↓
# BMI

# অথবা
# Birth Year
# ↓
# Age
# এইভাবে নতুন Feature তৈরি করা হয়।

# Part 5 : Column Delete: ধরো Country দরকার নেই।
df.drop("Country", axis=1)
# Output: Country Column বাদ, কিন্তু একটা বিষয় খেয়াল করো।

print(df)

# Country এখনও আছে! কেন? কারণ, drop() ডিফল্টভাবে Original Data পরিবর্তন করে না।
# Solution 1: 
df = df.drop("Country", axis=1)
# Solution 2 (বেশি ব্যবহার হয়):
df.drop("Country", axis=1, inplace=True)

# এখন Original DataFrame-ই পরিবর্তন হবে। 

# axis=1 মানে কী? DataFrame-এ দুইটি Axis থাকে।
#            Columns
#       --------------------
# Rows | Name | Age | CGPA

# Axis: axis=0 ↓ Rows
# axis=1 ↓ Columns .তাই,

df.drop("Country", axis=1)
# মানে Column Delete করো।

# Row Delete:
df.drop(0)
# মানে, প্রথম Row Delete। কারণ axis=0 Default হলো Row।

# Part 6 : Rename Column: ধরো CGPA-এর নাম GPA করব।
df.rename(
    columns={
        "CGPA":"GPA"
    }
)

# কিন্তু Original Change হবে না। তাই,

df.rename(
    columns={
        "CGPA":"GPA"
    },
    inplace=True
)

# Output:
# Name
# Age
# GPA

# Part 7 : Feature Engineering: এটাই AI-এর সবচেয়ে গুরুত্বপূর্ণ অংশ। ধরো, যাদের Age 22 বা তার বেশি তাদের Adult বলব।

df["Adult"] = df["Age"] >= 22
print(df)
# Output:
# Age   Adult
# 21    False
# 23    True
# 25    True
# 22    True
# এখানে নতুন Feature তৈরি হয়েছে।

# আরেকটি Example
df["Passed"] = df["CGPA"] >= 3.60
# Output
# CGPA   Passed
# 3.80    True
# 3.50    False
# 3.95    True
# 3.70    True

# বাস্তব AI Example: ধরো একটি Employee Dataset আছে। Age Salary Experience
# তুমি Feature তৈরি করলে। HighSalary Experienced Senior Tax Bonus PromotionEligible

# Machine Learning Model এই নতুন Feature-গুলো থেকেই ভালো শিখতে পারে।

import pandas as pd

students = {
    "Name": ["Rahim", "Karim", "Sakib", "Nusrat"],
    "Age": [20, 22, 24, 21],
    "CGPA": [3.80, 3.50, 3.95, 3.70]
}

df = pd.DataFrame(students)

# Add Columns
df["Department"] = ["CSE", "EEE", "BBA", "CSE"]
df["Country"] = "Bangladesh"

# Update Age
df["Age"] += 1

# Feature Engineering
df["Bonus"] = df["CGPA"] * 10
df["Passed"] = df["CGPA"] >= 3.60

# Rename
df.rename(columns={"CGPA": "GPA"}, inplace=True)

# Delete
df.drop("Country", axis=1, inplace=True)

print(df)

# Output
#      Name  Age   GPA Department  Bonus  Passed
# 0   Rahim   21  3.80        CSE   38.0    True
# 1   Karim   23  3.50        EEE   35.0   False
# 2   Sakib   25  3.95        BBA   39.5    True
# 3  Nusrat   22  3.70        CSE   37.0    True

# 🧠 আজকের মূল ধারণা: DataFrame শুধু ডেটা দেখার জন্য নয়, বরং পরিবর্তন করার জন্যও ব্যবহৃত হয়।

# Existing Data
#       │
#       ▼
# Add Column
#       │
#       ▼
# Update Column
#       │
#       ▼
# Delete Column
#       │
#       ▼
# Rename Column
#       │
#       ▼
# Feature Engineering
#       │
#       ▼
# Machine Learning Model



# endregion