# TrainTestSplit.py

```python
"""
=========================================================
Train Test Split
=========================================================

এই ফাইল থেকে যা শিখবে

১. Train-Test Split কী?
২. কেন দরকার?
৩. Model Training-এর Flow
৪. train_test_split() ব্যবহার
৫. random_state কী?
৬. test_size কী?
৭. shuffle কী?
৮. stratify কী?
৯. AI/ML Project-এ কোথায় ব্যবহার হয়?
=========================================================
"""
```

---

# 📖 Train-Test Split কী?

Machine Learning-এ **একটি Dataset-কে দুই (বা তিন) ভাগে ভাগ করার প্রক্রিয়াকে Train-Test Split বলে।**

এক ভাগ দিয়ে Model শেখে।

আরেক ভাগ দিয়ে Model-এর Performance পরীক্ষা করা হয়।

---

## 🤔 কেন দরকার?

ধরো তুমি একজন ছাত্র।

Final Exam-এর আগে বই দেখে অনেক Practice করলে।

তারপর Exam-এ সেই একই প্রশ্ন এলো।

তুমি 100% পাবে।

কিন্তু এতে বোঝা যাবে না তুমি সত্যিই শিখেছো কিনা।

Machine Learning-এও একই ব্যাপার।

যদি Model একই Data দেখে শেখে এবং সেই একই Data দিয়েই পরীক্ষা করা হয়—

তাহলে Model সব Answer মুখস্থ করে ফেলবে।

এটাকে বলে

> **Overfitting**

তাই Model-কে এমন Data-তে পরীক্ষা করতে হবে যেটা সে আগে কখনও দেখেনি।

এই কারণেই Train-Test Split করা হয়।

---

# 🧠 Core Concept

একটি Dataset

```
1000 Rows
```

এটাকে ভাগ করা হয়

```
Training Data

+

Testing Data
```

যেমন

```
1000

↓

800 Train

200 Test
```

অথবা

```
80%

20%
```

---

## Visual

```
Dataset

□□□□□□□□□□□□□□□□□□□□□□□□

↓

Train

□□□□□□□□□□□□□□□□□□□□

↓

Model Learns

↓

Test

□□□□□□□□

↓

Performance Check
```

---

# 🔬 Real Life Example

ধরো,

তুমি Driving শিখছো।

প্রথমে

৫০ দিন Practice করলে।

তারপর

Driving Test দিলে।

Practice

=

Training Data

Driving Test

=

Testing Data

যদি Practice-এর সময় যে Road-এ চালিয়েছো,

Exam-এও ঠিক সেই Road আসে,

তাহলে Driving Skill বোঝা যাবে না।

তাই নতুন Road দেওয়া হয়।

Machine Learning-এও একই।

---

# 🤖 AI/ML Example

ধরো

House Price Prediction।

তোমার কাছে

```
10000 টি বাড়ির তথ্য আছে।
```

তুমি

```
8000

↓

Training

Model শেখাবে
```

তারপর

```
2000

↓

Testing

Prediction করবে
```

এখন Model যদি নতুন House-এর দাম ভালো Predict করতে পারে,

তাহলেই Model ভালো।

---

# 🐍 প্রথম Example

```python
from sklearn.model_selection import train_test_split

numbers = [1,2,3,4,5,6,7,8,9,10]

train, test = train_test_split(
    numbers,
    test_size=0.2,
    random_state=42
)

print("Train:", train)
print("Test :", test)
```

---

### Output

```
Train: [....8টি সংখ্যা....]

Test : [....2টি সংখ্যা....]
```

কারণ

```
20%

of 10

=

2
```

---

# এবার Dataset দিয়ে দেখি

```python
import pandas as pd
from sklearn.model_selection import train_test_split

data = {
    "Age": [20,25,30,35,40,45,50,55,60,65],
    "Salary":[20,30,35,40,50,55,60,70,80,90]
}

df = pd.DataFrame(data)

train_df, test_df = train_test_split(
    df,
    test_size=0.2,
    random_state=42
)

print(train_df)
print()

print(test_df)
```

---

## কী হলো?

DataFrame

↓

Split

↓

৮০%

Training

২০%

Testing

---

# Feature এবং Target Split

Machine Learning-এ সাধারণত

```
X

=

Input
```

```
y

=

Output
```

---

Example

```python
import pandas as pd

data = {
    "Age":[20,25,30,35,40],
    "Experience":[1,2,3,4,5],
    "Salary":[20,25,35,45,60]
}

df = pd.DataFrame(data)

X = df[["Age","Experience"]]

y = df["Salary"]

print(X)

print()

print(y)
```

---

এরপর

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

এটাই প্রায় সব Machine Learning Project-এর Standard Code।

---

# 🧠 random_state কী?

এটা Interview-এর খুব Common Question।

ধরো,

তোমার Dataset

```
1

2

3

4

5

6

7

8

9

10
```

Split করার সময় Computer Randomভাবে Data ভাগ করবে।

প্রথমবার

```
Train

1 2 3 4 7 8 9 10

Test

5 6
```

দ্বিতীয়বার

```
Train

2 3 4 5 6 7 8 10

Test

1 9
```

দেখছো,

প্রতিবার Result বদলে যাচ্ছে।

---

যদি লিখি

```python
random_state=42
```

তাহলে

প্রতিবার একই Split হবে।

