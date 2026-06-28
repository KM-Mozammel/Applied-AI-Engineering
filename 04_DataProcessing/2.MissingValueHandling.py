# MissingValueHandling.py

```python
"""
=========================================================
Missing Value Handling
=========================================================

এই ফাইল থেকে যা শিখবে

১. Missing Value কী?
২. কেন Missing Value হয়?
৩. Missing Value-এর সমস্যা
৪. Missing Value খুঁজে বের করা
৫. Missing Value Delete করা
৬. Mean, Median, Mode দিয়ে Fill করা
৭. Forward Fill (ffill)
৮. Backward Fill (bfill)
৯. Interpolation
১০. AI/ML Project-এ Best Practice
=========================================================
"""
```

---

# 📖 Missing Value কী?

যখন Dataset-এর কোনো Cell-এ Data থাকে না, তখন তাকে **Missing Value** বলে।

Python/Pandas-এ সাধারণত Missing Value নিচের যেকোনো একটি হতে পারে—

```text
NaN
None
pd.NA
```

---

## 🤔 কেন Missing Value হয়?

বাস্তব জীবনের Dataset কখনোই সম্পূর্ণ হয় না।

ধরো একটি Hospital Database আছে।

| Name  | Age | Weight |
| ----- | --- | ------ |
| Rahim | 25  | 60     |
| Karim | ❌   | 72     |
| Hasan | 35  | ❌      |

এখানে

Age এবং Weight Missing।

---

## বাস্তব কারণ

* User তথ্য দেয়নি
* Sensor Data হারিয়েছে
* Database Error
* Data Collection Error
* File Corrupted
* Manual Entry ভুল

---

# 🧠 Core Concept

Dataset

```text
Age

20

25

NaN

35

40

NaN
```

↓

Model

❌ Error হতে পারে

↓

প্রথমে Missing Value Handle করতে হবে।

---

# 🔬 Real Life Example

ধরো,

একজন Teacher ছাত্রদের Result বানাচ্ছেন।

| Name | Math |
| ---- | ---- |
| A    | 90   |
| B    | 80   |
| C    | ?    |
| D    | 95   |

এখন Average বের করতে গেলে

C-এর নম্বর নেই।

তখন Teacher তিনটি কাজ করতে পারেন।

১.

C-কে বাদ দেওয়া।

২.

Average নম্বর বসানো।

৩.

পরে নম্বর পাওয়া গেলে Update করা।

Machine Learning-এও ঠিক একই।

---

# 🤖 AI/ML Example

ধরো,

একটি House Price Dataset

| Size | Bedroom | Price |
| ---- | ------- | ----- |
| 1200 | 3       | 50L   |
| 1500 | NaN     | 65L   |
| 1800 | 4       | 80L   |

Bedroom Missing।

Model Training-এর আগে এটা ঠিক করতে হবে।

---

# 🐍 Sample Dataset

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name":["Rahim","Karim","Hasan","Sakib"],
    "Age":[25,np.nan,30,35],
    "Salary":[40000,50000,np.nan,60000]
})

print(df)
```

Output

```text
    Name   Age   Salary
0  Rahim  25.0  40000
1  Karim   NaN  50000
2  Hasan  30.0    NaN
3  Sakib  35.0  60000
```

---

# Missing Value খুঁজে বের করা

## isnull()

```python
print(df.isnull())
```

Output

```text
False False False

False True False

False False True

False False False
```

True মানে

Missing আছে।

---

## isna()

একই কাজ।

```python
print(df.isna())
```

---

## কতগুলো Missing আছে?

```python
print(df.isnull().sum())
```

Output

```text
Name      0
Age       1
Salary    1
```

---

## পুরো Dataset-এ Missing আছে?

```python
print(df.isnull().values.any())
```

Output

```text
True
```

---

# Missing Value Delete

## dropna()

```python
print(df.dropna())
```

Output

```text
শুধু যেসব Row-তে Missing নেই
সেগুলো থাকবে।
```

---

Example

Before

| Name  | Age | Salary |
| ----- | --- | ------ |
| Rahim | 25  | 40000  |
| Karim | NaN | 50000  |
| Hasan | 30  | NaN    |

↓

After

| Name  | Age | Salary |
| ----- | --- | ------ |
| Rahim | 25  | 40000  |

---

## নির্দিষ্ট Column Missing হলে Delete

```python
df.dropna(subset=["Age"])
```

---

## Column Delete

```python
df.drop(columns=["Salary"])
```

এটা Missing Handle নয়।

এটা পুরো Column Delete করে।

---

# Mean দিয়ে Fill

ধরো

Age

```text
20

25

NaN

35

40
```

Mean

```text
(20+25+35+40)/4

=

