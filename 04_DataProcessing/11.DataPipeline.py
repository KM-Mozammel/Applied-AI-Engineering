# Pipeline.py

```python id="pl001"
"""
=========================================================
Machine Learning Pipeline
=========================================================

এই ফাইল থেকে যা শিখবে

১. Pipeline কী?
২. কেন Pipeline ব্যবহার করা হয়?
৩. Pipeline-এর Structure
৪. fit(), transform(), predict()
৫. Pipeline বনাম Manual Processing
৬. Data Leakage কীভাবে এড়ায়?
৭. sklearn.pipeline.Pipeline
৮. AI/ML Project-এ Best Practice
=========================================================
"""
```

---

# 📖 Pipeline কী?

**Pipeline** হলো Machine Learning-এর এমন একটি ব্যবস্থা যেখানে **Data Processing-এর সব Step একসাথে একটি Flow-তে যুক্ত থাকে।**

অর্থাৎ

```text id="pl101"
Raw Data

↓

Missing Value

↓

Encoding

↓

Scaling

↓

Feature Selection

↓

Model Training
```

সবগুলো Step একসাথে কাজ করে।

---

# 🤔 কেন Pipeline দরকার?

ধরো,

তুমি প্রতিদিন সকালে অফিসে যাও।

তোমার কাজের ধাপ

```text id="pl102"
ঘুম থেকে ওঠা

↓

ব্রাশ করা

↓

গোসল করা

↓

নাস্তা করা

↓

অফিসে যাওয়া
```

তুমি প্রতিদিন এই একই ধাপ অনুসরণ করো।

Machine Learning-এও একই ব্যাপার।

প্রতিটি Dataset-এর জন্য

* Missing Value Handle
* Encoding
* Scaling
* Model Training

আলাদা আলাদা না লিখে

Pipeline-এ একবার লিখলেই হয়।

---

# 🔬 Real Life Example

ধরো,

একটি Car Factory।

```text id="pl103"
Raw Steel

↓

Cutting

↓

Painting

↓

Assembly

↓

Testing

↓

Ready Car
```

এটাই একটি Production Pipeline।

Machine Learning-এও একই ধারণা।

---

# 🧠 Core Concept

Without Pipeline

```text id="pl104"
Load Data

↓

Handle Missing Value

↓

Encode

↓

Scale

↓

Split

↓

Train

↓

Predict
```

সব Step আলাদা।

---

With Pipeline

```text id="pl105"
Pipeline

↓

সব Step Automatic
```

---

# Manual Processing

```python id="pl106"
# Missing Value

# Encoding

# Scaling

# Model Training

# Prediction
```

প্রতিটি Step নিজে নিজে লিখতে হবে।

---

# Pipeline Processing

```python id="pl107"
Pipeline(

Step 1

↓

Step 2

↓

Step 3

↓

Model
)
```

একবার লিখলেই সব কাজ হবে।

---

# 🐍 প্রথম Pipeline

```python id="pl108"
from sklearn.pipeline import Pipeline

from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression

pipeline = Pipeline([

    ("scaler", StandardScaler()),

    ("model", LogisticRegression())

])

print(pipeline)
```

---

এখানে

Pipeline-এর দুটি Step

```text id="pl109"
Step 1

↓

StandardScaler

Step 2

↓

LogisticRegression
```

---

# Pipeline Train করা

```python id="pl110"
pipeline.fit(X_train, y_train)
```

এটি

Automatic

```text id="pl111"
StandardScaler.fit()

↓

StandardScaler.transform()

↓

Model.fit()
```

সব করে দেয়।

---

# Prediction

```python id="pl112"
prediction = pipeline.predict(X_test)
```

এটি

Automatic

```text id="pl113"
StandardScaler.transform()

↓

Model.predict()
```

---

# Pipeline-এর Flow

```text id="pl114"
Training

↓

fit()

↓

Scaler শেখে

↓

Data Scale

↓

Model শেখে

-------------------

Testing

↓

predict()

↓

Scaler Apply

↓

Prediction
```

---

# Pipeline Data Leakage কীভাবে কমায়?

আগে আমরা শিখেছি

ভুল

```python id="pl115"
scaler.fit(X_train)

scaler.fit(X_test)
```

---

Pipeline

নিজেই

```text id="pl116"
Train

↓

fit()

↓

Test

↓

transform()
```

Follow করে।

এতে Data Leakage হওয়ার সম্ভাবনা কমে।

---

# Multiple Step Pipeline

```python id="pl117"
from sklearn.pipeline import Pipeline

from sklearn.impute import SimpleImputer

from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression

pipeline = Pipeline([

    ("imputer", SimpleImputer()),

    ("scaler", StandardScaler()),

    ("model", LogisticRegression())

])
```

Flow

```text id="pl118"
Missing Value

↓

Scaling

↓

Model
```

---

# Pipeline-এ PCA যোগ করা

```python id="pl119"
from sklearn.pipeline import Pipeline

from sklearn.preprocessing import StandardScaler

from sklearn.decomposition import PCA

from sklearn.linear_model import LogisticRegression

pipeline = Pipeline([

    ("scaler", StandardScaler()),

    ("pca", PCA(n_components=2)),

    ("model", LogisticRegression())

])
```

Flow

```text id="pl120"
Scaling

↓

PCA

↓

Model
```

---

# Pipeline-এর Step দেখা

```python id="pl121"
print(pipeline.named_steps)
```

