# Formula: S = n/2 × (first + last)

a = 2   # First term
d = 3   # Common difference
n = 10  # Number of terms

# Calculate the stop value for the range function
stop = a + (n * d)

# Generate the sequence
sequence = list(range(a, stop, d))

# Calculate the sum (the series)
series_sum = sum(sequence)

print(f"Sequence: {sequence}")
# Output: [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]

print(f"Sum of Series: {series_sum}")
# Output: 155
