import numpy as np
from scipy.stats import t
from scipy.stats import norm



#==============================================
# Z-test, one tailed
#==============================================

def z_test_one_tailed(sample_data, mu_0, sigma, alpha, test_type = '>'):
    # sample mean
    x_bar = np.mean(sample_data)

    # sample size
    n = len(sample_data)

    # standard error of the mean
    se = sigma / np.sqrt(n)

    # test statistic (z-score)
    z = (x_bar - mu_0) / se

    # critical value and p-value for one-tailed test
    z_crit = norm.ppf(1 - alpha)
    p_value = 1 - norm.cdf(z)

    # print results

    print('\n\n' + '=' * 60)
    print(f'Test type: One-Tailed Z-test with Ha: mu {test_type} {mu_0}')
    print('=' * 60)
    print(f'Sample mean: {x_bar:.2f}')
    print(f'Standard error: {se:.2f}')
    print(f'Z-test statistic: {z:.2f}')
    print(f'Critical value: {z_crit:.2f}')
    print(f'P-value: {p_value:.4f}')

    # decision
    if test_type == '>':
        if z > z_crit:
            print('Reject the null hypothesis (H0)')
        else:
            print('Fail to reject the null hypothesis (H0)')
    elif test_type == '<':
        if z < -z_crit:
            print('Reject the null hypothesis (H0)')
        else:
            print('Fail to reject the null hypothesis (H0)')
    else:
        print('Invalid test type. Use ">" for H1: mu > mu_0 or "<" for H1: mu < mu_0.')
    
    return z, p_value

# Known population standard deviation
sigma = 15

# null hypothesis mean
mu_0 = 100 

# sample data
sample_data = np.array([90, 95, 100, 105, 110, 115, 120])

# alpha level
alpha = 0.05

# type of test: '>' for H1: mu > mu_0, '<' for H1: mu < mu_0
test_type = '>'

z_test_one_tailed(sample_data, mu_0, sigma, alpha, test_type)

#==============================================
# Z-test, two tailed
#==============================================

def z_test_two_tailed(sample_data, mu_0, sigma, alpha):
    # sample mean
    x_bar = np.mean(sample_data)

    # sample size
    n = len(sample_data)

    # standard error of the mean
    se = sigma / np.sqrt(n)

    # test statistic (z-score)
    z = (x_bar - mu_0) / se

    # critical values and p-value for two-tailed test
    z_crit = norm.ppf(1 - alpha/2)
    p_value = 2 * (1 - norm.cdf(abs(z)))

    # print results
    print('\n\n' + '=' * 60)
    print(f'Test type: Two-Tailed Z-test with Ha: mu ≠ {mu_0}')
    print('=' * 60)
    print(f'Sample mean: {x_bar:.2f}')
    print(f'Standard error: {se:.2f}')
    print(f'Z-test statistic: {z:.2f}')
    print(f'Critical values: ±{z_crit:.2f}')
    print(f'P-value: {p_value:.4f}')

    # decision
    if abs(z) > z_crit:
        print('Reject the null hypothesis (H0)')
    else:
        print('Fail to reject the null hypothesis (H0)')
    
    return z, p_value

# Known population standard deviation
sigma = 15

# null hypothesis mean
mu_0 = 100

# sample data
sample_data = np.array([90, 95, 100, 105, 110, 115, 120])

# alpha level
alpha = 0.05

z_test_two_tailed(sample_data, mu_0, sigma, alpha)

#==============================================
# T-test, one tailed
#==============================================

def t_test_one_tailed(sample_data, mu_0, alpha, test_type = '>'):
    # sample mean
    x_bar = np.mean(sample_data)

    # sample standard deviation
    s = np.std(sample_data, ddof=1)

    # sample size
    n = len(sample_data)

    # standard error of the mean
    se = s / np.sqrt(n)

    # test statistic (t-score)
    t_stat = (x_bar - mu_0) / se

    # degrees of freedom
    df = n - 1

    # critical value and p-value for one-tailed test
    t_crit = t.ppf(1 - alpha, df=df)
    p_value = 1 - t.cdf(t_stat, df=df)

    # print results
    print('\n\n' + '=' * 60)
    print(f'Test type: One-Tailed T-test with Ha: mu {test_type} {mu_0}')
    print('=' * 60)
    print(f'Sample mean: {x_bar:.2f}')
    print(f'Sample standard deviation: {s:.2f}')
    print(f'Standard error: {se:.2f}')
    print(f'T-test statistic: {t_stat:.2f}')
    print(f'Critical value: {t_crit:.2f}')
    print(f'P-value: {p_value:.4f}')

    # decision
    if test_type == '>':
        if t_stat > t_crit:
            print('Reject the null hypothesis (H0)')
        else:
            print('Fail to reject the null hypothesis (H0)')
    elif test_type == '<':
        if t_stat < -t_crit:
            print('Reject the null hypothesis (H0)')
        else:
            print('Fail to reject the null hypothesis (H0)')
    else:
        print('Invalid test type. Use ">" for H1: mu > mu_0 or "<" for H1: mu < mu_0.')
    
    return t_stat, p_value

# null hypothesis mean
mu_0 = 100

# sample data
sample_data = np.array([90, 95, 100, 105, 110, 115, 120])

# alpha level
alpha = 0.05

# type of test: '>' for H1: mu > mu_0, '<' for H1: mu < mu_0
test_type = '>'

t_test_one_tailed(sample_data, mu_0, alpha, test_type)


#==============================================
# T-test, two tailed
#==============================================

def t_test_two_tailed(sample_data, mu_0, alpha):
    # sample mean
    x_bar = np.mean(sample_data)

    # sample standard deviation
    s = np.std(sample_data, ddof=1)

    # sample size
    n = len(sample_data)

    # standard error of the mean
    se = s / np.sqrt(n)

    # test statistic (t-score)
    t_stat = (x_bar - mu_0) / se

    # degrees of freedom
    df = n - 1

    # critical values and p-value for two-tailed test
    t_crit = t.ppf(1 - alpha/2, df=df)

    p_value = 2 * (1 - t.cdf(abs(t_stat), df=df))

    # print results
    print('\n\n' + '=' * 60)
    print(f'Test type: Two-Tailed T-test with Ha: mu ≠ {mu_0}')
    print('=' * 60)
    print(f'Sample mean: {x_bar:.2f}')
    print(f'Sample standard deviation: {s:.2f}')
    print(f'Standard error: {se:.2f}')
    print(f'T-test statistic: {t_stat:.2f}')
    print(f'Critical values: ±{t_crit:.2f}')
    print(f'P-value: {p_value:.4f}')

    # decision
    if abs(t_stat) > t_crit:
        print('Reject the null hypothesis (H0)')
    else:
        print('Fail to reject the null hypothesis (H0)')
    
    return t_stat, p_value

# null hypothesis mean
mu_0 = 100

# sample data
sample_data = np.array([90, 95, 100, 105, 110, 115, 120])

# alpha level
alpha = 0.05

t_test_two_tailed(sample_data, mu_0, alpha)


