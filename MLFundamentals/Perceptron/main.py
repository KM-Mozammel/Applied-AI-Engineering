# AND Gate
training_data = [
    ([0, 0], 0),
    ([0, 1], 0),
    ([1, 0], 0),
    ([1, 1], 1)
]

w1 = 0.0
w2 = 0.0
bias = 0.0

learning_rate = 0.1

def activate(value):
    if value >= 0:
        return 1
    else:
        return 0