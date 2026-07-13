"""
============================================================
01_Introduction
============================================================
String Processing বলতে String (Text) নিয়ে কাজ করাকে বোঝায়। যেমন, "Hello World" থেকে,
• শব্দ বের করা, • ছোট হাতের লেখা বড় হাতের করা, • বড় হাতের লেখা ছোট হাতের করা, • নির্দিষ্ট শব্দ খুঁজে বের করা
• শব্দ পরিবর্তন করা, • Text পরিষ্কার করা, • Sentence ভাঙা, • Sentence জোড়া লাগানো

সবই String Processing। Python-এ প্রায় প্রতিটি Application-এ String Processing প্রয়োজন হয়। Examples: Search Engine, Chat Application, Compiler, Web Development, AI, Data Science, NLP, Cyber Security সব জায়গাতেই String Processing ব্যবহৃত হয়।
"""
# ============================================================
# 02_WhyStringProcessingExists
# ============================================================
"""
Computer মানুষের ভাষা বুঝে না। Computer শুধু Binary বোঝে। তাই মানুষের লেখা Text কে বিভিন্নভাবে Process করতে হয়।
Example: Input - "I love Python". কম্পিউটারকে হয়তো জানতে হবে-

• কয়টি শব্দ আছে?
• Python শব্দটি আছে?
• love কে like করা হবে?
• সব ছোট হাতের করা হবে?
• Extra Space সরানো হবে?
এই কাজগুলোর জন্য String Processing প্রয়োজন। AI, Search Engine, Chatbot, Email Filter,
Spell Checker, Translator— সব জায়গাতেই String Processing প্রথম ধাপ।
"""
# ============================================================
# 03_Syntax
# ============================================================
"""
String Method Call: string.method()
Example: 
text = "Python"
text.upper()
text.lower()
"""
text = "   I Love Python Programming   "
print(text.lower())
print(text.upper())
print(text.title())
print()

# ============================================================
# 04_Methods
# ============================================================

"""
Python-এর সবচেয়ে বেশি ব্যবহৃত String Methods:
split()
join()
replace()
find()
startswith()
endswith()
strip()
format()
f-string
regex (re module)
"""


# ------------------------------------------------------------
# split(): একটি String কে ভেঙে List বানায়। 
# ------------------------------------------------------------
text = "Python Java C++ Rust"
words = text.split()

print("split():")
print(words)
print()

# split with delimiter:
csv = "Apple,Banana,Mango"
print(csv.split(","))
print()

# ------------------------------------------------------------
# join(): অনেকগুলো String কে জোড়া লাগায়। join() List নেয়।
# ------------------------------------------------------------
words = ["I", "Love", "Python"]
sentence = " ".join(words)
print("join():")
print(sentence)
print()

path = "/".join(["home", "user", "downloads"])
print(path)
print()


# ------------------------------------------------------------
# replace(): একটি অংশকে অন্য অংশ দিয়ে পরিবর্তন করে।
# ------------------------------------------------------------
text = "I love Java"
new_text = text.replace("Java", "Python")

print("replace():")
print(new_text)
print()

# ------------------------------------------------------------
# find(): String-এর মধ্যে কোন শব্দ কোথায় আছে, তার Index দেয়। না পেলে -1 দেয়।
# ------------------------------------------------------------
text = "Python Programming"
print("find():")
print(text.find("Program"))
print(text.find("Java"))
print()

# ------------------------------------------------------------
# startswith(): String কোন অংশ দিয়ে শুরু হয়েছে?
# ------------------------------------------------------------
url = "https://google.com"

print("startswith():")
print(url.startswith("https"))
print(url.startswith("http"))
print()


# ------------------------------------------------------------
# endswith(): String কোন অংশ দিয়ে শেষ হয়েছে?
# ------------------------------------------------------------
filename = "image.png"

print("endswith():")
print(filename.endswith(".png"))
print(filename.endswith(".jpg"))
print()

# ------------------------------------------------------------
# strip(): শুরু এবং শেষের Extra Space সরায়।
# ------------------------------------------------------------
text = "      Python      "

print("strip():")
print("|" + text.strip() + "|")
print()

print(text.lstrip())
print(text.rstrip())
print()

