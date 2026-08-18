import numpy as np

def predict_next(model, input_words, word_to_id, id_to_word):
    x_ids = [word_to_id[w] for w in input_words]
    _, _, probs = model.forward(x_ids)
    predicted_id = np.argmax(probs)
    return id_to_word[predicted_id]


def generate_text(model, seed_text, word_to_id, id_to_word, sequence_length, max_words=20):
    generated = seed_text.lower().split()

    while len(generated) < max_words:
        context = generated[-sequence_length:]
        next_word = predict_next(model, context, word_to_id, id_to_word)
        generated.append(next_word)

    return " ".join(generated)