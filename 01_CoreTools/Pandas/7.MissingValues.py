চলুন এবার **`7.MissingValues.py`** শুরু করি।

এটি Pandas-এর সবচেয়ে গুরুত্বপূর্ণ অধ্যায়গুলোর একটি। বাস্তব জীবনের প্রায় সব Dataset-এ Missing Value থাকে। Machine Learning Model ট্রেইন করার আগে এগুলো Handle করা বাধ্যতামূলক।

---

```python
# ==========================================================
# Pandas Missing Values (বাংলা)
# ==========================================================

# Missing Value কী?
# ----------------------------------------------------------
# Dataset-এর কোনো Cell-এ যদি Value না থাকে,
# তাহলে সেটিকে Missing Value বলে।
#
# Pandas সাধারণত Missing Value-কে NaN (Not a Number)
# হিসেবে দেখায়।
#
# উদাহরণ
#
# Name     Age
#
# Rahim    20
# Karim    NaN
# Hasan    22
#
# AI/ML এ ব্যবহার:
#
# - Data Cleaning
# - Feature Engineering
# - Model Training এর আগে Data Prepare করা
# - Missing Data Analysis
#
# গুরুত্বপূর্ণ:
# বেশিরভাগ ML Algorithm NaN গ্রহণ করতে পারে না।
# তাই Training এর আগে Missing Value Handle করতে হবে।
```

---

# Sample Dataset

```python
import pandas as pd
import numpy as np

students = pd.DataFrame({
    "Name": ["Rahim", "Karim", "Hasan", "Mitu", None],
    "Age": [20, np.nan, 22, 21, 19],
    "Marks": [85, 90, np.nan, 88, 70],
    "Department": ["CSE", None, "EEE", "CSE", "BBA"]
})

print(students)
```

Output

```
    Name   Age  Marks Department
0  Rahim 20.0   85.0      CSE
1  Karim NaN    90.0      NaN
2  Hasan 22.0   NaN       EEE
3  Mitu  21.0   88.0      CSE
4  None  19.0   70.0      BBA
```

---

# NaN কী?

NaN অর্থ

```
Not a Number
```

এটি Pandas-এর Missing Value Representation।

---

# None vs NaN

```python
import numpy as np

print(None)

print(np.nan)
```

Output

```
None

nan
```

Python-এ

```
None
```

Pandas Numeric Column-এ

```
NaN
```

---

# ১. isna()

Missing Value খুঁজে বের করে।

```python
students.isna()
```

Output

```
True

False

False

True
```

---

# ২. isnull()

`isna()` এর Alternative।

```python
students.isnull()
```

দুটো একই কাজ করে।

---

# ৩. notna()

যেগুলো Missing না।

```python
students.notna()
```

---

# ৪. Missing Value Count

```python
students.isna().sum()
```

Output

```
Name          1

Age           1

Marks         1

Department    1
```

---

# Total Missing Value

```python
students.isna().sum().sum()
```

Output

```
4
```

---

# ৫. Missing Row Filter

```python
students[
    students["Age"].isna()
]
```

---

# ৬. Not Missing Row

```python
students[
    students["Age"].notna()
]
```

---

# ৭. dropna()

Missing Row Delete

```python
students.dropna()
```

Output

শুধু যেসব Row-এ কোনো Missing নেই।

---

# ৮. axis

Row Delete

```python
students.dropna(axis=0)
```

Column Delete

```python
students.dropna(axis=1)
```

---

# ৯. how="all"

সবগুলো Value Missing হলে Delete করবে।

```python
students.dropna(how="all")
```

---

# ১০. how="any"

একটিও Missing থাকলে Delete।

```python
students.dropna(how="any")
```

---

# ১১. subset

শুধু নির্দিষ্ট Column Check করবে।

```python
students.dropna(
    subset=["Marks"]
)
```

---

# ১২. fillna()

Missing Value Fill করা।

```python
students.fillna(0)
```

---

# ১৩. Fill String

```python
students.fillna("Unknown")
```

---

# ১৪. Specific Column Fill

```python
students["Age"] = students["Age"].fillna(0)
```

---

# ১৫. Different Value

```python
students.fillna({
    "Age":0,
    "Marks":-1,
    "Department":"Unknown"
})
```

---

# ১৬. Mean দিয়ে Fill

```python
students["Age"] = students["Age"].fillna(
    students["Age"].mean()
)
```

Mean

```
সবগুলোর Average
```

---

# ১৭. Median দিয়ে Fill

```python
students["Age"] = students["Age"].fillna(
    students["Age"].median()
)
```

Median

```
মাঝের সংখ্যা
```

Outlier থাকলে Median ভালো।

---

# ১৮. Mode দিয়ে Fill

```python
students["Department"] = students["Department"].fillna(
    students["Department"].mode()[0]
)
```

Mode

