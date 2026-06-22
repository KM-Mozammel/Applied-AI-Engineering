import pandas as pd

data = {
    'Name': ['Alice', 'Bob'],
    'Age': [25,30]
}

df = pd.DataFrame(data)

print("Pandas Table:\n", df)
print("\nJust the 'Age' column:\n", df['Age'])