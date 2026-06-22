from sklearn.ensemble import RandomForestClassifier
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

model = RandomForestClassifier()

model.fit(X,y)

print(model.predict([[30,1]]))

# Random Forest Manually
import random

# -----------------------------
# Training Data
# -----------------------------
X = [
    [25, 1],
    [35, 1],
    [15, 0],
    [16, 0]
]

y = [
    "Approve",
    "Approve",
    "Reject",
    "Reject"
]

# -----------------------------
# "Random" Decision Trees
# (simplified handcrafted rules)
# -----------------------------

def tree1(x):
    age, job = x
    if job == 1:
        return "Approve"
    else:
        return "Reject"


def tree2(x):
    age, job = x
    if age >= 20:
        return "Approve"
    else:
        return "Reject"


def tree3(x):
    age, job = x
    if age >= 18:
        return "Approve"
    else:
        return "Reject"


def tree4(x):
    age, job = x
    # slight variation to simulate randomness
    if age >= 30 or job == 1:
        return "Approve"
    else:
        return "Reject"


def tree5(x):
    age, job = x
    if job == 1 and age >= 18:
        return "Approve"
    else:
        return "Reject"


# -----------------------------
# Random Forest (Voting System)
# -----------------------------
def random_forest_predict(x):

    trees = [tree1, tree2, tree3, tree4, tree5]

    votes = []

    for tree in trees:
        votes.append(tree(x))

    # Count votes
    approve = 0
    reject = 0

    for v in votes:
        if v == "Approve":
            approve += 1
        else:
            reject += 1

    # Final decision
    if approve > reject:
        return "Approve"
    else:
        return "Reject"


# -----------------------------
# Test Prediction
# -----------------------------
test_input = [30, 1]

print("Input:", test_input)
print("Prediction:", random_forest_predict(test_input))