"""
=========================================================
DATA VISUALIZATION
=========================================================

Author : Mozammel Khandakar AI Engineering Notes

=========================================================
WHAT IS DATA VISUALIZATION?
=========================================================

Data Visualization হলো

Data কে Graph, Chart অথবা Plot আকারে
উপস্থাপন করা।

Machine Learning এর আগে Data বুঝতে
Visualization ব্যবহার করা হয়।

Raw Data

↓

Graph

↓

Insight

↓

Decision

---------------------------------------------------------

Example

Student Marks

45
67
89
95
74

এগুলো সংখ্যা দেখে বোঝা কঠিন।

কিন্তু Bar Chart দেখলে
এক সেকেন্ডেই বোঝা যায়
কে বেশি মার্কস পেয়েছে।

=========================================================
WHY DATA VISUALIZATION?
=========================================================

✔ Data বুঝতে

✔ Pattern খুঁজতে

✔ Outlier বের করতে

✔ Trend দেখতে

✔ Distribution বুঝতে

✔ Correlation দেখতে

✔ Presentation করতে

=========================================================
AI / ML USE CASE
=========================================================

✔ Exploratory Data Analysis (EDA)

✔ Feature Analysis

✔ Data Cleaning

✔ Outlier Detection

✔ Model Evaluation

✔ Loss Curve

✔ Accuracy Curve

✔ Confusion Matrix

=========================================================
MOST USED LIBRARIES
=========================================================

matplotlib

সবচেয়ে জনপ্রিয়

--------------------

pandas

Built-in plotting

--------------------

seaborn

Statistical Visualization

--------------------

plotly

Interactive Graph

=========================================================
IMPORT LIBRARIES
=========================================================
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

"""
=========================================================
SAMPLE DATA
=========================================================
"""

students = ["A", "B", "C", "D", "E"]
marks = [70, 82, 95, 60, 88]

"""
=========================================================
1. LINE CHART
=========================================================

কখন ব্যবহার করবো?

সময়ের সাথে পরিবর্তন দেখাতে।

Examples

✔ Stock Price

✔ Temperature

✔ Sales

✔ Accuracy

✔ Loss

=========================================================
"""

days = [1,2,3,4,5]

sales = [100,120,150,170,220]

plt.figure(figsize=(6,4))

plt.plot(days,sales)

plt.title("Sales Over Time")

plt.xlabel("Day")

plt.ylabel("Sales")

plt.grid()

plt.show()

"""
Output

একটি Line Graph

---------------------------------------------------------

AI Example

Epoch

↓

Accuracy

=========================================================
"""

"""
=========================================================
2. BAR CHART
=========================================================

Category Compare করার জন্য।

Example

Student Marks

=========================================================
"""

plt.figure(figsize=(6,4))

plt.bar(students,marks)

plt.title("Student Marks")

plt.xlabel("Student")

plt.ylabel("Marks")

plt.show()

"""
Output

প্রত্যেক Student এর জন্য
একটি করে Bar।

=========================================================
"""

"""
=========================================================
3. HORIZONTAL BAR
=========================================================
"""

plt.figure(figsize=(6,4))

plt.barh(students,marks)

plt.title("Horizontal Bar")

plt.show()

"""
=========================================================
4. HISTOGRAM
=========================================================

Distribution বোঝার জন্য।

Question

Data কি Normal?

কোন Range এ বেশি Value?

=========================================================
"""

ages = [18,20,21,22,22,22,23,24,25,26,27,30,30,35]

plt.figure(figsize=(6,4))

plt.hist(ages,bins=6)

plt.title("Age Distribution")

plt.show()

"""
Output

কোন Range এ
কত মানুষ আছে।

=========================================================
"""

"""
=========================================================
5. SCATTER PLOT
=========================================================

দুইটি Feature এর Relationship।

=========================================================
"""

height = [150,155,160,165,170,175,180]

weight = [45,50,58,60,68,74,80]

plt.figure(figsize=(6,4))

plt.scatter(height,weight)

plt.xlabel("Height")

plt.ylabel("Weight")

plt.title("Height vs Weight")

plt.show()

"""
Output

যদি Dot গুলো
এক লাইনের মতো হয়

↓

Positive Correlation

=========================================================
"""

"""
=========================================================
6. PIE CHART
=========================================================

Percentage দেখানোর জন্য।