# ------------------------------------------------------------
# format(): পুরোনো Style String Formatting
# ------------------------------------------------------------
name = "Mozammel"
age = 28

print("format():")
print("My name is {} and age is {}".format(name, age))
print()

# ------------------------------------------------------------
# f-string: Python 3.6+, সবচেয়ে জনপ্রিয় Formatting।
# ------------------------------------------------------------
name = "Mozammel"
language = "Python"

print("f-string:")
print(f"My name is {name}.")
print(f"I love {language}.")
print(f"2 + 5 = {2 + 5}")
print()

# ------------------------------------------------------------
# regex: Regular Expression, Pattern Matching-এর জন্য ব্যবহৃত হয়। Module - import re
# ------------------------------------------------------------

import re
text = "My phone number is 01712345678"
numbers = re.findall(r"\d+", text)

print("regex:")
print(numbers)
print()

emails = re.findall(r"\S+@\S+", "Contact me at abc@gmail.com")

print(emails)
print()


# ============================================================
# 05_TimeComplexity
# ============================================================

"""
Method                     Complexity
split()                    O(n)
join()                     O(n)
replace()                  O(n)
find()                     O(n)
startswith()               O(k)
endswith()                 O(k)
strip()                    O(n)
format()                   O(n)
f-string                   O(n)
regex                      সাধারণত O(n)

কিন্তু জটিল Pattern-এর ক্ষেত্রে, Backtracking হওয়ার কারণে অনেক বেশি সময় লাগতে পারে। n = String Length, k = Prefix অথবা Suffix Length
"""

# ============================================================
# 06_InternalWorking
# ============================================================

"""
Python String Immutable।

Memory:
+----------------------+
| Hello Python World   |
+----------------------+

replace():
+----------------------+
| Hello Java World     |
+----------------------+

পুরোনো String পরিবর্তন হয় না। নতুন String তৈরি হয়।
------------------------------------------------------------
split(): পুরো String Scan করে। Delimiter পেলেই নতুন Token তৈরি করে। শেষে List Return করে।
------------------------------------------------------------
join(): আগে মোট Length হিসাব করে। তারপর একবারেই নতুন String তৈরি করে। তাই join() অনেকগুলো String + দিয়ে যোগ করার চেয়ে দ্রুত।
------------------------------------------------------------
find(): বাম থেকে ডানে Scan করে। Character মিললে Index Return করে। না পেলে -1
------------------------------------------------------------
startswith(): শুরুর Character গুলো Compare করে।
------------------------------------------------------------
endswith(): শেষের Character Compare করে।
------------------------------------------------------------
strip(): শুরু ও শেষের Whitespace Scan করে। মাঝখানের Space মুছে না।
------------------------------------------------------------
format(): Placeholder খুঁজে Value বসায়।
------------------------------------------------------------
f-string: Compile হওয়ার সময়ই Expression Parse হয়। Runtime-এ দ্রুত String তৈরি হয়।
------------------------------------------------------------
regex: 
Regular Expression Engine
↓
Pattern Parse
↓
State Machine তৈরি
↓
Character Scan
↓
Match Return

Complex Pattern হলে Backtracking হতে পারে।
"""

# ============================================================
# 07_Examples
# ============================================================

print("========== Example 1 ==========")
sentence = "Machine Learning with Python"
print(sentence.split())
print()

print("========== Example 2 ==========")
items = ["AI", "ML", "DL"]
print(", ".join(items))
print()

print("========== Example 3 ==========")
text = "Python is good"
print(text.replace("good", "awesome"))
print()

print("========== Example 4 ==========")
email = "example@gmail.com"
print(email.endswith(".com"))
print()

print("========== Example 5 ==========")
user = "      Mozammel      "
print(user.strip())
print()

print("========== Example 6 ==========")
name = "Rahim"
score = 95
print(f"{name} scored {score}")
print()

print("========== Example 7 ==========")
paragraph = """
Python is easy.
Python is powerful.
Python is popular.
"""
print(paragraph.count("Python"))
print()

print("========== Example 8 ==========")
sentence = "one,two,three,four"
print(sentence.split(","))
print()

print("========== Example 9 ==========")
text = "My email is test@gmail.com"
emails = re.findall(r"\S+@\S+", text)
print(emails)
print()


# ============================================================
# 08_CommonMistakes
# ============================================================

