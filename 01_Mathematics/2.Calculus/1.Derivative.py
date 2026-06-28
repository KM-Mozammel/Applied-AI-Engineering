# Derivative : কত দ্রুত পরিবর্তন হচ্ছে?
# সমস্যা : "এই মুহূর্তে আপেলটা কত গতিতে নিচে নামছে?"

# Average speed বের করা সহজ: distance / time

# কিন্তু একটা নির্দিষ্ট মুহূর্তে speed? যেমন ঠিক t = 2 second এ? 
# এই প্রশ্ন থেকেই Derivative জন্ম নেয়।

# Derivative = Instantaneous Rate of Change; অর্থাৎ কোন জিনিস কত দ্রুত পরিবর্তিত হচ্ছে

def position(t):
    return t**2

def derivative(t):
    return 2*t

print(derivative(3))