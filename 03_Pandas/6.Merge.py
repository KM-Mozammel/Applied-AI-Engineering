চলুন এবার **`6.Merge.py`** শুরু করি।

এটি Pandas-এর সবচেয়ে গুরুত্বপূর্ণ Topic-গুলোর একটি। যদি আপনার **SQL JOIN** জানা থাকে, তাহলে এটি অনেক সহজ হবে। `merge()` মূলত SQL-এর `JOIN` এর Pandas সংস্করণ।

---

```python
# ==========================================================
# Pandas Merge (বাংলা)
# ==========================================================

# Merge কী?
# ----------------------------------------------------------
# দুটি বা তার বেশি DataFrame-কে একটি Common Column-এর মাধ্যমে
# একত্রিত করাকে Merge বলে।
#
# SQL এর JOIN এর মতো।
#
# উদাহরণ:
#
# Students Table
#
# ID   Name
# 1    Rahim
# 2    Karim
#
# Marks Table
#
# ID   Marks
# 1    90
# 2    80
#
# Merge করলে
#
# ID   Name    Marks
# 1    Rahim   90
# 2    Karim   80
#
# AI/ML এ ব্যবহার:
#
# - Customer তথ্য + Order History
# - Employee + Salary
# - User + Transaction
# - Product + Review
# - Multiple Dataset Combine
```

---

# Sample Data

```python
import pandas as pd

students = pd.DataFrame({
    "StudentID": [1, 2, 3, 4],
    "Name": ["Rahim", "Karim", "Hasan", "Mitu"]
})

marks = pd.DataFrame({
    "StudentID": [1, 2, 4, 5],
    "Marks": [90, 80, 95, 70]
})

print(students)

print()

print(marks)
```

Output

```
Students

StudentID Name

1 Rahim

2 Karim

3 Hasan

4 Mitu

----------------

Marks

StudentID Marks

1 90

2 80

4 95

5 70
```

---

# ১. Basic Merge (Inner Join)

```python
pd.merge(
    students,
    marks,
    on="StudentID"
)
```

Output

```
StudentID

Name

Marks

1 Rahim 90

2 Karim 80

4 Mitu 95
```

---

## কী হলো?

দুই Table-এ যেসব StudentID মিলেছে শুধুমাত্র সেগুলো এসেছে।

```
Students

1
2
3
4

Marks

1
2
4
5

↓

Common

1
2
4
```

---

# SQL Comparison

SQL

```sql
SELECT *
FROM Students s
INNER JOIN Marks m
ON s.StudentID = m.StudentID;
```

Pandas

```python
pd.merge(
    students,
    marks,
    on="StudentID"
)
```

---

# ২. Left Join

```python
pd.merge(
    students,
    marks,
    on="StudentID",
    how="left"
)
```

Output

```
1 Rahim 90

2 Karim 80

3 Hasan NaN

4 Mitu 95
```

---

## কী হলো?

Students Table-এর সব Row রাখা হয়েছে।

Marks না থাকলে

```
NaN
```

---

# SQL

```sql
LEFT JOIN
```

---

# ৩. Right Join

```python
pd.merge(
    students,
    marks,
    on="StudentID",
    how="right"
)
```

Output

```
1 Rahim 90

2 Karim 80

4 Mitu 95

5 NaN 70
```

---

# SQL

```sql
RIGHT JOIN
```

---

# ৪. Outer Join

```python
pd.merge(
    students,
    marks,
    on="StudentID",
    how="outer"
)
```

Output

```
1 Rahim 90

2 Karim 80

3 Hasan NaN

4 Mitu 95

5 NaN 70
```

---

## Outer Join

সব Row থাকবে।

```
Students

1
2
3
4

Marks

1
2
4
5

↓

1

2

3

4

5
```

---

# ৫. Merge Different Column Name

Students

```python
students = pd.DataFrame({
    "ID":[1,2,3],
    "Name":["Rahim","Karim","Hasan"]
})
```

Marks

```python
marks = pd.DataFrame({
    "StudentID":[1,2,3],
    "Marks":[80,90,95]
})
```

Merge

```python
pd.merge(
    students,
    marks,
    left_on="ID",
    right_on="StudentID"
)
```

---

# ৬. Multiple Key Merge

```python
student_exam = pd.DataFrame({
    "ID":[1,1,2,2],
    "Exam":["Mid","Final","Mid","Final"],
    "Marks":[70,90,65,88]
})

attendance = pd.DataFrame({
    "ID":[1,1,2,2],
    "Exam":["Mid","Final","Mid","Final"],
    "Attendance":[95,98,90,92]
})

pd.merge(
    student_exam,
    attendance,
    on=["ID","Exam"]
)
```

---

# ৭. Suffix

দুই DataFrame-এ একই Column থাকলে

```python
student1 = pd.DataFrame({
    "ID":[1,2],
    "Marks":[80,90]
})

student2 = pd.DataFrame({
    "ID":[1,2],
    "Marks":[85,95]
})
```

