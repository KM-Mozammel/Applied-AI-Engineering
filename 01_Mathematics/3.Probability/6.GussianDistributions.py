# Gaussian Distribution এর জন্ম: মানুষ দেখল, অনেক জিনিস Height, Weight, IQ, Exam Marks. একই pattern follow করে। মাঝখানে বেশি, দুই পাশে কম:

# Bell Curve:

#        /\
#       /  \
#      /    \
# ----/------\----

import numpy as np
data = np.random.normal(170,10,1000)
print(np.mean(data))

# ML Relation:
# Noise
# Feature Distribution
# Anomaly Detection