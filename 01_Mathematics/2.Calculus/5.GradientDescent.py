# Gradient Descent: সবচেয়ে দ্রুত নিচে নামার দিক কোনটি?
# ধরি পাহাড়ের চূড়ায় দাঁড়িয়ে আছো। তুমি নিচে নামতে চাও।
# Gradient দেখাচ্ছে: উপরে যাওয়ার দিক। তাহলে? উল্টো দিকে হাঁটো। এটাই Gradient Descent

# Formula: Xnew​ = Xold​−learning rate×gradient
# Loss Funcation: L(x)=x^2
# Derivative: L′(x)=2x

x = 8

learning_rate = 0.1

for i in range(10):

    gradient = 2*x

    x = x - learning_rate * gradient

    print(x)