"""
===========================================================
Complement of Sets (সেটের Complement)
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
Complement (Aᶜ বা A') হলো Set Theory এর একটি গুরুত্বপূর্ণ ধারণা।

Complement ব্যবহার করে Universal Set এর মধ্যে থাকা
কিন্তু নির্দিষ্ট Set এ নেই এমন element বের করা হয়।


Symbol:

Aᶜ

অথবা

A'


Example:


Universal Set:

U = {1,2,3,4,5,6}


A = {1,2,3}


তাহলে:


Aᶜ = {4,5,6}



অর্থাৎ:

U এর element থেকে A বাদ দিলে
যা থাকে সেটাই Complement।
"""


# ===========================================================
# 02_WhyThisConceptExistsInRelationToHistory
# ===========================================================

"""
ইতিহাস:

মানুষ যখন কোনো নির্দিষ্ট group এর বাইরে থাকা
বস্তু বা element খুঁজতে চেয়েছিল,
তখন Complement ধারণার প্রয়োজন হয়।


উদাহরণ:


একটি স্কুলে:


সব ছাত্র:

Universal Set


যারা Science বিভাগে:

A Set



Science এর বাইরে যারা আছে:

Aᶜ



এই "বাকি অংশ" বের করার জন্য Complement ব্যবহৃত হয়।


Set Theory তে Complement একটি গুরুত্বপূর্ণ
logical operation হিসেবে ব্যবহৃত হয়।
"""


# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
বাস্তব জীবনের উদাহরণ:


ধরি:


একটি ক্লাসে মোট ছাত্র:


U = {
Rahim,
Karim,
Hasan,
Jamal,
Rafi
}



যারা Football খেলে:


A = {
Rahim,
Hasan
}



যারা Football খেলে না:


Aᶜ


=

{
Karim,
Jamal,
Rafi
}



অর্থাৎ:

Total Students - Football Players

=

Non Football Players
"""


# ===========================================================
# 04_Definition
# ===========================================================

"""
Definition:


Universal Set এর মধ্যে থাকা
কিন্তু নির্দিষ্ট Set এর মধ্যে না থাকা
element গুলোকে সেই Set এর Complement বলে।


Mathematical Definition:


Aᶜ = {x : x ∈ U এবং x ∉ A}



যেখানে:


U = Universal Set

A = একটি Set


Example:


U={1,2,3,4,5}

A={1,2}


তাহলে:


Aᶜ={3,4,5}
"""


# ===========================================================
# 05_Formula
# ===========================================================

"""
Complement Formula:


Aᶜ = U - A



যেখানে:


U = Universal Set

A = Given Set



Cardinality Formula:


|Aᶜ| = |U| - |A|



Example:


U={1,2,3,4,5,6}

A={1,2,3}



|U| = 6

|A| = 3



|Aᶜ|

=

6 - 3

=

3
"""


# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
ধরি:


Universal Set:


U = {1,2,3,4,5,6,7,8}



A = {2,4,6}



Step 1:

Universal Set এর সব element:


1,2,3,4,5,6,7,8



Step 2:

A এর element বাদ দিই:


2,4,6



Step 3:

যেগুলো বাকি থাকে:


1,3,5,7,8



তাই:


Aᶜ

=

{1,3,5,7,8}



Cardinality:


|Aᶜ|

=

8 - 3

=

5
"""


# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
Venn Diagram:


        Universal Set (U)

    ______________________
   |                      |
   |    __________        |
   |   |          |       |
   |   |    A     |       |
   |   |  1 2 3   |       |
   |   |__________|       |
   |                      |
   |   4 5 6 7            |
   |______________________|



A এর বাইরে কিন্তু U এর ভিতরের অংশ:

Aᶜ



Computer Science এ:


Complement এর ধারণা:


NOT operation এর মতো কাজ করে।


Example:


Set:

A = {True values}



Complement:

Aᶜ = {False values}



Logic:

NOT A



Database:


WHERE condition NOT IN


এর মতো কাজ করে।
"""


# ===========================================================
# 08_Examples
# ===========================================================

"""
Example 1:

Basic Complement:

"""

U = {1,2,3,4,5,6}

A = {1,2,3}


complement = U - A


print(complement)



"""
Example 2:

Using function:

"""

def complement(universal, set_a):
    return universal - set_a


U = {10,20,30,40,50}

A = {20,40}


print(complement(U,A))



"""
Example 3:

Student Example:

"""

students = {
    "Rahim",
    "Karim",
    "Hasan",
    "Jamal"
}


python_students = {
    "Rahim",
    "Hasan"
}


not_python_students = students - python_students


print(not_python_students)



"""
Example 4:

Number Classification:

"""

U = set(range(1,11))


even = {
    2,4,6,8,10
}


odd = U - even


print(odd)



"""
Example 5:

Permission System:

"""

all_users = {
    "Admin",
    "Editor",
    "Viewer"
}


admins = {
    "Admin"
}


non_admins = all_users - admins


print(non_admins)



# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
Common Mistakes:


1. Universal Set ছাড়া Complement বের করা


Wrong:


Aᶜ


কারণ:

Complement সবসময় Universal Set এর উপর নির্ভর করে।



--------------------------------


2. Difference এবং Complement এক মনে করা


Difference:


A-B


Complement:


U-A



Complement এ সবসময় Universal Set থাকে।



--------------------------------


3. Universal Set ভুল নির্বাচন করা


Example:


U={1,2,3,4}

A={1,2}


Aᶜ={3,4}



যদি U পরিবর্তন হয়,
Complement পরিবর্তন হবে।



--------------------------------


4. Empty Set এর Complement ভুল বোঝা


U এর Complement:


∅ᶜ = U



--------------------------------


5. Set notation ভুল লেখা


Correct:

Aᶜ

A'

"""


# ===========================================================
# 10_Exercises
# ===========================================================

"""
Exercise 1:


U={1,2,3,4,5,6}

A={2,4,6}


Aᶜ বের করো।



Exercise 2:


U={a,b,c,d,e}

B={b,d}


Bᶜ বের করো।



Exercise 3:


একটি Class এর:

All Students

এবং

Passed Students


দিয়ে Failed Students বের করো।



Exercise 4:


Formula ব্যবহার করে:


|U| = 20

|A| = 8


তাহলে:

|Aᶜ| = ?



Exercise 5:


নিজের উদাহরণ দিয়ে
Universal Set এবং Complement তৈরি করো।
"""


# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
AI এবং Machine Learning এ Complement এর ব্যবহার:


1. Binary Classification


Positive Class:


A = Sick Patients



Complement:


Aᶜ = Healthy Patients



মানে:

NOT Positive



--------------------------------


2. Feature Selection


All Features:


U = {
age,
salary,
location,
experience
}



Selected Features:


A = {
age,
salary
}



Unused Features:


Aᶜ

=

{
location,
experience
}



--------------------------------


3. Data Filtering


Dataset:

All Data


Selected Data:


A



Remaining Data:


Aᶜ



--------------------------------


4. Computer Vision


Image Pixels:

All pixels


Detected Object Pixels:


A



Background Pixels:


Aᶜ



--------------------------------


5. Natural Language Processing


Vocabulary:

U


Known Words:

A


Unknown Words:


Aᶜ



Complement AI তে
Negative class, remaining data,
background detection এবং filtering এ ব্যবহৃত হয়।
"""


print("Complement of Sets শেখা সম্পন্ন!")