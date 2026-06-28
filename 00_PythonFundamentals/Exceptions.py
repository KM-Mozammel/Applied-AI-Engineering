# 1. Missing Values Handling
def normalize_data(data):
    try:
        return [x / max(data) for x in data]
    except ZeroDivisionError:
        print("Error: Dataset contains only zeros!")
        return data
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []
        
print(normalize_data([0, 0, 0]))  # fallback 

# 2. API Call Fallback
import requests

def fetch_data(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("Timeout! Retrying with backup API...")
        return {"status": "backup data"}
    except requests.exceptions.RequestException as e:
        print(f"API error: {e}")
        return None

print(fetch_data("https://invalid-api.com/data"))

# 3. Evaluation Metric Safety
def accuracy(y_true, y_pred):
    try:
        correct = sum(t == p for t, p in zip(y_true, y_pred))
        return correct / len(y_true)
    except ZeroDivisionError:
        print("Error: No samples provided!")
        return 0.0

print(accuracy([], []))  # safe fallback