Merge

```python
pd.merge(
    student1,
    student2,
    on="ID",
    suffixes=("_Old","_New")
)
```

Output

```
Marks_Old

Marks_New
```

---

# ৮. indicator=True

```python
pd.merge(
    students,
    marks,
    on="StudentID",
    how="outer",
    indicator=True
)
```

Output

```
both

left_only

right_only
```

---

## কী কাজে লাগে?

Data Validation

Checking Missing Record

---

# ৯. validate

```python
pd.merge(
    students,
    marks,
    on="StudentID",
    validate="one_to_one"
)
```

Relationship Check করে।

```
one_to_one

one_to_many

many_to_one

many_to_many
```

---

# ১০. merge() Method

এভাবেও লেখা যায়।

```python
students.merge(
    marks,
    on="StudentID"
)
```

---

# merge vs join

`merge()` সবচেয়ে বেশি ব্যবহার হয়।

`join()` Index-এর উপর কাজ করে।

---

# ১১. join()

```python
student = students.set_index("StudentID")

mark = marks.set_index("StudentID")

student.join(mark)
```

---

# ১২. concat()

Merge না।

DataFrame জোড়া দেয়।

```python
df1 = pd.DataFrame({
    "A":[1,2]
})

df2 = pd.DataFrame({
    "A":[3,4]
})

pd.concat([df1,df2])
```

Output

```
1

2

3

4
```

---

# Horizontal Concat

```python
pd.concat(
    [df1,df2],
    axis=1
)
```

---

# Merge vs Concat

```
Merge

Key ব্যবহার করে

↓

SQL JOIN

-------------------

Concat

সরাসরি DataFrame জোড়া দেয়

↓

Append
```

---

# Real Life Example

Customer

```
ID

Name
```

Orders

```
CustomerID

Amount
```

Merge

```python
pd.merge(
    customer,
    orders,
    left_on="ID",
    right_on="CustomerID"
)
```

---

# AI/ML এ ব্যবহার

## Customer + Purchase

```python
pd.merge(customer,purchase,on="CustomerID")
```

---

## Employee + Salary

```python
pd.merge(employee,salary,on="EmpID")
```

---

## Product + Review

```python
pd.merge(product,review,on="ProductID")
```

---

## User + Transaction

```python
pd.merge(user,transaction,on="UserID")
```

---

## Sensor Data Combine

```python
pd.merge(sensor1,sensor2,on="Time")
```

---

# SQL vs Pandas

| SQL             | Pandas                |
| --------------- | --------------------- |
| INNER JOIN      | `how="inner"`         |
| LEFT JOIN       | `how="left"`          |
| RIGHT JOIN      | `how="right"`         |
| FULL OUTER JOIN | `how="outer"`         |
| JOIN ON         | `on=`                 |
| Different Key   | `left_on`, `right_on` |

---

# Merge Cheat Sheet

| Method           | কাজ                     |
| ---------------- | ----------------------- |
| `merge()`        | Join DataFrame          |
| `on=`            | Common Column           |
| `left_on=`       | Left Key                |
| `right_on=`      | Right Key               |
| `how="inner"`    | Common Data             |
| `how="left"`     | Left সব Row             |
| `how="right"`    | Right সব Row            |
| `how="outer"`    | সব Row                  |
| `suffixes=`      | Duplicate Column Rename |
| `indicator=True` | Source Check            |
| `validate=`      | Relationship Validate   |
| `join()`         | Index Join              |
| `concat()`       | DataFrame Combine       |

---

# 🧠 এই অধ্যায় শেষে যা অবশ্যই জানতে হবে

* ✅ `merge()` কী এবং SQL `JOIN`-এর সাথে এর সম্পর্ক
* ✅ `inner`, `left`, `right`, `outer` join-এর পার্থক্য
* ✅ `on`, `left_on`, `right_on` ব্যবহার
* ✅ Multiple Key দিয়ে Merge করা
* ✅ `suffixes` দিয়ে একই নামের Column আলাদা করা
* ✅ `indicator=True` দিয়ে Merge Result যাচাই করা
* ✅ `validate` দিয়ে Relationship পরীক্ষা করা
* ✅ `join()` এবং `concat()`-এর পার্থক্য
* ✅ AI/ML-এ একাধিক Dataset একত্রিত করার বাস্তব ব্যবহার

---

### ⏭️ পরবর্তী ফাইল: **`7.MissingValues.py`**

এখানে আমরা গভীরভাবে শিখব:

* `isna()` / `isnull()`
* `notna()`
* `dropna()`
* `fillna()`
* `ffill()` / `bfill()`
* Mean, Median, Mode দিয়ে Missing Value পূরণ
* Interpolation
* AI/ML-এ Missing Data Handling Best Practices

এটি Data Cleaning-এর সবচেয়ে গুরুত্বপূর্ণ অধ্যায়গুলোর একটি।
