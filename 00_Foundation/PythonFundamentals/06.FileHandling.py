"""
============================================================
# 01_Introduction (ফাইল হ্যান্ডলিং কী?)
============================================================
File Handling অর্থ হলো Python ব্যবহার করে বিভিন্ন ধরনের ফাইল তৈরি করা, পড়া (Read), লেখা (Write), আপডেট করা (Append), এবং ডিলিট করা। বাস্তব জীবনে প্রায় সব সফটওয়্যারই কোনো না কোনোভাবে ফাইল ব্যবহার করে।
যেমন—
✅ User Data
✅ Configuration
✅ Images
✅ CSV Dataset
✅ JSON API Response
✅ AI Model
✅ Log Files

Python File Handling শেখা মানে হলো, Operating System-এর সাথে কথা বলতে শেখা।
------------------------------------------------------------
Python যেসব File সহজে Handle করতে পারে, 
1. txt
2. csv
3. json
4. pickle
5. yaml
6. binary file
7. image
8. audio
9. video
------------------------------------------------------------
সবচেয়ে গুরুত্বপূর্ণ Module, 
open()
pathlib
json
csv
pickle
yaml (PyYAML)
"""
# ============================================================
# 02_WhyFileHandlingExists
# ============================================================
""" কম্পিউটারের RAM অস্থায়ী। Program বন্ধ হয়ে গেলে RAM-এর সব Data হারিয়ে যায়। তাই Data Permanent রাখার জন্য File প্রয়োজন।
Example, Shopping App

User Login
↓
RAM
↓
Program বন্ধ
↓
সব User Data হারিয়ে গেল

সমাধান, User Data File-এ Save করো।
------------------------------------------------------------
AI Project:-

Dataset
↓
CSV File
↓
Python
↓
Train Model
↓
Model Save
↓
pickle / pt / pth
------------------------------------------------------------
কেন File Handling দরকার?
✅ Data Save করতে
✅ Dataset Load করতে
✅ Configuration রাখতে
✅ API Response Store করতে
✅ Model Save করতে
✅ Log রাখতে
✅ Report Generate করতে
"""
# ============================================================
# 03_Syntax
# ============================================================

"""
File Open: open(filename, mode)
Mode:-
r   Read
w   Write
a   Append
x   Create
b   Binary
t   Text
+   Read + Write
------------------------------------------------------------
Examples
"""
# Read: file = open("data.txt", "r")
# Write: file = open("data.txt", "w")
# Append: file = open("data.txt", "a")
# Binary: file = open("image.png", "rb")
# Better Way

"""
with open("data.txt","r") as file:
    data=file.read()

Automatically file close হয়ে যাবে।
"""
# ============================================================
# 04_Methods
# ============================================================
"""
=================================
TXT
=================================
read()
readline()
readlines()
write()
writelines()
close()
flush()
seek()
tell()
=================================
CSV
=================================
csv.reader()
csv.writer()
csv.DictReader()
csv.DictWriter()
=================================
JSON
=================================
json.load()
json.loads()
json.dump()
json.dumps()
=================================
PICKLE
=================================
pickle.dump()
pickle.load()
=================================
YAML
=================================
yaml.safe_load()
yaml.safe_dump()
=================================
PATHLIB
=================================
Path()
exists()
mkdir()
touch()
unlink()
rename()
glob()
iterdir()
is_file()
is_dir()
read_text()
write_text()
"""
# ============================================================
# TXT
# ============================================================
print("===== TXT =====")

with open("sample.txt", "w") as file:
    file.write("Hello Python\n")
    file.write("File Handling")

with open("sample.txt", "r") as file:
    print(file.read())

# ============================================================
# CSV
# ============================================================
import csv
print("\n===== CSV =====")

