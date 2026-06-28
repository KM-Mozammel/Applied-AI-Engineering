# Function is a small machine
# Input -> Done by Function -> Output

# Normalization
def normalize(data):
    min_val = min(data)
    max_val = max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]
data = [10, 20, 30]
print(normalize(data))

# Normaization using numpy
import numpy as np

def normalize_np(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))
arr = np.array([10, 20, 30])
print(normalize_np(arr))

# Normalization using Scikit-Learn
from sklearn.preprocessing import MinMaxScaler
import numpy as np

scaler = MinMaxScaler()
arr = np.array([[10], [20], [30]])
print(scaler.fit_transform(arr).flatten())


# ********** 2D Array NOrmalization
# Python
def normalize_2d(data):
    flat = [x for row in data for x in row]
    min_val, max_val = min(flat), max(flat)
    
    return [[(x - min_val) / (max_val - min_val) for x in row] for row in data]

data_2d = [[10, 20, 30],
           [40, 50, 60],
           [70, 80, 90]]
print(type(data_2d))

print(normalize_2d(data_2d))

# NumPy
import numpy as np

def normalize_np_2d(data):
    data = np.array(data, dtype=float)
    return (data - np.min(data)) / (np.max(data) - np.min(data))

arr_2d = [[10, 20, 30],
          [40, 50, 60],
          [70, 80, 90]]

print(normalize_np_2d(arr_2d))

# Scikit-Learn 
from sklearn.preprocessing import MinMaxScaler
import numpy as np

scaler = MinMaxScaler()
arr_2d = np.array([[10, 20, 30],
                   [40, 50, 60],
                   [70, 80, 90]])
normalized = scaler.fit_transform(arr_2d)
print(normalized)

# Row-Size Normalizetion
def normalize_rowwise(data):
    result = []
    for row in data:
        min_val, max_val = min(row), max(row)
        result.append([(x - min_val) / (max_val - min_val) for x in row])
    return result

data = [[10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]]

print("Row-wise (Pure):", normalize_rowwise(data))
# numpy
import numpy as np

def normalize_np_rowwise(data):
    arr = np.array(data, dtype=float)
    row_min = arr.min(axis=1).reshape(-1, 1)
    row_max = arr.max(axis=1).reshape(-1, 1)
    return (arr - row_min) / (row_max - row_min)

print("Row-wise (NumPy):\n", normalize_np_rowwise(data))

# Scikit-Learn
from sklearn.preprocessing import MinMaxScaler

def normalize_sklearn_rowwise(data):
    arr = np.array(data, dtype=float)
    normalized = []
    for row in arr:
        scaler = MinMaxScaler()
        normalized.append(scaler.fit_transform(row.reshape(-1, 1)).flatten())
    return np.array(normalized)

print("Row-wise (Sklearn):\n", normalize_sklearn_rowwise(data))



# Colum-Wise NOrmalization
def normalize_colwise(data):
    cols = list(zip(*data))  # transpose
    normalized_cols = []
    for col in cols:
        min_val, max_val = min(col), max(col)
        normalized_cols.append([(x - min_val) / (max_val - min_val) for x in col])
    return [list(row) for row in zip(*normalized_cols)]

print("Column-wise (Pure):", normalize_colwise(data))

# Numpy
def normalize_np_colwise(data):
    arr = np.array(data, dtype=float)
    col_min = arr.min(axis=0)
    col_max = arr.max(axis=0)
    return (arr - col_min) / (col_max - col_min)

print("Column-wise (NumPy):\n", normalize_np_colwise(data))

# Scikit-Learn
def normalize_sklearn_colwise(data):
    arr = np.array(data, dtype=float)
    scaler = MinMaxScaler()
    return scaler.fit_transform(arr)

print("Column-wise (Sklearn):\n", normalize_sklearn_colwise(data))

# Python, Z-score normalization
# Row-wise Z-score Normalization
def zscore_rowwise(data):
    result = []
    for row in data:
        mean = sum(row) / len(row)
        std = (sum((x - mean) ** 2 for x in row) / len(row)) ** 0.5
        result.append([(x - mean) / std for x in row])
    return result

data = [[10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]]

print("Row-wise Z-score (Pure):", zscore_rowwise(data))
# Column-wise Z-score Normalization
def zscore_colwise(data):
    cols = list(zip(*data))
    normalized_cols = []
    for col in cols:
        mean = sum(col) / len(col)
        std = (sum((x - mean) ** 2 for x in col) / len(col)) ** 0.5
        normalized_cols.append([(x - mean) / std for x in col])
    return [list(row) for row in zip(*normalized_cols)]

print("Column-wise Z-score (Pure):", zscore_colwise(data))

# NumPy Version
# Row-wise Z-score
import numpy as np

def zscore_np_rowwise(data):
    arr = np.array(data, dtype=float)
    mean = arr.mean(axis=1).reshape(-1, 1)
    std = arr.std(axis=1).reshape(-1, 1)
    return (arr - mean) / std

print("Row-wise Z-score (NumPy):\n", zscore_np_rowwise(data))

# Column-wise Z-score
def zscore_np_colwise(data):
    arr = np.array(data, dtype=float)
    mean = arr.mean(axis=0)
    std = arr.std(axis=0)
    return (arr - mean) / std

print("Column-wise Z-score (NumPy):\n", zscore_np_colwise(data))

# Scikit-Learn
# Column-wise Z-score
def zscore_sklearn_colwise(data):
    arr = np.array(data, dtype=float)
    scaler = StandardScaler()
    return scaler.fit_transform(arr)

print("Column-wise Z-score (Sklearn):\n", zscore_sklearn_colwise(data))

# Row-wise Z-score
from sklearn.preprocessing import StandardScaler

def zscore_sklearn_rowwise(data):
    arr = np.array(data, dtype=float)
    normalized = []
    for row in arr:
        scaler = StandardScaler()
        normalized.append(scaler.fit_transform(row.reshape(-1, 1)).flatten())
    return np.array(normalized)

print("Row-wise Z-score (Sklearn):\n", zscore_sklearn_rowwise(data))