# Custom Dataset Loader(Class)

class CustomDataset:
    def __init__(self, data):
        self.data = data
        
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        return self.data[idx]
    
dataset = CustomDataset([1, 2, 3, 4, 5])
print("Dataset length:", len(dataset))
print("First sample:", dataset[0])

# Model Architecture as Class
import numpy as np

class LinearModel:
    def __init__(self, input_dim):
        self.weights = np.random.randn(input_dim)
        self.bias = 0.0
        
    def forward(self, x):
        return np.dot(x, self.weights) + self.bias

model = LinearModel(input_dim = 3)
sample = np.array([1.0, 2.0, 3.0])
print("Prediction:", model.forward(sample))

# Inheritance in Python
class BaseModel:
    def train(self, data):
        print("Training on data:", data)

class ExtendedModel(BaseModel):
    def train(self, data):
        print("Custom training logic...")
        super().train(data)
        
model = ExtendedModel()
model.train([1, 2, 3])