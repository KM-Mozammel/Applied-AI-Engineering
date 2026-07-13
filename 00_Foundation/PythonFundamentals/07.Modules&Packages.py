"""
============================================================
# 01_Introduction (Module & Package কী?)
============================================================
Python-এর সবচেয়ে শক্তিশালী বৈশিষ্ট্যগুলোর একটি হলো Code Reusability। একবার কোনো Code লিখে সেটিকে বারবার ব্যবহার করা যায়। এই কাজটি করা হয়: ✅ Module, ✅ Package ব্যবহার করে।
------------------------------------------------------------
Module কী? একটি Python (.py) File-ই হলো একটি Module। Example - math.py, student.py, calculator.py, ai.py এগুলো প্রত্যেকটিই একটি Module।
------------------------------------------------------------
Package কী? অনেকগুলো Related Module-কে একটি Folder-এর মধ্যে সংগঠিত করলে তাকে Package বলে।
Example: 
project/
    app/
        __init__.py
        auth.py
        database.py
        utils.py
এখানে, app একটি Package।
------------------------------------------------------------
Python-এর হাজার হাজার Built-in এবং Third-party Module আছে। যেমন, math | random | os | sys | pathlib | json | csv | datetime | numpy | pandas | torch | tensorflow | requests | fastapi
------------------------------------------------------------
Module + Package শেখা মানে হলো নিজের Project-কে Professional ভাবে Organize করতে শেখা।
"""
# ============================================================
# 02_WhyModulesPackagesExist
# ============================================================
"""
ধরো তুমি ৫০০০ লাইনের একটি Program লিখেছো। সব Code যদি একটি File-এ থাকে main.py
তাহলে, ❌ Maintain করা কঠিন - ❌ Bug খুঁজে পাওয়া কঠিন - ❌ Reuse করা যায় না - ❌ Team Work কঠিন
------------------------------------------------------------
সমাধান, Project ভাগ করে ফেলো।
project/
    auth.py
    database.py
    api.py
    models.py
    utils.py
------------------------------------------------------------
এখন, Authentication -> auth.py | Database -> database.py | Helper Function -> utils.py
------------------------------------------------------------
AI Project: 
dataset.py -> Dataset Load
model.py   -> Neural Network
train.py   -> Training
predict.py -> Inference
config.py  -> Configuration
এভাবে Project অনেক সুন্দরভাবে ভাগ করা যায়।
"""
# ============================================================
# 03_Syntax
# ============================================================
"""
=============================
import : import module_name
Example: import math
=============================
from : from module import function
Example: from math import sqrt
=============================
Alias: import numpy as np
import pandas as pd
=============================
Multiple Import: import os
import sys
=============================
__name__ : if __name__ == "__main__":
    print("Run Directly")
=============================
pip: pip install numpy
=============================
venv : python -m venv venv
=============================
requirements.txt
=============================
pip freeze > requirements.txt
pip install -r requirements.txt
=============================
__init__.py
=============================
Package-কে Initialize করে।

Modern Python-এ এটি Optional, কিন্তু ব্যবহার করা Best Practice।
"""
# ============================================================
# 04_Methods / Concepts
# ============================================================
"""
import
from
as
dir()
help()
__name__
pip
venv
requirements.txt
__init__.py
"""

# ============================================================
# import
# ============================================================
print("===== import =====")
import math
print(math.sqrt(25))
print(math.pi)
# ============================================================
# from
# ============================================================
print("\n===== from =====")
from math import sqrt
print(sqrt(64))
# ============================================================
# alias
# ============================================================
print("\n===== alias =====")
import datetime as dt
print(dt.date.today())
# ============================================================
# dir()
# ============================================================
print("\n===== dir() =====")
print(dir(math)[:10])
# ============================================================
# help()
# ============================================================
"""
help(math)
help(str)
help(list)
Interactive Documentation দেখায়।
"""
# ============================================================
# __name__
# ============================================================
print("\n===== __name__ =====")
print(__name__)
if __name__ == "__main__":
    print("এই File টি সরাসরি Run হয়েছে।")
else:
    print("অন্য Module থেকে Import হয়েছে।")
# ============================================================
# pip
# ============================================================
"""
Package Install
pip install numpy
Package Upgrade
pip install --upgrade numpy
Package Remove
pip uninstall numpy
Installed Packages
pip list
Package Information
pip show numpy
"""
# ============================================================
# venv
# ============================================================
"""
Virtual Environment তৈরি
Windows
python -m venv venv
Activate
venv\\Scripts\\activate
Deactivate
deactivate
Linux / macOS
python3 -m venv venv
source venv/bin/activate
"""
# ============================================================
# requirements.txt
# ============================================================
"""
Current Environment-এর Package Save
pip freeze > requirements.txt
অন্য Computer-এ Install
pip install -r requirements.txt
Example requirements.txt
numpy==2.2.1
pandas==2.3.0
torch==2.8.0
fastapi==0.120.0
"""
# ============================================================
# __init__.py
# ============================================================
"""
Project Structure
myproject/
    app/
        __init__.py
        auth.py
        api.py
        database.py
__init__.py থাকলে Folder-টিকে Package হিসেবে Organize করা সহজ হয়। এখানে Common Import-ও করা যায়।
Example: 
from .auth import login
from .database import connect
"""
# ============================================================
# 05_TimeComplexity
# ============================================================