"""
১। text.replace("a","b") - অনেকে ভাবেন text পরিবর্তন হয়েছে। ভুল। কারণ replace() নতুন String Return করে। সঠিক text = text.replace(...)
------------------------------------------------------------
২। join() List নেয়। ভুল "a".join("hello"). যদিও এটি কাজ করে, এটি String-এর প্রতিটি Character-এর মাঝে
    "a" বসায়, যা অনেক সময় অনাকাঙ্ক্ষিত ফল দেয়। সাধারণত join() ব্যবহার করা হয় List-এর সাথে।
------------------------------------------------------------
৩। find() -1 দিতে পারে। তাই Index ব্যবহার করার আগে Check করা উচিত।
------------------------------------------------------------
৪। strip() মাঝখানের Space মুছে না। শুধু শুরু ও শেষের Space মুছে।
------------------------------------------------------------
৫। Regex Pattern ভুল লিখলে Unexpected Result পাওয়া যায়।
"""

# ============================================================
# 09_Exercises
# ============================================================

"""
Exercise 1: একটি String কে শব্দে ভাগ করো।
--------------------------------
Exercise 2: একটি List কে "-" দিয়ে Join করো।
--------------------------------
Exercise 3: সব "Python" কে "AI" দিয়ে Replace করো।
--------------------------------
Exercise 4: একটি Email ".com" দিয়ে শেষ হয়েছে কিনা দেখো।
--------------------------------
Exercise 5: Extra Space Remove করো।
--------------------------------
Exercise 6: নিজের নাম ও বয়স f-string দিয়ে Print করো।
--------------------------------
Exercise 7: Regex ব্যবহার করে একটি Paragraph থেকে সব সংখ্যা বের করো।
--------------------------------
Exercise 8: Regex ব্যবহার করে সব Email বের করো।
--------------------------------
Exercise 9: একটি URL "https://" দিয়ে শুরু হয়েছে কিনা দেখো।
--------------------------------
Exercise 10: CSV String কে List-এ Convert করো।
"""

# ============================================================
# 10_AIUsage (Use Case in AI Development)
# ============================================================

"""
NLP (Natural Language Processing)-এ String Processing হলো সবচেয়ে মৌলিক এবং গুরুত্বপূর্ণ ধাপ। কারণ AI-এর কাছে Text মূলত String হিসেবেই আসে। AI Pipeline-এর শুরুতে প্রায় সবসময় String Processing হয়।

User Input
        │
        ▼
Raw String
        │
        ▼
Lowercase করা
        │
        ▼
Extra Space Remove (strip)
        │
        ▼
Sentence Split
        │
        ▼
Word Split (Tokenization-এর প্রাথমিক ধাপ)
        │
        ▼
Replace / Clean
        │
        ▼
Regex দিয়ে Email, Phone, URL বের করা
        │
        ▼
Tokenizer
        │
        ▼
Embedding
        │
        ▼
LLM / NLP Model

বাস্তব AI Project-এ String Processing ব্যবহার হয়—

• ChatGPT-এর Prompt পরিষ্কার করতে
• Chatbot-এর User Message Process করতে
• Spam Detection
• Sentiment Analysis
• Machine Translation
• OCR-এর Text পরিষ্কার করতে
• Search Engine Query Normalize করতে
• Resume Parsing
• Email Classification
• Log Analysis
• Document Processing
• Voice-to-Text Output Clean করতে
• Named Entity Recognition (NER)-এর আগে Text প্রস্তুত করতে

AI Engineer হিসেবে Regex বিশেষভাবে কাজে লাগে—

✓ Email Extract
✓ Phone Number Detect
✓ URL Detect
✓ Date Detect
✓ Hashtag Detect
✓ Mention Detect (@username)
✓ HTML Tag Remove
✓ Special Character Remove

AI-তে সবচেয়ে বেশি ব্যবহৃত String Operations

✓ lower()
✓ split()
✓ join()
✓ replace()
✓ strip()
✓ find()
✓ regex
✓ f-string (Prompt Engineering-এর জন্য)

মনে রাখবে—

NLP uses strings everywhere.
Text Data → String
Prompt → String
Document → String
Chat → String
Search Query → String
Code → String

LLM-এর Input এবং Output—দুটিই মূলত String।
"""