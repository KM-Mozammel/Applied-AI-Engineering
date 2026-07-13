"""
===========================================================
Set (সেট)
===========================================================

Structure:

01_Introduction
02_WhyThisConceptExistsInRealtionTohistory
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
সেট (Set) হলো গণিতের একটি মৌলিক ধারণা যেখানে নির্দিষ্ট কিছু
বস্তু বা উপাদানকে একটি সংগ্রহ (collection) হিসেবে রাখা হয়।

উদাহরণ:

A = {1, 2, 3, 4, 5}

এখানে A একটি Set এবং এর element হলো:
1, 2, 3, 4, 5

Programming, Database, Mathematics এবং AI-তে Set অনেক গুরুত্বপূর্ণ।
"""


# ===========================================================
# 02_WhyThisConceptExistsInRelationToHistory
# ===========================================================

"""
ইতিহাস:

প্রাচীন গণিতে মানুষ সংখ্যা, বস্তু এবং বিভিন্ন জিনিসকে শ্রেণীবদ্ধ
করার প্রয়োজন অনুভব করেছিল।

যেমন:

- বিজোড় সংখ্যা
- জোড় সংখ্যা
- মৌলিক সংখ্যা
- নির্দিষ্ট এলাকার মানুষ

এই ধরনের collection নিয়ে কাজ করার জন্য Set ধারণার প্রয়োজন হয়।

আধুনিক Set Theory তৈরি করেন:

Georg Cantor (১৮৪৫-১৯১৮)

তিনি Infinite Set এবং Mathematical Set Theory নিয়ে কাজ করেন।

আজকের দিনে Set ব্যবহার হয়:

- Mathematics
- Computer Science
- Database
- Artificial Intelligence
"""


# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
বাস্তব জীবনের উদাহরণ:

ধরি:

একটি ক্লাসে ছাত্রদের নাম:

Students = {
    "Rahim",
    "Karim",
    "Hasan"
}

এটি একটি Set।

আরেকটি উদাহরণ:

Fruits = {
    "Apple",
    "Banana",
    "Mango"
}


Set এর বৈশিষ্ট্য:

1. Duplicate থাকে না

Example:

A = {1, 2, 2, 3}

আসলে:

A = {1, 2, 3}


2. Order গুরুত্বপূর্ণ নয়

A = {1,2,3}

এবং

B = {3,2,1}

দুটো Set একই।
"""


# ===========================================================
# 04_Definition
# ===========================================================

"""
Set Definition:

Set হলো এমন একটি well-defined collection যেখানে
প্রতিটি element unique থাকে।

Notation:

A = {elements}


Example:

A = {2,4,6,8}


Element membership:

যদি 4, A এর মধ্যে থাকে:

4 ∈ A


যদি 5, A এর মধ্যে না থাকে:

5 ∉ A


প্রধান ধরনের Set:

1. Empty Set

যার কোনো element নেই।

Example:

A = {}


2. Finite Set

যার element সংখ্যা সীমিত।

Example:

A = {1,2,3}


3. Infinite Set

যার element অসীম।

Example:

Natural Numbers:

N = {1,2,3,4,...}


4. Universal Set

যে Set নিয়ে আলোচনা করা হচ্ছে তার সব element।

Symbol:

U
"""


# ===========================================================
# 05_Formula
# ===========================================================

"""
Set এর কিছু গুরুত্বপূর্ণ Formula:


1. Union

দুইটি Set একত্র করা:

A ∪ B


Example:

A = {1,2,3}

B = {3,4,5}


A ∪ B = {1,2,3,4,5}



2. Intersection

দুই Set এর common element:

A ∩ B


Example:

A ∩ B = {3}



3. Difference

A এর element কিন্তু B তে নেই:

A - B


Example:

A - B = {1,2}



4. Cardinality

Set এর মোট element সংখ্যা:

|A|


Example:

A={1,2,3}

|A| = 3



5. Cartesian Product


A × B


Example:

A={1,2}

B={a,b}


A×B=

{
(1,a),
(1,b),
(2,a),
(2,b)
}

