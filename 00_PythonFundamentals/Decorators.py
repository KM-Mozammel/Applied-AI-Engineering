# Basic Decorator - Logging
# এখানে decorator function call এর আগে/পরে log করছে — training steps auto-log এর মতো।
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"{func.__name__} finished.")
        return result
    return wrapper

@log_decorator
def preprocess(data):
    return [x/10 for x in data]

print(preprocess([10, 20, 30]))

# Performance Profiling Decorator
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def train_model(data):
    time.sleep(1)  # simulate training
    return "Model trained!"

print(train_model([1,2,3]))


# ML Context – Custom Training Step
def training_logger(func):
    def wrapper(*args, **kwargs):
        print("Training step started...")
        result = func(*args, **kwargs)
        print("Training step completed.")
        return result
    return wrapper

@training_logger
def training_step(batch):
    return sum(batch)/len(batch)

print(training_step([1,2,3,4]))