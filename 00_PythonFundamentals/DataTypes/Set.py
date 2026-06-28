print("\n========== SET ==========")

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("A:", A)
print("B:", B)

# Add
A.add(10)

# Remove
A.remove(2)

# Discard
A.discard(100)

print("Updated A:", A)

# Union
print("Union:", A.union(B))

# Intersection
print("Intersection:", A.intersection(B))

# Difference
print("Difference:", A.difference(B))

# Symmetric Difference
print("Symmetric Difference:", A.symmetric_difference(B))

# Membership
print("3 in A?:", 3 in A)

# ML Example
animals = [
    "cat",
    "dog",
    "cat",
    "dog",
    "bird"
]

unique_animals = set(animals)

print("Original Labels:", animals)
print("Unique Labels:", unique_animals)
