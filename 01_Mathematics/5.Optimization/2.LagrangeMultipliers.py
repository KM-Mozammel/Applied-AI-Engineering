# Lagrange Multipliers: Optimization করার সময় নতুন সমস্যা দেখা দিল। "সবচেয়ে ভালো সমাধান চাই, কিন্তু কিছু শর্ত (Constraint) মানতে হবে।"

# উদাহরণ, ধরো তোমার কাছে ১০০০ টাকা আছে। তুমি Laptop কিনবে। কিন্তু Budget ≤ 1000 এই শর্ত মানতেই হবে।

# আরেকটি উদাহরণ, Maximum Profit -> Subject To Investment ≤ 1 Million. এখান থেকেই জন্ম Lagrange Multipliers

# ধারণা: Constraint সহ Optimization করার গণিত।
# Formula: L(x,λ)=f(x)+λ(g(x)−c)
# যেখানে, f(x)-> যেটা Optimize করতে চাই g(x) -> Constraint

import numpy as np

x = 2
objective = x**2
constraint = x - 2
lagrange = objective + 5*constraint
print(lagrange)

# ML Relation: Lagrange Multipliers ব্যবহার হয়, Support Vector Machine (SVM), Dual Optimization, Resource Allocation, Operations Research