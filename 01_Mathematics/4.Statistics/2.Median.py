# Median: ধরো, 20 - 22 - 21 - 25 - 500
# Mean = 117.6, যা বাস্তব অবস্থা বোঝায় না।
# তাই বিজ্ঞানীরা বললেন "মাঝখানের মানুষটাকে দেখি।" এভাবেই Median-এর জন্ম।

# What is the median of 1, 2, 3, 4, 5, 6, 7, 8, 9, 10?
# There are 10 values in the dataset. The number of terms  is even.

# Find the Middle Terms. 
# For an even dataset, find two middle terms.
# Locate positions n/2 and n/2 + 1. 
# These are the 5th and 6th terms. The 5th term 5. The 6 th term is 6. 

# Average the Middle Values Add the two middle values together: Sum = 5+6=11
# Divide the total sum by 2. median: 11/2=5.5

# The median of the dataset from 1 to 10 is 5.5 

import statistics
data = [20,22,21,25,500]
print(statistics.median(data))

# Output : 22
# ML Relation: Outlier থাকলে Median বেশি reliable।