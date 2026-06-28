# MinMaxScaler.py

```python id="mms001"
"""
=========================================================
MinMax Scaler
=========================================================

এই ফাইল থেকে যা শিখবে

১. MinMaxScaler কী?
২. Feature Scaling কেন দরকার?
৩. Min-Max Formula
৪. Feature Range কী?
৫. fit(), transform(), fit_transform()
৬. StandardScaler vs MinMaxScaler
৭. AI/ML Project-এ Best Practice
=========================================================
"""
```

---

# 📖 MinMaxScaler কী?

**MinMaxScaler** হলো এমন একটি Feature Scaling Technique যা প্রতিটি Feature-এর মানকে একটি নির্দিষ্ট Range-এর মধ্যে নিয়ে আসে।

সাধারণত

```text id="mms101"
0

থেকে

1
```

এর মধ্যে।

---

# 🤔 কেন দরকার?

ধরো একটি Dataset

| Age | Salary |
| --- | ------ |
| 20  | 30000  |
| 25  | 50000  |
| 30  | 70000  |

এখানে

```text id="mms102"
Age

20-30
```

কিন্তু

```text id="mms103"
Salary

30000-70000
```

Machine Learning Model Salary-কেই বেশি গুরুত্ব দিতে পারে।

তাই

দুটোকেই

```text id="mms104"
0

↓

1
```

Range-এ নিয়ে আসি।

---

# 🧠 Core Concept

Original Data

| Age |
| --- |
| 20  |
| 25  |
| 30  |
| 35  |
| 40  |

↓

MinMaxScaler

| Age  |
| ---- |
| 0.00 |
| 0.25 |
| 0.50 |
| 0.75 |
| 1.00 |

---

# 🔬 Real Life Example

ধরো,

একটি Exam-এর Full Mark

```text id="mms105"
100
```

Rahim পেয়েছে

```text id="mms106"
80
```

তাহলে

Percentage

```text id="mms107"
80 / 100

=

0.80
```

MinMaxScaler-ও ঠিক একইভাবে কাজ করে।

সব Value-কে একটি নির্দিষ্ট Range-এর মধ্যে নিয়ে আসে।

---

# 📐 Formula

MinMaxScaler-এর Formula

```text id="mms108"
X'

=

(X - Minimum)

/

(Maximum - Minimum)
```

---

# Step by Step Example

Dataset

```text id="mms109"
10

20

30

40

50
```

Minimum

```text id="mms110"
10
```

Maximum

```text id="mms111"
50
```

---

ধরো

Value = 30

Formula

```text id="mms112"
(30 - 10)

/

(50 - 10)

=

20 / 40

=

0.5
```

---

সবগুলো Value

| Original | Scaled |
| -------- | ------ |
| 10       | 0.00   |
| 20       | 0.25   |
| 30       | 0.50   |
| 40       | 0.75   |
| 50       | 1.00   |

---

# 🐍 প্রথম Example

```python id="mms113"
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

df = pd.DataFrame({
    "Age": [20, 25, 30, 35, 40]
})

scaler = MinMaxScaler()

scaled = scaler.fit_transform(df)

print(scaled)
```

Output

```text id="mms114"
[[0.00]

 [0.25]

 [0.50]

 [0.75]

 [1.00]]
```

---

# একাধিক Feature

```python id="mms115"
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.DataFrame({

    "Age":[20,25,30,35,40],

    "Salary":[30000,50000,70000,90000,110000]

})

scaler = MinMaxScaler()

scaled = scaler.fit_transform(df)

print(scaled)
```

---

ধারণাগত Output

| Age  | Salary |
| ---- | ------ |
| 0.00 | 0.00   |
| 0.25 | 0.25   |
| 0.50 | 0.50   |
| 0.75 | 0.75   |
| 1.00 | 1.00   |

---

# Feature Range পরিবর্তন করা

Default Range

```text id="mms116"
0

↓

1
```

কিন্তু চাইলে

```text id="mms117"
-1

↓

1
```

করতে পারি।

---

```python id="mms118"
scaler = MinMaxScaler(
    feature_range=(-1, 1)
)

scaled = scaler.fit_transform(df)
```

---

Output (ধারণাগত)

| Original | Scaled |
| -------- | ------ |
| 20       | -1.0   |
| 25       | -0.5   |
| 30       | 0.0    |
| 35       | 0.5    |
| 40       | 1.0    |

---

# fit()

```python id="mms119"
scaler.fit(df)
```

এটি শিখে

```text id="mms120"
Minimum

Maximum
```

---

# transform()

```python id="mms121"
scaled = scaler.transform(df)
```

আগে শেখা Minimum এবং Maximum ব্যবহার করে Data Scale করে।

---

# fit_transform()

```python id="mms122"
scaled = scaler.fit_transform(df)
```

এক লাইনে

```text id="mms123"
fit()

+

transform()
```

---

# Train এবং Test Data

ভুল

```python id="mms124"
scaler.fit(X_train)

scaler.fit(X_test)
```

---

সঠিক

```python id="mms125"
scaler.fit(X_train)

X_train = scaler.transform(X_train)

X_test = scaler.transform(X_test)
```

---

# 🤖 AI Example

Image Processing

Pixel Value

