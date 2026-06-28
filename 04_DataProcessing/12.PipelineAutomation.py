# PipelineAutomation.py

```python
"""
=========================================================
Production-Level Machine Learning Pipeline Automation
=========================================================

এই ফাইল থেকে যা শিখবে

১. Pipeline Automation কী?
২. কেন Automation দরকার?
৩. ColumnTransformer কী?
৪. Numeric এবং Categorical Feature আলাদা করা
৫. Complete Pipeline তৈরি করা
৬. GridSearchCV দিয়ে Hyperparameter Tuning
৭. Joblib দিয়ে Model Save করা
৮. Production Deployment Flow
৯. Best Practice
=========================================================
"""
```

---

# 📖 Pipeline Automation কী?

**Pipeline Automation** হলো এমন একটি ব্যবস্থা যেখানে

* Data Cleaning
* Missing Value Handling
* Encoding
* Scaling
* Feature Selection
* Model Training
* Hyperparameter Tuning

সবকিছু **Automatic** হয়ে যায়।

অর্থাৎ

একটি মাত্র

```python
pipeline.fit(X_train, y_train)
```

চালালেই

সব Step

নিজে নিজে Execute হবে।

---

# 🤔 কেন Automation দরকার?

ধরো,

তুমি একটি Restaurant-এ কাজ করো।

একটি Burger বানানোর Step

```text
Order

↓

Bread

↓

Patty

↓

Cheese

↓

Sauce

↓

Packing

↓

Delivery
```

প্রতিবার যদি সব Step হাতে করতে হয়,

তাহলে

* সময় বেশি লাগবে
* ভুল হবে
* Consistency থাকবে না

তাই

Burger Machine

↓

সবকিছু Automatic করে।

Machine Learning Pipeline-ও একইভাবে কাজ করে।

---

# 🧠 Real Project-এর Data

ধরো,

একটি Employee Dataset

| Age | Salary | City   | Gender | Experience | Target |
| --- | ------ | ------ | ------ | ---------- | ------ |
| 25  | 40000  | Dhaka  | Male   | 2          | 1      |
| 30  | 60000  | Khulna | Female | 5          | 0      |

এখানে

Numeric Feature

```text
Age

Salary

Experience
```

Categorical Feature

```text
City

Gender
```

---

# 🤔 সমস্যা কোথায়?

Numeric Data

↓

Scaling দরকার।

---

Categorical Data

↓

Encoding দরকার।

---

দুই ধরনের Data-এর জন্য

দুই ধরনের Processing লাগবে।

---

# 📖 ColumnTransformer কী?

**ColumnTransformer**

একই Dataset-এর

**ভিন্ন Column-এর জন্য ভিন্ন Processing করার ব্যবস্থা।**

---

Visual

```text
Dataset
      │
      ├──────────────┐
      │              │
      ▼              ▼
Numeric       Categorical
      │              │
Standard      OneHot
Scaler        Encoder
      │              │
      └──────┬───────┘
             ▼
      Combined Dataset
```

---

# 🐍 প্রথম ColumnTransformer

```python
from sklearn.compose import ColumnTransformer

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder

preprocessor = ColumnTransformer(

    transformers=[

        (
            "num",
            StandardScaler(),
            ["Age", "Salary"]
        ),

        (
            "cat",
            OneHotEncoder(),
            ["City"]
        )

    ]

)
```

---

এখানে

Numeric Column

↓

StandardScaler

---

Categorical Column

↓

OneHotEncoder

---

তারপর

দুটো আবার

একসাথে Merge হবে।

---

# 📖 Pipeline + ColumnTransformer

```python
from sklearn.pipeline import Pipeline

from sklearn.compose import ColumnTransformer

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder

from sklearn.linear_model import LogisticRegression

preprocessor = ColumnTransformer(

    [

        (
            "num",
            StandardScaler(),
            ["Age", "Salary"]
        ),

        (
            "cat",
            OneHotEncoder(),
            ["City"]
        )

    ]

)

pipeline = Pipeline(

    [

        ("preprocessing", preprocessor),

        ("model", LogisticRegression())

    ]

)
```

