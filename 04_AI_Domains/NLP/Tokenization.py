# Tokenizer Funcations
def tokenize(text):
    return text.split()

print(tokenize("AI makes life easier"))

# NumPy tokenizer Array
import numpy as np
tokens = np.array("AI makes life easier".split())
print(tokens)
print(type(tokens))

# Scikit-Learn tokenizer array
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(["AI makes life easier"])
print(vectorizer.get_feature_names_out())
print(X)
print(type(X))