rows = [
    ["Name", "Age"],
    ["Mozammel", 27],
    ["Rahim", 24]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# ============================================================
# JSON
# ============================================================
import json
print("\n===== JSON =====")

person = {
    "name": "Mozammel",
    "age": 27,
    "language": "Python"
}

with open("person.json", "w") as file:
    json.dump(person, file, indent=4)

with open("person.json", "r") as file:
    data = json.load(file)

print(data)

# ============================================================
# PICKLE
# ============================================================
import pickle
print("\n===== PICKLE =====")

numbers = [1, 2, 3, 4, 5]

with open("numbers.pkl", "wb") as file:
    pickle.dump(numbers, file)

with open("numbers.pkl", "rb") as file:
    loaded = pickle.load(file)

print(loaded)

# ============================================================
# YAML
# ============================================================

"""
PyYAML Install
pip install pyyaml
"""

try:
    import yaml

    print("\n===== YAML =====")

    config = {
        "host": "localhost",
        "port": 8000,
        "debug": True
    }

    with open("config.yaml", "w") as file:
        yaml.safe_dump(config, file)

    with open("config.yaml", "r") as file:
        loaded = yaml.safe_load(file)

    print(loaded)

except ModuleNotFoundError:
    print("\nPyYAML install করা নেই।")
    print("Run: pip install pyyaml")

# ============================================================
# PATHLIB
# ============================================================
from pathlib import Path
print("\n===== PATHLIB =====")

path = Path("hello.txt")
path.write_text("Hello Pathlib")
print(path.read_text())
print(path.exists())
print(path.is_file())

# ============================================================
# 05_TimeComplexity
# ============================================================

"""
Operation                 Complexity
------------------------------------
Read Entire File          O(n)
Write Entire File         O(n)
Append                    O(1) average
Seek                      O(1)
Tell                      O(1)
JSON Load                 O(n)
JSON Dump                 O(n)
CSV Read                  O(n)
CSV Write                 O(n)
Pickle Load               O(n)
Pickle Dump               O(n)
Path Exists               O(1)
------------------------------------------------------------
n = File Size
"""

# ============================================================
# 06_InternalWorking
# ============================================================
"""
Python File Handling-এর ভিতরে কী ঘটে?
Example:

with open("data.txt","r") as file:
↓
Python
↓
OS System Call
↓
Operating System
↓
File System
↓
SSD / HDD
↓
Bytes
↓
Python Decode
↓
Unicode String
------------------------------------------------------------
Write Process:

Python String
↓
UTF-8 Encode
↓
Bytes
↓
Operating System Buffer
↓
Disk
------------------------------------------------------------
with statement:

Enter
↓
Open File
↓
Work
↓
Exit
↓
Automatically Close
------------------------------------------------------------
Buffer কী? প্রতিটি Character সঙ্গে সঙ্গে Disk-এ লেখা হয় না। প্রথমে RAM Buffer-এ জমা হয়।
Buffer Full -> Disk Write, এভাবে File অনেক দ্রুত লেখা যায়।
"""
# ============================================================
# 07_Examples
# ============================================================

print("\n===== Example 1 =====")
with open("notes.txt", "w") as file:
    file.write("Python\n")
    file.write("AI\n")

print("\n===== Example 2 =====")
with open("notes.txt") as file:
    for line in file:
        print(line.strip())

print("\n===== Example 3 =====")
students = [
    {"name": "A", "marks": 80},
    {"name": "B", "marks": 90}
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

print("\n===== Example 4 =====")
folder = Path("AI_Project")

if not folder.exists():
    folder.mkdir()

print(folder.exists())

# ============================================================
# 08_CommonMistakes
# ============================================================
"""
১. file = open("data.txt"). File Close করতে ভুলে যাওয়া। সমাধান: with ব্যবহার করো।
------------------------------------------------------------
২. Read Mode-এ Write করা। open("a.txt","r") - file.write() - Error হবে।
------------------------------------------------------------
৩. Binary File Text Mode-এ খোলা। open("image.png","r") - উচিত open("image.png","rb")
------------------------------------------------------------
৪. Encoding Problem: UTF-8 না ব্যবহার করলে বাংলা নষ্ট হতে পারে। open("file.txt", encoding="utf-8")
------------------------------------------------------------
৫. json.load() এবং json.loads() দুটো আলাদা। load() -> File, loads() -> String
------------------------------------------------------------
৬. pickle File Not Trusted - Unknown Pickle File কখনো Load করা উচিত নয়। কারণ এতে Malicious Code থাকতে পারে।
"""

# ============================================================
# 09_Exercises
# ============================================================
"""
Exercise 1: একটি file তৈরি করো। message.txt তাতে Hello AI লিখো।
------------------------------------------------------------
Exercise 2: নিজের Name, Age, Country - JSON File-এ Save করো।
------------------------------------------------------------
Exercise 3: একটি CSV File তৈরি করো। Name,Marks ৩ জন Student যোগ করো।
------------------------------------------------------------
Exercise 4: Pathlib ব্যবহার করে Logs - Folder তৈরি করো।
------------------------------------------------------------
Exercise 5: একটি List Pickle File-এ Save করে, পুনরায় Load করো।
------------------------------------------------------------
Exercise 6: YAML Configuration তৈরি করো। host, port, database, debug
"""

# ============================================================
# 10_UseCase in AI Development
# ============================================================

"""
AI Engineer হিসেবে File Handling প্রতিদিন ব্যবহার করতে হবে।
------------------------------------------------------------
১. Dataset Load: CSV - JSON - TXT - Images
------------------------------------------------------------
২. Model Save: pickle - .joblib, .pt, .pth, .keras, .onnx
------------------------------------------------------------
৩. Configuration: config.yaml, settings.json
------------------------------------------------------------
৪. Prompt Store: prompt.txt, system_prompt.md
------------------------------------------------------------
৫. Chat History: conversation.json
------------------------------------------------------------
৬. Logs: training.log, error.log, prediction.log
------------------------------------------------------------
৭. Vector Database Export: json, pickle
------------------------------------------------------------
৮. AI Dataset Cleaning: Raw CSV -> Python -> Clean CSV -> Train Model
------------------------------------------------------------
৯. RAG (Retrieval-Augmented Generation): Documents -> TXT -> PDF -> Markdown -> Embedding -> Vector Database
------------------------------------------------------------
১০. Computer Vision: Images -> Read Binary -> NumPy Array -> PyTorch / TensorFlow
------------------------------------------------------------
AI Project Example:
datasets/
    train.csv
    test.csv
    config.yaml
models/
    model.pkl
logs/
    train.log
prompts/
    system_prompt.txt
outputs/
    prediction.json
------------------------------------------------------------
সংক্ষেপে, File Handling হলো AI Engineer-এর অন্যতম মৌলিক দক্ষতা। Dataset লোড করা থেকে শুরু করে Model সংরক্ষণ, Configuration ম্যানেজমেন্ট, Logging, Prompt Engineering এবং RAG—সব ক্ষেত্রেই File Handling অপরিহার্য।
"""