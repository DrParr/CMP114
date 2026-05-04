import matplotlib.pyplot as plt
from scipy.stats import linregress, t
import numpy as np


# Define test function we'll use
def f(x):
    return 2 * x + 6


def h(x):
    return 0.1 * x**2 + x + 1

# Get our x-values
X = np.linspace(0, 10, 100)

# Introduce some normally distributed error into the data
rng = np.random.default_rng(seed = 42)
error = rng.normal(loc=0.0, scale=1, size=len(X))

# Compute corresponding y-values
F = f(X) + error
H = h(X) + error

# =======================================================
# Example 1 - Linear Regression Basics
# =======================================================

# Instantiate the figure
fig, ax = plt.subplots(nrows = 2, ncols = 2, figsize = (12,6))

# Plot a scatter plot of our data
ax[0,0].scatter(X, F, color = 'k')

# add x and y labels
ax[0,0].set_xlabel("X")
ax[0,0].set_ylabel("Y")

# add a title
ax[0,0].set_title("Linear Regression")

# =======================================================
# Add linear regression in here
# =======================================================
res1 = linregress(X, F)

F_hat = X * res1.slope + res1.intercept

# Plot the 'best-fit' line on top of the data
ax[0,0].plot(X, F_hat, color = 'r', lw = 2)

# =======================================================
# Example 2 - Residual Plots
# =======================================================
ax[0,1].set_title("Residual Plot")
ax[0,1].scatter(X, F - F_hat, color = 'k')

# Plot a scatter plot of our data
ax[1,0].scatter(X, H, color = 'k')

# add x and y labels
ax[1,0].set_xlabel("X")
ax[1,0].set_ylabel("Y")

# add a title
ax[1,0].set_title("Linear Regression")

# =======================================================
# Add linear regression and residual plot in here
# =======================================================
res2 = linregress(X, H)

H_hat = X * res2.slope + res2.intercept

# Plot the 'best-fit' line on top of the data
ax[1,0].plot(X, H_hat, color = 'r', lw = 2)

# residual plot
ax[1,1].set_title("Residual Plot")
ax[1,1].scatter(X, H- H_hat, color = 'k')

# =======================================================
# Example 2 - Hypothesis Tests
# =======================================================

alpha = 0.05

# We get the pvalue for the slope for free from linregress
print(f"For regression1, Reject the Null Hypothesis that the slope = 0? {res1.pvalue < alpha}\n")
print(f"For regression2, Reject the Null Hypothesis that the slope = 0? {res2.pvalue < alpha}\n")

# For the intercept, we need to do it ourselves, but we have stderr_intercept
t_critical = t.ppf(1-alpha/2, df=len(X) - 2) # 2-tailed t test

test_statistic_reg1 = res1.intercept / res1.intercept_stderr
test_statistic_reg2 = res2.intercept / res2.intercept_stderr
print(f"For regression1, Reject the null hypothesis that the intercept = 0? {abs(test_statistic_reg1) > t_critical}")
print(f"For regression2, Reject the null hypothesis that the intercept = 0? {abs(test_statistic_reg2) > t_critical}")

# =======================================================
# =======================================================
plt.show()

















