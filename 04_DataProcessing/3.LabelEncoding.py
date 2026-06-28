# LabelEncoding.py

```python
"""
=========================================================
Label Encoding
=========================================================

এই ফাইল থেকে যা শিখবে

১. Label Encoding কী?
২. কেন দরকার?
৩. Machine Learning কেন String বুঝতে পারে না?
৪. LabelEncoder কীভাবে কাজ করে?
৫. Label Encoding-এর সুবিধা ও অসুবিধা
৬. Label Encoding কখন ব্যবহার করা উচিত?
৭. AI/ML Project-এ Best Practice
=========================================================
"""
```

---

# 📖 Label Encoding কী?

**Label Encoding** হলো এমন একটি পদ্ধতি যেখানে **Categorical (String) Data-কে Integer Number-এ রূপান্তর করা হয়।**

যেমন

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

এখানে প্রতিটি Category-কে একটি Unique Number দেওয়া হয়েছে।

---

# 🤔 কেন দরকার?

Machine Learning Model মূলত **গণিত (Mathematics)** করে।

সে যোগ, বিয়োগ, গুণ, ভাগ, Matrix Multiplication করতে পারে।

কিন্তু

```text
"Red"

"Blue"

"Green"
```

এই String-এর উপর কোনো Mathematical Operation করা যায় না।

তাই এগুলোকে আগে সংখ্যায় রূপান্তর করতে হয়।

---

# 🧠 Core Concept

ধরো Dataset

| Color |
| ----- |
| Red   |
| Blue  |
| Green |
| Blue  |
| Red   |

↓

Label Encoding

| Color |
| ----- |
| 2     |
| 0     |
| 1     |
| 0     |
| 2     |

এখন Model সহজেই এগুলো ব্যবহার করতে পারবে।

---

# 🔬 Real Life Example

ধরো একটি School-এ তিনটি House আছে।

```text
Red House

Blue House

Green House
```

Teacher Attendance Sheet-এ লিখলেন

```text
Red → 0

Blue → 1

Green → 2
```

এতে Data সংরক্ষণ সহজ হলো।

কিন্তু এর মানে **Green House > Blue House > Red House** নয়।

শুধু একটি Code দেওয়া হয়েছে।

ঠিক Label Encoding-এও তাই হয়।

---

# 🤖 AI/ML Example

একটি Employee Dataset

| Gender |
| ------ |
| Male   |
| Female |
| Female |
| Male   |

↓

Encoding

| Gender |
| ------ |
| 1      |
| 0      |
| 0      |
| 1      |

এখন Model Train করা যাবে।

---

# 🐍 প্রথম Example

```python
from sklearn.preprocessing import LabelEncoder

colors = ["Red", "Blue", "Green", "Blue", "Red"]

encoder = LabelEncoder()

encoded = encoder.fit_transform(colors)

print(encoded)
```

Output

```text
[2 0 1 0 2]
```

---

# Mapping কীভাবে দেখবো?

```python
print(encoder.classes_)
```

Output

```text
['Blue' 'Green' 'Red']
```

এখানে Alphabetical Order অনুযায়ী Mapping হয়েছে।

```text
Blue

↓

0

Green

↓

1

Red

↓

2
```

⚠️ **Mapping তুমি ঠিক করো না, `LabelEncoder` নিজেই Alphabetical Order অনুযায়ী ঠিক করে।**

---

# DataFrame Example

```python
import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.DataFrame({
    "Gender": ["Male", "Female", "Male", "Female", "Male"]
})

encoder = LabelEncoder()

df["Gender"] = encoder.fit_transform(df["Gender"])

print(df)
```

Output

```text
   Gender
0       1
1       0
2       1
3       0
4       1
```

---

# একাধিক Column Encode

```python
import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.DataFrame({
    "Gender": ["Male", "Female", "Male"],
    "City": ["Dhaka", "Rajshahi", "Dhaka"]
})

encoder = LabelEncoder()

df["Gender"] = encoder.fit_transform(df["Gender"])
df["City"] = encoder.fit_transform(df["City"])

print(df)
```

---

# Original Value ফেরত আনা

ধরো

```text
Male

↓

1

Female

↓

0
```

আবার String-এ ফিরতে চাই।

```python
decoded = encoder.inverse_transform([1, 0, 1])

print(decoded)
```

Output

```text
['Male' 'Female' 'Male']
```

এটাকে বলে **Decoding**।

---

# ⚠️ গুরুত্বপূর্ণ সমস্যা

ধরো

```text
Apple

↓

0

Banana

↓

1

Orange

↓

2
```

Model ভাবতে পারে

```text
Orange > Banana > Apple
```

কারণ

```text
2 > 1 > 0
```

কিন্তু বাস্তবে

