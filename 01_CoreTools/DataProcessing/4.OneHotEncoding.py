# OneHotEncoding.py

```python id="ohe001"
"""
=========================================================
One Hot Encoding
=========================================================

এই ফাইল থেকে যা শিখবে

১. One Hot Encoding কী?
২. কেন Label Encoding-এর পরিবর্তে One Hot Encoding ব্যবহার করা হয়?
৩. Dummy Variable কী?
৪. pd.get_dummies() ব্যবহার
৫. OneHotEncoder ব্যবহার
৬. drop_first কেন ব্যবহার করা হয়?
৭. AI/ML Project-এ Best Practice
=========================================================
"""
```

---

# 📖 One Hot Encoding কী?

**One Hot Encoding** হলো এমন একটি Encoding Technique যেখানে প্রতিটি Category-এর জন্য **আলাদা একটি Column তৈরি করা হয়।**

Category উপস্থিত থাকলে

```text
1
```

না থাকলে

```text
0
```

---

# 🤔 কেন দরকার?

আগের অধ্যায়ে আমরা দেখেছি

```text
Red

↓

0

Blue

↓

1

Green

↓

2
```

এখন Model ভাবতে পারে

```text
Green > Blue > Red
```

কারণ

```text
2 > 1 > 0
```

কিন্তু

বাস্তবে

```text
Red

Blue

Green
```

এর মধ্যে কোনো Rank নেই।

এই সমস্যার সমাধানই হলো

> **One Hot Encoding**

---

# 🧠 Core Concept

Dataset

| Color |
| ----- |
| Red   |
| Blue  |
| Green |

↓

One Hot Encoding

| Red | Blue | Green |
| --- | ---- | ----- |
| 1   | 0    | 0     |
| 0   | 1    | 0     |
| 0   | 0    | 1     |

এখানে

কোনো সংখ্যাই অন্য সংখ্যার চেয়ে বড় নয়।

সব Category সমান গুরুত্বপূর্ণ।

---

# 🔬 Real Life Example

ধরো,

একটি Room-এ তিনটি Light Switch আছে।

```text
Red Light

Blue Light

Green Light
```

যদি

Red Light ON হয়

তাহলে

```text
Red    = 1

Blue   = 0

Green  = 0
```

যদি

Blue Light ON হয়

```text
Red    = 0

Blue   = 1

Green  = 0
```

Machine Learning-এও ঠিক একইভাবে কাজ করে।

---

# 🤖 AI/ML Example

ধরো

একটি Animal Dataset

| Animal |
| ------ |
| Cat    |
| Dog    |
| Bird   |

↓

Encoding

| Cat | Dog | Bird |
| --- | --- | ---- |
| 1   | 0   | 0    |
| 0   | 1   | 0    |
| 0   | 0   | 1    |

এখন Model বুঝতে পারবে

Cat এবং Dog-এর মধ্যে কোনো ছোট-বড় সম্পর্ক নেই।

---

# 🐍 প্রথম Example

```python
import pandas as pd

df = pd.DataFrame({
    "Color": ["Red", "Blue", "Green", "Blue", "Red"]
})

encoded = pd.get_dummies(df)

print(encoded)
```

---

## Output

```text
   Color_Blue  Color_Green  Color_Red

0           0            0          1

1           1            0          0

2           0            1          0

3           1            0          0

4           0            0          1
```

---

# শুধুমাত্র একটি Column Encode

```python
encoded = pd.get_dummies(
    df,
    columns=["Color"]
)

print(encoded)
```

---

# একাধিক Column Encode

```python
import pandas as pd

df = pd.DataFrame({

    "Gender": ["Male","Female","Male"],

    "City": ["Dhaka","Rajshahi","Dhaka"]

})

encoded = pd.get_dummies(
    df,
    columns=["Gender","City"]
)

print(encoded)
```

Output

```text
Gender_Female

Gender_Male

City_Dhaka

City_Rajshahi
```

---

# Dummy Variable কী?

One Hot Encoding-এর মাধ্যমে তৈরি হওয়া প্রতিটি নতুন Column-কে

**Dummy Variable**

বলা হয়।

যেমন

```text
Color

↓

Color_Red

Color_Blue

Color_Green
```

---

# OneHotEncoder (Scikit-Learn)

Machine Learning Pipeline-এ সাধারণত এটা ব্যবহার করা হয়।

```python
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder()

data = [["Red"],

        ["Blue"],

        ["Green"]]

result = encoder.fit_transform(data)

print(result.toarray())
```

Output

```text
[[0. 0. 1.]

 [1. 0. 0.]

 [0. 1. 0.]]
```

---

# drop_first=True কেন ব্যবহার করা হয়?

ধরো

| Color |
| ----- |
| Red   |
| Blue  |
| Green |

Encoding করলে

| Red | Blue | Green |
| --- | ---- | ----- |
| 1   | 0    | 0     |
| 0   | 1    | 0     |
| 0   | 0    | 1     |

