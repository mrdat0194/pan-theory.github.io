import numpy as np
from scipy import stats

def relative_entropy(p, q):
    return sum(p[i] * np.log2(p[i]/q[i]) for i in range(len(p)))

a = relative_entropy([0.95,0.05], [0.2,0.8])

b = stats.entropy(pk = [0.95,0.05], qk = [0.2,0.8], base=2)

assert a == b

from sklearn.feature_selection import mutual_info_classif
from sklearn.metrics import mutual_info_score

a = np.array([0.25, 0.25, 0.2, 0.15, 0.15])
# b = np.array([0.25, 0.25, 0.2, 0.15, 0.15])

print(stats.entropy([0.25, 0.25, 0.2, 0.15, 0.15], base=2)) # express in bits
print(stats.entropy([0.25, 0.25, 0.2, 0.15, 0.15])) # entropy of 1.58, expressed in nats

# print(mutual_info_classif(a.reshape(-1,1), b, discrete_features = True)) # mutual information of 0.69, expressed in nats
# print(mutual_info_score(b,a))