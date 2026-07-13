# RobustScaler.py

```python id="rs001"
"""
=========================================================
Robust Scaler
=========================================================

এই ফাইল থেকে যা শিখবে

১. RobustScaler কী?
২. Outlier কী?
৩. কেন StandardScaler ও MinMaxScaler সবসময় ভালো নয়?
৪. Median কী?
৫. Quartile (Q1, Q2, Q3)
৬. IQR (Interquartile Range)
৭. RobustScaler-এর Formula
৮. কোন Model-এ ব্যবহার করা হয়?
৯. AI/ML Project-এ Best Practice
=========================================================
"""
```

---

# 📖 RobustScaler কী?

**RobustScaler** হলো এমন একটি Feature Scaling Technique যা **Outlier-এর প্রভাব কমিয়ে Data Scale করে।**

এটি

* Mean ব্যবহার করে না।
* Standard Deviation ব্যবহার করে না।

বরং

* Median
* IQR (Interquartile Range)

ব্যবহার করে।

---

# 🤔 কেন RobustScaler দরকার?

ধরো Salary Dataset

| Salary  |
| ------- |
| 30000   |
| 35000   |
| 40000   |
| 45000   |
| 5000000 |

এখানে

```text id="rs101"
5000000
```

একটি **Outlier**।

---

যদি

StandardScaler

বা

MinMaxScaler

ব্যবহার করো,

তাহলে

5000000-এর জন্য

বাকি সব Salary প্রায় একই রকম ছোট হয়ে যাবে।

---

RobustScaler

এই সমস্যাকে অনেকটাই কমিয়ে দেয়।

---

# 📖 Outlier কী?

**Outlier** হলো এমন একটি Value যা বাকি Data থেকে অনেক দূরে থাকে।

---

Example

```text id="rs102"
10

12

15

14

13

11

500
```

এখানে

```text id="rs103"
500
```

Outlier।

---

আরেকটি Example

Employee Salary

```text id="rs104"
30000

32000

35000

36000

4000000
```

4000000

Outlier।

---

# 🔬 Real Life Example

ধরো,

একটি গ্রামের মানুষের মাসিক আয়

```text id="rs105"
15000

18000

17000

20000

22000
```

হঠাৎ

একজন Billionaire এসে থাকলেন

```text id="rs106"
500000000
```

এখন Average Income বের করলে

পুরো গ্রামের Average অস্বাভাবিক হয়ে যাবে।

কিন্তু

Median

প্রায় একই থাকবে।

এ কারণেই RobustScaler Median ব্যবহার করে।

---

# 🧠 Core Concept

Original Data

```text id="rs107"
10

12

13

14

15

500
```

↓

RobustScaler

↓

Outlier-এর প্রভাব কম।

---

# 📖 Median কী?

Median

=

মাঝের Value।

---

Example

```text id="rs108"
10

20

30

40

50
```

Median

```text id="rs109"
30
```

---

Outlier থাকলে

```text id="rs110"
10

20

30

40

1000
```

Median

এখনও

```text id="rs111"
30
```

কিন্তু

Mean

হয়ে যায়

220

দেখছো,

Mean বদলে গেছে,

Median প্রায় একই।

---

# 📖 Quartile কী?

Quartile

মানে

Data-কে

**৪ ভাগে ভাগ করা।**

---

Dataset

```text id="rs112"
10

20

30

40

50

60

70

80
```

---

Q1

```text id="rs113"
25%
```

অবস্থান।

---

Q2

```text id="rs114"
50%
```

অবস্থান।

এটাই Median।

---

Q3

```text id="rs115"
75%
```

অবস্থান।

---

Visual

```text id="rs116"
Min

│

Q1

│

Median(Q2)

│

Q3

│

Max
```

---

# 📖 IQR কী?

IQR

=

Interquartile Range

Formula

```text id="rs117"
IQR

=

Q3

-

Q1
```

---

Example

```text id="rs118"
Q1 = 20

Q3 = 60
```

তাহলে

```text id="rs119"
IQR

=

40
```

---

# 📐 RobustScaler Formula

```text id="rs120"
X'

=

(X - Median)

/

IQR
```

---

দেখো,

StandardScaler

ব্যবহার করে

```text id="rs121"
Mean

Std
```

---

RobustScaler

ব্যবহার করে

```text id="rs122"
Median

IQR
```

---

# 🐍 প্রথম Example

```python
from sklearn.preprocessing import RobustScaler
import pandas as pd

df = pd.DataFrame({
    "Salary": [
        30000,
        35000,
        40000,
        45000,
        5000000
    ]
})

scaler = RobustScaler()

scaled = scaler.fit_transform(df)

print(scaled)
```

---

Output

```text id="rs123"
Outlier থাকবে,

কিন্তু

বাকি Value

অস্বাভাবিকভাবে Compress হবে না।
```

---

# StandardScaler বনাম RobustScaler

Dataset

```text id="rs124"
10

20

30

40

1000
```

---

StandardScaler

↓

1000-এর জন্য

সব Value

অনেক ছোট হয়ে যাবে।

---

RobustScaler

↓

Median

এবং

IQR

ব্যবহার করবে।

↓

Outlier-এর প্রভাব কম হবে।

---

# তিনটি Scaler তুলনা

