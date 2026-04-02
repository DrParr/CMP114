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













# =======================================================
# Example 2 - Residual Plots
# =======================================================
# ax[0,1].set_title("Residual Plot")
# ax[0,1].scatter(X, F - F_hat, color = 'k')

# # Plot a scatter plot of our data
# ax[1,0].scatter(X, H, color = 'k')

# # add x and y labels
# ax[1,0].set_xlabel("X")
# ax[1,0].set_ylabel("Y")

# # add a title
# ax[1,0].set_title("Linear Regression")


# =======================================================
# Add linear regression and residual plot in here
# =======================================================












# =======================================================
# Example 2 - Hypothesis Tests
# =======================================================







# =======================================================
# =======================================================
