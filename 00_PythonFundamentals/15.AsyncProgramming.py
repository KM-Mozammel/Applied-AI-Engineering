"""
==================================================
01_Introduction
================================================== 
Asynchronous Programming (Async Programming) হলো এমন একটি Programming Technique যেখানে একটি Task অপেক্ষা (Waiting) করার সময় CPU অন্য কাজ করতে পারে। Python-এ Async Programming-এর মূল Keyword তিনটি- ✔ async, ✔ await, ✔ asyncio
--------------------------------------------------
Real Life Example: ধরো, তুমি Restaurant-এ Order করলে। 
Synchronous: Order দিলে -> Chef রান্না শেষ না করা পর্যন্ত তুমি দাঁড়িয়ে থাকলে।
--------------------------------------------------
Asynchronous: Order দিলে -> Chef রান্না করছে -> এদিকে তুমি Phone দেখছো, বন্ধুর সাথে কথা বলছো, Email Reply দিচ্ছো -> খাবার Ready হলে তুমি নিয়ে নিলে।
--------------------------------------------------
Programming-এও একই ঘটনা ঘটে। যদি Network Request করতে ২ সেকেন্ড লাগে CPU বসে থাকবে কেন? ততক্ষণে অন্য কাজ করতে পারে।
==================================================
02_WhyAsyncProgrammingExists
==================================================
ধরো, তোমার Program ৩টি API Call করবে। প্রতিটি API Response Time 2 Seconds
--------------------------------------------------
Synchronous: API 1 -> 2 sec | API 2 -> 2 sec | API 3 -> 2 sec. Total: 6 Seconds
--------------------------------------------------
Asynchronous: API 1 + API 2 + API 3 একসাথে Start -> সব Complete -> প্রায় 2 Seconds
--------------------------------------------------
Async Programming মূলত, I/O Bound কাজের জন্য। যেমন, ✔ API Call, ✔ Database Query, ✔ File Download, ✔ Upload, ✔ WebSocket, ✔ LLM API

==================================================
03_Syntax
==================================================
Simple Async Function:

import asyncio

async def hello():
    print("Hello")
asyncio.run(hello())

--------------------------------------------------
Using await:
import asyncio

async def hello():
    await asyncio.sleep(2)
    print("Done")
asyncio.run(hello())
--------------------------------------------------
Output: (2 Seconds Wait) -> Done

==================================================
04_Methods
==================================================
async: একটি Coroutine Define করে।
async def fetch():
    ...
--------------------------------------------------
await: Coroutine Complete হওয়া পর্যন্ত বর্তমান Coroutine Pause করে।
await fetch()
--------------------------------------------------
asyncio.run(): Event Loop Start করে। asyncio.run(main())
--------------------------------------------------
asyncio.sleep(): Non-blocking Sleep; await asyncio.sleep(1)
--------------------------------------------------
asyncio.gather(): একাধিক Coroutine একসাথে Run করে।
await asyncio.gather(task1(), task2(), task3())

==================================================
05_TimeComplexity
==================================================
Async Programming, Algorithm-এর Complexity পরিবর্তন করে না।
Example: API Call - O(n) ই থাকবে।
--------------------------------------------------
কিন্তু, Waiting Time অনেক কমিয়ে দেয়। CPU Utilization Improve করে।

==================================================
06_InternalWorking
==================================================
Example:

async def work():
    await asyncio.sleep(2)
--------------------------------------------------
Step 1: async Function Call করলে, Function Execute হয় না। Coroutine Object তৈরি হয়। work() -> Coroutine Object
--------------------------------------------------
Step 2: asyncio.run(): Event Loop তৈরি করে।
--------------------------------------------------
Step 3: Event Loop - Coroutine চালায়।
--------------------------------------------------
Step 4: await asyncio.sleep() দেখলে Coroutine Pause হয়। CPU অন্য Coroutine Execute করে।
--------------------------------------------------
Step 5: ২ সেকেন্ড পরে Coroutine Resume হয়।
--------------------------------------------------
Flow: Coroutine -> Event Loop -> await -> Pause -> Run Other Task -> Resume -> Finish

==================================================
07_Examples
==================================================
Example 1: Simple Async

import asyncio

async def hello():
    print("Hello")
asyncio.run(hello())
--------------------------------------------------
Example 2: Async Sleep

import asyncio

async def task():
    print("Start")
    await asyncio.sleep(2)
    print("End")
asyncio.run(task())
--------------------------------------------------
Example 3:  Multiple Tasks

import asyncio

async def worker(name):
    print(f"{name} Started")
    await asyncio.sleep(2)
    print(f"{name} Finished")

async def main():
    await asyncio.gather(
        worker("A"),
        worker("B"),
        worker("C")
    )

asyncio.run(main())
--------------------------------------------------
Example 4: Simulating LLM API Calls

import asyncio

async def call_llm(prompt):
    print(f"Sending: {prompt}")
    await asyncio.sleep(2)
    return f"Response for {prompt}"

async def main():
    responses = await asyncio.gather(
        call_llm("Explain AI"),
        call_llm("Write Python"),
        call_llm("Summarize PDF")
    )
    print(responses)
asyncio.run(main())

--------------------------------------------------
Example 5: Download Multiple Files

import asyncio

async def download(file):
    print(f"Downloading {file}")
    await asyncio.sleep(1)
    print(f"{file} Done")

async def main():
    await asyncio.gather(
        download("a.pdf"),
        download("b.pdf"),
        download("c.pdf")
    )

asyncio.run(main())

==================================================
08_CommonMistakes
==================================================
❌ Mistake 1: await ছাড়া Coroutine Call করা। fetch() - ভুল। ✔ await fetch()
--------------------------------------------------
❌ Mistake 2: async Function: Normal Function-এর মতো Call করা। main() ভুল। ✔ asyncio.run(main())
--------------------------------------------------
❌ Mistake 3:  CPU Bound কাজে Async ব্যবহার করা। Large Matrix Multiplication, Image Training, Deep Learning এগুলো Async-এর জন্য নয়। Threading, Multiprocessing, GPU ব্যবহার করা উচিত।
--------------------------------------------------
❌ Mistake 4: time.sleep() ব্যবহার করা। ভুল time.sleep(2) Event Loop Block করে। ঠিক: await asyncio.sleep(2)

==================================================
09_Exercises
==================================================
Exercise 1: একটি async Function লিখো। যা Hello Print করবে।
--------------------------------------------------
Exercise 2: ২টি Coroutine একসাথে Run করো।
--------------------------------------------------
Exercise 3: ৫টি File Download Simulate করো।
--------------------------------------------------
Exercise 4: ৩টি API Call asyncio.gather() দিয়ে Run করো।
--------------------------------------------------
Exercise 5: একটি ChatGPT API Simulation তৈরি করো। Prompt পাঠাবে Response Return করবে।

==================================================
10_AIUsage (Use Case in AI Development)
==================================================
Machine Learning Training-এর জন্য Async খুব বেশি প্রয়োজন হয় না। কারণ Training মূলত CPU Bound / GPU Bound।
--------------------------------------------------
কিন্তু, LLM Application Development-এ Async অত্যন্ত গুরুত্বপূর্ণ।
--------------------------------------------------
১। Multiple LLM API Calls: একসাথে OpenAI, Gemini, Claude Call করা যায়।
--------------------------------------------------
২। RAG Pipeline: Vector Search -> LLM Call -> Database Query সব Async হতে পারে।
--------------------------------------------------
৩। FastAPI: FastAPI-এর অধিকাংশ Endpoint async হিসেবে লেখা হয়। Example: 
async def predict():
    ...
--------------------------------------------------
৪। WebSocket Chat: Streaming Response, Token by Token Send করতে Async ব্যবহার হয়।
--------------------------------------------------
৫। AI Agent: একটি Agent: Google Search, Database, LLM, Weather API সব একসাথে Call করতে পারে।
--------------------------------------------------
৬। Batch API Processing: 100টি Prompt: Sequential -> Slow | Async -> Much Faster
--------------------------------------------------
৭। Document Processing: একসাথে PDF, Image, OCR, LLM সব Pipeline Parallel I/O-তে চালানো যায়।
--------------------------------------------------
Summary: async -> Coroutine তৈরি করে। await -> বর্তমান Coroutine Pause করে। asyncio -> Event Loop পরিচালনা করে। Async Programming মূলত I/O Bound কাজের জন্য। Deep Learning Training-এ কম ব্যবহৃত হলেও LLM, FastAPI, RAG, AI Agent, Streaming, API Integration, MLOps এসব ক্ষেত্রে Async Programming অত্যন্ত গুরুত্বপূর্ণ।
"""