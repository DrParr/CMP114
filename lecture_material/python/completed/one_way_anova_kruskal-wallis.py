import pandas as pd
from scipy.stats import f_oneway, kruskal

#=============================================================
# Import the Data
#=============================================================
#csv (comma separated), without header
#data = pd.read_csv('filename.csv', header = None, delimiter = ',')

#csv (comma separated), with header
#data = pd.read_csv('filename.csv', delimiter = ',')

#tsv (tab separated), without header
#data = pd.read_csv('filename.txt', header = None, delimiter = '\t')

#tsv (tab separated), with header
#data = pd.read_csv('filename.txt', delimiter = '\t')

#=============================================================
# Select the Groups
#=============================================================
# For data with no header
# group1 = data[0]
# group2 = data[1]

# For data with header
# group1 = data["Columnname1"]
# group2 = data["ColumnName2"]

#=============================================================
# One way ANOVA
#=============================================================
# Perform the one-way ANOVA
f_statistic, p_value = f_oneway(col0, col1, col2, col3, col4)

# Print the results
print(f"F-statistic: {f_statistic}")
print(f"P-value: {p_value}")

# Interpretation (using a common alpha level of 0.05)
alpha = 0.05
if p_value < alpha:
    print("Result: Reject the null hypothesis (H0). At least one group mean is different.")
else:
    print("Result: Fail to reject the null hypothesis (H0). Group means are likely similar.")


#=============================================================
# Kruskal Wallis
#=============================================================


# Perform the Kruskal-Wallis H-test
h_statistic, p_value = kruskal(drug_A, drug_B, drug_C)

print(f"Kruskal-Wallis H-statistic: {h_statistic}")
print(f"P-value: {p_value}")


# Interpret the results (commonly using a significance level of 0.05)
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a statistically significant difference between at least one pair of group medians.")
else:
    print("Fail to reject the null hypothesis: There is not enough evidence to suggest a difference in medians across groups.")