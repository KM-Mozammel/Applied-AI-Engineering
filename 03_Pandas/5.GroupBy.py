চলুন এবার **`5.GroupBy.py`** শুরু করি।

এটি Pandas-এর সবচেয়ে গুরুত্বপূর্ণ Topic-গুলোর একটি। SQL-এর `GROUP BY` এর মতোই এটি কাজ করে এবং Data Analysis, Feature Engineering, EDA (Exploratory Data Analysis), Machine Learning—সব জায়গাতেই ব্যাপকভাবে ব্যবহৃত হয়।

---

```python
# ==========================================================
# Pandas GroupBy (বাংলা)
# ==========================================================

# GroupBy কী?
# ----------------------------------------------------------
# একই ধরনের (same category) Data গুলোকে একসাথে Group করে
# তাদের উপর বিভিন্ন Calculation (Aggregation) করার প্রক্রিয়াকে GroupBy বলে।
#
# SQL এর GROUP BY এর মতো।
#
# উদাহরণ:
#
# Student Marks
#
# CSE
#   Rahim
#   Hasan
#
# EEE
#   Karim
#   Mitu
#
# এরপর প্রতিটি Department-এর
# Average Marks
# Total Marks
# Maximum Marks
# Count
#
# বের করা যায়।
#
# AI/ML এ ব্যবহার:
#
# - Exploratory Data Analysis (EDA)
# - Category Wise Statistics
# - Feature Engineering
# - Customer Analysis
# - Sales Analysis
# - Data Summarization
```

---

# Sample Dataset

```python
import pandas as pd

students = pd.DataFrame({
    "Name": ["Rahim", "Karim", "Hasan", "Nayeem", "Mitu", "Siam"],
    "Department": ["CSE", "EEE", "CSE", "BBA", "EEE", "CSE"],
    "Gender": ["Male", "Male", "Male", "Male", "Female", "Male"],
    "Marks": [85, 60, 92, 70, 88, 76],
    "Age": [20, 18, 22, 19, 21, 23]
})

print(students)
```

Output

```
     Name Department Gender  Marks  Age
0   Rahim        CSE   Male     85   20
1   Karim        EEE   Male     60   18
2   Hasan        CSE   Male     92   22
3  Nayeem        BBA   Male     70   19
4    Mitu        EEE Female     88   21
5    Siam        CSE   Male     76   23
```

---

# ১. Basic GroupBy

```python
students.groupby("Department")
```

এটি এখনো কোনো Result দেয় না।

এটি শুধু Data-কে Group করে।

---

# Group গুলো কেমন?

```
CSE

Rahim
Hasan
Siam

-------------------

EEE

Karim
Mitu

-------------------

BBA

Nayeem
```

---

# ২. Count

```python
students.groupby("Department").count()
```

Output

```
Department

BBA 1

CSE 3

EEE 2
```

---

# ৩. Size()

Count করার আরেকটি উপায়।

```python
students.groupby("Department").size()
```

Output

```
BBA    1
CSE    3
EEE    2
```

---

## Count vs Size

```
count()

Missing Value বাদ দেয়

-------------------

size()

সব Row গণনা করে
```

---

# ৪. Sum()

```python
students.groupby("Department")["Marks"].sum()
```

Output

```
BBA

70

CSE

253

EEE

148
```

---

# ৫. Mean()

```python
students.groupby("Department")["Marks"].mean()
```

Output

```
BBA

70

CSE

84.33

EEE

74
```

---

# Mean কেন গুরুত্বপূর্ণ?

AI Project-এ Category Wise Average বের করতে।

উদাহরণ

```
Average Salary

Average Age

Average Purchase

Average Rating
```

---

# ৬. Max()

```python
students.groupby("Department")["Marks"].max()
```

---

# ৭. Min()

```python
students.groupby("Department")["Marks"].min()
```

---

# ৮. Multiple Aggregation

একসাথে অনেক Calculation।

```python
students.groupby("Department")["Marks"].agg(
    ["count", "sum", "mean", "max", "min"]
)
```

Output

```
count

sum

mean

max

min
```

---

# agg() কী?

Aggregation Function

একাধিক Function একসাথে চালায়।

---

# ৯. Group Multiple Column

```python
students.groupby(
    ["Department", "Gender"]
).mean(numeric_only=True)
```

Group হবে

```
CSE + Male

EEE + Male

EEE + Female

BBA + Male
```

---

# ১০. Select Multiple Columns

```python
students.groupby("Department")[["Marks", "Age"]].mean()
```

Output

```
Average Marks

Average Age
```

---

# ১১. Get One Group

```python
group = students.groupby("Department")

print(group.get_group("CSE"))
```

Output

```
Rahim

Hasan

Siam
```

---

# ১২. Iterate Group