"""
Operation                    Complexity
----------------------------------------
import small module          O(1)
Large module import          O(n)
Function Call                O(1)
Package Lookup               O(1)
dir(module)                  O(n)
help(module)                 O(n)
pip install                  Network + Disk নির্ভর
venv create                  O(n)
requirements install         Package সংখ্যার উপর নির্ভর
------------------------------------------------------------
n = Module-এর Size অথবা
Number of Objects
"""
# ============================================================
# 06_InternalWorking
# ============================================================

"""
ধরো তুমি লিখলে, import math Python কী করে?
Program
↓
import math
↓
sys.modules-এ Check করে
↓
আগে Import হয়েছে?
↓ 
হ্যাঁ
↓
আগের Module ব্যবহার করবে
↓
না
↓
math.py / Compiled Extension খুঁজবে
↓
Load করবে
↓
Execute করবে
↓
Memory-তে রাখবে
↓
sys.modules-এ Cache করবে
------------------------------------------------------------
পরবর্তী Import -> Memory থেকেই ব্যবহার করবে। তাই একই Module বারবার Import করলে
প্রতিবার নতুন করে Load হয় না।
------------------------------------------------------------
__name__ কী? যদি File সরাসরি Run হয় __name__ == "__main__" যদি অন্য File Import করে __name__ = Module-এর নাম
------------------------------------------------------------
venv কী করে? System Python থেকে আলাদা নিজস্ব Python, Interpreter, Package, Scripts, Library তৈরি করে। এতে Project-এর Dependency এক Project থেকে অন্য Project-এ Conflict করে না।
"""

# ============================================================
# 07_Examples
# ============================================================

print("\n===== Example 1 =====")
import random
print(random.randint(1, 10))

print("\n===== Example 2 =====")
from pathlib import Path
path = Path("example.txt")
print(path.name)

print("\n===== Example 3 =====")
import json
person = {
    "name": "Mozammel",
    "age": 27
}
print(json.dumps(person, indent=4))

print("\n===== Example 4 =====")
import statistics
numbers = [10, 20, 30, 40]
print(statistics.mean(numbers))

# ============================================================
# 08_CommonMistakes
# ============================================================

"""
১. import * from math import * এটি Avoid করা উচিত। কারণ Namespace নষ্ট হয়।
------------------------------------------------------------
২. নিজের File-এর নাম math.py, json.py, random.py রাখা। এতে Built-in Module Shadow হয়ে যায়।
------------------------------------------------------------
৩. Virtual Environment ব্যবহার না করা। Project Dependency Conflict হতে পারে।
------------------------------------------------------------
৪. requirements.txt Update না করা। Team-এর অন্য Member Project Run করতে পারবে না।
------------------------------------------------------------
৫. Import-এর Circular Dependency তৈরি করা। A Import করছে B - B আবার Import করছে A - Error হতে পারে।
------------------------------------------------------------
৬. if __name__ == "__main__" ব্যবহার না করা। তাহলে Import করার সময়ও Test Code Execute হবে।
"""

# ============================================================
# 09_Exercises
# ============================================================

"""
Exercise 1: math Module Import করে sqrt(), pi ব্যবহার করো।
------------------------------------------------------------
Exercise 2: নিজের calculator.py Module তৈরি করো। এর ভিতরে add(), subtract(), multiply() লিখে অন্য File থেকে Import করো।
------------------------------------------------------------
Exercise 3: একটি Package তৈরি করো। 
app/
    __init__.py
    auth.py
    database.py
------------------------------------------------------------
Exercise 4: Virtual Environment তৈরি করো।
------------------------------------------------------------
Exercise 5: numpy Install করো। requirements.txt তৈরি করো।
------------------------------------------------------------
Exercise 6: একটি File-এ __name__ Print করে দেখো। Run করলে এবং Import করলে কি পরিবর্তন হয়?
"""
# ============================================================
# 10_UseCase in AI Development
# ============================================================
"""
AI Engineer হিসেবে Module ও Package প্রতিদিন ব্যবহার করতে হবে।
------------------------------------------------------------
১. AI Library Import: 
import torch
import tensorflow
import transformers
import numpy as np
import pandas as pd
------------------------------------------------------------
২. Dataset Module: dataset.py -> Dataset Load
------------------------------------------------------------
৩. Model Module: model.py -> Neural Network
------------------------------------------------------------
৪. Training Module: train.py -> Training Logic
------------------------------------------------------------
৫. Prediction Module: predict.py -> Inference
------------------------------------------------------------
৬. Utility Module: utils.py -> Helper Function - Logging - Metrics
------------------------------------------------------------
৭. Configuration: config.py -> Environment Variable, PI Key, Hyperparameter
------------------------------------------------------------
৮. Virtual Environment: প্রতিটি AI Project-এর জন্য আলাদা venv ব্যবহার করা উচিত।
------------------------------------------------------------
৯. requirements.txt: Team Member অথবা Server-এ - এক Command-এ সব Package Install করা যায়। pip install -r requirements.txt
------------------------------------------------------------
১০. Large AI Project Structure:
ai_project/
    app/
        __init__.py
        dataset.py
        model.py
        train.py
        predict.py
        utils.py
    data/
    models/
    notebooks/
    requirements.txt
    main.py
------------------------------------------------------------
সংক্ষেপে, Module শেখায় Code Reuse করতে। Package শেখায় Project Organize করতে। pip শেখায় Library Install করতে। venv শেখায় Dependency আলাদা রাখতে। requirements.txt শেখায় Project Share করতে। এগুলো ছাড়া Professional Python বা AI Development প্রায় অসম্ভব।
"""