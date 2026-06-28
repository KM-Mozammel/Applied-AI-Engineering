# PCA.py (Principal Component Analysis)

```python id="pca001"
"""
=========================================================
Principal Component Analysis (PCA)
=========================================================

এই ফাইল থেকে যা শিখবে

১. PCA কী?
২. Dimension কী?
৩. Dimension Reduction কেন দরকার?
৪. Principal Component কী?
৫. Variance কী?
৬. Explained Variance Ratio
৭. Eigenvector ও Eigenvalue (Intuition)
৮. sklearn.decomposition.PCA
৯. AI/ML Project-এ Best Practice
=========================================================
"""
```

---

# 📖 PCA কী?

**PCA (Principal Component Analysis)** হলো একটি **Dimension Reduction Technique**।

এটি Dataset-এর গুরুত্বপূর্ণ তথ্য (Information) যতটা সম্ভব রেখে,

**কম সংখ্যক Feature-এ Data-কে রূপান্তর করে।**

---

# 🤔 কেন PCA দরকার?

ধরো,

একটি Dataset-এ

```text id="pca101"
1000 Feature
```

আছে।

কিন্তু

Model-এর জন্য

সব Feature সমান গুরুত্বপূর্ণ নয়।

অনেক Feature

* একই তথ্য দেয়।
* Duplicate Information বহন করে।
* Noise তৈরি করে।

PCA

↓

সবচেয়ে গুরুত্বপূর্ণ Information রেখে

↓

Feature কমিয়ে দেয়।

---

# 🧠 প্রথমে Dimension কী?

ধরো,

তোমার কাছে শুধু

```text id="pca102"
Height
```

আছে।

এটি

```text id="pca103"
1 Dimension
```

---

যদি

```text id="pca104"
Height

Weight
```

থাকে,

তাহলে

```text id="pca105"
2 Dimension
```

---

যদি

```text id="pca106"
Height

Weight

Age
```

থাকে,

তাহলে

```text id="pca107"
3 Dimension
```

---

সুতরাং

**একটি Feature = একটি Dimension**

---

# 🔬 Real Life Example

ধরো,

একজন ছাত্র সম্পর্কে তথ্য

```text id="pca108"
Height

Weight

BMI
```

BMI আসলে

Height

এবং

Weight

থেকেই বের হয়।

তাই

BMI নতুন Information দিচ্ছে না।

PCA বুঝতে পারে

```text id="pca109"
Height

Weight

BMI
```

↓

একই ধরনের Information।

↓

একটি Feature বাদ দেওয়া যায়।

---

# 🤖 AI Example

Face Recognition

একটি ছবি

```text id="pca110"
100 × 100 Pixel
```

=

```text id="pca111"
10000 Feature
```

কিন্তু

সব Pixel সমান গুরুত্বপূর্ণ নয়।

PCA

↓

10000 Feature

↓

100 Feature

↓

Face চিনতে পারে।

---

# 🧠 Core Concept

Original Dataset

| Height | Weight | BMI |
| ------ | ------ | --- |
| 170    | 70     | 24  |
| 175    | 74     | 24  |
| 180    | 80     | 25  |

↓

PCA

↓

| PC1 | PC2  |
| --- | ---- |
| 1.2 | -0.3 |
| 1.8 | 0.1  |
| 2.4 | 0.2  |

দেখো,

৩টি Feature

↓

২টি Feature

---

# 📖 Variance কী?

Variance

মানে

**Data কতটা ছড়িয়ে আছে।**

---

Example

Dataset-1

```text id="pca112"
10

11

10

11

10
```

Variance

↓

কম।

---

Dataset-2

```text id="pca113"
10

40

80

120

200
```

Variance

↓

অনেক বেশি।

---

PCA

সবচেয়ে বেশি Variance থাকা Direction খুঁজে বের করে।

---

# 📖 Principal Component কী?

Principal Component

=

Data-এর নতুন Axis।

---

Original

```text id="pca114"
Height

Weight
```

↓

PCA

↓

```text id="pca115"
PC1

PC2
```

এগুলো

Original Feature নয়।

নতুন Feature।

---

# Visual

Original

```text id="pca116"
Height

↑

|

|

|

|

+-----------------> Weight
```

---

PCA

Data-এর সবচেয়ে গুরুত্বপূর্ণ Direction খুঁজে নেয়।

```text id="pca117"
        PC1

       ↗

     ↗

   ↗

 +

 |

 |

 ↓

PC2
```

PC1

↓

Maximum Information।

---

# 📖 Explained Variance

PCA

প্রতিটি Component

কত Information রাখছে,

তা বলে।

---

Example

```text id="pca118"
PC1

↓

85%
```

```text id="pca119"
PC2

↓

10%
```

```text id="pca120"
PC3

↓

5%
```

মোট

```text id="pca121"
100%
```

---

যদি

PC1

*

PC2

=

95%

হয়,

তাহলে

PC3

বাদ দেওয়া যায়।

---

# 📖 Eigenvector ও Eigenvalue (Intuition)

