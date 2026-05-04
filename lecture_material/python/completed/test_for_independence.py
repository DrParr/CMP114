import numpy as np
from scipy.stats import chi2_contingency

# Hard-code your matrix here
data = np.array([
[200,130,40],
[220,280,30],
[20,60,20]   
])

# Perform test
chi2, p, dof, expected = chi2_contingency(data)

# Output results
print(f"Chi-Square Statistic: {chi2:.4f}")
print(f"P-value:              {p:.4e}")
print(f"Degrees of Freedom:    {dof}")
print("\nExpected Frequencies:")
print(expected)