import numpy as np
roads = [
    ("House", "Bus Stop"),
    ("Bus Stop", "Office"),
    ("Office", "Mall"),
    ("Mall", "Park"),

    ("Park", "School"),
    ("School", "Hospital"),
    ("Hospital", "Library"),

    ("Mall", "Restaurant"),
    ("Restaurant", "Coffee Shop"),
    ("Coffee Shop", "Bakery"),
    ("Bakery", "Bookstore"),

    ("Mall", "Bank"),
    ("Bank", "Police Station"),
    ("Police Station", "Fire Station"),

    ("Mall", "Gym"),
    ("Gym", "Pharmacy"),
    ("Pharmacy", "Supermarket"),

    ("Airport", "Hotel"),
    ("Hotel", "Museum"),
    ("Museum", "Stadium"),

    ("Train Station", "Bus Terminal"),
    ("Bus Terminal", "Metro Station"),

    ("IT Park", "Tech Hub"),
    ("Tech Hub", "University"),
    ("University", "University Hall"),

    ("Science Center", "Botanical Garden"),

    ("Bridge", "Factory"),
    ("Factory", "Warehouse"),
    ("Warehouse", "Port"),
    ("Port", "Harbor"),

    ("Forest", "Mountain"),
    ("Mountain", "Lake"),
    ("Lake", "Beach"),
]

coordinates = np.array(
    [
        [0, 0], [3, 4], [6, 8], [3, 5], [3, 0], [0, 8],
        [2, 7], [5, 1],
        [8, 2], [7, 6],
        [9, 4], [10, 8],
        [12, 3], [11, 7],
        [13, 5], [14, 2],
        [15, 6], [16, 1],
        [17, 8], [18, 4],
        [19, 7], [20, 2],
        [21, 6], [22, 3],
        [23, 8], [24, 5],
        [25, 1], [26, 7], [27, 4], [28, 2], [29, 6], [30, 3], [31, 8], [32, 5], [33, 1], [34, 7], [35, 4], [36, 2], [37, 6], [38, 3], [39, 8], [40, 5],
        [41, 1], [42, 7], [43, 4], [44, 2],
        [45, 6], [46, 3], [47, 8], [48, 5],
    ]
)

labels = [
    "House", "Office", "Park", "Bus Stop", "Bar", "Playground", "School", "Hospital", "Mall", "Library",
    "Restaurant",
    "University", "Bank", "Police Station",
    "Fire Station", "Cinema", "Gym", "Pharmacy", "Supermarket", "Stadium", "Museum",
    "Hotel", "Airport", "Train Station",
    "Coffee Shop", "Bakery",
    "Bookstore", "Post Office",
    "Gas Station", "Temple", "Mosque", "Church", "Zoo", "Aquarium", "Lake", "Beach", "Mountain", "Forest", "Bridge", "Factory", "Warehouse",
    "Port", "Harbor", "Bus Terminal", "Metro Station",
    "IT Park", "Tech Hub","University Hall", "Science Center", "Botanical Garden",
]
