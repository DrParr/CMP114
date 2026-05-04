import pandas as pd
from scipy.stats import f_oneway, tukey_hsd, dunnett

# Import the data from 
data = pd.read_csv('')

# we can group the data by drug type
grouped = data.groupby('')

# How many groups do we have? How many in each group?
print(grouped.count())


#=============================================================
# One way ANOVA
#=============================================================

# Perform the one-way ANOVA
f_statistic, p_value = f_oneway(group1, group2, group3, ...)

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
# Tukey HSD Post-hoc Test
#=============================================================

res = tukey_hsd(group1, group2, group3, ...)

print("Tukey HSD Post-hoc Test Results:")
print(res)


#=============================================================
# Dunnett's Post-hoc Test
#=============================================================

# lets say, for example, drug A is the control group
res = dunnett(drug_B, drug_C, control=drug_A, alternative='two-sided')

print("Dunnett's Post-hoc Test Results:")
print(res)








