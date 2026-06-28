# Iterative Solvers: ধরো তোমাকে সমাধান করতে হবে x^2 = 2. কিন্তু Exact Formula ব্যবহার করতে চাও না। তাহলে? বিজ্ঞানীরা বললেন— "একবারে উত্তর বের করো না। ধীরে ধীরে উত্তরটির দিকে এগো।"এভাবেই Iterative Solver-এর জন্ম।

# ধারণা: একটি Guess দিয়ে শুরু করো। তারপর বারবার Update করো। 
# Guess: 1 ↓ 1.5 ↓ 1.416 ↓ 1.4143 ↓ 1.41421 প্রতিটি Step আগের চেয়ে ভালো।

# Python (Newton-Raphson Method):::

x = 1

for i in range(6):

    x = (x + 2/x)/2

    print(x)

    
# Visualization: Wrong Guess ↓ Better Guess ↓ Even Better Guess ↓ Almost Correct ↓ Correct Enough

# ML Relation: এখানেই একটি গুরুত্বপূর্ণ সম্পর্ক আছে। Gradient Descent-ও আসলে একটি Iterative Solver।

# Random Weight ↓ Gradient ↓ Update ↓ Gradient ↓ Update ↓ Loss কমে↓Best Weight

# Neural Network কখনোই একবারে সঠিক Weight পায় না। হাজার হাজার Iteration-এর মাধ্যমে শেখে।