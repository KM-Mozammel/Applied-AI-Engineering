print("\n========== LIST ==========")

numbers = [10, 20, 30, 40]

print("Original:", numbers)

# Access
print("First Item:", numbers[0])
print("Last Item:", numbers[-1])

# Update
numbers[0] = 100

# Add
numbers.append(50)

# Insert
numbers.insert(1, 15)

# Extend
numbers.extend([60, 70])

print("After Additions:", numbers)

# Remove
numbers.remove(30)

# Pop
removed_item = numbers.pop()

print("Popped Item:", removed_item)

# Length
print("Length:", len(numbers))

# Sort
numbers.sort()
print("Sorted:", numbers)

# Reverse
numbers.reverse()
print("Reversed:", numbers)

# Count
print("Count of 20:", numbers.count(20))

# Index
print("Index of 40:", numbers.index(40))

# Loop
print("\nLooping Through List:")
for item in numbers:
    print(item)

# List Comprehension
squares = [x * x for x in range(6)]

print("Squares:", squares)

# ML Example Dataset
ages = [18, 22, 25, 30, 35]
print("Dataset:", ages)