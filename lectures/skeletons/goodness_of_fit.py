import scipy.stats as stats

# Sample data for observed and expected frequencies
observed_data = []
expected_data = []

# Number of observations and significance level



# Chi-Square Goodness of Fit Test



# chi square test statistic and p value
print('chi_square_test_statistic is : ' + str(chi_square_test_statistic))
print('p_value : ' + str(p_value))

# find Chi-Square critical value
critical_value = stats.chi2.ppf(1-alpha, df=n-1)
print('critical_value : ' + str(critical_value))