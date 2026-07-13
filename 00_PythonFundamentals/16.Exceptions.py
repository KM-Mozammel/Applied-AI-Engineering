"""
==================================================
01_Introduction
==================================================
Exception হলো Program চলাকালীন ঘটে যাওয়া এমন একটি Error, যা Program-এর Normal Flow বন্ধ করে দিতে পারে। 
Python-এ Exception Handle করার জন্য ব্যবহার করা হয়-
✔ try
✔ except
✔ else
✔ finally
✔ raise
--------------------------------------------------
Without Exception Handling: Program -> Error -> Program Crash
--------------------------------------------------
With Exception Handling: Program -> Error -> Handle Error -> Continue Execution
--------------------------------------------------
Real Life Example: ধরো, তুমি ATM থেকে টাকা তুলতে গেলে। Balance নেই। ATM বন্ধ হয়ে যায় না। বরং Message দেখায় "Insufficient Balance" এটাই Exception Handling।

==================================================
02_WhyExceptionsExist
==================================================
বাস্তব Program-এ সব Input সঠিক হবে না। যেমন,
✔ User ভুল Number দিবে
✔ File থাকবে না
✔ Database Down হতে পারে
✔ API কাজ নাও করতে পারে
✔ Internet Disconnect হতে পারে
যদি এগুলো Handle না করা হয় Program Crash করবে।
--------------------------------------------------
Without Exception Handling: API Call -> Network Error -> Program Crash
--------------------------------------------------
With Exception Handling: API Call -> Network Error -> Fallback -> Continue

==================================================
03_Syntax
==================================================
Basic Example:

try:
    number = 10/0
except ZeroDivisionError:
    print("Cannot Divide By Zero")

--------------------------------------------------
Multiple Exception:

try:
    ...
except ValueError:
    ...
except TypeError:
    ...
--------------------------------------------------
else:

try:
    print("Success")
except:
    print("Error")
else:
    print("No Exception")

--------------------------------------------------
finally:

try:
    ...
finally:
    print("Always Execute")

==================================================
04_Methods
==================================================
try: Risky Code এখানে লেখা হয়।
--------------------------------------------------
except: Exception Handle করে।
--------------------------------------------------
else:  Exception না হলে Execute হয়।
--------------------------------------------------
finally: Exception হোক বা না হোক সবসময় Execute হয়।
--------------------------------------------------
raise: নিজের Exception তৈরি করতে।
Example: 

age = -5
if age < 0:
    raise ValueError("Age Cannot Be Negative")

==================================================
05_TimeComplexity
==================================================
try - O(1)
--------------------------------------------------
except - O(1)
--------------------------------------------------
Exception Handling: Algorithm-এর Complexity পরিবর্তন করে না। শুধু Error Handle করে।

==================================================
06_InternalWorking
==================================================
Example:

try:
    10/0

except ZeroDivisionError:
    print("Error")

--------------------------------------------------
Step 1: Interpreter: try Block Execute করে।
Step 2: 10/0 Execute হয়।
Step 3: CPU Detect করে Division By Zero
Step 4: Python: ZeroDivisionError Object তৈরি করে।
Step 5: Matching except Block খুঁজে।
Step 6: except Execute হয়। Program Continue করে।
--------------------------------------------------
Flow: try ->  Exception ->  Exception Object ->  Matching except -> Handle -> Continue

==================================================
07_Examples
==================================================
Example 1: Division Safety

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Cannot Divide"
print(divide(10,0))
--------------------------------------------------
Example 2: Missing Values Handling

def normalize_data(data):
    try:
        return [x/max(data) for x in data]
    except ZeroDivisionError:
        print("Dataset contains only zeros")
        return data

    except Exception as e:
        print(e)
        return []
--------------------------------------------------
Example 3: API Call Fallback

import requests

def fetch_data(url):
    try:
        response=requests.get(url,timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("Timeout")
        return {"status":"backup"}
    except requests.exceptions.RequestException:
        return None
--------------------------------------------------

Example 4: Evaluation Metric Safety

def accuracy(y_true,y_pred):
    try:
        correct=sum(
            t==p
            for t,p in zip(y_true,y_pred)
        )
        return correct/len(y_true)
    except ZeroDivisionError:
        return 0.0

--------------------------------------------------

Example 5: Custom Exception

def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient Balance")
withdraw(100,500)

==================================================
08_CommonMistakes
==================================================
❌ Mistake 1: সব Exception ধরো
except:
    pass
ভুল। Error লুকিয়ে যায়।

✔
except Exception as e:

    print(e)

--------------------------------------------------
❌ Mistake 2: try Block-এর ভিতরে অনেক Code লেখা। শুধু Risky Code রাখো।
--------------------------------------------------
❌ Mistake 3: Specific Exception না ধরা। ভুল, except Exception ঠিক except ZeroDivisionError | except FileNotFoundError
--------------------------------------------------
❌ Mistake 4: finally ব্যবহার না করা। File, Database, Socket সব Close করার জন্য finally ব্যবহার করো।

==================================================
09_Exercises
==================================================
Exercise 1: Division Function তৈরি করো। ZeroDivision Handle করবে।
--------------------------------------------------
Exercise 2: File Open করো। File না থাকলে Message দেখাও।
--------------------------------------------------
Exercise 3: Negative Number দিলে raise ValueError করো।
--------------------------------------------------
Exercise 4: API Simulation Timeout Exception Handle করো।
--------------------------------------------------
Exercise 5: Custom Exception Class তৈরি করো।

==================================================
10_AIUsage (Use Case in AI Development)
==================================================
AI Engineering-এ Exception Handling অত্যন্ত গুরুত্বপূর্ণ।
--------------------------------------------------
১। Dataset Validation: Missing Value -> Handle
--------------------------------------------------
২। Model Loading: Model File না থাকলে Fallback Model Load করা।
--------------------------------------------------
৩। API Retry: OpenAI, Gemini, Claude Timeout হলে Retry অথবা Backup ব্যবহার করা।
--------------------------------------------------
৪। GPU Error: CUDA Out Of Memory ->  Catch Exception -> Reduce Batch Size -> Retry
--------------------------------------------------
৫। Data Pipeline: CSV -> Image -> PDF -> Corrupted File হলে Skip করে Next File Process করা।
--------------------------------------------------
৬। Model Evaluation: Empty Dataset -> Accuracy Division Error ->Return Safe Default
--------------------------------------------------
৭। Production AI System: Prediction Failure -> Log Exception -> Fallback Response -> System Running থাকে।
--------------------------------------------------
Summary: 
try -> Risky Code
except -> Handle Error
else -> No Error হলে Execute
finally -> Always Execute
raise -> নিজের Exception তৈরি

Professional Backend, AI Engineering, Machine Learning, Data Pipeline, LLM Application এবং Production System-এ Exception Handling অপরিহার্য।
"""