```
সবচেয়ে বেশি ব্যবহৃত Value
```

Categorical Data-র জন্য খুব ভালো।

---

# ১৯. Forward Fill

```python
students.ffill()
```

উপরের Value নিচে Copy হবে।

Example

```
10

NaN

NaN

30
```

↓

```
10

10

10

30
```

---

# ২০. Backward Fill

```python
students.bfill()
```

নিচের Value উপরে Copy হবে।

---

# ২১. interpolate()

সংখ্যার মাঝে Value অনুমান করে।

```python
numbers = pd.DataFrame({
    "Value":[10,np.nan,30,40]
})

numbers.interpolate()
```

Output

```
10

20

30

40
```

---

# ২২. inplace=True

```python
students.fillna(
    0,
    inplace=True
)
```

মূল DataFrame পরিবর্তন হবে।

---

# ২৩. replace()

NaN Replace

```python
students.replace(
    np.nan,
    0
)
```

---

# ২৪. info()

Missing Value বুঝতে।

```python
students.info()
```

Output

```
Non-Null Count
```

খুব গুরুত্বপূর্ণ।

---

# ২৫. describe()

```python
students.describe()
```

Missing Value Ignore করে Statistics দেয়।

---

# Missing Value Visualization

```
Original

Age

20

NaN

22

↓

fillna(mean)

20

21

22
```

---

# Mean vs Median vs Mode

| Method | ব্যবহার                 |
| ------ | ----------------------- |
| Mean   | Numeric Continuous Data |
| Median | Outlier থাকলে           |
| Mode   | Categorical Data        |

---

# AI/ML এ বাস্তব ব্যবহার

## Age Fill

```python
df["Age"] = df["Age"].fillna(
    df["Age"].median()
)
```

---

## Salary Fill

```python
df["Salary"] = df["Salary"].fillna(
    df["Salary"].mean()
)
```

---

## Category Fill

```python
df["City"] = df["City"].fillna(
    "Unknown"
)
```

---

## Drop Empty Row

```python
df = df.dropna()
```

---

## Find Missing

```python
df.isna().sum()
```

---

# Missing Values Cheat Sheet

| Method          | কাজ                |
| --------------- | ------------------ |
| `isna()`        | Missing Check      |
| `isnull()`      | Missing Check      |
| `notna()`       | Not Missing        |
| `dropna()`      | Remove Missing     |
| `fillna()`      | Fill Missing       |
| `ffill()`       | Forward Fill       |
| `bfill()`       | Backward Fill      |
| `interpolate()` | Estimate Value     |
| `replace()`     | Replace NaN        |
| `info()`        | Non-Null Count     |
| `describe()`    | Summary Statistics |

---

# ⚠️ ML Best Practices

❌ সবসময় `dropna()` ব্যবহার করবেন না।

কারণ—

* অনেক Data হারিয়ে যেতে পারে।
* Dataset ছোট হয়ে যেতে পারে।
* Model-এর Performance কমে যেতে পারে।

সাধারণ নিয়ম:

* **Numeric Column** → Mean বা Median দিয়ে Fill করুন।
* **Categorical Column** → Mode বা `"Unknown"` দিয়ে Fill করুন।
* যদি কোনো Column-এর **৮০–৯০% এর বেশি Value Missing** থাকে, তাহলে সেই Column বাদ দেওয়ার কথা বিবেচনা করুন।

---

# 🧠 এই অধ্যায় শেষে যা অবশ্যই জানতে হবে

* ✅ `NaN`, `None` এবং Missing Value-এর ধারণা
* ✅ `isna()`, `isnull()`, `notna()`
* ✅ `dropna()` এর `axis`, `how`, `subset`
* ✅ `fillna()` বিভিন্ন উপায়ে ব্যবহার
* ✅ Mean, Median, Mode দিয়ে Missing Value পূরণ
* ✅ `ffill()`, `bfill()`, `interpolate()`
* ✅ `info()` দিয়ে Non-Null Count দেখা
* ✅ AI/ML-এ Missing Data Handling-এর Best Practices

---

## ⏭️ Pandas Core শেষ! এখন পরবর্তী ফাইলগুলো হবে

1. **`CSVLoading.py`** → CSV, Excel, JSON, SQL, Parquet ইত্যাদি Data Load ও Save
2. **`FeatureEngineering.py`** → `map()`, `apply()`, `applymap()` (বা `map()` DataFrame-এ নতুন API অনুযায়ী), `transform()`, `cut()`, `qcut()`, Encoding, Feature Creation ইত্যাদি।

এই দুইটি অধ্যায়ের পর আপনার **Pandas-এর ৯৫% বাস্তব ব্যবহার** সম্পন্ন হয়ে যাবে এবং আপনি NumPy + Pandas ব্যবহার করে AI/ML-এর Data Processing-এর জন্য প্রস্তুত থাকবেন।
