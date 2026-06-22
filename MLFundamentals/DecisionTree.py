from sklearn.tree import DecisionTreeClassifier
import numpy as np

X = np.array([
 [25,1],
 [35,1],
 [15,0],
 [16,0]
])

y = np.array([
 "Approve",
 "Approve",
 "Reject",
 "Reject"
])

model = DecisionTreeClassifier()

model.fit(X,y)

print(model.predict([[30,1]]))

# Manually Programming

# Age, HasJob

data = [
    [25, 1],
    [35, 1],
    [15, 0],
    [16, 0]
]

labels = [
    "Approve",
    "Approve",
    "Reject",
    "Reject"
]

# New person
age = 30
has_job = 1

# Decision Tree

if has_job == 1:
    prediction = "Approve"
else:
    prediction = "Reject"

print(prediction)