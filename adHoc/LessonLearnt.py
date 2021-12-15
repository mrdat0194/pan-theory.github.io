from scipy.stats import norm

a = norm.cdf(350,250,75)
a = norm.ppf(0.95,250,75)

print(a)