"""


# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
Union:

ধরি,

A={1,2,3}

B={3,4,5}


দুইটি Set combine করলে:

{1,2,3,3,4,5}


কিন্তু Set duplicate রাখে না।

তাই:

A∪B={1,2,3,4,5}



Intersection:

যে element দুই জায়গায় আছে:

A={1,2,3}

B={3,4,5}


Common:

{3}


তাই:

A∩B={3}



Cardinality:

Set এর element গুনলেই সংখ্যা পাওয়া যায়।

A={10,20,30}

তাহলে:

|A|=3
"""


# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
Visualization:

Set কে সাধারণত Venn Diagram দিয়ে দেখানো হয়।

Example:

A:

 ________
|        |
| 1 2 3 |
|________|


B:

 ________
|        |
| 3 4 5 |
|________|


Overlap অংশ:

A ∩ B

= {3}



Computer Science এ:

Python Set internally Hash Table ব্যবহার করে।

Example:

numbers = {1,2,3}


Memory:

Hash Table:

Hash(1) -> location
Hash(2) -> location
Hash(3) -> location


এজন্য:

Search:

O(1) average time complexity

হয়।
"""


# ===========================================================
# 08_Examples
# ===========================================================

"""
Example 1:

Python Set:

"""

numbers = {1, 2, 3, 4, 5}

print(numbers)


"""
Example 2:

Duplicate remove:

"""

numbers = [1,2,2,3,3,4]

unique_numbers = set(numbers)

print(unique_numbers)



"""
Example 3:

Union:

"""

A = {1,2,3}

B = {3,4,5}

print(A | B)



"""
Example 4:

Intersection:

"""

print(A & B)



"""
Example 5:

Difference:

"""

print(A - B)



"""
Example 6:

Membership checking:

"""

fruits = {"apple", "banana"}

print("apple" in fruits)



# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
Common Mistakes:

1. Duplicate আশা করা

Wrong:

A={1,1,2,3}

Result:

{1,2,3}



2. Index ব্যবহার করা

Set এ index নেই।

Wrong:

A[0]


কারণ Set unordered.



3. Empty Set ভুল লেখা

Wrong:

{}

এটি Dictionary তৈরি করে।


Correct:

set()



4. Mutable element রাখা

Wrong:

{
    [1,2]
}


কারণ list mutable।



5. Order এর উপর নির্ভর করা

Set এর order guaranteed নয়।
"""


# ===========================================================
# 10_Exercises
# ===========================================================

"""
Exercise 1:

একটি Set তৈরি করো:

numbers = {10,20,30,40}


Exercise 2:

দুইটি Set এর Union বের করো।


Exercise 3:

দুইটি Set এর Intersection বের করো।


Exercise 4:

একটি List থেকে duplicate remove করো Set ব্যবহার করে।


Exercise 5:

Check করো একটি element Set এর মধ্যে আছে কিনা।


Exercise 6:

নিজের নামের অক্ষরগুলো দিয়ে একটি Set তৈরি করো।

Example:

name = "python"

output:

{'p','y','t','h','o','n'}
"""


# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
AI এবং Machine Learning এ Set এর ব্যবহার:


1. Feature Selection

Machine Learning এ অনেক feature থাকে।

Set ব্যবহার করে:

common_features = 
features_model_A ∩ features_model_B


দুই model এর common feature পাওয়া যায়।



2. Data Cleaning

Duplicate data remove করতে:

data = set(dataset)



3. NLP (Natural Language Processing)

Vocabulary তৈরি:

sentence:

"I love AI"


Words:

{
"I",
"love",
"AI"
}



4. Recommendation System

User interest:

User_A = {"Python","AI","Math"}

User_B = {"Python","AI","Web"}


Common interest:

User_A ∩ User_B


Result:

{"Python","AI"}



5. Graph Algorithm

Visited nodes tracking:

visited = set()

এটি BFS এবং DFS এ ব্যবহৃত হয়।



6. Database

Unique records maintain করতে Set concept ব্যবহার হয়।



Set হলো AI এবং Computer Science এর
একটি fundamental data structure।
"""


print("Set শেখা সম্পন্ন!")