---

Flow

```text
Dataset

↓

ColumnTransformer

↓

Scaling

+

Encoding

↓

Logistic Regression
```

---

# Training

```python
pipeline.fit(X_train, y_train)
```

Automatic

```text
Scaling

↓

Encoding

↓

Model Training
```

---

# Prediction

```python
prediction = pipeline.predict(X_test)
```

Automatic

```text
Scaling

↓

Encoding

↓

Prediction
```

---

# 📖 Hyperparameter Tuning কী?

আগে আমরা

নিজে নিজে

Parameter দিতাম।

```python
LogisticRegression(
    C=1
)
```

কিন্তু

Best Parameter

কোনটি?

---

Machine নিজেই বের করতে পারে।

---

# GridSearchCV

Visual

```text
Model

↓

C = 0.1

↓

Accuracy

↓

C = 1

↓

Accuracy

↓

C = 10

↓

Accuracy

↓

Best Parameter
```

---

# 🐍 GridSearchCV Example

```python
from sklearn.model_selection import GridSearchCV

parameters = {

    "model__C": [
        0.1,
        1,
        10
    ]

}

grid = GridSearchCV(

    pipeline,

    param_grid=parameters,

    cv=5

)

grid.fit(X_train, y_train)
```

---

Best Parameter

```python
print(grid.best_params_)
```

Output

```text
{'model__C':1}
```

---

Best Accuracy

```python
print(grid.best_score_)
```

---

# 📖 Cross Validation

আগে

একবার

Train

↓

একবার

Test

---

Cross Validation

```text
Fold 1

Fold 2

Fold 3

Fold 4

Fold 5
```

প্রতিবার

Train/Test বদলায়।

↓

আরও Reliable Result পাওয়া যায়।

---

# 📖 Joblib কী?

Training করতে

কখনও

২ ঘণ্টা

বা

১০ ঘণ্টা

লাগতে পারে।

প্রতিবার আবার Training কেন?

---

Joblib

↓

Model Save করে।

---

# Save Model

```python
import joblib

joblib.dump(

    pipeline,

    "model.pkl"

)
```

---

# আবার Load করা

```python
model = joblib.load(
    "model.pkl"
)
```

---

Prediction

```python
model.predict(X_test)
```

আবার Training লাগবে না।

---

# 🤖 Production Flow

```text
CSV

↓

Pipeline

↓

Train

↓

Best Model

↓

Save (.pkl)

↓

API

↓

Prediction
```

---

# 🤖 FastAPI Example

```python
prediction = model.predict(
    new_data
)
```

User

↓

Prediction

↓

Response

---

# Complete Production Pipeline

```text
CSV

↓

Train-Test Split

↓

ColumnTransformer

├── Numeric

│     ↓

│ StandardScaler

│

└── Categorical

      ↓

 OneHotEncoder

↓

Pipeline

↓

GridSearchCV

↓

Best Model

↓

Joblib

↓

FastAPI

↓

Prediction
```

---

# AI Engineer Workflow

```text
Business Problem

↓

Collect Data

↓

EDA

↓

Missing Value

↓

Encoding

↓

Scaling

↓

Feature Selection

↓

Pipeline

↓

GridSearchCV

↓

Evaluation

↓

Save Model

↓

Deploy API

↓

Prediction
```

---

# ⚠️ Common Mistakes

### ❌ Numeric Feature-এ OneHotEncoder দেওয়া

ভুল।

---

### ❌ Categorical Feature-এ StandardScaler দেওয়া

ভুল।

---

### ❌ Model Save না করা

Production-এ সমস্যা হবে।

---

### ❌ Manual Processing করা

Production-এ সবসময় Pipeline ব্যবহার করো।

---

# 🎯 Interview Questions

### ১. ColumnTransformer কী?

