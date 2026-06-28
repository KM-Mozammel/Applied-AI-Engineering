দারুণ। এবার শুরু করি **`CSVLoading.py`**।

এটি শুধু CSV Loading নয়, বরং **Pandas-এর Input/Output (I/O)** অধ্যায়। বাস্তব AI/ML Project-এ ৯০% সময় আপনি Dataset Load এবং Save করবেন।

---

```python
# ==========================================================
# Pandas CSV Loading (বাংলা)
# ==========================================================

# Data Loading কী?
# ----------------------------------------------------------
# বাইরের কোনো File, Database বা API থেকে Data এনে
# Pandas DataFrame-এ সংরক্ষণ করাকে Data Loading বলে।
#
# AI/ML Workflow
#
# CSV
# Excel
# JSON
# SQL
# API
#
#        ↓
#
# Pandas DataFrame
#
#        ↓
#
# Data Cleaning
#
#        ↓
#
# Feature Engineering
#
#        ↓
#
# Machine Learning
#
#
# Pandas Data Load করার জন্য অনেক Function দেয়।
#
# সবচেয়ে বেশি ব্যবহৃত:
#
# read_csv()
# read_excel()
# read_json()
# read_sql()
# read_parquet()
```

---

# Sample CSV

ধরুন আমাদের একটি CSV File আছে

```
students.csv
```

```
ID,Name,Age,Department,Marks
1,Rahim,20,CSE,85
2,Karim,18,EEE,60
3,Hasan,22,CSE,92
4,Mitu,21,BBA,88
```

---

# ১. read_csv()

সবচেয়ে বেশি ব্যবহৃত Function।

```python
import pandas as pd

df = pd.read_csv("students.csv")

print(df)
```

Output

```
   ID Name Age Department Marks
0 1 Rahim 20 CSE 85
1 2 Karim 18 EEE 60
2 3 Hasan 22 CSE 92
3 4 Mitu 21 BBA 88
```

---

# DataFrame Check

```python
print(type(df))
```

Output

```
<class 'pandas.core.frame.DataFrame'>
```

---

# ২. প্রথম কয়েকটি Row

```python
df.head()
```

Default

```
প্রথম ৫টি Row
```

---

```python
df.head(2)
```

Output

```
Rahim

Karim
```

---

# ৩. শেষ কয়েকটি Row

```python
df.tail()
```

---

```python
df.tail(2)
```

---

# ৪. Shape

```python
df.shape
```

Output

```
(Row, Column)
```

Example

```
(1000,5)
```

---

# ৫. Columns

```python
df.columns
```

Output

```
Index([
'ID',
'Name',
'Age',
'Department',
'Marks'
])
```

---

# ৬. Index

```python
df.index
```

---

# ৭. info()

সবচেয়ে গুরুত্বপূর্ণ Function।

```python
df.info()
```

Output

```
Rows

Columns

Data Types

Missing Values
```

---

# ৮. describe()

```python
df.describe()
```

Numeric Summary দেয়।

```
Mean

Max

Min

Std
```

---

# ৯. dtypes

```python
df.dtypes
```

Output

```
ID int64

Name object

Age int64
```

---

# ১০. usecols

শুধু কিছু Column Load

```python
df = pd.read_csv(
    "students.csv",
    usecols=["Name","Marks"]
)
```

---

# ১১. nrows

প্রথম কয়েকটি Row Load

```python
df = pd.read_csv(
    "students.csv",
    nrows=100
)
```

---

# ১২. skiprows

কিছু Row Skip

```python
df = pd.read_csv(
    "students.csv",
    skiprows=2
)
```

---

# ১৩. names

নিজের Column Name

CSV

```
1,Rahim,20
2,Karim,18
```

```python
df = pd.read_csv(
    "students.csv",
    names=["ID","Name","Age"]
)
```

---

# ১৪. header=None

CSV-তে Header না থাকলে

```python
df = pd.read_csv(
    "students.csv",
    header=None
)
```

---

# ১৫. index_col

একটি Column-কে Index বানানো

```python
df = pd.read_csv(
    "students.csv",
    index_col="ID"
)
```

---

# ১৬. parse_dates

Date Automatically Convert

CSV

```
JoinDate
2025-01-01
```

```python
df = pd.read_csv(
    "students.csv",
    parse_dates=["JoinDate"]
)
```

---

# ১৭. dtype

নিজে Data Type দিবেন

```python
df = pd.read_csv(
    "students.csv",
    dtype={
        "Age":"float",
        "Marks":"int"
    }
)
```

---

# ১৮. na_values

কোন Value-কে Missing ধরবে

CSV

```
NA

Unknown

Missing
```

```python
df = pd.read_csv(
    "students.csv",
    na_values=[
        "Unknown",
        "NA"
    ]
)
```

---

# ১৯. Encoding

বাংলা File

```python
df = pd.read_csv(
    "students.csv",
    encoding="utf-8"
)
```

Windows CSV হলে কখনও কখনও

```python
encoding="utf-8-sig"
```

---

# ২০. Large CSV

Chunk করে Load

```python
chunks = pd.read_csv(
    "students.csv",
    chunksize=1000
)

for chunk in chunks:
    print(chunk.shape)
```

