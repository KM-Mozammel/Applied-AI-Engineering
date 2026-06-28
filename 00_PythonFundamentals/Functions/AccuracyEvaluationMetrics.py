# Pure Python
def accuracy(y_true, y_pred):
    correct = sum(t == p for t, p in zip(y_true, y_pred))
    return correct / len(y_true)

print(accuracy([1, 0, 1], [1, 0, 0]))

# NumPy
import numpy as np
def accuracy_np(y_true, y_pred):
    return np.mean(y_true == y_pred)

output = accuracy_np(
    np.array([1,0,1]), 
    np.array([1,0,0])
)
print(output)

# Scikit-Learn
from sklearn.metrics import accuracy_score
print(accuracy_score([1,0,1], [1,0,0]))

# Very Basic Demo
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Step 1: Simulated "voice features"
# ধরুন 3 জন মানুষ আছে (person1, person2, person3)
# প্রতিটি মানুষের জন্য আমরা random feature বানাচ্ছি
np.random.seed(42)  # reproducibility

X = np.vstack([
    np.random.normal(0, 1, (10, 5)),   # person1 features
    np.random.normal(5, 1, (10, 5)),   # person2 features
    np.random.normal(10, 1, (10, 5))   # person3 features
])

y = np.array(["person1"]*10 + ["person2"]*10 + ["person3"]*10)

# Step 2: Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 3: Simple classifier (KNN)
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# Step 4: Predictions
y_pred = model.predict(X_test)

# Step 5: Accuracy function
def accuracy(y_true, y_pred):
    correct = np.sum(y_true == y_pred)
    total = len(y_true)
    return correct / total

print("Predictions:", y_pred)
print("True labels:", y_test)
print("Accuracy:", accuracy(y_test, y_pred))