এটাকে বলে

> **Reproducibility (একই ফলাফল পুনরায় পাওয়া)**

---

# 🧠 test_size কী?

এটা বলে কত শতাংশ Data Test হবে।

```
test_size=0.2

↓

20%

Test
```

```
test_size=0.3

↓

30%

Test
```

```
test_size=0.4

↓

40%

Test
```

---

# 🧠 train_size

Test-এর বদলে Train-ও নির্দিষ্ট করা যায়।

```python
train_size=0.7
```

মানে

```
70%

Train

30%

Test
```

---

# 🧠 shuffle

Default

```python
shuffle=True
```

মানে

আগে Randomভাবে Data মিশিয়ে তারপর ভাগ করবে।

---

যদি

```python
shuffle=False
```

তাহলে

```
প্রথম অংশ

↓

Train

শেষ অংশ

↓

Test
```

যেমন

```
1

2

3

4

5

6

7

8

9

10
```

↓

```
Train

1-8

Test

9-10
```

⚠️ Time Series Data ছাড়া সাধারণত `shuffle=True` ব্যবহার করা হয়।

---

# 🧠 stratify

ধরো Dataset

```
Cat

95%

Dog

5%
```

যদি Random Split করো,

তাহলে Test Data-তে হয়তো Dog একটাও নাও থাকতে পারে।

এটা Model Evaluation-কে ভুল করে দিতে পারে।

তাই

```python
stratify=y
```

ব্যবহার করলে Train এবং Test—দুটিতেই একই Class Ratio বজায় থাকে।

উদাহরণ:

| Dataset  | Cat | Dog |
| -------- | --: | --: |
| Original | 95% |  5% |
| Train    | 95% |  5% |
| Test     | 95% |  5% |

---

# 🧠 Complete Example

```python
import pandas as pd
from sklearn.model_selection import train_test_split

data = {
    "Age":[20,25,30,35,40,45,50,55],
    "Experience":[1,2,3,4,5,6,7,8],
    "Salary":[20,30,40,50,60,70,80,90]
}

df = pd.DataFrame(data)

X = df[["Age","Experience"]]
y = df["Salary"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

print("X_train")
print(X_train)

print("\nX_test")
print(X_test)

print("\ny_train")
print(y_train)

print("\ny_test")
print(y_test)
```

---

# ⚠️ Common Mistakes

❌ একই Data দিয়ে Train এবং Test করা।

❌ `random_state` না দেওয়া (শেখার সময়)।

❌ খুব ছোট Dataset-এ ৫০% Test রাখা।

❌ Time Series Data-তে `shuffle=True` ব্যবহার করা।

❌ `X` এবং `y` আলাদা না করে Split করা।

---

# 🎯 Interview Questions

### ১. Train-Test Split কেন ব্যবহার করা হয়?

Model নতুন (Unseen) Data-তে কেমন কাজ করবে তা যাচাই করার জন্য।

---

### ২. `random_state` কেন ব্যবহার করা হয়?

যাতে প্রতিবার একইভাবে Data Split হয় এবং ফলাফল পুনরায় পাওয়া যায় (Reproducibility)।

---

### ৩. `test_size=0.2` মানে কী?

Dataset-এর ২০% Test এবং ৮০% Train হবে।

---

### ৪. `shuffle=False` কখন ব্যবহার করবেন?

মূলত Time Series বা Sequence Data-এর ক্ষেত্রে, যেখানে Data-এর ক্রম গুরুত্বপূর্ণ।

---

### ৫. `stratify=y` কেন ব্যবহার করা হয়?

Train এবং Test Data-তে Class-এর অনুপাত একই রাখতে।

---

# 🚀 Practice Task

### Task ১

১ থেকে ১০০ পর্যন্ত সংখ্যা নিয়ে `train_test_split()` ব্যবহার করো।

* `test_size=0.2`
* `random_state=42`

---

### Task ২

একটি DataFrame তৈরি করো যেখানে থাকবে:

* Name
* Age
* Salary

এবং সেটিকে ৭০%-৩০% অনুপাতে ভাগ করো।

---

### Task ৩

`random_state=42` এবং `random_state=7` দিয়ে Split করে পার্থক্য দেখো।

---

### Task ৪

`shuffle=True` এবং `shuffle=False` ব্যবহার করে Output তুলনা করো।

---

## 📌 মনে রাখার Shortcut

```text
Dataset
    │
    ▼
Feature (X) + Target (y)
    │
    ▼
train_test_split()
    │
    ├── X_train → Model শেখে
    ├── y_train → সঠিক উত্তর
    ├── X_test  → Model পরীক্ষা
    └── y_test  → আসল উত্তর দিয়ে Performance যাচাই

মূল Parameters:
✔ test_size   → কত % Test Data
✔ train_size  → কত % Train Data
✔ random_state → একই Split পুনরায় পাওয়ার জন্য
✔ shuffle      → Split-এর আগে Data মিশাবে কিনা
✔ stratify     → Class Ratio একই রাখবে
```

পরবর্তী অধ্যায়ে আমরা **`MissingValueHandling.py`** শিখব, যেখানে বাস্তব Dataset-এর `NaN`, `None`, খালি সেল এবং Missing Data কীভাবে সঠিকভাবে Handle করতে হয় তা বিস্তারিতভাবে শিখব।
