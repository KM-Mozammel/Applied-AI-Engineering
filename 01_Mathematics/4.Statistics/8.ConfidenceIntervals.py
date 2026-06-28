# Confidence Interval: সব মানুষের Height মাপা সম্ভব না। তাই Sample নেওয়া হলো। কিন্তু প্রশ্ন— "এই Sample কি পুরো Population-কে ঠিকভাবে প্রতিনিধিত্ব করছে?" তাই জন্ম হলো Confidence Interval।

# Example: Average Height 170 cm ±2 cm 95% Confidence

import scipy.stats as stats
mean = 170
margin = 2
print(mean-margin, mean+margin)

# ML Relation: Model Evaluation, A/B Testing, Clinical Trials