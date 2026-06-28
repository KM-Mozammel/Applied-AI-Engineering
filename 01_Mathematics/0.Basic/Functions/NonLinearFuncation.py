from scipy.optimize import fsolve

# Define a function returning the equations set to 0
def equations(vars):
    x, y = vars
    eq1 = x**2 + y - 5
    eq2 = x - y - 1
    return [eq1, eq2]

# Initial guess for [x, y]
initial_guess = [1, 1]

# Find the root
solution = fsolve(equations, initial_guess)

print(f"x = {solution[0]}, y = {solution[1]}")
# Output: x = 2.0, y = 1.0 (finds the root closest to the guess)
