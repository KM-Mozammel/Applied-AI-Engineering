# | Height | Label |
# | ------ | ----- |
# | 150    | Child |
# | 160    | Child |
# | 180    | Adult |
# | 190    | Adult |

from sklearn.neighbors import KNeighborsClassifier
import numpy as np

X = np.array([
 [150],
 [160],
 [180],
 [190]
])

y = np.array([
 "Child",
 "Child",
 "Adult",
 "Adult"
])

model = KNeighborsClassifier(n_neighbors=3)

model.fit(X, y)

print(model.predict([[170]]))



# Manuall Programming

# Training data

X = [150, 160, 180, 190]

y = ["Child", "Child", "Adult", "Adult"]

k = 3

new_height = 170

# Calculate distance to every known example

distances = []

for i in range(len(X)):

    distance = abs(new_height - X[i])

    distances.append((distance, y[i]))

print("All Distances:")
print(distances)

# Sort by nearest distance

distances.sort(key=lambda x: x[0])

print("\nSorted Distances:")
print(distances)

# Take K nearest neighbors

neighbors = distances[:k]

print("\nNearest Neighbors:")
print(neighbors)

# Voting

votes = {}

for distance, label in neighbors:

    if label not in votes:
        votes[label] = 0

    votes[label] += 1

print("\nVotes:")
print(votes)

# Find winner

prediction = max(votes, key=votes.get)

print("\nPrediction:", prediction)