Output

```text id="pl122"
scaler

pca

model
```

---

# নির্দিষ্ট Step Access করা

```python id="pl123"
pipeline.named_steps["scaler"]
```

---

# Pipeline-এর সুবিধা

✅ Code ছোট হয়।

---

✅ Repeat করা সহজ।

---

✅ Data Leakage কম হয়।

---

✅ Production Ready।

---

✅ Debug করা সহজ।

---

✅ Cross Validation সহজ।

---

# Pipeline-এর অসুবিধা

❌ শুরুতে একটু কঠিন মনে হতে পারে।

---

❌ Custom Processing লিখতে হলে Custom Transformer বানাতে হয়।

---

# 🤖 AI Example

Email Spam Detection

```text id="pl124"
Raw Email

↓

Text Cleaning

↓

TF-IDF

↓

Scaling (যদি প্রয়োজন হয়)

↓

Model

↓

Spam / Not Spam
```

এটাও একটি Pipeline।

---

# Real Project Pipeline

```text id="pl125"
CSV

↓

Missing Value

↓

Encoding

↓

Scaling

↓

Feature Selection

↓

PCA

↓

Model

↓

Prediction
```

---

# sklearn Pipeline Methods

| Method          | কাজ            |
| --------------- | -------------- |
| fit()           | Training       |
| transform()     | Data Transform |
| fit_transform() | দুটো একসাথে    |
| predict()       | Prediction     |
| score()         | Accuracy       |

---

# 🤖 AI Pipeline

```text id="pl126"
Load Dataset

↓

Train-Test Split

↓

Pipeline.fit()

↓

Prediction

↓

Evaluation
```

---

# ⚠️ Common Mistakes

### ❌ Train-Test Split-এর আগে Pipeline-এ পুরো Dataset Fit করা

ভুল।

আগে

```text id="pl127"
Train-Test Split
```

তারপর

```python id="pl128"
pipeline.fit(X_train, y_train)
```

---

### ❌ Pipeline ছাড়া Manual Processing

Production Project-এ এড়িয়ে চলা ভালো।

---

### ❌ Test Data-তে fit()

Pipeline ব্যবহার করলে এই ভুল হওয়ার সম্ভাবনা কমে।

---

# 🎯 Interview Questions

### ১. Pipeline কী?

Data Processing এবং Model Training-এর সব Step-কে একসাথে যুক্ত করার ব্যবস্থা।

---

### ২. Pipeline কেন ব্যবহার করা হয়?

* Code Clean হয়।
* Data Leakage কমে।
* Production Ready হয়।

---

### ৩. Pipeline-এর শেষ Step কী হয়?

সাধারণত

```text id="pl129"
Machine Learning Model
```

---

### ৪. Pipeline কি Prediction করতে পারে?

✅ হ্যাঁ।

```python id="pl130"
pipeline.predict()
```

---

### ৫. Pipeline কি Cross Validation-এর সাথে ব্যবহার করা যায়?

✅ হ্যাঁ।

এটাই Best Practice।

---

# 🚀 Practice Task

### Task ১

একটি Pipeline তৈরি করো।

```text id="pl131"
StandardScaler

↓

LogisticRegression
```

---

### Task ২

Pipeline-এ

```text id="pl132"
StandardScaler

↓

PCA

↓

LogisticRegression
```

যোগ করো।

---

### Task ৩

`pipeline.named_steps`

Print করো।

---

### Task ৪

`fit()`

এবং

`predict()`

ব্যবহার করো।

---

# 📌 মনে রাখার Shortcut

```text id="pl133"
Raw Data
     │
     ▼
Pipeline
     │
     ├── Missing Value
     ├── Encoding
     ├── Scaling
     ├── PCA
     └── Model
           │
           ▼
Prediction

Methods

fit()
transform()
fit_transform()
predict()
score()

✔ Clean Code
✔ Reusable
✔ Production Ready
✔ Data Leakage কম
```

---

# 🧠 Data Processing Journey (এ পর্যন্ত)

```text id="pl134"
Raw Dataset
      │
      ▼
Missing Value Handling
      │
      ▼
Encoding
(Label / One Hot / Target)
      │
      ▼
Train-Test Split
      │
      ▼
Feature Scaling
(Standard / MinMax / Robust)
      │
      ▼
PCA
      │
      ▼
Feature Selection
      │
      ▼
Pipeline
      │
      ▼
Machine Learning Model
```

---

# 🎯 Pipeline বনাম Manual Processing (Interview Summary)

| Manual Processing            | Pipeline         |
| ---------------------------- | ---------------- |
| অনেক Code                    | কম Code          |
| ভুল হওয়ার সম্ভাবনা বেশি      | কম               |
| Data Leakage-এর ঝুঁকি বেশি   | কম               |
| Production-এর জন্য কম উপযোগী | Production Ready |
| Maintain করা কঠিন            | Maintain করা সহজ |

---

## 🎯 পরবর্তী অধ্যায়: **`PipelineAutomation.py`**

এখানে আমরা শিখব কীভাবে **ColumnTransformer**, **Pipeline**, **GridSearchCV**, এবং **Joblib** একসাথে ব্যবহার করে একটি **Production-Level Automated Machine Learning Pipeline** তৈরি করা যায়। এটি Senior ML Engineer এবং AI Engineer Interview-এর জন্য অত্যন্ত গুরুত্বপূর্ণ একটি টপিক।
