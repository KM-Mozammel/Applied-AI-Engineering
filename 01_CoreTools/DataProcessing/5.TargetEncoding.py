# TargetEncoding.py

```python id="te001"
"""
=========================================================
Target Encoding
=========================================================

এই ফাইল থেকে যা শিখবে

১. Target Encoding কী?
২. কেন One Hot Encoding-এর বিকল্প হিসেবে ব্যবহার করা হয়?
৩. Target Mean কী?
৪. High Cardinality কী?
৫. Data Leakage কী?
৬. Target Encoding-এর সুবিধা ও অসুবিধা
৭. AI/ML Project-এ Best Practice
=========================================================
"""
```

---

# 📖 Target Encoding কী?

**Target Encoding** হলো এমন একটি Encoding Technique যেখানে প্রতিটি Category-কে তার **Target Variable-এর Average (Mean)** দিয়ে Replace করা হয়।

অর্থাৎ

Category

↓

Target-এর Average

---

# 🤔 কেন দরকার?

আগের অধ্যায়ে আমরা দেখেছি

One Hot Encoding

```text id="te101"
Red

Blue

Green
```

↓

```text id="te102"
Red

Blue

Green

↓

3টি নতুন Column
```

কিন্তু যদি

```text id="te103"
১০,০০০টি City
```

থাকে?

তাহলে

```text id="te104"
১০,০০০টি নতুন Column
```

তৈরি হবে।

এতে

* Memory বেশি লাগবে।
* Training ধীর হবে।
* Model জটিল হবে।

এই সমস্যার সমাধান হলো

> **Target Encoding**

---

# 🧠 Core Concept

ধরো Dataset

| City     | Salary |
| -------- | ------ |
| Dhaka    | 50     |
| Dhaka    | 70     |
| Khulna   | 30     |
| Khulna   | 50     |
| Rajshahi | 80     |

---

প্রথমে প্রতিটি City-এর Average Salary বের করি।

Dhaka

```text id="te105"
(50+70)/2

=

60
```

Khulna

```text id="te106"
(30+50)/2

=

40
```

Rajshahi

```text id="te107"
80
```

---

Encoding-এর পরে

| City |
| ---- |
| 60   |
| 60   |
| 40   |
| 40   |
| 80   |

---

# 🔬 Real Life Example

ধরো,

একটি Restaurant Rating Dataset আছে।

| Restaurant | Rating |
| ---------- | ------ |
| A          | 5      |
| A          | 4      |
| B          | 2      |
| B          | 3      |
| C          | 5      |

Target Encoding করলে

Restaurant A

↓

Average Rating

```text id="te108"
(5+4)/2

=

4.5
```

Restaurant B

↓

```text id="te109"
2.5
```

Restaurant C

↓

```text id="te110"
5
```

---

# 🤖 AI/ML Example

ধরো

House Price Prediction

| City   | Price |
| ------ | ----- |
| Dhaka  | 80    |
| Dhaka  | 90    |
| Khulna | 40    |
| Khulna | 50    |

Encoding করলে

| City |
| ---- |
| 85   |
| 85   |
| 45   |
| 45   |

Model এখন String-এর পরিবর্তে Meaningful Number পাচ্ছে।

---

# 🐍 Manual Example

```python
import pandas as pd

df = pd.DataFrame({

    "City": [
        "Dhaka",
        "Dhaka",
        "Khulna",
        "Khulna",
        "Rajshahi"
    ],

    "Salary": [
        50,
        70,
        30,
        50,
        80
    ]
})

mean_encoding = df.groupby("City")["Salary"].mean()

print(mean_encoding)
```

Output

```text
City

Dhaka       60

Khulna      40

Rajshahi    80
```

---

# Mapping করা

```python
df["City"] = df["City"].map(mean_encoding)

print(df)
```

Output

| City | Salary |
| ---- | ------ |
| 60   | 50     |
| 60   | 70     |
| 40   | 30     |
| 40   | 50     |
| 80   | 80     |

---

# groupby() কীভাবে কাজ করলো?

```python
mean_encoding = (
    df
    .groupby("City")["Salary"]
    .mean()
)
```

এখানে

```text id="te111"
groupby()

↓

একই City-কে একসাথে করলো

↓

mean()

↓

Average বের করলো
```

---

# High Cardinality কী?

Cardinality মানে

**কতগুলো Unique Category আছে।**

যেমন

```text
Gender

Male

Female
```

Unique

```text
2
```

Low Cardinality

---

আর যদি

```text
Product ID

P00001

P00002

...

P50000
```

Unique

```text
50000
```

High Cardinality

---

# কেন Target Encoding ভালো?

One Hot Encoding

```text
50000 Product

↓

50000 Column
```

Target Encoding

```text
50000 Product

↓

1 Column
```

---

# ⚠️ সবচেয়ে গুরুত্বপূর্ণ বিষয়

## Data Leakage

এটা Interview-এর সবচেয়ে জনপ্রিয় প্রশ্নগুলোর একটি।

---

ধরো

Model Train করার আগে

পুরো Dataset-এর Mean বের করলে

Test Data-এর Information-ও Encoding-এর মধ্যে চলে আসবে।

এটাকে বলে

> **Data Leakage**

---

ভুল

```text
Train

+

Test

↓

Average বের করা
```

---

সঠিক