```python
group = students.groupby("Department")

for name, data in group:

    print(name)

    print(data)

    print("----------------")
```

Output

```
CSE

...

EEE

...

BBA

...
```

---

# ১৩. as_index=False

Default

```python
students.groupby("Department").mean(numeric_only=True)
```

Department Index হয়ে যায়।

---

Normal DataFrame চাইলে

```python
students.groupby(
    "Department",
    as_index=False
).mean(numeric_only=True)
```

---

# ১৪. sort=False

Default

```
Alphabetically Sort করে।
```

বন্ধ করতে

```python
students.groupby(
    "Department",
    sort=False
).sum(numeric_only=True)
```

---

# ১৫. Named Aggregation

```python
students.groupby("Department").agg(

    AverageMarks=("Marks", "mean"),

    HighestMarks=("Marks", "max"),

    TotalStudents=("Name", "count")
)
```

Output

```
AverageMarks

HighestMarks

TotalStudents
```

---

# ১৬. value_counts()

কখনও GroupBy এর বিকল্প।

```python
students["Department"].value_counts()
```

Output

```
CSE 3

EEE 2

BBA 1
```

---

# ১৭. nunique()

Unique Count

```python
students.groupby("Department")["Gender"].nunique()
```

---

# ১৮. first()

```python
students.groupby("Department").first()
```

---

# ১৯. last()

```python
students.groupby("Department").last()
```

---

# ২০. describe()

```python
students.groupby("Department")["Marks"].describe()
```

Output

```
count

mean

std

min

25%

50%

75%

max
```

---

# GroupBy Visualization

```
Original Data

Rahim  CSE 85

Karim  EEE 60

Hasan  CSE 92

Mitu   EEE 88

↓

GroupBy

CSE

85

92

76

↓

Mean

84.33

--------------------

EEE

60

88

↓

Mean

74
```

---

# AI/ML এ বাস্তব ব্যবহার

## Category Wise Average

```python
df.groupby("Product")["Price"].mean()
```

---

## Customer Spending

```python
df.groupby("Customer")["Amount"].sum()
```

---

## Average Rating

```python
df.groupby("Movie")["Rating"].mean()
```

---

## Fraud Detection

```python
df.groupby("User")["Transaction"].count()
```

---

## Sales Analysis

```python
df.groupby("City")["Sales"].sum()
```

---

## Feature Engineering

```python
df["AverageSalary"] = (
    df.groupby("Department")["Salary"]
      .transform("mean")
)
```

> **`transform()`** সম্পর্কে আমরা Feature Engineering অধ্যায়ে বিস্তারিত শিখব।

---

# SQL vs Pandas

| SQL                 | Pandas                  |
| ------------------- | ----------------------- |
| GROUP BY Department | `groupby("Department")` |
| COUNT(*)            | `.count()` / `.size()`  |
| SUM()               | `.sum()`                |
| AVG()               | `.mean()`               |
| MAX()               | `.max()`                |
| MIN()               | `.min()`                |

---

# সবচেয়ে বেশি ব্যবহৃত Methods

| Method           | কাজ                |
| ---------------- | ------------------ |
| `count()`        | Count              |
| `size()`         | Total Row          |
| `sum()`          | যোগফল              |
| `mean()`         | Average            |
| `max()`          | Maximum            |
| `min()`          | Minimum            |
| `agg()`          | একাধিক Aggregation |
| `first()`        | প্রথম Row          |
| `last()`         | শেষ Row            |
| `describe()`     | Summary Statistics |
| `get_group()`    | নির্দিষ্ট Group    |
| `nunique()`      | Unique Count       |
| `value_counts()` | Frequency Count    |

---

# 🧠 এই অধ্যায় শেষে যা অবশ্যই জানতে হবে

* ✅ `groupby()` কী এবং কেন ব্যবহার করা হয়
* ✅ `count()` ও `size()`-এর পার্থক্য
* ✅ `sum()`, `mean()`, `max()`, `min()` ব্যবহার
* ✅ `agg()` দিয়ে একাধিক Aggregation করা
* ✅ একাধিক Column দিয়ে Group করা
* ✅ `get_group()` এবং `for` loop দিয়ে Group Iterate করা
* ✅ `as_index=False` ও `sort=False`-এর ব্যবহার
* ✅ `describe()` দিয়ে Group Summary দেখা
* ✅ SQL `GROUP BY` এবং Pandas `groupby()`-এর মিল
* ✅ AI/ML-এ EDA, Data Analysis এবং Feature Engineering-এ GroupBy-এর বাস্তব ব্যবহার

---

**পরবর্তী ফাইল:** **`6.Merge.py`**, যেখানে আমরা `merge()`, `join()`, `concat()`, `inner`, `left`, `right`, `outer join`—সবকিছু SQL-এর সাথে তুলনা করে বাংলায় শিখব।
