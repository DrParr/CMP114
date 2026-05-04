from scipy.stats import kurtosis, skew
from numpy.random import normal
from scipy.stats import norm
import numpy as np


#=====================================================
# Normal Distribution PDF
#=====================================================

# Define a function to calculate N(x, mu, sigma)
def normal_dist(x, mu=0, sigma=1):
    coeff = 1 / (sigma * np.sqrt(2 * np.pi))
    exponent = -0.5 * ((x - mu) / sigma) ** 2
    return coeff * np.exp(exponent)

# Calculate for a single value of x
y = normal_dist(2, mu=2, sigma=0.5)  # should be about 0.8

#=====================================================
# Normal Distribution PDF and CDF
#=====================================================

# norm.pdf(x, loc=mean, scale=std_dev) 
y = norm.pdf(2, loc=2, scale=0.5)

a = 1
b = 2

# norm.cdf(x, loc=mean, scale=std_dev)
probability = norm.cdf(b, loc=2, scale=0.5) - norm.cdf(a, loc=2,scale=0.5)

#=====================================================
# Skew and Kurtosis
#=====================================================
X = normal(loc = 0, scale = 1, size = 10000)

sk = skew(X)
kurt = kurtosis(X, fisher = False)