```text
Train

↓

Average বের করা

↓

Test-এ Apply করা
```

---

# Scikit-Learn-এ কেন নেই?

`LabelEncoder` এবং `OneHotEncoder` আছে।

কিন্তু

```text
TargetEncoder
```

অনেক দিন পর্যন্ত Scikit-Learn-এ ছিল না (অনেকে `category_encoders` লাইব্রেরি ব্যবহার করত)।

কারণ

এটি ভুলভাবে ব্যবহার করলে Data Leakage হওয়ার ঝুঁকি বেশি।

---

# Label vs One Hot vs Target

| Feature          | Label      | One Hot     | Target     |
| ---------------- | ---------- | ----------- | ---------- |
| Output           | ১টি Column | অনেক Column | ১টি Column |
| Ordering         | হতে পারে   | না          | না         |
| Memory           | কম         | বেশি        | কম         |
| High Cardinality | খারাপ      | খুব খারাপ   | খুব ভালো   |

---

# Target Encoding কখন ব্যবহার করবো?

✅

যখন

```text
City

Product ID

User ID

Zip Code

Company
```

এবং

হাজার হাজার Unique Value থাকে।

---

❌

যদি

```text
Gender

Yes/No

True/False
```

হয়,

তাহলে Target Encoding দরকার নেই।

---

# 🤖 AI Pipeline

```text
Dataset

↓

Train-Test Split

↓

Training Data

↓

Target Encoding শেখা

↓

Training Data Encode

↓

Test Data Encode

↓

Model Training
```

> **খেয়াল করো:** Target Encoding-এর আগে **Train-Test Split** করা খুব গুরুত্বপূর্ণ, যাতে Test Data-এর তথ্য Training-এর মধ্যে না চলে আসে।

---

# ⚠️ Common Mistakes

### ❌ পুরো Dataset-এর Mean ব্যবহার করা

এতে

Data Leakage হবে।

---

### ❌ Low Cardinality Data-তে Target Encoding করা

Gender

↓

Target Encoding

প্রয়োজন নেই।

---

### ❌ Missing Value Handle না করে Encoding করা

আগে

```text
Missing Value

↓

তারপর Encoding
```

---

# 🎯 Interview Questions

### ১. Target Encoding কী?

প্রতিটি Category-কে Target-এর Average দিয়ে Replace করা।

---

### ২. One Hot Encoding-এর তুলনায় সুবিধা কী?

অনেক Column তৈরি করে না।

---

### ৩. High Cardinality কী?

যখন অনেক Unique Category থাকে।

---

### ৪. সবচেয়ে বড় ঝুঁকি কী?

Data Leakage।

---

### ৫. Data Leakage কীভাবে এড়াবো?

শুধু Training Data-তে Mean শিখে, সেই Mapping Test Data-তে Apply করবো।

---

# 🚀 Practice Task

### Task ১

নিচের Dataset তৈরি করো।

| City     | Salary |
| -------- | ------ |
| Dhaka    | 50     |
| Dhaka    | 70     |
| Khulna   | 30     |
| Khulna   | 50     |
| Rajshahi | 80     |

`groupby()` ব্যবহার করে প্রতিটি City-এর Average Salary বের করো।

---

### Task ২

`map()` ব্যবহার করে City-কে Average Salary দিয়ে Replace করো।

---

### Task ৩

ভাবো,

১০,০০০টি Product ID থাকলে

One Hot Encoding ভালো হবে

নাকি

Target Encoding?

কেন?

---

### Task ৪

নিচের Data-এর জন্য কোন Encoding ব্যবহার করবে?

```text
Gender

Male

Female
```

---

### Task ৫

নিচের Data-এর জন্য?

```text
ProductID

P1001

P1002

P1003

...

P50000
```

---

# 📌 মনে রাখার Shortcut

```text id="te999"
Categorical Data
        │
        ▼
Unique Value কত?

        │
 ┌──────┴─────────┐
 │                │
 কম              অনেক
 │                │
 ▼                ▼
One Hot      Target Encoding

Target Encoding

Category
      │
      ▼
Target-এর Mean
      │
      ▼
একটি Numeric Column

✔ High Cardinality-এর জন্য সেরা
✔ Memory কম লাগে
✔ Column বাড়ে না

⚠️ সবচেয়ে বড় সতর্কতা:
শুধু Training Data থেকে Mean শিখবে।
নাহলে Data Leakage হবে।
```

---

# 🎓 Encoding Techniques Summary (এ পর্যন্ত)

| Technique            | কবে ব্যবহার করবেন                                 |
| -------------------- | ------------------------------------------------- |
| **Label Encoding**   | Ordinal Data (Small, Medium, Large)               |
| **One Hot Encoding** | Nominal Data (Color, Country, Gender)             |
| **Target Encoding**  | High Cardinality Data (City, Product ID, User ID) |

---

## 🎯 পরবর্তী অধ্যায়: `StandardScaler.py`

এখানে আমরা শিখব **Feature Scaling**-এর সবচেয়ে গুরুত্বপূর্ণ ধারণা। বুঝব কেন Machine Learning Model-এ `Age = 25` এবং `Salary = 500000` একসাথে দিলে সমস্যা হয়, এবং কীভাবে **StandardScaler** ডেটাকে Mean = 0 এবং Standard Deviation = 1-এ রূপান্তর করে Model-এর Training আরও কার্যকর করে।
