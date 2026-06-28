print("\n========== INTEGER ==========")

age = 26
epochs = 100

print("Age:", age)
print("Type:", type(age))

# Arithmetic
print("Addition:", age + 10)
print("Subtraction:", age - 5)
print("Multiplication:", age * 2)
print("Division:", age / 2)
print("Power:", age ** 2)
print("Modulus:", age % 5)

# Binary / Octal / Hex
print("Binary:", bin(epochs))
print("Octal:", oct(epochs))
print("Hex:", hex(epochs))

# Bit Length
print("Bit Length:", epochs.bit_length())

# Comparison
print("Age > 20:", age > 20)
print("Age == 26:", age == 26)

# ML Example
epochs = 100
batch_size = 32

print("Epochs:", epochs)
print("Batch Size:", batch_size)