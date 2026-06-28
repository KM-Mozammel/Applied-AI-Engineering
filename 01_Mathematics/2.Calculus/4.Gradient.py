# Gradient : সবচেয়ে দ্রুত উপরে ওঠার দিক কোনটি?

# Partial Derivative পাওয়ার পরে বিজ্ঞানীরা নতুন প্রশ্ন করলেন। ধরি তুমি পাহাড়ের উপর দাঁড়িয়ে আছো। কোন দিকে গেলে সবচেয়ে দ্রুত উপরে উঠব?

# Partial derivative শুধু বলে: x দিকে ঢাল কত? y দিকে ঢাল কত?
# Gradient বলে: সবচেয়ে খাড়া উপরের দিক কোনটা?

# Example : f(x,y)=x^2 + y^2
# Gradient: ∇f=(2x,2y)

def gradient(x,y):
    return (2*x,2*y)

print(gradient(3,4))

# Output: (6,8)

# Visualization: ধরি

# x direction slope = 6
# y direction slope = 8

# Gradient vector: (6,8). এটাই steepest ascent direction।