# Exercise 1: ১ থেকে ১০ পর্যন্ত সংখ্যা Return করে এমন Iterator তৈরি করো।

# class Numbers:
#     def __init__(self):
#         self.current = 1
        
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.current > 10:
#             raise StopIteration
#         number = self.current
#         self.current += 1
#         return number

# numbers = Numbers()

# for value in numbers:
#     print(value)
# --------------------------------------------------
# Exercise 2: Reverse Iterator তৈরি করো। Input: [1,2,3,4] Output: 4 3 2 1
# class ReverseIterator:
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data) - 1
        
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.index < 0:
#             raise StopIteration
#         value = self.data[self.index]
#         self.index -= 1
#         return value
    
# reverseNum = ReverseIterator([1, 2, 3, 4, 6, 10, 56, 2])

# for num in reverseNum:
#     print(num)

# --------------------------------------------------
# Exercise 3: String Iterator- HELLO - Output: H E L L O

# class stringIterator:
#     def __init__(self, string: str):
#         self.string = string
#         self.strLength = len(string)
#         self.index = 0
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.index >= self.strLength:
#             raise StopIteration
        
#         char = self.string[self.index]
#         self.index += 1
#         return char
    
# string_iter = stringIterator("HELLO")

# for letter in string_iter:
#     print(letter)


# --------------------------------------------------
# Exercise 4: BatchLoader Modify করো। যাতে Drop Last Batch Option থাকে। Example: Batch Size = 4 - Dataset: 10 Elements

# class BatchLoader:
#     def __init__(self, dataset, batch_size, drop_last = False):
#         self.dataset = dataset
#         self.batch_size = batch_size
#         self.drop_last = drop_last
#         self.index = 0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index >= len(self.dataset):
#             raise StopIteration

#         batch = self.dataset[self.index:self.index+self.batch_size]
        
#         if self.drop_last and len(batch) < self.batch_size:
#             raise StopIteration
        
#         self.index += self.batch_size
        
#         return batch
        

# batchLoader = BatchLoader([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], batch_size=4, drop_last=True)

# for item in batchLoader:
#     print(item)

# Output: 4 4 2 যদি drop_last=True হয় Output 4 4 শেষের 2 Elements Skip হবে।
# --------------------------------------------------
# Exercise 5: CSV File Iterator তৈরি করো। যাতে একবারে একটি Row Return করে।
# import csv

# class SCVIterator:
#     def __init__(self, filename: str):
#         self.file = open(filename, "r")
#         self.reader = csv.reader(self.file)
#         next(self.reader)
    
#     def __iter__(self):
#         return self    
    
#     def __next__(self):
#         return next(self.reader)
    
#     def close(self):
#         self.file.close()
        
# csv_iterator = SCVIterator("./practices/sample_dataset.csv")

# for row in csv_iterator:
#     print(row)
    
# csv_iterator.close()


arr = [1, 2, 3, 65, 5, 6, 7, 8]

print(arr[1:4])