30
```

তাহলে

NaN

↓

30

---

Python

```python
df["Age"] = df["Age"].fillna(df["Age"].mean())
```

---

# Median দিয়ে Fill

যখন Outlier থাকে।

```python
df["Age"] = df["Age"].fillna(df["Age"].median())
```

---

# Mode দিয়ে Fill

Category Data-এর জন্য।

Example

```text
Red

Blue

Blue

NaN

Green
```

Mode

```text
Blue
```

Python

```python
df["Color"] = df["Color"].fillna(df["Color"].mode()[0])
```

---

# Constant Value দিয়ে Fill

```python
df["Age"] = df["Age"].fillna(0)
```

অথবা

```python
df["City"] = df["City"].fillna("Unknown")
```

---

# Forward Fill (ffill)

আগের Value ব্যবহার করবে।

Dataset

```text
10

20

NaN

NaN

50
```

↓

```text
10

20

20

20

50
```

Python

```python
df.ffill(inplace=True)
```

---

# Backward Fill (bfill)

পরের Value ব্যবহার করবে।

Dataset

```text
10

20

NaN

NaN

50
```

↓

```text
10

20

50

50

50
```

Python

```python
df.bfill(inplace=True)
```

---

# Interpolation

দুই পাশের Value দেখে মাঝখানের Value বের করে।

Dataset

```text
10

20

NaN

40

50
```

↓

```text
10

20

30

40

50
```

Python

```python
df.interpolate(inplace=True)
```

---

# কোন Method কখন ব্যবহার করবো?

| Data Type         | Best Method   |
| ----------------- | ------------- |
| Numeric           | Mean          |
| Numeric + Outlier | Median        |
| Category          | Mode          |
| Time Series       | ffill / bfill |
| Continuous Data   | Interpolation |

---

# ⚠️ Common Mistakes

❌ Missing Value না দেখে Model Train করা।

❌ Category Data-তে Mean ব্যবহার করা।

ভুল

```python
City

Dhaka

NaN

Chittagong
```

Mean সম্ভব না।

---

❌ Outlier থাকলেও Mean ব্যবহার করা।

Median ভালো।

---

❌ অনেক Missing থাকলেও Blindভাবে Fill করা।

---

# 🤖 Real AI Pipeline

```text
Load Dataset

↓

Check Missing Value

↓

Handle Missing Value

↓

Encoding

↓

Scaling

↓

Train-Test Split

↓

Model Training
```

> **নোট:** বাস্তব প্রজেক্টে অনেক Data Scientist প্রথমে `Train-Test Split` করেন, তারপর শুধুমাত্র Training Data থেকে Mean/Median শিখে Test Data-তে প্রয়োগ করেন। এতে **Data Leakage** এড়ানো যায়।

---

# 🎯 Interview Questions

### ১. Missing Value কী?

যে Cell-এ কোনো Data নেই তাকে Missing Value বলে।

---

### ২. Missing Value কীভাবে খুঁজবেন?

```python
isnull()

isna()

sum()
```

---

### ৩. Mean এবং Median-এর পার্থক্য?

Mean Average।

Median মাঝের Value।

Outlier থাকলে Median ভালো।

---

### ৪. Category Data-তে কোন Method?

Mode।

---

### ৫. Time Series Data-তে?

Forward Fill

Backward Fill

---

# 🚀 Practice Task

### Task ১

নিচের Dataset বানাও।

```python
Age

20

25

NaN

40

35
```

Mean দিয়ে Fill করো।

---

### Task ২

Color Column বানাও।

```text
Red

Blue

NaN

Blue

Green
```

Mode দিয়ে Fill করো।

---

### Task ৩

নিচের Data-তে `ffill()` এবং `bfill()` ব্যবহার করে Output তুলনা করো।

```text
10
20
NaN
NaN
50
```

---

### Task ৪

`isnull().sum()` ব্যবহার করে প্রতিটি Column-এ কতটি Missing Value আছে তা বের করো।

---

# 📌 মনে রাখার Shortcut

```text
Missing Value
      │
      ▼
Check
(isnull / isna)
      │
      ▼
Decision
      │
      ├── Delete → dropna()
      ├── Mean → fillna(mean)
      ├── Median → fillna(median)
      ├── Mode → fillna(mode)
      ├── Constant → fillna(value)
      ├── Forward Fill → ffill()
      ├── Backward Fill → bfill()
      └── Interpolation → interpolate()

Best Practice:
✔ Numeric → Mean/Median
✔ Categorical → Mode
✔ Time Series → ffill()/bfill()
✔ Always check missing values before training a model.
```

➡️ পরবর্তী অধ্যায়ে আমরা **`LabelEncoding.py`** শিখব। সেখানে দেখব কেন Machine Learning Model সরাসরি `"Male"`, `"Female"`, `"Dhaka"`, `"Blue"` ইত্যাদি String বুঝতে পারে না এবং কীভাবে এগুলোকে সংখ্যায় রূপান্তর করা হয়।
