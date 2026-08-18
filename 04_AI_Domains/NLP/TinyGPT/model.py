import numpy as np
from utils import softmax


class TinyGPT:
    def __init__(self, vocab_size, embedding_dim, sequence_length):
        self.vocab_size = vocab_size
        self.embedding_dim = embedding_dim
        self.sequence_length = sequence_length

        self.E = np.random.randn(vocab_size, embedding_dim) * 0.1
        self.P = np.random.randn(sequence_length, embedding_dim) * 0.1

        self.Wq = np.random.randn(embedding_dim, embedding_dim) * 0.1
        self.Wk = np.random.randn(embedding_dim, embedding_dim) * 0.1
        self.Wv = np.random.randn(embedding_dim, embedding_dim) * 0.1

        self.Wo = np.random.randn(embedding_dim, vocab_size) * 0.1
        
    def self_attention(self, X):
        Q = X @ self.Wq
        K = X @ self.Wk
        V = X @ self.Wv

        scores = (Q @ K.T) / np.sqrt(self.embedding_dim)

        mask = np.triu(np.ones_like(scores), k=1) * -1e9
        scores += mask

        attention = np.array([softmax(row) for row in scores])
        output = attention @ V

        return output, attention

    def forward(self, x_ids):
        X = self.E[x_ids] + self.P
        H, attention = self.self_attention(X)
        logits = H[-1] @ self.Wo
        probs = softmax(logits)
        return H, attention, probs