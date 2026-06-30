# Dataset: list of tuples (feature, label)
dataset = [(i, 2 * i + 1) for i in range(10)]


# Function to compute predictions.
def prediction(x, w, b):
    return w * x + b


# Wrap training functions with a logger decorator.
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name}...")
        return func(*args, **kwargs)

    return wrapper


# exception catch errors like division by zero or missing data.
@logger
def loss(y_true, y_pred):
    try:
        return sum((yt - yp) ** 2 for yt, yp in zip(y_true, y_pred)) / len(y_true)
    except ZeroDivisionError:
        print("Error: Empty dataset!")
        return None


# Create a generator that yields batches of data.
def batch_generator(data, batch_size):
    for i in range(0, len(data), batch_size):
        yield data[i : i + batch_size]


# Build an iterator class of infinite epochs
class EpochIterator:
    def __init__(self, data, epochs):
        self.data = data
        self.epochs = epochs
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.epochs:
            raise StopIteration
        self.current += 1
        return self.data


class LinearModel:
    def __init__(self, w=0.0, b=0.0, lr=0.01):
        self.w = w
        self.b = b
        self.lr = lr

    @logger
    def train(self, data, epochs=5, batch_size=2):
        for epoch_data in EpochIterator(data, epochs):
            for batch in batch_generator(epoch_data, batch_size):
                xs, ys = zip(*batch)
                preds = [predict(x, self.w, self.b) for x in xs]
                l = loss(ys, preds)
                print(f"Epoch {self.w:.2f}, Loss={l:.4f}")
                # simple gradient update
                self.w += self.lr * sum((y - p) * x for x, y, p in zip(xs, ys, preds))
                self.b += self.lr * sum((y - p) for y, p in zip(ys, preds))

model = LinearModel(lr=0.001)
model.train(dataset, epochs=3, batch_size=3)