# Exercise 1: একটি async Function লিখো। যা Hello Print করবে।
import asyncio

# async def sayHello():
#     print("Hello")

# asyncio.run(sayHello())
# --------------------------------------------------
# Exercise 2: ২টি Coroutine একসাথে Run করো।
# async def task1():
#     print("Task 1 Started")
#     await asyncio.sleep(2)
#     print("Task 1 Finished")

# async def task2():
#     print("Task 2 Started")
#     await asyncio.sleep(2)
#     print("Task 2 Finished")


# async def main():
#     await asyncio.gather(
#         task1(),
#         task2()
#     )
    
# asyncio.run(main())
# --------------------------------------------------
# Exercise 3: ৫টি File Download Simulate করো।

# async def download(file: str):
#     print(f"Downloading {file}")
#     await asyncio.sleep(3)
#     print(f"Download Completed: {file}")
    
# async def main():
#     await asyncio.gather(
#         download("a.pdf"),
#         download("b.pdf"),
#         download("c.pdf"),
#         download("d.pdf"),
#         download("e.pdf"),
#     )

# asyncio.run(main())

# --------------------------------------------------
# Exercise 4: ৩টি API Call asyncio.gather() দিয়ে Run করো।
# async def callAPI(url: str):
#     print(f"Calling: {url}")
#     await asyncio.sleep(2)
#     print(f"Response for URL: {url}")
    
# async def main():
#     await asyncio.gather(
#         callAPI("www.file.com/get/users"),
#         callAPI("www.file.com/get/list"),
#         callAPI("www.file.com/get/url"),
#     )

# asyncio.run(main())
# --------------------------------------------------
# Exercise 5: একটি ChatGPT API Simulation তৈরি করো। Prompt পাঠাবে Response Return করবে।

async def ChatGPT(prompt: str):
    print(f"Reciveing Prompt: {prompt}")
    await asyncio.sleep(1)
    print(f"ChatGPT response for: {prompt}")
    
asyncio.run(ChatGPT("Hi"))