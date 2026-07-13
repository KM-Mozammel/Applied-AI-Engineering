# Filtering কী?: DataFrame থেকে নির্দিষ্ট condition অনুযায়ী row নির্বাচন করাকে Filtering বলে।
#
# SQL এর WHERE clause এর মতো।
#
# SELECT * FROM students WHERE age > 20;
#
# Pandas এ: df[df["Age"] > 20]
#
# AI/ML এ Filtering অনেক গুরুত্বপূর্ণ। ব্যবহার হয়: Missing data বাদ দেওয়া. Positive samples নেওয়া. Outlier remove করা. নির্দিষ্ট class নির্বাচন করা. Data cleaning

import pandas as pd

students = pd.DataFrame({
    "Name": ["Rahim", "Karim", "Hasan", "Nayeem", "Mitu"],
    "Age": [20, 18, 22, 19, 21],
    "Department": ["CSE", "EEE", "CSE", "BBA", "EEE"],
    "Marks": [85, 60, 92, 70, 88]
})

print(students)
print("\n")

# Single Condition
result = students[students["Marks"] > 80]
print(result)

# ভিতরে কী হচ্ছে? students["Marks"] > 80

# Output
# 0     True
# 1    False
# 2     True
# 3    False
# 4     True

# এটাকে বলে Boolean Mask. এরপর Pandas শুধুমাত্র True row গুলো রেখে দেয়।

# Equal Condition
print("\n")
print("Equal Condition: Department == CSE \n")
result = students[students["Department"] == "CSE"]
print(result)

# Not Equal Condition
print("\n")
print("Not Equal Condition: Department != EEE \n")
result = students[students["Department"] != "EEE"]
print(result)

# Greater Than
result = students[students["Age"] > 20]

# Less Than
result = students[students["Age"] < 20]

# Grater Than or Equal
result = students[students["Marks"] >= 85]

# Less Than or Equal
result = students[students["Marks"] <= 70]

# Comparison Operators: > < >= <= == != এগুলো সব Filtering এ ব্যবহার হয়।

#Multiple Condition (AND): &
result = students[
    (students["Department"] == "EEE") &
    (students["Marks"] > 80)
]
# Output: Mitu
# কেন () ব্যবহার করি? ভুল: students["Age"] > 20 & students["Marks"] > 80 Python বুঝবে 20 & students["Marks"] যা ভুল। 
# সঠিক, (students["Age"] > 20) & (students["Marks"] > 80)

# Multiple Condition (OR) OR Operator - |
students[
    (students["Department"] == "BBA") |
    (students["Marks"] > 90)
]

# Output: Hasan Nayeem

# NOT Condition: NOT Operator ~
students[
    ~(students["Department"] == "CSE")
]
# Output: Karim, Nayeem, Mitu

# Boolean Mask Variable: AI Project-এ এটা খুব বেশি ব্যবহার হয়।
mask = students["Marks"] >= 80
print(mask)
print(students[mask])

# isin() একাধিক Value Filter
students[
    students["Department"].isin(["CSE", "EEE"])
]

# Output: Rahim, Karim, Hasan, Mitu

# between()
students[
    students["Marks"].between(70,90)
]

# Output: Rahim Nayeem Mitu

# string contains() - Case Sensitive।
students[
    students["Name"].str.contains("a")
]

# Case Ignore
students[
    students["Name"].str.contains("a", case=False)
]

# startswith()
students[
    students["Name"].str.startswith("R")
]

# endswith()
students[
    students["Name"].str.endswith("m")
]

# Filtering + Specific Columns
students.loc[
    students["Marks"] > 80,
    ["Name","Marks"]
]

# Output: Name Marks

# query() - এটা SQL এর মতো দেখতে।
students.query("Marks > 80")

# Multiple:
students.query("Age > 20 and Marks > 80")

# nlargest() - Top Student
students.nlargest(3,"Marks")

# nsmallest()
students.nsmallest(2,"Marks")

# Empty Result
students[
    students["Marks"] > 100
]

# Output: Empty DataFrame

# Filter Missing Value
students[
    students["Marks"].notna()
]
students[
    students["Marks"].isna()
]


# AI/ML এ বাস্তব ব্যবহার: Data Cleaning - df[df["Age"] > 0]
# Remove Outlier - df[df["Salary"] < 100000]
# Positive Reviews - df[df["Sentiment"] == "Positive"]
# Train শুধুমাত্র Approved Data - df[df["Approved"] == True]
# নির্দিষ্ট Label - cats = df[df["Label"] == "Cat"]

# Filtering Cheat Sheet:
# কাজ	          Syntax
# Equal	            ==
# Not Equal	        !=
# Greater	        >
# Less	            <
# AND	            &
# OR	            |
# NOT	            ~
# Multiple Values   isin()
# Range	           between()
# Contains	       str.contains()
# Starts With	str.startswith()
# Ends With	     str.endswith()
# Query	          query()
# Missing	      isna()
# Not Missing	   notna()
# Top Rows	       nlargest()
# Bottom Rows	   nsmallest()