=========================================================
"""

languages = ["Python","Java","C++"]

users = [70,20,10]

plt.figure(figsize=(6,6))

plt.pie(users,
labels=languages,
autopct="%1.1f%%")

plt.title("Programming Language Usage")

plt.show()

"""
=========================================================
7. BOX PLOT
=========================================================

Outlier বের করার জন্য।

Machine Learning এ
খুব গুরুত্বপূর্ণ।

=========================================================
"""

salary = [20,21,22,22,23,24,25,26,120]

plt.figure(figsize=(6,4))

plt.boxplot(salary)

plt.title("Salary")

plt.show()

"""
Output

120

Outlier হিসেবে দেখা যাবে।

=========================================================
"""

"""
=========================================================
8. MULTIPLE LINE
=========================================================
"""

accuracy = [60,68,75,81,88]

loss = [0.9,0.7,0.5,0.3,0.1]

epochs = [1,2,3,4,5]

plt.figure(figsize=(6,4))

plt.plot(epochs,accuracy,label="Accuracy")

plt.plot(epochs,loss,label="Loss")

plt.legend()

plt.title("Training")

plt.show()

"""
AI Example

Training Curve

=========================================================
"""

"""
=========================================================
9. GRID
=========================================================
"""

plt.figure(figsize=(6,4))

plt.plot(days,sales)

plt.grid(True)

plt.show()

"""
Grid
Graph পড়া সহজ করে।

=========================================================
"""

"""
=========================================================
10. COLOR
=========================================================
"""

plt.figure(figsize=(6,4))

plt.plot(days,sales,color="red")

plt.show()

"""
Common Colors

red

green

blue

black

orange

purple

=========================================================
"""

"""
=========================================================
11. MARKER
=========================================================
"""

plt.figure(figsize=(6,4))

plt.plot(days,sales,marker="o")

plt.show()

"""
Useful Marker

o

*

x

^

s

=========================================================
"""

"""
=========================================================
12. LINE STYLE
=========================================================
"""

plt.figure(figsize=(6,4))

plt.plot(days,sales,
linestyle="--")

plt.show()

"""
Styles

-

--

:

-.

=========================================================
"""

"""
=========================================================
13. FIGURE SIZE
=========================================================
"""

plt.figure(figsize=(10,5))

plt.plot(days,sales)

plt.show()

"""
Width = 10

Height = 5

=========================================================
"""

"""
=========================================================
14. SAVE GRAPH
=========================================================
"""

plt.figure(figsize=(6,4))

plt.plot(days,sales)

plt.savefig("sales.png")

"""
Graph
Current Folder এ Save হবে।

=========================================================
"""

"""
=========================================================
15. REAL AI PROJECT
=========================================================

Customer Dataset

↓

Load CSV

↓

Check Missing Values

↓

Histogram

↓

Boxplot

↓

Correlation

↓

Feature Selection

↓

Train Model

↓

Accuracy Curve

↓

Confusion Matrix

=========================================================
"""

"""
=========================================================
INTERVIEW QUESTIONS
=========================================================

Q.

Histogram কেন ব্যবহার করি?

Answer

Distribution বোঝার জন্য।

---------------------------------------------------------

Q.

Scatter Plot কেন ব্যবহার করি?

Answer

Feature Relationship দেখার জন্য।

---------------------------------------------------------

Q.

Outlier বের করতে কোন Plot?

Answer

Box Plot

---------------------------------------------------------

Q.

Time Series এর জন্য?

Answer

Line Chart

---------------------------------------------------------

Q.

Category Compare?

Answer

Bar Chart

---------------------------------------------------------

Q.

Percentage দেখাতে?

Answer

Pie Chart

=========================================================
COMMON MISTAKES
=========================================================

❌ Label না দেওয়া

❌ Title না দেওয়া

❌ Wrong Chart ব্যবহার করা

❌ Too many Colors

❌ Grid ব্যবহার না করা

❌ Different Scale Ignore করা

=========================================================
SUMMARY
=========================================================

Data

↓

Visualization

↓

Pattern

↓

Insight

↓

Cleaning

↓

Feature Engineering

↓

Model Training

↓

Evaluation

=========================================================

সবচেয়ে বেশি ব্যবহৃত Charts

★★★★★ Line Chart

★★★★★ Bar Chart

★★★★★ Histogram

★★★★★ Scatter Plot

★★★★★ Box Plot

★★★★★ Pie Chart

=========================================================

AI Engineer হিসেবে
এই ৬টি Chart ৯০% Project এ
ব্যবহার হবে।

=========================================================
"""