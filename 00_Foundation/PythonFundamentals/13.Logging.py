"""
==================================================
01_Introduction
==================================================
Logging হলো Program চলাকালীন বিভিন্ন Event, Error, Warning এবং Information Record করার একটি Standard System। নতুন Programmer-রা সাধারণত print() ব্যবহার করে Debug করে। কিন্তু Professional Software Development-এ logging ব্যবহার করা হয়।
--------------------------------------------------
Instead of: print("User Logged In")
Use: 
import logging
logging.info("User Logged In")
--------------------------------------------------

Logging-এর উদ্দেশ্য

✔ Debug করা
✔ Error Track করা
✔ Production Monitoring
✔ Crash Investigation
✔ User Activity Record করা
✔ System Health Monitor করা

--------------------------------------------------
Python-এর Logging Module Python-এর Standard Library-এর অংশ। কোন Package Install করতে হয় না। import logging

==================================================
02_WhyLoggingExists
==================================================

ধরো একটি Web Application Server চলছে। একদিন User Report করলো "Login কাজ করছে না।" যদি শুধু print() ব্যবহার করো Server Restart হলে সব Message হারিয়ে যাবে। কিন্তু Logging করলে সব Message File-এ Save থাকবে।

Example

12:00 User Login
12:01 Database Connected
12:02 Invalid Password
12:03 Server Error

তখন সহজেই Problem বের করা যায়।
--------------------------------------------------
Without Logging: Program -> print() -> Console -> Lost
--------------------------------------------------
With Logging: Program -> Logger -> Console -> Log File -> Future Investigation
==================================================
03_Syntax
==================================================

Basic Example: 

import logging
logging.basicConfig(level=logging.INFO)
logging.info("Application Started")
--------------------------------------------------
Output: INFO:root:Application Started
--------------------------------------------------
Logging Levels: 
DEBUG
INFO
WARNING
ERROR
CRITICAL

==================================================
04_Methods
==================================================

logging.debug(): Developer Information
logging.debug("Variable x = 20")
--------------------------------------------------
logging.info(): General Information
logging.info("Application Started")
--------------------------------------------------
logging.warning(): Unexpected Situation
logging.warning("Disk Space Low")
--------------------------------------------------
logging.error(): Recoverable Error
logging.error("Database Connection Failed")
--------------------------------------------------
logging.critical(): Very Serious Error
logging.critical("Server Crashed")
--------------------------------------------------
logging.exception(): Exception-এর Stack Trace সহ Log করে।

try:
    10/0
except Exception:
    logging.exception("Division Error")
    
==================================================
05_TimeComplexity
==================================================
Logging Operation, Average Time Complexity - O(1) কারণ সাধারণ Message Append করা হয়।
--------------------------------------------------
Memory Complexity: O(1)
--------------------------------------------------
File Logging: Disk I/O থাকার কারণে কিছুটা Slow হতে পারে।

==================================================
06_InternalWorking
==================================================
Example: logging.info("Application Started")
--------------------------------------------------
Step 1: CPU -> logging.info() Function Call করে।
--------------------------------------------------
Step 2: Logger Object -> Level Check করে। INFO >= Current Level ? Yes হলে
--------------------------------------------------
Step 3: LogRecord তৈরি হয়। LogRecord, Message, Level, Time, File Name, Line Number, Thread
--------------------------------------------------
Step 4: Formatter - Message Format করে। Example, 2026-07-09 12:30 INFO Application Started
--------------------------------------------------
Step 5: Handler - Console/File-এ লিখে দেয়। Console or application.log
--------------------------------------------------
Flow: Application -> Logger -> LogRecord -> Formatter -> Handler -> Console / File

==================================================
07_Examples
==================================================
Example 1: Basic Logging

import logging
logging.basicConfig(level=logging.INFO)
logging.info("Application Started")
logging.warning("Low Memory")
logging.error("Database Failed")

--------------------------------------------------
Example 2: File Logging

import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)

logging.info("User Logged In")

--------------------------------------------------
Example 3: Custom Format

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"

)

logging.info("Application Started")
Output: 2026-07-09 10:30:20 | INFO | Application Started
--------------------------------------------------

Example 4: Logging Exception

import logging
logging.basicConfig(level=logging.INFO)

try:
    number = 10/0
except Exception:
    logging.exception("Calculation Failed")


==================================================
08_CommonMistakes
==================================================

❌ Mistake 1: সব জায়গায় print() ব্যবহার করা। print("Database Error") Professional নয়। logging.error("Database Error")
--------------------------------------------------
❌ Mistake 2: সব Message INFO রাখা। logging.info("Server Crashed") ভুল। ✔ logging.critical("Server Crashed")
--------------------------------------------------
❌ Mistake 3: Exception Ignore করা।

except:
    pass

ভুল।
✔
except Exception:
    logging.exception("Unexpected Error")

--------------------------------------------------
❌ Mistake 4: Sensitive Information Log করা। logging.info(password) ভুল। Password, Token, Secret Key, OTP, API Key, Log করা উচিত নয়।
==================================================
09_Exercises
==================================================
Exercise 1: INFO Level-এর একটি Logger তৈরি করো।
--------------------------------------------------
Exercise 2: সব ধরনের Logging Level ব্যবহার করো। DEBUG, INFO, WARNING, ERROR, CRITICAL
--------------------------------------------------
Exercise 3: Log File তৈরি করো। logs/app.log এ Log Save হবে।
--------------------------------------------------
Exercise 4: Exception Handle করে logging.exception() ব্যবহার করো।
--------------------------------------------------
Exercise 5: Timestamp, Level এবং Message সহ Custom Formatter তৈরি করো।

==================================================
10_AIUsage (Use Case in AI Development)
==================================================
AI Application-এ Logging অত্যন্ত গুরুত্বপূর্ণ।
--------------------------------------------------
১। Model Training: Epoch, Loss, Accuracy, Learning Rate সব Logging করা হয়।
Example:

Epoch 10
Loss = 0.031
Accuracy = 98.2%
--------------------------------------------------

২। Data Pipeline: 

Dataset Load
↓
Preprocessing
↓
Feature Engineering
↓
Training

প্রতিটি Step Log করা হয়।
--------------------------------------------------
৩। Model Serving: Prediction Request -> Inference Time -> Response -> Error সব Log করা হয়।
--------------------------------------------------
৪। GPU Monitoring: GPU Memory, CUDA Error, Batch Time সব Logging করা হয়।
--------------------------------------------------
৫। API Monitoring: FastAPI, Flask, Django সব API Request Log করে। Request -> Authentication -> Prediction -> Response
--------------------------------------------------
৬। Distributed AI Training: একাধিক Machine-এ Training চললে প্রতিটি Worker আলাদা Log তৈরি করে।
--------------------------------------------------
৭। MLOps: MLflow, Kubeflow, Weights & Biases, TensorBoard সব Logging Concept ব্যবহার করে।
--------------------------------------------------
Summary: print() -> Temporary || Development: logging -> Persistent -> Production Ready -> Debugging -> Monitoring -> AI Pipeline Professional Software Development-এ print() কেবল ছোট Debug-এর জন্য ব্যবহার করা হয়। Production, AI, Backend, DevOps এবং Enterprise Application-এ
সবসময় Logging ব্যবহার করা হয়।
"""