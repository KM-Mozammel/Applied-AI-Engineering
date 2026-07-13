"""
===========================================================
Intersection of Sets (সেটের Intersection)
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
Intersection (∩) হলো Set Theory এর একটি গুরুত্বপূর্ণ operation।

Intersection ব্যবহার করে দুই বা তার বেশি Set এর মধ্যে
common (সাধারণ) element বের করা হয়।

Symbol:

∩


Example:

A = {1,2,3,4}

B = {3,4,5,6}


A ∩ B


Result:

{3,4}


কারণ 3 এবং 4 দুইটি Set-এই আছে।
"""


# ===========================================================
# 02_WhyThisConceptExistsInRelationToHistory
# ===========================================================

"""
ইতিহাস:

মানুষ যখন বিভিন্ন group বা category নিয়ে কাজ শুরু করে,
তখন তাদের মধ্যে মিল খুঁজে বের করার প্রয়োজন হয়।


উদাহরণ:

একটি স্কুলে:

Football খেলোয়াড়দের Group

এবং

Cricket খেলোয়াড়দের Group


যারা দুই খেলাই খেলে তাদের খুঁজে বের করতে হবে।


এই ধরনের common element খুঁজে বের করার জন্য
Intersection ধারণার প্রয়োজন হয়।


Set Theory তে Georg Cantor Intersection কে
একটি মৌলিক operation হিসেবে প্রতিষ্ঠিত করেন।
"""


# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
বাস্তব জীবনের উদাহরণ:


ধরি:

Python শেখে:

A = {
"Rahim",
"Karim",
"Hasan"
}


AI শেখে:

B = {
"Hasan",
"Jamal",
"Rafi"
}



যারা Python এবং AI দুইটিই শেখে:


A ∩ B


Result:

{
"Hasan"
}



অর্থাৎ Intersection শুধু common data রাখে।
"""


# ===========================================================
# 04_Definition
# ===========================================================

"""
Definition:

দুইটি Set এর মধ্যে যে element গুলো উভয় Set-এ বিদ্যমান,
সেগুলো নিয়ে নতুন Set তৈরি করাকে Intersection বলে।


Mathematical Definition:


A ∩ B = {x : x ∈ A এবং x ∈ B}


মানে:

যে x একই সাথে A এবং B তে আছে,
সেটি Intersection এর অংশ হবে।



Example:


A={1,2,3}

B={2,3,4}


A∩B

=

{2,3}
"""


# ===========================================================
# 05_Formula
# ===========================================================

"""
Intersection Formula:


A ∩ B = Common elements of A and B



Cardinality:


|A ∩ B|

=

Number of common elements



Union এর সাথে সম্পর্ক:


|A ∪ B|

=

|A| + |B| - |A ∩ B|



এখানে Intersection দেখায়
কোন element দুই জায়গায় common আছে।
"""


# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
ধরি:


A = {1,2,3,4}

B = {3,4,5,6}



Step 1:

A এর element:

1,2,3,4



Step 2:

B এর element:

3,4,5,6



Step 3:

Common element খুঁজি:


A তে আছে:

1 ✔
2 ✔
3 ✔
4 ✔


B তে আছে:

3 ✔
4 ✔
5 ✔
6 ✔



দুই জায়গায় থাকা element:


3,4



তাই:


A ∩ B = {3,4}



Cardinality:


|A∩B| = 2
"""


# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
Venn Diagram:


          A
      __________
     /          \
    /   1 2      \
   |      _____   |
   |     | 3 4 |  |
   |      -----   |
    \            /
     \__________/


          B


মাঝের অংশ:

A ∩ B


মানে:

দুই Circle এর overlap অংশ।



Computer Science এ:


Python Set Intersection:


A & B


অথবা


A.intersection(B)



Internal Working:


1. ছোট Set নির্বাচন করা হয়।
2. প্রতিটি element এর hash check করা হয়।
3. অন্য Set এ element থাকলে রাখা হয়।


Average Time Complexity:

O(min(n,m))


যেখানে:

n = A এর size

m = B এর size
"""


# ===========================================================
# 08_Examples
# ===========================================================

"""
Example 1:

Basic Intersection:

"""

A = {1,2,3,4}

B = {3,4,5,6}


result = A & B


print(result)



"""
Example 2:

Using intersection() method:

"""

result = A.intersection(B)

print(result)



"""
Example 3:

Multiple Sets:

"""

A = {1,2,3,4}

B = {2,3,5}

C = {3,4,5}


result = A & B & C


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


ai_students = {
    "Hasan",
    "Jamal"
}


common_students = python_students & ai_students


print(common_students)



"""
Example 5:

Common skills:

"""

developer1 = {
    "Python",
    "SQL",
    "React"
}


developer2 = {
    "Python",
    "Java",
    "SQL"
}


common_skills = developer1.intersection(developer2)


print(common_skills)



# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
Common Mistakes:


1. Intersection এ সব element থাকবে ভাবা


Wrong:

{1,2,3} ∩ {3,4,5}


Answer:

{1,2,3,4,5}


Correct:

{3}



--------------------------------


2. + অথবা - operator ব্যবহার করা


Wrong:


A + B


Correct:


A & B



--------------------------------


3. Empty Intersection বুঝতে না পারা


Example:


A={1,2}

B={3,4}


A∩B


Result:


set()



--------------------------------


4. Duplicate আশা করা


Set duplicate রাখে না।



--------------------------------


5. List এর index ব্যবহার করা


Intersection result Set হয়,
তাই index থাকে না।
"""


# ===========================================================
# 10_Exercises
# ===========================================================

"""
Exercise 1:


A={10,20,30,40}

B={30,40,50,60}


Intersection বের করো।



Exercise 2:


তিনটি Set এর common element বের করো।



Exercise 3:


দুইটি List থেকে common item বের করো
Set ব্যবহার করে।



Exercise 4:


একটি Social Media System এ:

User A likes:

{
"Python",
"AI",
"Music"
}


User B likes:

{
"AI",
"Music",
"Game"
}


Common interest বের করো।



Exercise 5:


Formula ব্যবহার করে:


A={1,2,3,4,5}

B={4,5,6,7}


|A∩B|

বের করো।
"""


# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
AI এবং Machine Learning এ Intersection এর ব্যবহার:


1. Feature Matching


Model A:

{
age,
salary,
experience
}


Model B:

{
age,
location,
experience
}



Common Feature:


{
age,
experience
}



--------------------------------


2. NLP (Natural Language Processing)


Document A:

{
python,
machine,
learning
}


Document B:

{
python,
deep,
learning
}



Common words:


{
python,
learning
}



--------------------------------


3. Recommendation System


User A:

{
AI,
Python,
Music
}


User B:

{
Python,
Music,
Game
}



Common Interest:


{
Python,
Music
}



--------------------------------


4. Similarity Calculation


Machine Learning এ
দুইটি data point কতটা similar
তা বের করতে Intersection ব্যবহার হয়।



--------------------------------


5. Database Query


Multiple conditions:


Users who are:

Python learners

AND

AI learners


এটি Intersection এর মতো কাজ করে।



Intersection হলো
Data Matching এবং Similarity Finding এর
একটি গুরুত্বপূর্ণ mathematical concept।
"""


print("Intersection of Sets শেখা সম্পন্ন!")