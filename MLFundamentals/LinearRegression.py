# Used when output is a number.
# Examle = Hours Studied -> Exam Score

# | Hours | Score |
# | ----- | ----- |
# | 1     | 40    |
# | 2     | 50    |
# | 3     | 60    |
# | 4     | 70    |

# So the hidden rule is: Every +1 in X increases y by +10
# So the real function is: y=10x+30

# Normal Equation -> w=(X^T*X)−1X^T*sy

from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1],[2],[3],[4]])
y = np.array([40,50,60,70])

model = LinearRegression()

model.fit(X,y)

print(model.predict([[5]])) # becomes: y=10(5)+30=80


# “Given past examples, 
# find the best straight line that explains the relationship between input and output, 
# then use it to predict future values.”

# UseCase *********XXXX*************
# Salary prediction: Experience → Salary
# Example:
# 1 year → 30k
# 2 years → 40k
# Predict: “What is salary for 5 years?”

# House price prediction: Size → Price
# Example:
# 1000 sqft → $50k
# 2000 sqft → $100k

# Sales forecasting
# Advertising → Sales
# Example: More ads → more sales

# Weather prediction Temperature history → future temperature

# Business analytics

# demand prediction
# revenue prediction
# cost estimation