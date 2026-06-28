# P-Value: Hypothesis Testing-এর পরে প্রশ্ন এল "কতটা Evidence থাকলে Null Hypothesis বাদ দেব?" এখান থেকে P-Value. 
# Rule : P < 0.05 Reject H₀

from scipy.stats import ttest_ind
group1 = [10,11,12]
group2 = [20,21,22]
_, p = ttest_ind(group1,group2)
print(p)

# ML Relation: Scientific Research, Model Comparison, Drug Testing, Feature Importance