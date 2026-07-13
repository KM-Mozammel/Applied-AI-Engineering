"""
==================================================
01_Introduction
==================================================
Iterator হলো Python-এর এমন একটি Object যেটি একবারে একটি করে Data Return করে।

Iterator-এর মূল উদ্দেশ্য হলো:
✔ Memory Efficient হওয়া
✔ Large Dataset নিয়ে কাজ করা
✔ Data Stream করা
✔ Lazy Evaluation করা

Iterator একসাথে সব Data Memory-তে Load করে না। উদাহরণ,

numbers = [10,20,30]
for num in numbers:
    print(num)

এখানে for loop আসলে Iterator ব্যবহার করছে।
--------------------------------------------------
Iterator Protocol: যে Object-এর মধ্যে, __iter__(), __next__() থাকে, সেটিই Iterator।

==================================================
02_WhyIteratorsExists
==================================================
ধরো তোমার কাছে, 10 কোটি Row-এর Database আছে। যদি সব Row একসাথে Memory-তে Load করো RAM শেষ হয়ে যাবে। 
তাই Python Iterator তৈরি করেছে যাতে, একটি Row তারপর আরেকটি Row তারপর আরেকটি Row এভাবে প্রয়োজন অনুযায়ী Data পাওয়া যায়।
এটাকে বলে, Lazy Loading।

Without Iterator: Database │ Load Everything │ Huge RAM Usage
With Iterator: Database │ Next() │ One Row │ Next() │ One Row │ Next() │ One Row
Memory Efficient।

==================================================
03_Syntax
==================================================
Iterator তৈরি করতে, ১। __iter__() ২। __next__() implement করতে হয়।
Example, 

class Counter:
    def __init__(self):
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == 5:
            raise StopIteration
        self.i += 1
        return self.i

counter = Counter()

for value in counter:
    print(value)

Output: 1 - 2 - 3 - 4 - 5
==================================================
04_Methods: Iterator Protocol-এ মূলত দুটি Method থাকে।
==================================================
--------------------------------------------------
__iter__() - Iterator Return করে।

def __iter__(self):
    return self

--------------------------------------------------
__next__(): পরবর্তী Value Return করে।

def __next__(self):
    if finished:
        raise StopIteration
    return value

--------------------------------------------------
next(): Built-in Function

it = iter([1,2,3])
print(next(it))
print(next(it))
print(next(it))

Output: 1 2 3
==================================================
05_TimeComplexity
==================================================
next() Time Complexity - O(1) কারণ একবারে মাত্র একটি Element Return করে।
Memory Complexity - O(1) কারণ পুরো Collection Copy করে না।

==================================================
06_InternalWorking
==================================================

Example: 
numbers = [10,20,30]
it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))

----------------------------------------
Step 1 -> numbers তৈরি হয়।
Heap:
numbers
│
├──10
├──20
└──30

----------------------------------------
Step 2 -> iter(numbers) একটি Iterator Object তৈরি করে। Iterator index = 0
----------------------------------------
Step 3 -> next(it) - Iterator , index=0 Return 10 index = 1
----------------------------------------
Step 4 -> next(it) - Return 20, index = 2
----------------------------------------
Step 5 -> next(it) - Return 30, index = 3
----------------------------------------
Step 6 -> next(it) - index == len(), তাই StopIteration Raise হয়।
--------------------------------------------------
for Loop আসলে ভিতরে যা করে, it = iter(numbers)

while True:
    try:
        item = next(it)
        print(item)
    except StopIteration:
        break
অর্থাৎ, for Loop নিজেই Iterator ব্যবহার করে।

==================================================
07_Examples
==================================================

Example 1: Simple Iterator

class Counter:

    def __init__(self):
        self.i = 0
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= 3:
            raise StopIteration

        self.i += 1
        return self.i

for x in Counter():
    print(x)

--------------------------------------------------

Example 2: Batch Loader - Iterator-এর সবচেয়ে জনপ্রিয় Use Case। Iterators → finite dataset কে batch-wise consume করা যায়।

class BatchLoader:

    def __init__(self, data, batch_size):
        self.data = data
        self.batch_size = batch_size
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.index >= len(self.data):
            raise StopIteration

        batch = self.data[self.index:self.index+self.batch_size]
        self.index += self.batch_size
        return batch


dataset = list(range(1,21))
loader = BatchLoader(dataset,5)

for batch in loader:
    print(batch)

Output:  [1,2,3,4,5] [6,7,8,9,10] ...

--------------------------------------------------

Example 3: 
Manual next()

nums = iter([100,200,300])

print(next(nums))
print(next(nums))
print(next(nums))

==================================================
08_CommonMistakes
==================================================

❌ Mistake 1: __next__ এর বদলে next লিখে ফেলা

class Test:
    def next(self):
        pass

এটি Iterator হবে না। 
✔ def __next__(self):
     ...

--------------------------------------------------

❌ Mistake 2: StopIteration Raise না করা।

if end:
    return None

ভুল। ✔ raise StopIteration

--------------------------------------------------

❌ Mistake 3: __iter__ Return না করা।
✔
def __iter__(self):
    return self

--------------------------------------------------

❌ Mistake 4: Iterator Reuse করতে চাওয়া।

it = iter([1,2])

for i in it:
    print(i)

for i in it:
    print(i)

দ্বিতীয় Loop কিছুই Print করবে না। কারণ, Iterator Exhausted হয়ে গেছে। নতুন Iterator বানাতে হবে। it = iter([1,2])

==================================================
09_Exercises
==================================================

Exercise 1: ১ থেকে ১০ পর্যন্ত সংখ্যা Return করে এমন Iterator তৈরি করো।
--------------------------------------------------
Exercise 2: Reverse Iterator তৈরি করো। Input: [1,2,3,4] Output: 4 3 2 1
--------------------------------------------------
Exercise 3: String Iterator- HELLO - Output: H E L L O
--------------------------------------------------
Exercise 4: BatchLoader Modify করো। যাতে Drop Last Batch Option থাকে। Example: Batch Size = 4 - Dataset: 10 Elements
Output: 4 4 2 যদি drop_last=True হয় Output 4 4 শেষের 2 Elements Skip হবে।
--------------------------------------------------
Exercise 5: CSV File Iterator তৈরি করো। যাতে একবারে একটি Row Return করে।

==================================================
10_AIUsage (Use Case in AI Development)
==================================================

AI এবং Machine Learning-এ Iterator অত্যন্ত গুরুত্বপূর্ণ।

১। Mini Batch Training: একসাথে পুরো Dataset Memory-তে Load করা হয় না। বরং

Batch
↓
Forward Pass
↓
Backward Pass
↓
Next Batch

এভাবে Training চলে।

--------------------------------------------------

২। DataLoader: PyTorch-এর DataLoader Iterator-এর উপর ভিত্তি করে তৈরি।
for images, labels in train_loader:
    ...
train_loader-এর ভিতরে __iter__ এবং __next__ কাজ করে।
--------------------------------------------------
৩। Streaming Dataset: যেমন, YouTube Videos, Sensor Data, Live Camera Feed সব জায়গায় Iterator ব্যবহার করা হয়।
--------------------------------------------------
৪। NLP: বড় Text Corpus এক লাইন -> পরের লাইন -> পরের লাইন এভাবে পড়া হয়।
--------------------------------------------------
৫। ETL Pipeline: Database -> Iterator -> Transform -> Save একসাথে কোটি কোটি Row Load না করে একটি করে Process করা হয়।
--------------------------------------------------
৬। Distributed Training: একাধিক GPU-তে Batch ভাগ করে পাঠাতে Iterator ব্যবহৃত হয়। GPU-1 - Batch 1, GPU-2 - Batch 2, GPU-3 - Batch 3
--------------------------------------------------

সারসংক্ষেপ, Iterator মানে "একবারে একটি Data দাও" Generator হলো "প্রয়োজন হলে Data তৈরি করো" List হলো "সব Data একসাথে Memory-তে রাখো" AI, Deep Learning, Data Engineering, Web Streaming, Database Processing—প্রায় সব জায়গাতেই Iterator ব্যবহৃত হয়।
"""