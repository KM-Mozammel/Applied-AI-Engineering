# প্রথমে বুঝি Index আসলে কী? ধরো তোমার একটা Excel Sheet আছে।

# Roll	Name	Age
# 101	Rahim	20
# 102	Karim	22
# 103	Sakib	24

# এখন প্রশ্ন। Rahim-কে খুঁজবে কীভাবে? দুইভাবে।

# উপায় ১: Row Number দেখে: 0 1 2 
# উপায় ২: Roll Number দেখে: 101 102 103

# দ্বিতীয় পদ্ধতিটাই বেশি অর্থপূর্ণ। এটাই Index-এর ধারণা। Index কী? Index হলো DataFrame-এর প্রতিটি Row-এর পরিচয় (Label)।

# Visual
#   DataFrame
# Index
# 0 ------ Rahim
# 1 ------ Karim
# 2 ------ Sakib

# Default Index:
import pandas as pd
students = {
    "Name": ["Rahim", "Karim", "Sakib"],
    "Age": [20, 22, 24]
}
df = pd.DataFrame(students)
print(df)
# Output:
#    Name    Age
# 0 Rahim   20
# 1 Karim   22
# 2 Sakib   24
# এখানে, 0 1 2 এগুলোই Default Index।
# Show Index:
print(df.index)
# Output: RangeIndex(start=0, stop=3, step=1) মানে 0 1 2

#Custom Index: কেন Custom Index দরকার? ধরো Student ID আছে।
# ID: 1001 1002 1003
# এখন এগুলোই যদি Index হয়? তাহলে Student খুঁজে পাওয়া আরও সহজ হবে।

# set_index()
students = {
    "ID": [1001, 1002, 1003],
    "Name": ["Rahim", "Karim", "Sakib"],
    "Age": [20, 22, 24]
}

df = pd.DataFrame(students)
print(df)
df = df.set_index("ID")
print(df)
# ID আর Column নেই। এটা এখন Index।
# Data access:
print("\n")
print(df.loc[1002])
#  reset_index()
print("Reset Index: \n")
df = df.reset_index()
print(df)
#Remove the old index column:
print("Drop = True; \n")
df = df.reset_index(drop = True)
print(df)
# another way to create custom index:
df = pd.DataFrame(
    students,
    index = ["A", "B", "c"]
)
print(df)

# Index পরিবর্তন
df.index = ["X", "Y", "Z"]
print(df)

#Index - এর নাম দেওয়া। 
df.index.name = "Student"
print(df)

# AI Example: ধরো তোমার কাছে একটি Face Recognition Dataset আছে।

# ImageID
# image_001
# image_002
# image_003

# এখন, df.set_index("ImageID") - তাহলে, df.loc["image_002"] দিয়েই নির্দিষ্ট ছবির তথ্য পাওয়া যাবে।

# আরেকটি AI Example: ধরো Stock Market Data।
# Date:
# 2025-01-01
# 2025-01-02
# 2025-01-03
# এখানে Date-কে Index বানানো হয়। df.set_index("Date") . তারপর df.loc["2025-01-02"]. সেই দিনের সমস্ত তথ্য পাওয়া যায়।

# region sort_index()
import pandas as pd

students = {
    "Age": [20, 22, 24]
}

df = pd.DataFrame(
    students,
    index=["C", "A", "B"]
)
print("Unsorted Index:", df)
df = df.sort_index()
df.index.name = "Index"
print("Sorted Index:", df)
df = df.sort_index(ascending=False)
print("Descending Sort:", df)

# Sort by values()
print("\n Short by Values()")
students = {
    "Name": ["Rahim", "Karim", "Sakib"],
    "Age": [24, 20, 22]
}
df = pd.DataFrame(students)
print("Unsorted: ", df)
df = df.sort_values("Age", ascending=False)
print("Sorted by Age:", df)

# ReIndex() : আমরা Index-এর Order নিজের মতো করতে চাই।
df = pd.DataFrame(
    {
        "Age":[20,22,24]
    },
    index=["Rahim","Karim","Sakib"]
)

df.reindex([
    "Sakib",
    "Rahim",
    "Karim"
])

# যদি Index না থাকে?
df.reindex([
    "Rahim",
    "Nusrat",
    "Karim"
])
# Output:
# Rahim    20
# Nusrat   NaN
# Karim    22
# খেয়াল করো। Nusrat ছিল না। তাই NaN এসেছে।

print("\n")
print("\n")
#Index Alignment
math = pd.Series(
    [80,90],
    index=["Rahim","Karim"]
)

english = pd.Series(
    [5,10],
    index=["Karim","Rahim"]
)
print("index alignment: \n", math + english)

# Multi-Index: 
print("\n")
print("\n")
print("Multi Index: ")

df = pd.DataFrame(
    {
        "Marks":[80,85,75,90]
    },
    index=[
        ["CSE","CSE","EEE","EEE"],
        ["Rahim","Karim","Sakib","Nusrat"]
    ]
)

print(df)
print(df.loc[("CSE", "Rahim")])
print(df.loc["CSE"])


# Indexing-এর সম্পূর্ণ মানসিক মডেল:
#                     DataFrame
#                          │
#         ┌────────────────┴────────────────┐
#         │                                 │
#      Columns                          Index
#         │                                 │
#         │                                 │
#  sort_values()                    sort_index()
#         │                                 │
#         └──────────────┬──────────────────┘
#                        │
#                    reindex()
#                        │
#                        ▼
#                Index Alignment
#                        │
#                        ▼
#                   MultiIndex