from sklearn.svm import SVC
import numpy as np

X = np.array([
 [1,1],
 [2,2],
 [5,5],
 [6,6]
])

y = np.array([0,0,1,1])

model = SVC()

model.fit(X,y)

print(model.predict([[3,3]]))

# Manuall Programming
# Training data
X = [
    [1, 1],
    [2, 2],
    [5, 5],
    [6, 6]
]

y = [0, 0, 1, 1]

# -----------------------------
# Manual SVM-like decision boundary
# -----------------------------
# We assume:
# x + y = 6 is the separating hyperplane

def manual_svm_predict(point):

    x, y_val = point

    # compute decision value
    decision = x + y_val

    # classify based on boundary
    if decision < 6:
        return 0
    else:
        return 1


# -----------------------------
# Test
# -----------------------------
print(manual_svm_predict([3, 3]))