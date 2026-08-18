import numpy as np


def train(model, tokens, sequence_length, epochs, learning_rate):
    for epoch in range(epochs):
        total_loss = 0

        for i in range(len(tokens) - sequence_length):
            x_ids = tokens[i:i + sequence_length]
            target_id = tokens[i + sequence_length]

            H, _, probs = model.forward(x_ids)

            loss = -np.log(probs[target_id] + 1e-9)
            total_loss += loss

            dlogits = probs.copy()
            dlogits[target_id] -= 1

            model.Wo -= learning_rate * np.outer(H[-1], dlogits)

        if (epoch + 1) % 50 == 0:
            print(f"Epoch {epoch + 1}/{epochs}, Loss: {total_loss:.4f}")