import numpy as np
import pandas as pd
from scipy.stats import chi2, chi2_contingency
import numpy
import matplotlib.pyplot as plt
from scipy.stats import norm, chisquare

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
Observe = [0 if i == 0 else (cumulative[i] - cumulative[i-1])
            for i in range(len(cumulative)) ]

#

average = np.mean(df['Demand'])
std = np.std(df['Demand'])

expCum = norm(average,std).cdf(edges[:-1])

Expected = [expCum[i]*len(df) if i == 0 else (expCum[i] - expCum[i-1])*len(df)
            for i in range(len(expCum))]

p_value = chisquare(Observe, f_exp=Expected)

ob = [0,1,1,3,2,7,12,9,7,8,7,1,0,2,0,0,0]

ex = [0.15,0.34,0.90,2.01,3.79,6.08,8.28,9.57,9.39,7.82,5.53,3.32,1.69,0.73,0.27,0.08,0.02]

p_value2 = chisquare(ob, f_exp=ex)
print(p_value2)

g, p1, dof, expctd = chi2_contingency(np.array([ob, ex]))
print(p1)

g, p2, dof, expctd = chi2_contingency(np.array([Observe, Expected]))
print(p2)
