def build_vocab(text):
    words = text.split()
    vocab = sorted(set(words))

    word_to_id = {w: i for i, w in enumerate(vocab)}
    id_to_word = {i: w for w, i in word_to_id.items()}

    tokens = [word_to_id[w] for w in words]

    return words, vocab, word_to_id, id_to_word, tokens