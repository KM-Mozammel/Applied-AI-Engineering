# Binomial Distribution এর জন্ম: মানুষ জানতে চাইল। 10 বার coin toss করলে, কয়বার Head আসবে? এখান থেকে Binomial Distribution

from math import comb

n = 10
k = 6
p = 0.5

prob = comb(n,k)*(p**k)*((1-p)**(n-k))

print(prob)

# ML Relation: Success / Failure
# Click / No Click
# Buy / Not Buy
# Spam / Not Spam