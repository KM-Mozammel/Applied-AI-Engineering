"""
=========================================================
TEXT PREPROCESSING
=========================================================

Text Data খুবই Dirty হয়।

Computer মানুষের মতো ভাষা বুঝে না।

সে শুধু Number বোঝে।

তাই Text → Clean → Token → Number

এই পুরো Process-কে বলা হয়

Text Preprocessing

---------------------------------------------------------
Real Life

Original Sentence

"I LOVE Programming!!! 😍😍😍"

Machine এর জন্য

love programming

অথবা

[103,44]

=========================================================
WHY TEXT PREPROCESSING?
=========================================================

কারণ Raw Text এ থাকে

✔ Uppercase
✔ Lowercase
✔ Emoji
✔ URL
✔ HTML
✔ Punctuation
✔ Numbers
✔ Stop Words
✔ Extra Spaces
✔ Typo

এসব Machine Learning Model এর Accuracy কমিয়ে দেয়।

=========================================================
AI/ML USE CASE
=========================================================

✔ Sentiment Analysis
✔ Chatbot
✔ LLM
✔ GPT
✔ BERT
✔ Translation
✔ Spam Detection
✔ News Classification
✔ Search Engine
✔ Recommendation System

=========================================================
STEP 1
LOWERCASING
=========================================================

সব অক্ষর ছোট হাতের করা।

LOVE
Love
love

সব একই হবে।

"""

text = "I LOVE Python"

clean = text.lower()

print(clean)

"""
Output

i love python

---------------------------------------------------------
কেন?

LOVE
Love
love

এগুলো Machine এর কাছে আলাদা শব্দ।

Lower করলে একই হয়ে যায়।

=========================================================
STEP 2
REMOVE PUNCTUATION
=========================================================

Remove

.
,
!
?
:
;
"

"""

import string

text = "Hello!!! How are you?"

translator = str.maketrans("", "", string.punctuation)

clean = text.translate(translator)

print(clean)

"""
Output

Hello How are you

=========================================================
STEP 3
REMOVE EXTRA SPACE
=========================================================

"""

text = "Hello      World"

clean = " ".join(text.split())

print(clean)

"""
Output

Hello World

=========================================================
STEP 4
TOKENIZATION
=========================================================

Sentence

↓

Word

---------------------------------------------------------

"I love AI"

↓

["I","love","AI"]

"""

text = "I love AI"

tokens = text.split()

print(tokens)

"""
Output

['I','love','AI']

=========================================================
STEP 5
REMOVE STOP WORDS
=========================================================

Stop Words

the
is
are
a
an
of
to

এগুলো Meaning খুব বেশি বহন করে না।

"""

stop_words = {"the","is","a","an","to"}

sentence = "the cat is running"

words = sentence.split()

clean = [w for w in words if w not in stop_words]

print(clean)

"""
Output

['cat','running']

=========================================================
STEP 6
STEMMING
=========================================================

running
runner
runs

↓

run

"""

from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

print(stemmer.stem("running"))

"""
Output

run

=========================================================
STEP 7
LEMMATIZATION
=========================================================

Better than Stemming

running

↓

run

better

↓

good

"""

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("running","v"))

"""
Output

run

=========================================================
STEP 8
REMOVE URL
=========================================================

"""

import re

text = "Visit https://openai.com"

clean = re.sub(r"http\\S+","",text)

print(clean)

"""
Output

Visit

=========================================================
STEP 9
REMOVE NUMBER
=========================================================

"""

text = "I have 100 apples"

clean = re.sub(r"\d+","",text)

print(clean)

"""
Output

I have apples

=========================================================
STEP 10
REMOVE EMOJI
=========================================================

Emoji

😀😂😍❤️🔥

Machine এর জন্য Noise হতে পারে।

"""

text = "I love AI ❤️"

clean = text.encode("ascii","ignore").decode()

print(clean)

"""
Output

I love AI

=========================================================
STEP 11
VECTORIZATION
=========================================================

Machine Text বুঝে না।

তাই Text →

Number

Example

Dog

↓

12

Cat

↓

30

=========================================================
Bag Of Words
=========================================================

Sentence

I Love AI

↓

[1,1,1]

=========================================================
TF-IDF
=========================================================

যে Word বেশি গুরুত্বপূর্ণ
তার Weight বেশি।

=========================================================
WORD EMBEDDING
=========================================================

Word →

Vector

King

↓

[0.31,-0.88,...]

GPT, BERT
Embedding ব্যবহার করে।

=========================================================
IMPORTANT LIBRARIES
=========================================================

✔ nltk
✔ spacy
✔ sklearn
✔ transformers
✔ sentence-transformers

=========================================================
INTERVIEW QUESTIONS
=========================================================

Q.
Difference between

Tokenization

and

Embedding?

Answer

Tokenization

Sentence → Words

Embedding

Words → Vector

---------------------------------------------------------

Q

Difference between

Stem

and

Lemma

Stem

Fast
Less Accurate

Lemma

Slow
More Accurate

=========================================================
REAL PROJECT
=========================================================

Spam Detection

Email

↓

Cleaning

↓

Tokenization

↓

Stop Word Removal

↓

TF-IDF

↓

Model

↓

Spam / Not Spam

=========================================================
SUMMARY
=========================================================

Raw Text

↓

Lowercase

↓

Remove Punctuation

↓

Remove URL

↓

Remove Emoji

↓

Remove Numbers

↓

Tokenize

↓

Remove Stop Words

↓

Stem/Lemmatize

↓

Vectorize

↓

Machine Learning Model
=========================================================
"""