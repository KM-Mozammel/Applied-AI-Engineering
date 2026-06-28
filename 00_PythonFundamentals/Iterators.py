# Iterators → finite dataset কে batch-wise consume করা যায়।

# Batch Loader
class BatchLoader:
    def __init__(self, data, batch_size):
        self.data = data
        self.batch_size = batch_size
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        batch = self.data[self.index:self.index+self.batch_size]
        self.index += self.batch_size
        return batch

dataset = list(range(1, 21))  # 20 samples
loader = BatchLoader(dataset, batch_size=5)

for batch in loader:
    print("Batch:", batch)