বড় Dataset-এর জন্য খুব গুরুত্বপূর্ণ।

---

# Save CSV

```python
df.to_csv(
    "output.csv"
)
```

---

Index বাদ দিতে

```python
df.to_csv(
    "output.csv",
    index=False
)
```

---

# Excel File

Load

```python
df = pd.read_excel(
    "students.xlsx"
)
```

---

Specific Sheet

```python
df = pd.read_excel(
    "students.xlsx",
    sheet_name="Sheet2"
)
```

---

Save

```python
df.to_excel(
    "output.xlsx",
    index=False
)
```

---

# JSON

Load

```python
df = pd.read_json(
    "students.json"
)
```

---

Save

```python
df.to_json(
    "students.json",
    orient="records"
)
```

---

# SQL

Database থেকে

```python
import sqlite3

conn = sqlite3.connect("school.db")

df = pd.read_sql(
    "SELECT * FROM Students",
    conn
)
```

---

Save SQL

```python
df.to_sql(
    "Students",
    conn,
    if_exists="replace",
    index=False
)
```

---

# Parquet

AI Project-এ অনেক ব্যবহৃত।

```python
df = pd.read_parquet(
    "students.parquet"
)
```

Save

```python
df.to_parquet(
    "students.parquet"
)
```

---

# Pickle

Python Object Save

```python
df.to_pickle(
    "students.pkl"
)
```

Load

```python
pd.read_pickle(
    "students.pkl"
)
```

---

# Compression

```python
df.to_csv(
    "students.csv.gz",
    compression="gzip"
)
```

---

# File Exists কিনা

```python
import os

os.path.exists(
    "students.csv"
)
```

---

# AI/ML Workflow

```
CSV File

↓

read_csv()

↓

DataFrame

↓

info()

↓

isna()

↓

Cleaning

↓

Feature Engineering

↓

Train Model
```

---

# সবচেয়ে বেশি ব্যবহৃত Functions

| Function         | কাজ          |
| ---------------- | ------------ |
| `read_csv()`     | CSV Load     |
| `to_csv()`       | CSV Save     |
| `read_excel()`   | Excel Load   |
| `to_excel()`     | Excel Save   |
| `read_json()`    | JSON Load    |
| `to_json()`      | JSON Save    |
| `read_sql()`     | SQL Load     |
| `to_sql()`       | SQL Save     |
| `read_parquet()` | Parquet Load |
| `to_parquet()`   | Parquet Save |
| `read_pickle()`  | Pickle Load  |
| `to_pickle()`    | Pickle Save  |

---

# AI Engineer হিসেবে যেগুলো অবশ্যই জানতে হবে ⭐⭐⭐⭐⭐

| Method        | গুরুত্ব |
| ------------- | ------- |
| `read_csv()`  | ⭐⭐⭐⭐⭐   |
| `head()`      | ⭐⭐⭐⭐⭐   |
| `tail()`      | ⭐⭐⭐⭐    |
| `info()`      | ⭐⭐⭐⭐⭐   |
| `describe()`  | ⭐⭐⭐⭐⭐   |
| `shape`       | ⭐⭐⭐⭐⭐   |
| `columns`     | ⭐⭐⭐⭐⭐   |
| `dtypes`      | ⭐⭐⭐⭐⭐   |
| `usecols`     | ⭐⭐⭐⭐    |
| `parse_dates` | ⭐⭐⭐⭐    |
| `dtype`       | ⭐⭐⭐⭐    |
| `na_values`   | ⭐⭐⭐⭐    |
| `chunksize`   | ⭐⭐⭐⭐    |
| `to_csv()`    | ⭐⭐⭐⭐⭐   |

---

# 🧠 এই অধ্যায় শেষে যা অবশ্যই জানতে হবে

* ✅ `read_csv()` দিয়ে CSV File Load করা
* ✅ `head()`, `tail()`, `shape`, `columns`, `info()`, `describe()` দিয়ে Dataset বুঝতে শেখা
* ✅ `usecols`, `nrows`, `skiprows`, `index_col` ব্যবহার
* ✅ `dtype`, `parse_dates`, `na_values` দিয়ে Data Load Control করা
* ✅ `to_csv()` দিয়ে Data Save করা
* ✅ Excel, JSON, SQL, Parquet-এর Basic Load/Save
* ✅ বড় Dataset-এর জন্য `chunksize` ব্যবহার
* ✅ AI/ML Project-এর শুরুতে Data Inspection Workflow

---

## ⏭️ শেষ অধ্যায়: `FeatureEngineering.py`

এটি Pandas-এর সবচেয়ে শক্তিশালী অধ্যায়। এখানে আমরা শিখব:

* `map()`
* `replace()`
* `apply()`
* `applymap()` (এবং Pandas 2.x-এ এর বিকল্প ব্যবহার)
* `transform()`
* `assign()`
* `cut()`
* `qcut()`
* `get_dummies()`
* Feature Creation
* Encoding Techniques
* AI/ML Feature Engineering Best Practices

এই অধ্যায় শেষ হলে আপনার **NumPy + Pandas** AI Engineering-এর জন্য একটি শক্ত ভিত্তি তৈরি হয়ে যাবে।
