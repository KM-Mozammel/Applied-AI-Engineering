# Markov Chains জন্ম: রাশিয়ান গণিতবিদ Andrey Markov জানতে চাইলেন, বর্তমান জানা থাকলে, ভবিষ্যৎ অনুমান করা যায়?

# Example: Weather Sunny -> Rainy -> Cloudy
# Markov Rule: Future depends only on Present

import random

states = {
    "Sunny":["Sunny","Rainy"],
    "Rainy":["Cloudy","Sunny"],
    "Cloudy":["Rainy","Sunny"]
}

current = "Sunny"

for _ in range(5):
    current = random.choice(states[current])
    print(current)
    
# Markov Chains -> Hidden Markov Models -> Speech Recognition -> NLP -> Transformers-এর আগের Language Models