| Scaler         | কী ব্যবহার করে? | Outlier-এর প্রভাব |
| -------------- | --------------- | ----------------- |
| StandardScaler | Mean + Std      | বেশি              |
| MinMaxScaler   | Min + Max       | সবচেয়ে বেশি       |
| RobustScaler   | Median + IQR    | সবচেয়ে কম         |

---

# fit()

```python
scaler.fit(X_train)
```

শিখে

```text id="rs125"
Median

Q1

Q3

IQR
```

---

# transform()

```python
X_test = scaler.transform(X_test)
```

Scale করে।

---

# fit_transform()

```python
X_train = scaler.fit_transform(X_train)
```

এক লাইনে

```text id="rs126"
fit()

+

transform()
```

---

# Train এবং Test

সঠিক

```python
scaler.fit(X_train)

X_train = scaler.transform(X_train)

X_test = scaler.transform(X_test)
```

---

# 🤖 AI Example

Bank Fraud Detection

Transaction Amount

```text id="rs127"
100

120

150

200

500000
```

Outlier আছে।

↓

RobustScaler

↓

Model

---

# কোথায় ব্যবহার করবো?

✅

যখন

Dataset-এ

Outlier আছে।

---

যেমন

* Salary Prediction
* House Price
* Financial Data
* Medical Data
* Sensor Data

---

# কোথায় ব্যবহার করবো না?

যদি

Dataset

আগেই Clean হয়

এবং

Outlier না থাকে,

তাহলে

StandardScaler

যথেষ্ট।

---

# 🤖 AI Pipeline

```text id="rs128"
Dataset

↓

Missing Value

↓

Encoding

↓

Train-Test Split

↓

RobustScaler

↓

Model Training
```

---

# ⚠️ Common Mistakes

### ❌ Outlier না দেখেই Scaler নির্বাচন করা

প্রথমে

Dataset Explore করো।

তারপর সিদ্ধান্ত নাও।

---

### ❌ Test Data-তে fit()

ভুল।

---

### ❌ Train-Test Split-এর আগে Scaling

Data Leakage হতে পারে।

---

# 🎯 Interview Questions

### ১. RobustScaler কী?

Median এবং IQR ব্যবহার করে Data Scale করে।

---

### ২. কেন Median ব্যবহার করে?

কারণ

Median

Outlier-এর দ্বারা খুব কম প্রভাবিত হয়।

---

### ৩. IQR কী?

```text id="rs129"
Q3

-

Q1
```

---

### ৪. Outlier থাকলে কোন Scaler সবচেয়ে ভালো?

RobustScaler।

---

### ৫. StandardScaler এবং RobustScaler-এর পার্থক্য কী?

| StandardScaler    | RobustScaler       |
| ----------------- | ------------------ |
| Mean ব্যবহার করে  | Median ব্যবহার করে |
| Std ব্যবহার করে   | IQR ব্যবহার করে    |
| Outlier Sensitive | Outlier Resistant  |

---

# 🚀 Practice Task

### Task ১

নিচের Dataset Scale করো।

```text
10

20

30

40

1000
```

---

### Task ২

StandardScaler

এবং

RobustScaler

দিয়ে Output Compare করো।

---

### Task ৩

নিজে

Median

এবং

IQR

হিসাব করো।

---

### Task ৪

House Price Dataset-এ

একটি Outlier যোগ করে

তিনটি Scaler Compare করো।

---

# 📌 মনে রাখার Shortcut

```text id="rs130"
Dataset
      │
      ▼
Outlier আছে?

      │
 ┌────┴────┐
 │         │
না        হ্যাঁ
 │         │
 ▼         ▼
Standard  Robust
Scaler    Scaler

Formula

(X - Median)
──────────────
     IQR

Median = মাঝের Value
IQR = Q3 - Q1

✔ Financial Data
✔ Medical Data
✔ Salary Data
✔ House Price

Train → fit + transform
Test  → শুধুমাত্র transform
```

---

# 🧠 Feature Scaling Summary (এ পর্যন্ত)

| Scaler             | Formula                   | Outlier         | Output                        |
| ------------------ | ------------------------- | --------------- | ----------------------------- |
| **StandardScaler** | `(X - Mean) / Std`        | ❌ Sensitive     | Mean = 0, Std = 1             |
| **MinMaxScaler**   | `(X - Min) / (Max - Min)` | ❌ খুব Sensitive | নির্দিষ্ট Range (সাধারণত 0-1) |
| **RobustScaler**   | `(X - Median) / IQR`      | ✅ Resistant     | Median-কেন্দ্রিক Scaling      |

---

## 🎯 পরবর্তী অধ্যায়: `PCA.py`

এখন আমরা Data Processing-এর সবচেয়ে গুরুত্বপূর্ণ এবং Interview-তে সবচেয়ে বেশি জিজ্ঞাসিত একটি Topic শিখব—**Principal Component Analysis (PCA)**।

সেখানে আমরা ধাপে ধাপে শিখব:

* 📖 PCA কী?
* 🤔 কেন Dimension Reduction দরকার?
* 🧠 Principal Component কী?
* 📐 Eigenvector ও Eigenvalue-এর Intuition
* 📊 Explained Variance
* 🐍 `sklearn.decomposition.PCA`
* 🤖 AI/ML-এ PCA-এর বাস্তব ব্যবহার (Face Recognition, Image Compression, Feature Reduction)
