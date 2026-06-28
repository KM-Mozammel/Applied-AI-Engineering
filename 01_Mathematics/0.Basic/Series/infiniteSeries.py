# Convergent infinite series

import sympy as sp

# Define the variable/index
n = sp.Symbol('n', integer=True)

# Define an infinite series, for example: 1 / n^2 from n=1 to infinity
# (This is the famous Basel problem)
series = sp.Sum(1 / n**2, (n, 1, sp.oo))

print("Formula:")
sp.pprint(series)

print("\nExact Sum:")
print(series.doit())  # Computes the analytical value: pi^2 / 6
