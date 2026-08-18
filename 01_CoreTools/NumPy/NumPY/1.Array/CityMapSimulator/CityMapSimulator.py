# Gps Route Projects:
import matplotlib.pyplot as plt
from data import labels, coordinates, roads

# Place -> Coordinate Mapping
place_map = {}

for label, point in zip(labels, coordinates):
    place_map[label] = point

x = coordinates[:, 0]
y = coordinates[:, 1]

plt.figure(figsize=(10, 10))
plt.scatter(x, y)

for (px, py), label in zip(coordinates, labels):
    plt.text(px, py, label)
    
for start, end in roads:
    start_point = place_map[start]
    end_point = place_map[end]
    
    plt.plot(
        [start_point[0], end_point[0]],
        [start_point[1], end_point[1]],
        color="blue",
        linewidth = 2
    )

plt.grid(True)

plt.axhline(0, color="black")
plt.axvline(0, color="black")

plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")

plt.title("City Map Simulator")

plt.show()
