# Exercise 1: একটি file তৈরি করো। message.txt তাতে Hello AI লিখো।
# with open("message.txt", "w") as file:
#     file.write("Hello AI")

# ------------------------------------------------------------
# Exercise 2: নিজের Name, Age, Country - JSON File-এ Save করো।
import csv
import json
person_info = {
    "name": "John Doe",
    "age": 30,
    "country": "USA"
}
# with open("person_info.json", "w") as json_file:
#     json.dump(person_info, json_file)

# ------------------------------------------------------------
# Exercise 3: একটি CSV File তৈরি করো। Name,Marks ৩ জন Student যোগ করো।
# with open("students.csv", "w", newline="") as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(["Name", "Marks"])
#     writer.writerow(["Alice", 85])
#     writer.writerow(["Bob", 90])
# ------------------------------------------------------------
# Exercise 4: Pathlib ব্যবহার করে Logs - Folder তৈরি করো।
from pathlib import Path

# path = Path("Logs")
# path.mkdir(exist_ok=True)
# ------------------------------------------------------------
# Exercise 5: একটি List Pickle File-এ Save করে, পুনরায় Load করো।
import pickle
# list = ["apple", "banana", "cherry"]
# with open("fruits.pkl", "wb") as file:
#     pickle.dump(list, file)

with open("fruits.pkl", "rb") as file:
    loaded_list = pickle.load(file)
    print(loaded_list)
# ------------------------------------------------------------
# Exercise 6: YAML Configuration তৈরি করো। host, port, database, debug
import yaml

config = {
    "host": "localhost",
    "port": 5432,
    "database": "mydb",
    "debug": True
}

with open("config.yaml", "w") as yaml_file:
    yaml.dump(config, yaml_file)