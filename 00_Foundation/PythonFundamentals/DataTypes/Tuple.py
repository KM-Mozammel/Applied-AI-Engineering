print("\n========== TUPLE ==========")

point = (10, 20, 30)

print("Tuple:", point)
print("Type:", type(point))

# Access
print("First Item:", point[0])

# Length
print("Length:", len(point))

# Count
print("Count of 20:", point.count(20))

# Index
print("Index of 30:", point.index(30))

# Slicing
print("Slice:", point[0:2])

# Packing
person = ("Mozammel", 28, "Dhaka")

# Unpacking
name, age, city = person

print("Name:", name)
print("Age:", age)
print("City:", city)

# ML Example
image_size = (224, 224)
print("Image Size:", image_size)
