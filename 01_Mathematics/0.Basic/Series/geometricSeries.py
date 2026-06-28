# Formula: S = a(1-rⁿ)/(1-r)

def generate_geometric_series(a, r, n):
    """
    a: first term
    r: common ratio
    n: number of terms
    """
    return [a * (r ** i) for i in range(n)]

# Example: First 5 terms with a=2, r=3
print(generate_geometric_series(2, 3, 5))
# Output: [2, 6, 18, 54, 162]
