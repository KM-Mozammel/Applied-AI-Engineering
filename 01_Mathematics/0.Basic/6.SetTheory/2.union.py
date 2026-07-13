"""
===========================================================
Union of Sets (সেটের Union)
===========================================================

Structure:

01_Introduction
02_WhyThisConceptExistsInRelationTohistory
03_RealLifeIntuition
04_Definition
05_Formula
06_Derivation (How the formula comes)
07_InternalWorking / Visualization
08_Examples
09_CommonMistakes
10_Exercises
11_AIUsage (Machine Learning / AI)

===========================================================
"""


# ===========================================================
# 01_Introduction
# ===========================================================

"""
Union (∪) হলো Set Theory এর একটি গুরুত্বপূর্ণ operation।

Union ব্যবহার করে দুই বা তার বেশি Set এর সব unique element
একত্র করা হয়।

Symbol:

∪

Example:

A = {1,2,3}

B = {3,4,5}


A ∪ B

Result:

{1,2,3,4,5}


এখানে duplicate element (3) একবারই থাকবে।
"""


# ===========================================================
# 02_WhyThisConceptExistsInRelationToHistory
# ===========================================================

"""
ইতিহাস:

মানুষ যখন বিভিন্ন group বা collection নিয়ে কাজ করতে শুরু করে,
তখন একাধিক collection একত্র করার প্রয়োজন হয়।

উদাহরণ:

একটি গ্রামের মানুষ:

Group A = কিছু মানুষ

Group B = কিছু মানুষ


দুই group এর মোট মানুষ বের করতে হলে
একটি নতুন collection তৈরি করতে হয়।

এই প্রয়োজন থেকেই Union ধারণা এসেছে।

Georg Cantor এর Set Theory তে Union একটি মৌলিক operation।
"""


# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
বাস্তব জীবনের উদাহরণ:


ধরি:

একজন ছাত্র Python এবং Math শেখে।


Python Students:

A = {
"Rahim",
"Karim",
"Hasan"
}


Math Students:

B = {
"Hasan",
"Jamal",
"Rafi"
}



দুই বিষয়ের মোট ছাত্র:

A ∪ B


Result:

{
"Rahim",
"Karim",
"Hasan",
"Jamal",
"Rafi"
}



Hasan দুই জায়গায় থাকলেও
একবার গণনা হবে।
"""


# ===========================================================
# 04_Definition
# ===========================================================

"""
Definition:

দুইটি Set এর সব element একত্র করে,
duplicate বাদ দিয়ে নতুন Set তৈরি করাকে Union বলে।


Mathematical Definition:


A ∪ B = {x : x ∈ A অথবা x ∈ B}


মানে:

যেসব element A অথবা B যেকোনো একটিতে আছে,
সব Union এ থাকবে।


Example:

A = {1,2,3}

B = {4,5,6}


A ∪ B

=

{1,2,3,4,5,6}
"""


# ===========================================================
# 05_Formula
# ===========================================================

"""
Union Formula:


A ∪ B = All elements of A and B


Cardinality Formula:

যদি A এবং B overlap করে:


|A ∪ B|

=

|A| + |B| - |A ∩ B|



কারণ:

Common element দুইবার গণনা হয়।

তাই Intersection বাদ দিতে হয়।



Example:

A={1,2,3}

B={3,4,5}



|A| = 3

|B| = 3

|A∩B| = 1



|A∪B|

=

3+3-1

=

5
"""


# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
ধরি:


A = {1,2,3}

B = {3,4,5}



Step 1:

A এর element:

1,2,3


Step 2:

B এর element:

3,4,5


Step 3:

Combine:


1,2,3,3,4,5


Step 4:

Set duplicate রাখে না:


1,2,3,4,5



তাই:


A ∪ B = {1,2,3,4,5}



Cardinality:

A তে 3 টি

B তে 3 টি


মোট:

6


কিন্তু 3 দুইবার এসেছে।


তাই:

6 - 1 = 5
"""


# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
Venn Diagram:


        _________
       /         \
      /    A      \
     |   1 2 3     |
     |      ___    |
      \    /   \  /
       \__/ 3  \/
       /        \
      |  B       |
      | 4 5      |
       \________/


Union হলো পুরো দুইটি Circle এর area।

A ∪ B

=

A এর সব + B এর সব


Computer Science এ:


Python Set Union:


A | B


অথবা


A.union(B)


Internally:

1. প্রথম Set এর hash table copy করে
2. দ্বিতীয় Set এর element add করে
3. Duplicate hash value বাদ দেয়


Average Time Complexity:

O(n+m)

যেখানে:

n = A এর size

m = B এর size
"""


# ===========================================================
# 08_Examples
# ===========================================================

"""
Example 1:

Basic Union:

"""

A = {1,2,3}

B = {3,4,5}

result = A | B

print(result)



"""
Example 2:

Using union() method:
"""

result = A.union(B)

print(result)



"""
Example 3:

Three Sets Union:
"""

A = {1,2}

B = {2,3}

C = {3,4}


result = A | B | C


print(result)



"""
Example 4:

Real life example:
"""

python_students = {
    "Rahim",
    "Karim",
    "Hasan"
}


java_students = {
    "Hasan",
    "Jamal"
}


all_students = python_students | java_students


print(all_students)



"""
Example 5:

Finding total unique data:
"""

database1 = {
    "user1",
    "user2"
}


database2 = {
    "user2",
    "user3"
}


all_users = database1.union(database2)


print(all_users)



# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
Common Mistakes:


1. Union এ duplicate থাকবে ভাবা


Wrong:

{1,2,3} ∪ {3,4}


Answer:

{1,2,3,3,4}


Correct:

{1,2,3,4}



--------------------------------


2. List এর মতো index ব্যবহার করা


Wrong:


union_result[0]


কারণ Set unordered।



--------------------------------


3. + operator ব্যবহার করা


Wrong:


A + B


Set এ + কাজ করে না।


Correct:


A | B



--------------------------------


4. Type ভুল করা


Wrong:

{}

এটি Dictionary।


Correct:

set()



--------------------------------


5. Empty Set handling না জানা

Empty Set এর Union:


A ∪ {}

=

A
"""


# ===========================================================
# 10_Exercises
# ===========================================================

"""
Exercise 1:

দুইটি Set তৈরি করো:

A={10,20,30}

B={30,40,50}


Union বের করো।



Exercise 2:

তিনটি Set এর Union বের করো।



Exercise 3:

দুইটি List এর duplicate remove করে
Union তৈরি করো।



Exercise 4:

একটি Student Management System এ:

Class_A students

Class_B students


সব unique student বের করো।



Exercise 5:

Formula ব্যবহার করে বের করো:


A={1,2,3,4}

B={4,5,6}


|A∪B|
"""


# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
AI এবং Machine Learning এ Union এর ব্যবহার:


1. Feature Combination


Model A features:

{
age,
salary,
experience
}


Model B features:

{
age,
location,
education
}



Union:


{
age,
salary,
experience,
location,
education
}



--------------------------------


2. NLP Vocabulary


Document 1:

{
python,
ai,
machine
}


Document 2:

{
ai,
data,
learning
}



Combined vocabulary:


{
python,
ai,
machine,
data,
learning
}



--------------------------------


3. Dataset Merging


Training Dataset:

A


New Dataset:

B


Combined Dataset:

A ∪ B



--------------------------------


4. Recommendation System


User A interest:

{
AI,
Python
}


User B interest:

{
Python,
Web
}



Combined Interest:


{
AI,
Python,
Web
}



--------------------------------


5. Search Engine


Multiple document এর keywords
একত্র করতে Union ব্যবহার হয়।



Union হলো Data Science এবং AI তে
data combining এর একটি গুরুত্বপূর্ণ concept।
"""


print("Union of Sets শেখা সম্পন্ন!")