```text
Apple

Banana

Orange
```

এর মধ্যে কোনো ছোট-বড় সম্পর্ক নেই।

এটাকে বলে **False Ordering Problem**।

---

# তাহলে Label Encoding কখন ব্যবহার করবো?

## ✅ Ordinal Data

যেখানে আসলেই একটি Order আছে।

যেমন

```text
Small

Medium

Large
```

↓

```text
0

1

2
```

এখানে

Large

>

Medium

>

Small

এটা সত্যি।

তাই Label Encoding ব্যবহার করা যায়।

---

আরেকটি Example

```text
Education

Primary

Secondary

Higher Secondary

Bachelor

Master
```

এখানে Order আছে।

---

# ❌ Nominal Data

যেখানে কোনো Order নেই।

যেমন

```text
Red

Blue

Green
```

অথবা

```text
Dhaka

Khulna

Rajshahi
```

অথবা

```text
Cat

Dog

Bird
```

এখানে Label Encoding ব্যবহার করলে Model বিভ্রান্ত হতে পারে।

এক্ষেত্রে **One Hot Encoding** ভালো।

---

# 🤖 AI Pipeline

```text
Raw Dataset

↓

Missing Value Handling

↓

Label Encoding

↓

Scaling

↓

Train-Test Split

↓

Model Training
```

> **নোট:** বাস্তব Pipeline-এ Encoding সাধারণত Train Data-তে `fit()` করা হয় এবং Test Data-তে `transform()` করা হয়।

---

# ⚠️ Common Mistakes

### ❌ সব Category-তে Label Encoding ব্যবহার করা

ভুল

```text
Country

Bangladesh

India

Japan
```

এখানে One Hot Encoding ভালো।

---

### ❌ Train ও Test-এ আলাদা Encoder ব্যবহার করা

ভুল

Train

```text
Male → 1
Female → 0
```

Test

```text
Male → 0
Female → 1
```

Model ভুল Prediction করবে।

---

### ❌ Test Data-তে `fit_transform()` ব্যবহার করা

সঠিক

```python
encoder.fit(train_data)

encoder.transform(test_data)
```

---

# 🎯 Interview Questions

### ১. Label Encoding কী?

Categorical Data-কে Integer Number-এ রূপান্তরের প্রক্রিয়া।

---

### ২. কেন প্রয়োজন?

কারণ Machine Learning Model String বুঝতে পারে না।

---

### ৩. সবচেয়ে বড় সমস্যা কী?

False Ordering।

Model মনে করতে পারে

```text
2 > 1 > 0
```

যদিও বাস্তবে এমন সম্পর্ক নেই।

---

### ৪. Ordinal Data কী?

যেখানে আসলেই একটি ক্রম (Order) আছে।

যেমন

```text
Small

Medium

Large
```

---

### ৫. Nominal Data-তে কী ব্যবহার করবেন?

One Hot Encoding।

---

# 🚀 Practice Task

### Task ১

নিচের List Encode করো।

```python
["Red", "Blue", "Green", "Blue", "Red"]
```

---

### Task ২

নিচের DataFrame Encode করো।

```text
Gender

Male

Female

Female

Male
```

---

### Task ৩

`inverse_transform()` ব্যবহার করে Original Value ফিরিয়ে আনো।

---

### Task ৪

ভাবো নিচের Data-এর জন্য Label Encoding ঠিক হবে নাকি One Hot Encoding?

```text
Country

Bangladesh

India

Japan
```

---

### Task ৫

ভাবো নিচের Data-এর জন্য Label Encoding ঠিক হবে নাকি One Hot Encoding?

```text
T-Shirt Size

Small

Medium

Large
```

---

# 📌 মনে রাখার Shortcut

```text
Categorical Data (String)
            │
            ▼
     Label Encoding
            │
            ▼
 String → Integer

Example:
Male   → 1
Female → 0

✔ ভালো যখন:
- Ordinal Data
- Order আছে

❌ ভালো না যখন:
- Nominal Data
- Order নেই

সাবধান:
Label Encoding সংখ্যা তৈরি করে, কিন্তু সেই সংখ্যা সবসময় "বড়" বা "ছোট" বোঝায় না।
```

---

## 🎯 পরবর্তী অধ্যায়

পরবর্তী ফাইল **`OneHotEncoding.py`**।

এখানে আমরা শিখব কেন **Nominal Data (Country, Color, City, Animal)**-এর জন্য One Hot Encoding সবচেয়ে নিরাপদ এবং কীভাবে এটি **False Ordering Problem** সম্পূর্ণভাবে দূর করে। এটি Data Processing-এর সবচেয়ে গুরুত্বপূর্ণ Encoding Techniques-এর একটি।
