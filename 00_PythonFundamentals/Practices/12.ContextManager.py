# Exercise 1: with open() ব্যবহার করে একটি File পড়ো।

# with open("data.txt", "r") as f:
#     data = f.read()
#     print(data)

# Exercise 2: নিজের Context Manager তৈরি করো।

# class MyContext:
#     def __enter__(self):
#         print("Resource Open")
#         return self
    
#     def __exit__(self, exc_type, exc, tb):
#         print("Resource Closed")
        
# with MyContext():
#     print(open("data.txt", "r").read())

# Exercise 3: __enter__() Call হলে "Connected" Print করো।
# class MyContext:
#     def __enter__(self):
#         print("Connected")
#         return self
    
#     def __exit__(self, exe_type, exc, tb):
#         pass    

# with MyContext():
#     pass

# Exercise 4: __exit__() Call হলে "Disconnected" Print করো।

# class MyContext:
#     def __enter__(self):
#         print("Connected")
#         return self
    
#     def __exit__(self, exe_type, exc, tb):
#         print("Disconnected")    

# with MyContext():
#     pass

# Exercise 5: contextlib.contextmanager ব্যবহার করে Context Manager বানাও।

# from contextlib import contextmanager

# @contextmanager
# def my_context():
#     print("Open")
#     yield
#     print("Close")
    
# with my_context():
#     print("Working")

# Exercise 6: Timer Context Manager তৈরি করো, যা Execution Time Measure করবে।
# import time
# from contextlib import contextmanager

# @contextmanager
# def timer():
#     start = time.perf_counter()
#     yield
#     end = time.perf_counter()
#     print(f"Execution Time: {end - start:.6f} seconds")

# with timer():
#     total = 0
#     for i in range(1_000_000):
#         total += 1
        
# print(total)

# Exercise 7: Database Connection Context Manager তৈরি করো।
import sqlite3

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
    
    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        print("Database Connected")
        return self.conn
    
    def __exit__(self, exc_type, exc, tb):
        self.conn.close()
        print("Database Closed")
        
with Database("students.db") as conn:
    cursor = conn.cursor()
    
    cursor.execute(""" 
                   CREATE TABLE IF NOT EXISTS students(
                       id INTEGER PRIMARY KEY,
                       name TEXT
                   )
                   """)
    cursor.execute("INSERT INTO students (name) VALUES (?)", ("Mozammel",))
    conn.commit()
    cursor.execute("SELECT * FROM students")
    
    for row in cursor.fetchall():
        print(row)

# Exercise 8: Thread Lock-এর জন্য with lock ব্যবহার করো।
import threading
import time

lock = threading.Lock()
counter = 0

def increment():
    global counter

    for _ in range(100000):
        with lock:
            counter += 1

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()

print("Counter =", counter)

# Exercise 9: একটি Temporary File Context Manager তৈরি করো।
import tempfile
import os

class TemporaryFile:
    def __enter__(self):
        self.file = tempfile.NamedTemporaryFile(mode = "w+", delete=False)
        print("Temporary File Created")
        return self.file
    
    def __exit__(self, exc_type, exc, tb):
        self.file.close()
        os.remove(self.file.name)
        print("Temporary File Deleted")

with TemporaryFile() as f:
    f.write("Hello Temporary File!")
    f.seek(0)
    print(f.read())


# Exercise 10: নিজের Logger Context Manager তৈরি করো যা Context Enter ও Exit হলে Log Print করবে।

class Logger:
    def __enter__(self):
        print("[LOG] Entering Context")
        return self
    
    def __exit__(self, exc_type, exc, tb):
        print("[LOG] Exiting Context")
        
with Logger():
    print("Doing some work..." )