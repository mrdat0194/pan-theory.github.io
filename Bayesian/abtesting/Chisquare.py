import numpy as np
import pandas as pd
from scipy.stats import chi2, chi2_contingency
import numpy
import matplotlib.pyplot as plt
from scipy.stats import norm,chisquare

def get_p_value(T):
    # same as scipy.stats.chi2_contingency(T, correction=False)
    det = T[0,0]*T[1,1] - T[0,1]*T[1,0]
    c2 = float(det) / T[0].sum() * det / T[1].sum() * T.sum() / T[:,0].sum() / T[:,1].sum()
    p = 1 - chi2.cdf(x=c2, df=1)
    return p

# get data
df = pd.read_csv('DailySale.csv')

bin_range = [i for i in range(0, 40, 2)]

hist, edges = np.histogram(
    df['Demand'],
    bins=20,
    range=(0, max(df['Demand'])),
    density=False)

cumulative = np.cumsum(hist)
# plot the cumulative function
plt.plot(edges[:-1], cumulative, label='data')

#
Observe = [ 0 if i == 0 else (cumulative[i] - cumulative[i-1]) for i in range(len(cumulative)) ]

#

average = np.mean(df['Demand'])
std = np.std(df['Demand'])

expCum = norm(average,std).cdf(edges[:-1])

Expected = [expCum[i]*len(df) if i == 0 else (expCum[i] - expCum[i-1])*len(df) for i in range(len(expCum))]

p_value = chisquare(Observe, f_exp=Expected)
p_value1 = chisquare(df['Demand'])


print(p_value)
print(p_value1)
