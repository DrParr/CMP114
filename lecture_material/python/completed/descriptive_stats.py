import numpy as np
import random

# Set the seed to a specific value (e.g., 42) 
random.seed(42) 

# Generate the set with list enumeration
X = [random.randint(0, 100) for _ in range(10)]

#===========================================
# Mean
#===========================================
# Calculate the mean with numpy
mean = np.mean(X)

# Or without a package
mean = sum(X) / len(X)


#===========================================
# Median
#===========================================
# Find the median with numpy
median = np.median(X)


#===========================================
# Variance
#===========================================
# Find the median with numpy
# ddof = 1 for sample variance
variance = np.var(X, ddof=1)

#===========================================
# Standard Deviation
#===========================================
# Find the median with numpy
# ddof = 1 for sample variance
standard_deviation = np.std(X, ddof=1)


#===========================================
# Quartiles
#===========================================
# Q1, Median (Q2), Q3
quartiles = np.quantile(X, [0.25, 0.5, 0.75]) 

Q1 = quartiles[0]
Q3 = quartiles[2]
IQR = Q3 - Q1