অনেকেই এই অংশে ভয় পায়।

আসলে Concept খুব সহজ।

---

ধরো,

একটি পাহাড়।

তুমি

যে Direction-এ নিচে নামবে,

সেই Direction-এ সবচেয়ে দ্রুত নামা যাবে।

সেই Direction

↓

Eigenvector

---

আর

সেই Direction

কতটা গুরুত্বপূর্ণ,

↓

Eigenvalue

---

PCA

Eigenvector ব্যবহার করে

নতুন Axis তৈরি করে।

---

# 🐍 প্রথম Example

```python
from sklearn.decomposition import PCA
import pandas as pd

df = pd.DataFrame({

    "Height":[170,175,180,185],

    "Weight":[70,74,80,85]

})

pca = PCA(n_components=1)

result = pca.fit_transform(df)

print(result)
```

---

Output

```text id="pca122"
একটি মাত্র নতুন Feature

PC1
```

---

# দুইটি Component

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)

result = pca.fit_transform(df)

print(result)
```

---

# Explained Variance দেখা

```python
print(
    pca.explained_variance_ratio_
)
```

Output

```text id="pca123"
[0.96

 0.04]
```

মানে

```text id="pca124"
PC1

96%
```

Information

---

```text id="pca125"
PC2

4%
```

Information

---

# কতগুলো Component রাখবো?

ধরো

```text id="pca126"
10 Feature
```

↓

PCA

↓

```python
PCA(n_components=0.95)
```

মানে

```text id="pca127"
95%

Information

রাখবে।
```

এবং

বাকিগুলো বাদ দেবে।

---

# 🤖 AI Example

Image Compression

```text id="pca128"
10000 Pixel
```

↓

PCA

↓

```text id="pca129"
500 Feature
```

↓

Storage কম।

↓

Speed বেশি।

---

# PCA-এর সুবিধা

✅ Feature কমে।

---

✅ Training Speed বাড়ে।

---

✅ Noise কমে।

---

✅ Overfitting কমতে পারে।

---

✅ Visualization সহজ হয়।

---

# PCA-এর অসুবিধা

❌ Original Feature হারিয়ে যায়।

---

❌ Explain করা কঠিন।

---

❌ সবসময় Accuracy বাড়ে না।

---

# PCA-এর আগে কী করতে হবে?

সবচেয়ে গুরুত্বপূর্ণ বিষয়।

PCA

Distance-এর উপর নির্ভর করে।

তাই

আগে

```text id="pca130"
StandardScaler
```

করতে হবে।

---

Pipeline

```text id="pca131"
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

PCA

↓

Model Training
```

---

# ⚠️ Common Mistakes

### ❌ Scaling ছাড়া PCA করা

সবচেয়ে Common Mistake।

---

### ❌ Explained Variance না দেখা।

---

### ❌ সব Component রেখে PCA করা।

তাহলে

PCA করারই দরকার নেই।

---

# 🎯 Interview Questions

### ১. PCA কী?

Dimension Reduction Technique।

---

### ২. PCA-এর লক্ষ্য কী?

কম Feature-এ

বেশি Information রাখা।

---

### ৩. PCA-এর আগে কী করতে হয়?

StandardScaler।

---

### ৪. Principal Component কী?

Original Feature-এর Combination থেকে তৈরি নতুন Feature।

---

### ৫. Explained Variance কী?

প্রতিটি Principal Component

কত Information ধরে রেখেছে।

---

# 🚀 Practice Task

### Task ১

Height এবং Weight Dataset-এ

```python
PCA(n_components=1)
```

ব্যবহার করো।

---

### Task ২

`explained_variance_ratio_`

Print করো।

---

### Task ৩

StandardScaler ছাড়া PCA চালাও।

তারপর

StandardScaler দিয়ে PCA চালাও।

Output Compare করো।

---

### Task ৪

Iris Dataset ব্যবহার করে

4 Feature

↓

2 Feature

করো।

---

# 📌 মনে রাখার Shortcut

```text id="pca132"
অনেক Feature
        │
        ▼
StandardScaler
        │
        ▼
PCA
        │
        ▼
Principal Components
        │
        ▼
কম Feature
বেশি Information

✔ Training Faster
✔ Memory কম
✔ Noise কম
✔ Overfitting কমতে পারে

মনে রাখবে:

PCA-এর আগে অবশ্যই StandardScaler।
```

---

# 🧠 এখন পর্যন্ত Data Processing Flow

```text
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
PCA (Dimension Reduction)
      │
      ▼
Model Training
```

---

## 🎯 পরবর্তী অধ্যায়: **`FeatureSelection.py`**

এখানে আমরা শিখব **PCA** এবং **Feature Selection**-এর আসল পার্থক্য, Feature Importance, Correlation, Filter Method, Wrapper Method, Embedded Method এবং বাস্তব AI Project-এ কীভাবে সঠিক Feature নির্বাচন করা হয়। এটি Machine Learning Interview-এর অন্যতম গুরুত্বপূর্ণ টপিক।
