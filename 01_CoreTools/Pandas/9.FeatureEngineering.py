দারুণ। এবার আমরা **Pandas-এর শেষ এবং সবচেয়ে গুরুত্বপূর্ণ অধ্যায়** শুরু করবো।

# `8.FeatureEngineering.py`

> **Feature Engineering** হলো Raw Data থেকে Machine Learning Model-এর জন্য নতুন বা আরও ভালো Feature (Column) তৈরি করার প্রক্রিয়া।

বাস্তব AI Engineer-এর ৭০% কাজই Feature Engineering।

---

```python
# ==========================================================
# Pandas Feature Engineering (বাংলা)
# ==========================================================

# Feature Engineering কী?
# ----------------------------------------------------------
# Dataset-এর Existing Data ব্যবহার করে
# নতুন Feature (Column) তৈরি করা,
# Existing Feature পরিবর্তন করা,
# অথবা Machine Learning-এর জন্য Data প্রস্তুত করাকে
# Feature Engineering বলে।
#
#
# উদাহরণ
#
# Name    BirthYear
#
# Rahim   2000
#
#
# নতুন Feature
#
# Age = 2026 - BirthYear
#
#
# AI/ML এ ব্যবহার
#
# • New Feature Create
# • Encoding
# • Scaling এর আগে Preparation
# • Data Transformation
# • Category Conversion
# • Model Accuracy Improve
#
#
# Feature Engineering অনেক সময়
# Model পরিবর্তনের থেকেও বেশি Accuracy বাড়ায়।
```

---

# Sample Dataset

```python
import pandas as pd

students = pd.DataFrame({

    "Name":["Rahim","Karim","Hasan","Mitu"],

    "Department":["CSE","EEE","BBA","CSE"],

    "Marks":[85,60,92,88],

    "Age":[20,18,22,21]

})

print(students)
```

---

# ১. নতুন Column তৈরি

```python
students["PassMarks"] = 40

print(students)
```

Output

```
Name

Marks

PassMarks
```

---

# ২. Existing Column থেকে নতুন Column

```python
students["DoubleMarks"] = students["Marks"] * 2
```

---

# ৩. Formula ব্যবহার

```python
students["Percentage"] = students["Marks"] / 100
```

---

# ৪. String Combine

```python
students["StudentInfo"] = (

    students["Name"]

    + " - "

    + students["Department"]

)
```

Output

```
Rahim - CSE
```

---

# ৫. map()

একটি Value কে অন্য Value-তে Convert করে।

```python
department_map = {

    "CSE":"Computer Science",

    "EEE":"Electrical",

    "BBA":"Business"

}

students["Department"] = students["Department"].map(

    department_map

)
```

---

# map() Visualization

```
CSE

↓

Computer Science

----------------

EEE

↓

Electrical
```

---

# ৬. replace()

```python
students["Department"] = students["Department"].replace({

    "CSE":"Computer Science",

    "EEE":"Electrical"

})
```

---

## map vs replace

| map()           | replace()                     |
| --------------- | ----------------------------- |
| Mapping-এর জন্য | Replace-এর জন্য               |
| না থাকলে NaN    | না থাকলে আগের Value রেখে দেয় |

Example

```python
s = pd.Series(["A","B","C"])

print(s.map({"A":"Apple"}))
```

Output

```
Apple

NaN

NaN
```

---

```python
print(s.replace({"A":"Apple"}))
```

Output

```
Apple

B

C
```

---

# ৭. apply()

সবচেয়ে গুরুত্বপূর্ণ Function।

একটি Function পুরো Column-এর প্রতিটি Value-এর উপর চালায়।

```python
def pass_fail(mark):

    if mark >= 80:

        return "Pass"

    return "Fail"

students["Result"] = students["Marks"].apply(pass_fail)
```

---

Short Version

```python
students["Result"] = students["Marks"].apply(

    lambda x:

    "Pass" if x >= 80 else "Fail"

)
```

---

# apply() Visualization

```
85

↓

Pass

------------

60

↓

Fail
```

---

# ৮. apply() Multiple Column

```python
students.apply(

    lambda row:

    row["Marks"] + row["Age"],

    axis=1

)
```

## axis=1

Row অনুযায়ী কাজ করে।

---

# ৯. transform()

Group অনুযায়ী নতুন Value তৈরি।

```python
students["AverageMarks"] = (

students.groupby("Department")["Marks"]

.transform("mean")

)
```

Output

```
Department Average
```

সব Row-তে একই Group Average বসবে।

---

Visualization

```
CSE

85

88

↓

86.5

86.5
```

---

# ১০. assign()

নতুন DataFrame Return করে।

```python
students2 = students.assign(

    Bonus=students["Marks"]+5

)
```

Original DataFrame পরিবর্তন হবে না।

---

# ১১. cut()

Continuous Data কে Category বানায়।

```python
students["Grade"] = pd.cut(

    students["Marks"],

    bins=[0,50,70,85,100],

    labels=[

        "F",

        "C",

        "B",

        "A"

    ]

)
```

---

Visualization

```
0-----50

↓

F

------------

50-----70

↓

C
```

---

# ১২. qcut()

Equal Quantity

```python
students["Group"] = pd.qcut(

    students["Marks"],

    q=4,

    labels=[

        "Q1",

        "Q2",

        "Q3",

        "Q4"

    ]

)
```

