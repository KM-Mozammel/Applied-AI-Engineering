# Partial Derivative : অনেক Variable থাকলে একটি Variable-এর প্রভাব কত?
# Newton এর পরে বিজ্ঞানীরা আরও জটিল সমস্যা পেলেন। আগে ছিল: f(x), এখন: f(x,y,z)

# house_price = size + location + age

# এখন প্রশ্ন: size বাড়লে কী হবে? location স্থির রেখে। এখান থেকে জন্ম Partial Derivative

# Example: f(x,y)=x^2+y^2
# x অনুযায়ী: ∂x / ∂f = 2x
# y অনুযায়ী: ∂y / ∂f = 2y

def partial_x(x):
    return 2*x

def partial_y(y):
    return 2*y

# Machine Learning-এ Loss(w1,w2,w3,...) প্রতিটি weight-এর জন্য derivative বের করতে হয়।