একই Dataset-এর ভিন্ন Column-এর জন্য ভিন্ন Preprocessing করার ব্যবস্থা।

---

### ২. GridSearchCV কী?

Best Hyperparameter খুঁজে বের করার Algorithm।

---

### ৩. Joblib কেন ব্যবহার করা হয়?

Trained Model Save এবং পরে Load করার জন্য।

---

### ৪. Pipeline Automation-এর সুবিধা কী?

* Automation
* Clean Code
* Data Leakage কম
* Production Ready

---

### ৫. Production ML Pipeline-এর সাধারণ ধাপ কী?

```text
Data

↓

Preprocessing

↓

Training

↓

Evaluation

↓

Save Model

↓

Deploy

↓

Prediction
```

---

# 🚀 Practice Task

### Task ১

একটি Dataset তৈরি করো যেখানে থাকবে

```text
Age

Salary

City

Target
```

ColumnTransformer ব্যবহার করে

* Age, Salary → `StandardScaler`
* City → `OneHotEncoder`

---

### Task ২

উপরের Preprocessor-কে `Pipeline`-এর সাথে যুক্ত করো।

---

### Task ৩

`GridSearchCV` ব্যবহার করে `LogisticRegression`-এর `C` Parameter-এর Best Value বের করো।

---

### Task ৪

Train করা Pipeline-কে

```python
joblib.dump()
```

দিয়ে Save করো।

---

### Task ৫

`joblib.load()` দিয়ে Model Load করে নতুন Data-তে Prediction করো।

---

# 📌 মনে রাখার Shortcut

```text
Raw Dataset
      │
      ▼
Train-Test Split
      │
      ▼
ColumnTransformer
      │
      ├── Numeric
      │      │
      │      ▼
      │ StandardScaler
      │
      └── Categorical
             │
             ▼
      OneHotEncoder
             │
             ▼
Pipeline
      │
      ▼
GridSearchCV
      │
      ▼
Best Model
      │
      ▼
Joblib (.pkl)
      │
      ▼
FastAPI / Flask
      │
      ▼
Prediction

✔ Production Ready
✔ Automated
✔ Reusable
✔ Easy Deployment
✔ Data Leakage কম
```

---

# 🎓 Data Processing Roadmap (Completed)

```text
Raw Dataset
      │
      ▼
Load Data (Pandas)
      │
      ▼
EDA (Explore Data)
      │
      ▼
Missing Value Handling
      │
      ▼
Encoding
├── Label Encoding
├── One-Hot Encoding
└── Target Encoding
      │
      ▼
Train-Test Split
      │
      ▼
Feature Scaling
├── StandardScaler
├── MinMaxScaler
└── RobustScaler
      │
      ▼
PCA (Dimension Reduction)
      │
      ▼
Feature Selection
      │
      ▼
Pipeline
      │
      ▼
ColumnTransformer
      │
      ▼
GridSearchCV
      │
      ▼
Joblib
      │
      ▼
Production Deployment
```

---

# 🎯 পরবর্তী অধ্যায় (Model Building শুরু)

এখন Data Processing সম্পূর্ণ হয়েছে। পরবর্তী ধাপে আমরা **Machine Learning Models** শেখা শুরু করব। শেখার আদর্শ ক্রম হবে:

1. **Linear Regression** (Regression-এর ভিত্তি)
2. **Logistic Regression** (Classification-এর ভিত্তি)
3. **K-Nearest Neighbors (KNN)**
4. **Decision Tree**
5. **Random Forest**
6. **Support Vector Machine (SVM)**
7. **Naive Bayes**
8. **K-Means Clustering**
9. **Ensemble Learning (Bagging, Boosting, XGBoost)**
10. **Model Evaluation Metrics**

এটি Machine Learning-এর মূল অংশ, যেখানে প্রতিটি অ্যালগরিদমকে একই স্টাইলে—**Concept → Intuition → Mathematics → Python → Real AI Example → Interview Questions → Practice**—শিখব।
