# FeatureSelection.py

```python id="fs001"
"""
=========================================================
Feature Selection
=========================================================

এই ফাইল থেকে যা শিখবে

১. Feature Selection কী?
২. কেন Feature Selection দরকার?
৩. Feature Selection vs PCA
৪. Feature Importance
৫. Correlation Based Selection
৬. Filter Method
৭. Wrapper Method
৮. Embedded Method
৯. sklearn Feature Selection
১০. AI/ML Project-এ Best Practice
=========================================================
"""
```

---

# 📖 Feature Selection কী?

**Feature Selection** হলো Dataset থেকে **সবচেয়ে গুরুত্বপূর্ণ Feature-গুলো নির্বাচন করা এবং অপ্রয়োজনীয় Feature বাদ দেওয়ার প্রক্রিয়া।**

অর্থাৎ

```text id="fs101"
১০০টি Feature

↓

৩০টি সবচেয়ে গুরুত্বপূর্ণ Feature
```

---

# 🤔 কেন Feature Selection দরকার?

ধরো,

একটি Student Dataset

| Name | Roll | Height | Weight | BMI | Salary |
| ---- | ---- | ------ | ------ | --- | ------ |

এখানে

```text id="fs102"
Name

Roll
```

Prediction-এর জন্য হয়তো কোনো কাজে লাগবে না।

আবার

```text id="fs103"
Weight

BMI
```

একই ধরনের Information দিতে পারে।

সব Feature ব্যবহার করলে

* Training ধীর হবে।
* Memory বেশি লাগবে।
* Overfitting হতে পারে।
* Noise বাড়বে।

তাই প্রয়োজনীয় Feature বেছে নেওয়া হয়।

---

# 🧠 Core Concept

Original Dataset

```text id="fs104"
Age

Height

Weight

BMI

Salary

Name

Phone

Address
```

↓

Feature Selection

↓

```text id="fs105"
Age

Height

Weight

Salary
```

---

# 🔬 Real Life Example

ধরো,

তুমি একজন ক্রিকেটার নির্বাচন করছো।

তোমার কাছে তথ্য আছে

```text id="fs106"
নাম

জার্সি নম্বর

উচ্চতা

Batting Average

Bowling Average

চুলের রং

প্রিয় খাবার
```

একজন ভালো ক্রিকেটার নির্বাচন করতে

```text id="fs107"
চুলের রং

প্রিয় খাবার
```

কোনো কাজে লাগবে না।

তুমি রাখবে

```text id="fs108"
Batting Average

Bowling Average
```

ঠিক Feature Selection-ও তাই করে।

---

# 🤖 AI Example

House Price Prediction

Dataset

| Area | Bedroom | Bathroom | Owner Name | House Color | Price |
| ---- | ------- | -------- | ---------- | ----------- | ----- |

Model-এর জন্য

```text id="fs109"
Owner Name
```

হয়তো প্রয়োজন নেই।

কিন্তু

```text id="fs110"
Area

Bedroom

Bathroom
```

খুব গুরুত্বপূর্ণ।

---

# 🧠 Feature Selection vs PCA

এটি Interview-এর সবচেয়ে Common Question।

| Feature Selection     | PCA                               |
| --------------------- | --------------------------------- |
| Original Feature রাখে | নতুন Feature তৈরি করে             |
| কিছু Feature বাদ দেয়  | সব Feature মিশিয়ে Component বানায় |
| সহজে Explain করা যায়  | Explain করা কঠিন                  |
| Feature-এর নাম থাকে   | Feature-এর নাম থাকে না            |

---

### উদাহরণ

Original

| Age | Salary | Height |

---

Feature Selection

↓

| Age | Salary |

Height বাদ।

---

PCA

↓

| PC1 | PC2 |

Age, Salary, Height

সব মিশে গেছে।

---

# 📖 Feature Importance কী?

Feature Importance

মানে

**কোন Feature Prediction-এর জন্য কতটা গুরুত্বপূর্ণ।**

Example

House Price

| Feature    | Importance |
| ---------- | ---------- |
| Area       | 90%        |
| Bedroom    | 70%        |
| Garage     | 30%        |
| Owner Name | 1%         |

↓

Owner Name বাদ দেওয়া যায়।

---

# 📖 Correlation কী?

Correlation

মানে

দুটি Feature

কতটা সম্পর্কযুক্ত।

---

Example

| Height | Weight |
| ------ | ------ |
| 170    | 70     |
| 175    | 74     |
| 180    | 80     |

Height বাড়লে

Weight-ও বাড়ছে।

↓

Positive Correlation

---

Example

| Temperature | Jacket Sales |
| ----------- | ------------ |
| 35°C        | 10           |
| 20°C        | 100          |

Temperature কমলে

Jacket Sales বাড়ছে।

↓

Negative Correlation

---

# Correlation Matrix

```python
import pandas as pd

print(df.corr(numeric_only=True))
```

Output (উদাহরণ)

|            | Age  | Salary | Experience |
| ---------- | ---- | ------ | ---------- |
| Age        | 1.00 | 0.80   | 0.75       |
| Salary     | 0.80 | 1.00   | 0.90       |
| Experience | 0.75 | 0.90   | 1.00       |

---

যদি

```text id="fs111"
Correlation

=

0.99
```

হয়,

তাহলে

দুটি Feature প্রায় একই Information দিচ্ছে।

একটি বাদ দেওয়া যায়।

---

# 📖 Feature Selection-এর ৩টি Method

---

# ১️⃣ Filter Method

সবচেয়ে সহজ Method।

Model Train করার আগেই Feature নির্বাচন করা হয়।

Example

* Correlation
* Chi-Square Test
* ANOVA
* Mutual Information

