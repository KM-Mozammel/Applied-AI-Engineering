from config import *
from data_loader import load_text
from tokenizer import build_vocab
from model import TinyGPT
from trainer import train
from generator import generate_text

def main():
    text = load_text("data.txt")

    words, vocab, word_to_id, id_to_word, tokens = build_vocab(text)

    print(f"Vocabulary Size: {len(vocab)}")
    print(f"Total Tokens: {len(tokens)}")

    model = TinyGPT(
        vocab_size=len(vocab),
        embedding_dim=EMBEDDING_DIM,
        sequence_length=SEQUENCE_LENGTH
    )

    train(
        model,
        tokens,
        sequence_length=SEQUENCE_LENGTH,
        epochs=EPOCHS,
        learning_rate=LEARNING_RATE
    )

    print("\nGenerated Text:")
    print(generate_text(
        model,
        "the sky is blue",
        word_to_id,
        id_to_word,
        SEQUENCE_LENGTH,
        max_words=20
    ))

if __name__ == "__main__":
    main()