```text id="mms126"
0

↓

255
```

↓

MinMaxScaler

↓

```text id="mms127"
0.0

↓

1.0
```

এটি Deep Learning-এ খুবই সাধারণ।

---

# StandardScaler vs MinMaxScaler

| StandardScaler            | MinMaxScaler                    |
| ------------------------- | ------------------------------- |
| Mean = 0                  | Min = 0                         |
| Std = 1                   | Max = 1                         |
| Negative Value থাকতে পারে | সব Value নির্দিষ্ট Range-এ থাকে |
| Outlier-এর প্রভাব বেশি    | Outlier-এর প্রভাব বেশি          |
| Z-Score ব্যবহার করে       | Min-Max Formula ব্যবহার করে     |

---

# কখন কোনটি ব্যবহার করবো?

## ✅ MinMaxScaler

যখন

* Neural Network
* Deep Learning
* Image Processing
* Feature-এর Range নির্দিষ্ট রাখতে চাই

---

## ✅ StandardScaler

যখন

* Linear Regression
* Logistic Regression
* SVM
* KNN
* PCA

---

# ⚠️ Outlier-এর সমস্যা

Dataset

```text id="mms128"
10

20

30

40

1000
```

Minimum

```text id="mms129"
10
```

Maximum

```text id="mms130"
1000
```

এখন

20

↓

খুব ছোট Number হয়ে যাবে।

কারণ

1000 একটি Outlier।

তাই

MinMaxScaler

Outlier-এর জন্য খুব Sensitive।

---

# 🤖 AI Pipeline

```text id="mms131"
Dataset

↓

Missing Value

↓

Encoding

↓

Train-Test Split

↓

MinMaxScaler

↓

Model Training
```

---

# ⚠️ Common Mistakes

### ❌ Test Data-তে fit()

ভুল।

---

### ❌ Outlier থাকলেও MinMaxScaler ব্যবহার করা

এক্ষেত্রে

```text id="mms132"
RobustScaler
```

ভালো হতে পারে।

---

### ❌ Train-Test Split-এর আগে Scaling করা

ভুল।

এতে

Data Leakage

হতে পারে।

---

# 🎯 Interview Questions

### ১. MinMaxScaler কী?

Feature-কে নির্দিষ্ট Range (সাধারণত 0-1)-এ নিয়ে আসে।

---

### ২. Formula কী?

```text id="mms133"
(X - Min)

/

(Max - Min)
```

---

### ৩. Default Range কী?

```text id="mms134"
0

↓

1
```

---

### ৪. Feature Range পরিবর্তন করা যায়?

✅ হ্যাঁ।

```python id="mms135"
feature_range=(-1,1)
```

---

### ৫. Outlier থাকলে MinMaxScaler ভালো?

❌ না।

---

# 🚀 Practice Task

### Task ১

নিচের Data Scale করো।

```text id="mms136"
10

20

30

40

50
```

---

### Task ২

Age এবং Salary Scale করো।

---

### Task ৩

`feature_range=(-1,1)` ব্যবহার করো।

---

### Task ৪

StandardScaler এবং MinMaxScaler-এর Output তুলনা করো।

---

### Task ৫

নিচের Data-তে Outlier-এর প্রভাব পর্যবেক্ষণ করো।

```text id="mms137"
10

20

30

40

1000
```

---

# 📌 মনে রাখার Shortcut

```text id="mms138"
Feature Scaling
        │
        ▼
MinMaxScaler
        │
        ▼
Min → 0
Max → 1

Formula

(X - Min)
────────────
(Max - Min)

Methods

fit()            → Min & Max শিখে
transform()      → Data Scale করে
fit_transform()  → দুটো একসাথে

✔ Neural Network
✔ Deep Learning
✔ Image Processing

❌ Outlier থাকলে সতর্ক

Train → fit + transform
Test  → শুধুমাত্র transform
```

---

# 🧠 StandardScaler vs MinMaxScaler (Interview Summary)

| বিষয়          | StandardScaler     | MinMaxScaler              |
| ------------- | ------------------ | ------------------------- |
| Formula       | `(X - Mean) / Std` | `(X - Min) / (Max - Min)` |
| Output Range  | নির্দিষ্ট নয়       | সাধারণত 0 থেকে 1          |
| Mean          | 0                  | নির্দিষ্ট নয়              |
| Std           | 1                  | নির্দিষ্ট নয়              |
| Outlier       | প্রভাবিত হয়        | আরও বেশি প্রভাবিত হয়      |
| Deep Learning | ব্যবহার করা যায়    | **খুব জনপ্রিয়**           |
| KNN / SVM     | **খুব জনপ্রিয়**    | ব্যবহার করা যায়           |

---

## 🎯 পরবর্তী অধ্যায়: `RobustScaler.py`

এখানে আমরা শিখব **RobustScaler**, যা **Outlier (অস্বাভাবিক বড় বা ছোট মান)** থাকলেও ভালোভাবে Feature Scaling করতে পারে। পাশাপাশি Median, Quartile, IQR (Interquartile Range) কী এবং কেন RobustScaler Outlier-এর ক্ষেত্রে StandardScaler ও MinMaxScaler-এর চেয়ে ভালো কাজ করে, তা বিস্তারিতভাবে বুঝব।
