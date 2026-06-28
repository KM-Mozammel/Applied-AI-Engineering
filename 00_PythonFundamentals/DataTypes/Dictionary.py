print("\n========== DICTIONARY ==========")

student = {
    "name": "Mozammel",
    "age": 28,
    "city": "Dhaka"
}

print("Student:", student)
print("Type:", type(student))

# Access
print("Name:", student["name"])
print("Age:", student.get("age"))

# Add New Key
student["cgpa"] = 3.80

# Update
student["city"] = "Tangail"

print("Updated Student:", student)

# Keys
print("Keys:", student.keys())

# Values
print("Values:", student.values())

# Items
print("Items:", student.items())

# Check Existence
print("Has Name?:", "name" in student)

# Loop
print("\nDictionary Loop:")

for key, value in student.items():
    print(key, "=>", value)

# Delete
del student["age"]

print("After Delete:", student)

# ML Example
model_config = {
    "learning_rate": 0.001,
    "epochs": 100,
    "batch_size": 32
}

print("Model Config:", model_config)