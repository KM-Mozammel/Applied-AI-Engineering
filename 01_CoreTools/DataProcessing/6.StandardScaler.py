# StandardScaler.py

```python id="ss001"
"""
=========================================================
Standard Scaler
=========================================================

এই ফাইল থেকে যা শিখবে

১. Feature Scaling কী?
২. কেন Scaling দরকার?
৩. StandardScaler কী?
৪. Mean এবং Standard Deviation
৫. Z-Score Formula
৬. fit(), transform(), fit_transform()
৭. কোন Model-এ ব্যবহার করা হয়?
৮. AI/ML Project-এ Best Practice
=========================================================
"""
```

---

# 📖 Feature Scaling কী?

**Feature Scaling** হলো বিভিন্ন Feature-এর মানকে একই Scale বা Range-এ নিয়ে আসার প্রক্রিয়া।

ধরো,

| Age | Salary |
| --- | ------ |
| 20  | 30,000 |
| 25  | 50,000 |
| 30  | 80,000 |

এখানে

```text id="ss101"
Age

20-30
```

কিন্তু

```text id="ss102"
Salary

30000-80000
```

দুটি Feature-এর Scale সম্পূর্ণ আলাদা।

---

# 🤔 কেন Scaling দরকার?

Machine Learning Model সাধারণত Distance এবং Gradient-এর উপর কাজ করে।

যদি একটি Feature-এর মান

```text id="ss103"
20
```

এবং আরেকটি Feature-এর মান

```text id="ss104"
500000
```

হয়,

তাহলে Model Salary-কেই বেশি গুরুত্ব দিতে পারে।

Age প্রায় উপেক্ষিত হয়ে যেতে পারে।

---

# 🔬 Real Life Example

ধরো,

দুইজন মানুষ দড়ি টানছে।

একজনের শক্তি

```text id="ss105"
10
```

আরেকজনের

```text id="ss106"
1000
```

তাহলে

১০ শক্তির মানুষের প্রভাব প্রায় থাকবে না।

ঠিক Machine Learning-এও তাই।

বড় সংখ্যার Feature ছোট সংখ্যার Feature-কে চাপা দিতে পারে।

---

# 🧠 Core Concept

Original Data

| Age | Salary |
| --- | ------ |
| 20  | 30000  |
| 25  | 50000  |
| 30  | 80000  |

↓

StandardScaler

| Age   | Salary |
| ----- | ------ |
| -1.22 | -1.07  |
| 0.00  | -0.27  |
| 1.22  | 1.34   |

দেখো,

এখন দুটো Feature-ই প্রায় একই Scale-এ এসেছে।

---

# 📐 StandardScaler কী করে?

এটি প্রতিটি Feature-এর

* Mean = 0
* Standard Deviation = 1

করে দেয়।

---

# Mean কী?

Mean = Average

Example

```text id="ss107"
10

20

30
```

Mean

```text id="ss108"
(10+20+30)/3

=

20
```

---

# Standard Deviation কী?

এটি বলে

**ডেটা Mean থেকে কতটা ছড়িয়ে আছে।**

ছোট Standard Deviation

↓

সব Data কাছাকাছি।

বড় Standard Deviation

↓

Data অনেক ছড়িয়ে আছে।

---

# 📐 Z-Score Formula

StandardScaler-এর মূল Formula

```text id="ss109"
X'

=

(X - Mean)

/

Standard Deviation
```

এটাকে

**Z-Score Normalization**-ও বলা হয়।

---

# সহজ উদাহরণ

Age

```text id="ss110"
20

25

30
```

Mean

```text id="ss111"
25
```

Standard Deviation

ধরি

```text id="ss112"
5
```

তাহলে

Age = 20

```text id="ss113"
(20-25)/5

=

-1
```

Age = 25

```text id="ss114"
(25-25)/5

=

0
```

Age = 30

```text id="ss115"
(30-25)/5

=

1
```

---

# 🐍 প্রথম Example

```python id="ss116"
from sklearn.preprocessing import StandardScaler
import pandas as pd

df = pd.DataFrame({
    "Age": [20, 25, 30, 35, 40]
})

scaler = StandardScaler()

scaled = scaler.fit_transform(df)

print(scaled)
```

Output

```text id="ss117"
[[-1.41]

 [-0.71]

 [ 0.00]

 [ 0.71]

 [ 1.41]]
```

---

# একাধিক Feature

```python id="ss118"
import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.DataFrame({

    "Age":[20,25,30,35,40],

    "Salary":[30000,50000,70000,90000,110000]

})

scaler = StandardScaler()

scaled = scaler.fit_transform(df)

print(scaled)
```

---

# Output (ধারণাগত)

