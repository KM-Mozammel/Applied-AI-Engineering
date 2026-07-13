"""
===========================================================
Difference of Sets (সেটের Difference)
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
Difference (−) হলো Set Theory এর একটি গুরুত্বপূর্ণ operation।

Difference ব্যবহার করে একটি Set থেকে অন্য Set এর element
বাদ দিয়ে নতুন Set তৈরি করা হয়।


Symbol:

−


Example:


A = {1,2,3,4}

B = {3,4,5,6}


A - B


Result:

{1,2}


কারণ:

A তে আছে:

1,2,3,4


B তে আছে:

3,4,5,6


A থেকে B এর common element বাদ দিলে:

1,2 থাকে।
"""


# ===========================================================
# 02_WhyThisConceptExistsInRelationToHistory
# ===========================================================

"""
ইতিহাস:

মানুষ যখন বিভিন্ন group বা collection নিয়ে কাজ শুরু করে,
তখন শুধু মিল খোঁজা নয়, বরং একটি group থেকে অন্য group
বাদ দেওয়ার প্রয়োজন হয়।


উদাহরণ:

একটি স্কুলে:

সব ছাত্রদের Set

এবং

পরীক্ষায় অনুপস্থিত ছাত্রদের Set


যারা উপস্থিত ছিল তাদের বের করতে হলে:

সব ছাত্র - অনুপস্থিত ছাত্র


এই ধারণা থেকেই Difference operation এসেছে।


Set Theory তে Difference একটি গুরুত্বপূর্ণ operation।
"""


# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
বাস্তব জীবনের উদাহরণ:


ধরি:


All Students:

A = {
"Rahim",
"Karim",
"Hasan",
"Jamal"
}



Passed Students:

B = {
"Rahim",
"Hasan"
}



যারা Pass করেনি:


A - B


Result:


{
"Karim",
"Jamal"
}



অর্থাৎ Difference একটি Set থেকে
অন্য Set এর অংশ বাদ দেয়।
"""


# ===========================================================
# 04_Definition
# ===========================================================

"""
Definition:


A এবং B দুইটি Set হলে,
A থেকে B এর element বাদ দেওয়ার operation কে
Difference বলে।


Mathematical Definition:


A - B = {x : x ∈ A এবং x ∉ B}



মানে:


যে element A তে আছে,
কিন্তু B তে নেই,
সেগুলো Difference এর অংশ হবে।



Example:


A={1,2,3,4}

B={3,4,5}


A-B


=

{1,2}
"""


# ===========================================================
# 05_Formula
# ===========================================================

"""
Difference Formula:


A - B

=

A এর element যা B তে নেই



Similarly:


B - A

=

B এর element যা A তে নেই



Example:


A={1,2,3,4}

B={3,4,5,6}



A-B

=

{1,2}



B-A

=

{5,6}



Important:

A-B এবং B-A সাধারণত সমান হয় না।
"""


# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
ধরি:


A = {1,2,3,4,5}

B = {4,5,6,7}



Step 1:

A এর element:


1,2,3,4,5



Step 2:

B এর element:


4,5,6,7



Step 3:

A এর element check করি:


1 → B তে নেই ✔

2 → B তে নেই ✔

3 → B তে নেই ✔

4 → B তে আছে ✘

5 → B তে আছে ✘



তাই:


A-B


=

{1,2,3}



Cardinality:


|A-B| = 3
"""


# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
Venn Diagram:


        A
    ___________
   /           \
  /  1 2 3      \
 |       _____   |
 |      | 4 5 |  |
  \     |_____|
   \___________/


        B


A-B হলো:

A এর সেই অংশ
যেখানে B নেই।



Computer Science এ:


Python:


A - B


অথবা:


A.difference(B)



Internal Working:


1. প্রথম Set এর element নেয়।
2. দ্বিতীয় Set এর hash table এ search করে।
3. যেগুলো পাওয়া যায় না সেগুলো রাখে।


Average Time Complexity:


O(n)


যেখানে:

n = প্রথম Set এর size
"""


# ===========================================================
# 08_Examples
# ===========================================================

"""
Example 1:

Basic Difference:

"""

A = {1,2,3,4}

B = {3,4,5,6}


result = A - B


print(result)



"""
Example 2:

Using difference() method:

"""

result = A.difference(B)

print(result)



"""
Example 3:

Reverse Difference:

"""

result = B - A

print(result)



"""
Example 4:

Real life example:

"""

all_students = {
    "Rahim",
    "Karim",
    "Hasan",
    "Jamal"
}


present_students = {
    "Rahim",
    "Hasan"
}


absent_students = all_students - present_students


print(absent_students)



"""
Example 5:

Finding missing skills:

"""

required_skills = {
    "Python",
    "SQL",
    "React",
    "Docker"
}


my_skills = {
    "Python",
    "SQL"
}


missing_skills = required_skills - my_skills


print(missing_skills)



# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
Common Mistakes:


1. Difference কে Symmetric ভাবা


Wrong:


A-B = B-A


Correct:


A-B != B-A



--------------------------------


2. Union এর মতো কাজ করবে ভাবা


A-B সব element রাখে না।

শুধু A এর unique element রাখে।



--------------------------------


3. Empty Set ভুল বোঝা


A - empty set


=

A



--------------------------------


4. Set এ duplicate আশা করা


Difference duplicate remove করে।



--------------------------------


5. Operator ভুল ব্যবহার করা


Wrong:


A / B


Correct:


A - B
"""


# ===========================================================
# 10_Exercises
# ===========================================================

"""
Exercise 1:


A={10,20,30,40}

B={30,40,50}


A-B বের করো।



Exercise 2:


B-A বের করো।



Exercise 3:


দুইটি List থেকে
শুধু প্রথম List এর unique item বের করো।



Exercise 4:


একটি Job Requirement:


Required:

{
Python,
SQL,
React,
Docker
}


Your Skill:


{
Python,
SQL
}


Missing skill বের করো।



Exercise 5:


দুটি Set দিয়ে প্রমাণ করো:


A-B != B-A
"""


# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
AI এবং Machine Learning এ Difference এর ব্যবহার:


1. Feature Difference


Required Features:

{
age,
salary,
experience,
location
}


Available Features:

{
age,
salary
}



Missing Features:


Required - Available


=

{
experience,
location
}



--------------------------------


2. Data Cleaning


নতুন Dataset থেকে
পুরনো Dataset এর data বাদ দিতে Difference ব্যবহার হয়।



--------------------------------


3. NLP


Old Vocabulary:


{
python,
ai,
data
}


New Vocabulary:


{
python,
ai,
data,
ml
}



New Words:


New - Old


=

{
ml
}



--------------------------------


4. Recommendation System


User এর দেখা item:


{
Movie1,
Movie2
}



Total Available:


{
Movie1,
Movie2,
Movie3,
Movie4
}



Not Watched:


Available - Watched



--------------------------------


5. Machine Learning Pipeline


Training data থেকে
validation data আলাদা করতে
Difference concept ব্যবহার করা যায়।



Difference হলো
Data Filtering এবং Data Comparison এর
একটি গুরুত্বপূর্ণ mathematical concept।
"""


print("Difference of Sets শেখা সম্পন্ন!")