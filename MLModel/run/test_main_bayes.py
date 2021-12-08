from MLModel.data_pipeline import data_helper
from MLModel.model import bayesian
import pandas as pd
import warnings
import os
from sklearn.exceptions import DataConversionWarning
from sklearn.exceptions import UndefinedMetricWarning
from MLModel import DATA_DIR
import numpy as np
from sklearn.model_selection import train_test_split
from MLModel.model.code import common

warnings.filterwarnings(action='ignore', category=DataConversionWarning)
warnings.filterwarnings(action='ignore', category=UndefinedMetricWarning)

## Trial 1
# data = pd.read_csv('/Users/petern/ML-From-Scratch/mlfromscratch/data/TempLinkoping2016.txt', sep="\t")
# time = np.atleast_2d(data["time"].values).T
# temp = np.atleast_2d(data["temp"].values).T
#
# X = time # fraction of the year [0, 1]
# y = temp

## Trial 2
DATA = common.dataDirectory()

LOAN3000_CSV = DATA / 'loan3000.csv'
LOAN_DATA_CSV = DATA / 'loan_data.csv.gz'
FULL_TRAIN_SET_CSV = DATA / 'full_train_set.csv.gz'

## Naive Bayes
### The Naive Solution

loan_data = pd.read_csv(LOAN_DATA_CSV)

# convert to categorical
loan_data.outcome = loan_data.outcome.astype('category')
loan_data.outcome.cat.reorder_categories(['paid off', 'default'])
loan_data.purpose_ = loan_data.purpose_.astype('category')
loan_data.home_ = loan_data.home_.astype('category')
loan_data.emp_len_ = loan_data.emp_len_.astype('category')

predictors = ['purpose_', 'home_', 'emp_len_']
outcome = 'outcome'
X = pd.get_dummies(loan_data[predictors], prefix='', prefix_sep='')
y = loan_data[outcome]

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.4)

print(X_train)
print(Y_train)

bayes_model = bayesian.model_bayes(X_train, X_test, Y_train, Y_test)
