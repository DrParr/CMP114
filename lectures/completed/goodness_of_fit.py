import scipy.stats as stats

# Sample data for observed and expected frequencies
observed_data = [8, 6, 10, 7, 8, 11, 9]
expected_data = [9, 8, 11, 8, 10, 7, 6]

# Number of observations and significance level
n = len(observed_data)
alpha = 0.05


# Chi-Square Goodness of Fit Test
chi_square_test_statistic, p_value = stats.chisquare(observed_data, expected_data)


# chi square test statistic and p value
print('chi_square_test_statistic is : ' + str(chi_square_test_statistic))
print('p_value : ' + str(p_value))

# find Chi-Square critical value
critical_value = stats.chi2.ppf(1-alpha, df=n-1)
print('critical_value : ' + str(critical_value))