Difference

```
cut()

Equal Range

-------------------

qcut()

Equal Number of Rows
```

---

# ১৩. get_dummies()

Categorical Encoding

```python
pd.get_dummies(

    students,

    columns=["Department"]

)
```

Output

```
Department_CSE

Department_EEE

Department_BBA
```

---

# কেন দরকার?

Machine Learning

String বুঝে না।

```
CSE

EEE

↓

1

0
```

---

# ১৪. astype()

Type Change

```python
students["Age"] = students["Age"].astype(float)
```

---

# ১৫. clip()

Value Limit

```python
students["Marks"] = students["Marks"].clip(

    lower=70,

    upper=90

)
```

---

# ১৬. rank()

```python
students["Rank"] = students["Marks"].rank(

    ascending=False

)
```

---

# ১৭. sort_values()

```python
students.sort_values(

    by="Marks",

    ascending=False

)
```

---

# ১৮. rename()

```python
students.rename(

    columns={

        "Marks":"Score"

    }

)
```

---

# ১৯. pipe()

Pipeline Style Code

```python
def add_bonus(df):

    df["Bonus"] = df["Marks"]+5

    return df

students.pipe(add_bonus)
```

---

# ২০. Feature Creation Example

```python
students["AgeGroup"] = pd.cut(

    students["Age"],

    bins=[0,18,25,40],

    labels=[

        "Teen",

        "Young",

        "Adult"

    ]

)
```

---

# AI/ML Example

Salary Dataset

```python
df["SalaryPerAge"] = (

df["Salary"]

/

df["Age"]

)
```

---

Purchase Dataset

```python
df["Total"] = (

df["Price"]

*

df["Quantity"]

)
```

---

Movie Dataset

```python
df["Hit"] = (

df["Rating"] > 8

)
```

---

Customer Dataset

```python
df["VIP"] = (

df["Purchase"]

>

10000

)
```

---

# Feature Engineering Workflow

```
Raw Data

↓

Cleaning

↓

Missing Value

↓

Encoding

↓

Feature Create

↓

Scaling

↓

Train Model
```

---

# সবচেয়ে বেশি ব্যবহৃত Methods

| Method          | কাজ            |
| --------------- | -------------- |
| `map()`         | Mapping        |
| `replace()`     | Replace        |
| `apply()`       | Custom Logic   |
| `transform()`   | Group Feature  |
| `assign()`      | New Column     |
| `cut()`         | Equal Range    |
| `qcut()`        | Equal Quantity |
| `get_dummies()` | Encoding       |
| `astype()`      | Change Type    |
| `clip()`        | Limit Value    |
| `rank()`        | Ranking        |
| `sort_values()` | Sort           |
| `rename()`      | Rename         |
| `pipe()`        | Pipeline       |

---

# ⭐ AI Engineer হিসেবে সবচেয়ে গুরুত্বপূর্ণ

| Method          | গুরুত্ব |
| --------------- | ------- |
| `apply()`       | ⭐⭐⭐⭐⭐   |
| `map()`         | ⭐⭐⭐⭐⭐   |
| `transform()`   | ⭐⭐⭐⭐⭐   |
| `get_dummies()` | ⭐⭐⭐⭐⭐   |
| `cut()`         | ⭐⭐⭐⭐    |
| `astype()`      | ⭐⭐⭐⭐⭐   |
| `assign()`      | ⭐⭐⭐⭐    |
| `replace()`     | ⭐⭐⭐⭐    |
| `sort_values()` | ⭐⭐⭐⭐    |
| `rename()`      | ⭐⭐⭐     |

---

# 🧠 এই অধ্যায় শেষে যা অবশ্যই জানতে হবে

* ✅ নতুন Feature (Column) তৈরি করা
* ✅ `map()` এবং `replace()`-এর পার্থক্য
* ✅ `apply()` দিয়ে Custom Logic প্রয়োগ করা
* ✅ `transform()` দিয়ে Group-wise Feature তৈরি করা
* ✅ `assign()` ব্যবহার করে নতুন DataFrame তৈরি করা
* ✅ `cut()` ও `qcut()` দিয়ে Continuous Data Categorize করা
* ✅ `get_dummies()` দিয়ে One-Hot Encoding করা
* ✅ `astype()` দিয়ে Data Type পরিবর্তন করা
* ✅ `clip()`, `rank()`, `sort_values()`, `rename()`, `pipe()` ব্যবহার
* ✅ Feature Engineering Workflow বুঝে AI/ML Model-এর জন্য Data প্রস্তুত করা

---

## 🎉 অভিনন্দন!

এখন আপনি **Python → NumPy → Pandas**-এর প্রায় সব গুরুত্বপূর্ণ বিষয় শেষ করেছেন।

### পরবর্তী Roadmap (AI Engineer-এর জন্য)

```
Python ✅

↓

Mathematics ✅

↓

NumPy ✅

↓

Pandas ✅

↓

Matplotlib

↓

Seaborn

↓

Scikit-Learn

↓

Machine Learning

↓

PyTorch

↓

Transformers

↓

LLM

↓

RAG

↓

AI Agent

↓

MLOps
```

এই ধারাবাহিকতায় এগোলে প্রতিটি ধাপ আগেরটির উপর ভিত্তি করে তৈরি হবে, ফলে AI Engineering শেখা অনেক সহজ হবে।
