# Hypothesis Testing: বিজ্ঞানীরা জানতে চাইলেন "এই পরিবর্তনটা সত্যি? নাকি শুধু ভাগ্য?"

# Example: নতুন Medicine পুরোনো Medicine কোনটা ভালো? দুটি ধারণা তৈরি হলো

# H₀: Null Hypothesis -> No Difference
# H₁: Alternative Hypothesis -> Difference Exists

from scipy.stats import ttest_ind
group1 = [10,11,12]
group2 = [20,21,22]
print(ttest_ind(group1,group2))

# ML Relation: A/B Testing, Experiment Design, Feature Comparison