---

Python

```python
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif

selector = SelectKBest(
    score_func=f_classif,
    k=2
)

X_new = selector.fit_transform(X, y)
```

---

# ২️⃣ Wrapper Method

এখানে

Model বারবার Train করা হয়।

তারপর

সেরা Feature নির্বাচন করা হয়।

সবচেয়ে জনপ্রিয়

```text id="fs112"
Recursive Feature Elimination

(RFE)
```

---

Python

```python
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression

model = LinearRegression()

selector = RFE(
    estimator=model,
    n_features_to_select=2
)

X_new = selector.fit_transform(X, y)
```

---

# ৩️⃣ Embedded Method

Model নিজেই Feature Importance বের করে।

সবচেয়ে জনপ্রিয়

* Random Forest
* XGBoost
* LightGBM
* Lasso Regression

---

Python

```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()

model.fit(X, y)

print(model.feature_importances_)
```

Output

```text
[0.42

0.31

0.20

0.07]
```

---

# কোন Method কখন ব্যবহার করবো?

| Method   | Speed | Accuracy |
| -------- | ----- | -------- |
| Filter   | ⭐⭐⭐⭐⭐ | ⭐⭐⭐      |
| Wrapper  | ⭐⭐    | ⭐⭐⭐⭐⭐    |
| Embedded | ⭐⭐⭐⭐  | ⭐⭐⭐⭐     |

---

# 🤖 AI Example

Spam Detection

Original Feature

```text id="fs113"
5000 Words
```

↓

Feature Selection

↓

```text id="fs114"
300 Important Words
```

↓

Model দ্রুত Train হবে।

---

# AI Pipeline

```text id="fs115"
Dataset

↓

Missing Value

↓

Encoding

↓

Train-Test Split

↓

Scaling

↓

Feature Selection

↓

Model Training
```

---

# ⚠️ Common Mistakes

### ❌ Name, ID, Phone Number Model-এ দেওয়া

এগুলো সাধারণত Prediction-এর জন্য কাজে আসে না।

---

### ❌ PCA এবং Feature Selection একই ভাবা

দুটো সম্পূর্ণ আলাদা।

---

### ❌ পুরো Dataset ব্যবহার করে Feature Selection করা

সঠিক Pipeline

```text
Train-Test Split

↓

Feature Selection (Train)

↓

Test-এ Apply
```

কারণ

Data Leakage হতে পারে।

---

# 🎯 Interview Questions

### ১. Feature Selection কী?

গুরুত্বপূর্ণ Feature রেখে অপ্রয়োজনীয় Feature বাদ দেওয়া।

---

### ২. PCA এবং Feature Selection-এর পার্থক্য কী?

Feature Selection Original Feature রাখে।

PCA নতুন Feature তৈরি করে।

---

### ৩. Correlation কী?

দুটি Feature-এর মধ্যে সম্পর্কের পরিমাণ।

---

### ৪. সবচেয়ে জনপ্রিয় তিনটি Method কী?

* Filter
* Wrapper
* Embedded

---

### ৫. Random Forest কীভাবে Feature Selection-এ সাহায্য করে?

এটি প্রতিটি Feature-এর Importance Score বের করে দেয়।

---

# 🚀 Practice Task

### Task ১

একটি Dataset তৈরি করো যেখানে থাকবে

```text
Age

Salary

Experience

Height
```

`corr()` ব্যবহার করে Correlation Matrix বের করো।

---

### Task ২

`SelectKBest()` ব্যবহার করে সবচেয়ে গুরুত্বপূর্ণ ২টি Feature নির্বাচন করো।

---

### Task ৩

`RandomForestClassifier` ব্যবহার করে Feature Importance বের করো।

---

### Task ৪

Feature Selection এবং PCA-এর Output Compare করো।

---

# 📌 মনে রাখার Shortcut

```text
Original Dataset
        │
        ▼
Feature Selection
        │
        ▼
শুধু গুরুত্বপূর্ণ Feature

Methods

Filter
│
├── Correlation
├── Chi-Square
└── ANOVA

Wrapper
│
└── RFE

Embedded
│
├── Random Forest
├── XGBoost
└── Lasso

✔ Training Faster
✔ Overfitting কম
✔ Explain করা সহজ

Feature Selection
    ≠
PCA
```

---

# 🧠 PCA vs Feature Selection (Final Summary)

| বিষয়                  | PCA | Feature Selection |
| --------------------- | --- | ----------------- |
| Feature কমায়          | ✅   | ✅                 |
| Original Feature রাখে | ❌   | ✅                 |
| নতুন Feature তৈরি করে | ✅   | ❌                 |
| Explain করা সহজ       | ❌   | ✅                 |
| Noise কমায়            | ✅   | কিছুটা            |
| Data Compression      | ✅   | ❌                 |

---

## 🎯 পরবর্তী অধ্যায়: **`Pipeline.py`**

এটি পুরো **Data Processing** অধ্যায়ের সবচেয়ে গুরুত্বপূর্ণ অংশ।

এখানে আমরা শিখব কীভাবে একটি **Production-ready Machine Learning Pipeline** তৈরি করতে হয়, যেখানে একসাথে থাকবে:

* 📖 `Pipeline` কী?
* 🤔 কেন Pipeline ব্যবহার করা হয়?
* 🧹 Missing Value Handling
* 🏷️ Encoding
* 📏 Scaling
* 🧠 Feature Selection
* 🤖 Model Training

সবকিছু **একটি Pipeline-এর মাধ্যমে** করা হবে—যেটি বাস্তব Machine Learning Project এবং Interview-তে অত্যন্ত গুরুত্বপূর্ণ।
