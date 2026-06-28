# Chain Rule: Function-এর ভিতরে Function হলে?

# Derivative আবিষ্কারের পরে নতুন সমস্যা এল। ধরো Function-এর ভিতরে Function আছে। y = (x² + 1)³

# এখন, নিউটন দেখলেন

# Outer Function: (x²+1)³
# Inner Function: x²+1

# দুটোর পরিবর্তন একসাথে হচ্ছে। এখান থেকে জন্ম নেয় Chain Rule
# Formula: dy / dx = dy / du * du / dx

# Example: y = (x**2 + 1)**3
# Inner: u = x**2 + 1
# Outer: y = u**3
# Derivative: 3u² × 2x


def chain_rule(x):
    return 3*(x**2+1)**2 * (2*x)

print(chain_rule(2))

# Deep Learning-এর পুরো Backpropagation Chain Rule-এর উপর দাঁড়িয়ে।
# Input -> Layer1 -> Layer2 -> Layer3 -> Loss
# প্রতিটি layer এর derivative বের করতে হয়।