| Age   | Salary |
| ----- | ------ |
| -1.41 | -1.41  |
| -0.71 | -0.71  |
| 0     | 0      |
| 0.71  | 0.71   |
| 1.41  | 1.41   |

---

# fit() কী?

```python
scaler.fit(df)
```

এটি

শুধু

```text id="ss119"
Mean

Standard Deviation
```

শিখে রাখে।

কোনো Data পরিবর্তন করে না।

---

# transform()

```python
scaled = scaler.transform(df)
```

আগে শেখা Mean এবং Standard Deviation ব্যবহার করে Data Scale করে।

---

# fit_transform()

```python
scaled = scaler.fit_transform(df)
```

এক লাইনে

```text id="ss120"
fit()

+

transform()
```

---

# Train এবং Test Data

সবচেয়ে গুরুত্বপূর্ণ বিষয়।

ভুল

```python
scaler.fit(X_train)

scaler.fit(X_test)
```

এতে

Train-এর Mean

এবং

Test-এর Mean

আলাদা হবে।

---

সঠিক

```python
scaler.fit(X_train)

X_train = scaler.transform(X_train)

X_test = scaler.transform(X_test)
```

Test Data-তে কখনো

```python
fit()
```

করবে না।

---

# 🤖 AI Example

House Price Prediction

| Age | Salary |
| --- | ------ |
| 20  | 50000  |
| 25  | 100000 |

↓

Scaling

↓

Model Training

↓

Prediction

---

# কোন Model-এ StandardScaler দরকার?

✅ Distance Based Model

* KNN

* K-Means

* SVM

---

✅ Gradient Based Model

* Logistic Regression

* Linear Regression

* Neural Network

---

❌ সাধারণত প্রয়োজন হয় না

* Decision Tree

* Random Forest

* XGBoost

কারণ

এগুলো Distance-এর উপর নির্ভর করে না।

---

# ⚠️ Common Mistakes

### ❌ পুরো Dataset-এ fit() করা

আগে

```text id="ss121"
Train-Test Split
```

তারপর

```text id="ss122"
fit(X_train)
```

---

### ❌ Test Data-তে fit()

ভুল।

---

### ❌ Target (y)-কে Scale করা

সবসময় প্রয়োজন হয় না।

শুধু বিশেষ ক্ষেত্রে (কিছু Regression Problem) করা হয়।

---

# 🤖 AI Pipeline

```text id="ss123"
Dataset

↓

Missing Value

↓

Encoding

↓

Train-Test Split

↓

StandardScaler

↓

Model Training
```

---

# 🎯 Interview Questions

### ১. StandardScaler কী?

Feature-কে Mean = 0 এবং Standard Deviation = 1-এ রূপান্তর করে।

---

### ২. Formula কী?

```text id="ss124"
(X - Mean)

/

Standard Deviation
```

---

### ৩. fit() কী করে?

Mean এবং Standard Deviation শিখে।

---

### ৪. transform() কী করে?

শেখা Mean এবং Standard Deviation ব্যবহার করে Data Scale করে।

---

### ৫. Test Data-তে fit() করা যাবে?

❌ না।

শুধু

```python
transform()
```

করতে হবে।

---

# 🚀 Practice Task

### Task ১

নিচের Data Scale করো।

```python
Age

20

25

30

35

40
```

---

### Task ২

Age এবং Salary একসাথে Scale করো।

---

### Task ৩

`fit()`, `transform()`, `fit_transform()` আলাদা আলাদা ব্যবহার করে পার্থক্য দেখো।

---

### Task ৪

Train এবং Test Data আলাদা করে Scale করো।

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
```

ব্যবহার করো।

---

# 📌 মনে রাখার Shortcut

```text id="ss125"
Feature Scaling
        │
        ▼
StandardScaler
        │
        ▼
Mean = 0
Std  = 1

Formula

(X - Mean)
────────────
 Standard Deviation

Methods

fit()            → Mean & Std শিখে
transform()      → Data Scale করে
fit_transform()  → দুটো একসাথে

✔ KNN
✔ SVM
✔ Logistic Regression
✔ Neural Network

❌ Decision Tree
❌ Random Forest

সবসময় মনে রাখবে:

Train → fit + transform
Test  → শুধুমাত্র transform
```

---

## 🎯 পরবর্তী অধ্যায়

আমরা এখন **`MinMaxScaler.py`** শিখব, যেখানে Data-কে **0 থেকে 1** (বা অন্য নির্দিষ্ট Range)-এর মধ্যে নিয়ে আসা হয়। এরপর StandardScaler এবং MinMaxScaler-এর পার্থক্য, সুবিধা-অসুবিধা এবং কোন পরিস্থিতিতে কোনটি ব্যবহার করা উচিত তা বিস্তারিতভাবে শিখব।