এখানে

```text
Red + Blue + Green = 1
```

সবসময় সত্য।

তাই

একটি Column বাদ দিলেও

বাকি Column দেখে

বাদ দেওয়া Column-এর মান বের করা যায়।

---

Python

```python
encoded = pd.get_dummies(
    df,
    drop_first=True
)
```

Output

```text
Blue

Green
```

Red Column থাকবে না।

---

# কেন এটা করা হয়?

এটাকে বলে

> **Dummy Variable Trap**

যখন একটি Dummy Variable অন্য Dummy Variable থেকে সম্পূর্ণভাবে নির্ণয় করা যায়, তখন তাদের মধ্যে **Perfect Correlation** তৈরি হয়।

বিশেষ করে **Linear Regression**-এর মতো কিছু Model-এ এটি সমস্যা তৈরি করতে পারে।

---

# Label Encoding বনাম One Hot Encoding

| Label Encoding            | One Hot Encoding          |
| ------------------------- | ------------------------- |
| String → Number           | String → Multiple Columns |
| False Ordering হতে পারে   | কোনো Ordering নেই         |
| কম Memory লাগে            | বেশি Memory লাগে          |
| Ordinal Data-এর জন্য ভালো | Nominal Data-এর জন্য ভালো |

---

# Ordinal বনাম Nominal

## Ordinal

```text
Small

Medium

Large
```

এখানে

Order আছে।

↓

Label Encoding

---

## Nominal

```text
Red

Blue

Green
```

এখানে

Order নেই।

↓

One Hot Encoding

---

# 🤖 AI Pipeline

```text
Dataset

↓

Missing Value

↓

Encoding

    │

    ├── Ordinal

    │      │

    │      ▼

    │ Label Encoding

    │

    └── Nominal

           │

           ▼

     One Hot Encoding

↓

Scaling

↓

Model Training
```

---

# ⚠️ Common Mistakes

### ❌ সব Data-তে One Hot Encoding করা

যদি

```text
Country
```

Column-এ

১০,০০০টি Unique Value থাকে,

তাহলে

১০,০০০টি নতুন Column তৈরি হবে।

এটাকে বলে

> **High Cardinality Problem**

---

### ❌ Ordinal Data-তে One Hot Encoding করা

```text
Small

Medium

Large
```

এখানে Label Encoding ভালো।

---

### ❌ Training এবং Test আলাদাভাবে Encode করা

সবসময়

```python
fit()

↓

transform()
```

ব্যবহার করবে।

---

# 🎯 Interview Questions

### ১. One Hot Encoding কী?

প্রতিটি Category-এর জন্য আলাদা Binary Column তৈরি করার পদ্ধতি।

---

### ২. কেন ব্যবহার করা হয়?

False Ordering দূর করার জন্য।

---

### ৩. Dummy Variable কী?

Encoding-এর পরে তৈরি হওয়া Binary Column।

---

### ৪. drop_first কেন ব্যবহার করা হয়?

Dummy Variable Trap এড়ানোর জন্য।

---

### ৫. One Hot Encoding-এর অসুবিধা কী?

অনেক Unique Value থাকলে অনেক Column তৈরি হয়।

---

# 🚀 Practice Task

### Task ১

নিচের Data Encode করো।

```text
Color

Red

Blue

Green

Blue

Red
```

---

### Task ২

`pd.get_dummies()` ব্যবহার করো।

---

### Task ৩

`drop_first=True` ব্যবহার করে Output তুলনা করো।

---

### Task ৪

নিচের Data-এর জন্য কোন Encoding ব্যবহার করবে?

```text
Education

Primary

Secondary

Bachelor

Master
```

---

### Task ৫

নিচের Data-এর জন্য?

```text
Country

Bangladesh

India

Japan

USA
```

---

# 📌 মনে রাখার Shortcut

```text
Categorical Data
        │
        ▼
Order আছে?
        │
   ┌────┴────┐
   │         │
  হ্যাঁ      না
   │         │
   ▼         ▼
Label     One Hot
Encoding  Encoding

One Hot Encoding:

Red
Blue
Green

↓

Red Blue Green

1    0     0

0    1     0

0    0     1

✔ Nominal Data-এর জন্য সেরা
✔ False Ordering নেই
✔ Dummy Variable তৈরি হয়
❌ বেশি Unique Value হলে অনেক Column তৈরি হয়
```

---

## 🎯 পরবর্তী অধ্যায়: `TargetEncoding.py`

এখানে আমরা শিখব **Target Encoding**—যেটি High Cardinality (যেমন: ১০,০০০টি City, Product ID, User ID) Categorical Data-এর জন্য একটি শক্তিশালী Encoding Technique। পাশাপাশি বুঝব কেন এটি শক্তিশালী হলেও **Data Leakage**-এর ঝুঁকি থাকে এবং কীভাবে নিরাপদভাবে ব্যবহার করতে হয়।
