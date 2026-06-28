# Generators → infinite বা on-demand data stream তৈরি করে।

# Generator - Infinite Stream
import random
def data_stream():
    while True:
        yield random.randint(0, 100)  # infinite samples

gen = data_stream()
for _ in range(5):
    print("Sample:", next(gen))


# MINI ML context
def batch_generator(data, batch_size):
    for i in range(0, len(data), batch_size):
        yield data[i:i+batch_size]

dataset = list(range(1, 11))  # 10 samples
for batch in batch_generator(dataset, 3):
    print("Training on batch:", batch)
