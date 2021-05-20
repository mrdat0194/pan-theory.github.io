import pandas as pd
from helper_functions import plotter
import numpy as np

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy import stats
import pymc3
from Bayesian import DATA_DIR
import os
import statsmodels.api as sm


def loadData(data_path):

    data_frame = pd.read_csv(data_path)

    return data_frame


def get_column(data_column):

    data_values = data_column.values.reshape(-1)

    return data_values


def remove_missing_data(gdp_data, mortality_data):

    gdps = []
    mortalities = []
    for i in range(len(gdp_data)):
        if str(gdp_data[i]) != "nan":
            if str(mortality_data[i]) != "nan":
                gdps.append(gdp_data[i])
                mortalities.append(mortality_data[i])

    return gdps, mortalities


def fit_normal_dist_model(gdps, mortalities):

    regressor = LinearRegression()

    regressor.fit(np.log(np.array(gdps).reshape(-1, 1)),
                  np.log(np.array(mortalities).reshape(-1, 1)))  # training the algorithm

    # To retrieve the intercept:
    intercept = regressor.intercept_[0]
    print("Regression intercept ", intercept)

    # For retrieving the slope:
    slope = regressor.coef_[0][0]
    print("Regression coeficient ", slope)

    gdp_log_lower = 2.5
    gdp_log_upper = 11

    gdp_log_range = np.arange(gdp_log_lower, gdp_log_upper, 0.5)
    mortality_log_values = [gdp * slope + intercept for gdp in gdp_log_range]

    return gdp_log_range, mortality_log_values, intercept, slope


def calculate_standard_deviation(values):

    standard_error = np.std(values)

    return standard_error


def calculate_degrees_of_freedom(values):

    n = len(values)
    dof = n - 1

    return dof

"""
This code was taken form the PyMC library https://github.com/pymc-devs/pymc
"""

import numpy as np

def calc_min_interval(x, alpha):
    """Internal method to determine the minimum interval of a given width
    Assumes that x is sorted numpy array.
    """

    n = len(x)
    cred_mass = 1.0-alpha

    interval_idx_inc = int(np.floor(cred_mass*n))
    n_intervals = n - interval_idx_inc
    interval_width = x[interval_idx_inc:] - x[:n_intervals]

    if len(interval_width) == 0:
        raise ValueError('Too few elements for interval calculation')

    min_idx = np.argmin(interval_width)
    hdi_min = x[min_idx]
    hdi_max = x[min_idx+interval_idx_inc]
    return hdi_min, hdi_max


def hpd(x, alpha=0.05):
    """Calculate highest posterior density (HPD) of array for given alpha.
    The HPD is the minimum width Bayesian credible interval (BCI).
    :Arguments:
        x : Numpy array
        An array containing MCMC samples
        alpha : float
        Desired probability of type I error (defaults to 0.05)
    """

    # Make a copy of trace
    x = x.copy()
    # For multivariate node
    if x.ndim > 1:
        # Transpose first, then sort
        tx = np.transpose(x, list(range(x.ndim))[1:]+[0])
        dims = np.shape(tx)
        # Container list for intervals
        intervals = np.resize(0.0, dims[:-1]+(2,))
        # print(dims[:-1])
        for index in make_indices(dims[:-1]):
            try:
                index = tuple(index)
            except TypeError:
                pass

            # Sort trace
            sx = np.sort(tx[index])
            # Append to list
            intervals[index] = calc_min_interval(sx, alpha)
        # Transpose back before returning
        return np.array(intervals)
    else:
        # Sort univariate node
        sx = np.sort(x)
        return np.array(calc_min_interval(sx, alpha))


def main():
    """ Load and pre-process data. """
    data_path = os.path.join(DATA_DIR,"posterior_posteriorsGdpInfantMortality.csv")
    data_path = (data_path)

    GDP_data = loadData(data_path)

    alphas = get_column(GDP_data["alpha"])
    betas = get_column(GDP_data["beta"])
    sigmas = get_column(GDP_data["sigma"])

    dof = calculate_degrees_of_freedom(alphas)

    std_alpha = calculate_standard_deviation(alphas)
    std_beta = calculate_standard_deviation(betas)
    std_sigma = calculate_standard_deviation(sigmas)

    print("No. Degrees of Freedom: ", dof)
    print()
    print("Standard Deviations ")
    print("alpha: ", std_alpha)
    print("beta: ", std_beta)
    print("sigma: ", std_sigma)

    print()
    """ Credible intervals of 80 % around the highest density regions. """
    print("Credible intervals of 80 % around the highest density regions")
    # print("alpha: ", pymc3.data.hpd(alphas, alpha=0.2))
    # print("beta: ", pymc3.data.hpd(betas, alpha=0.2))
    # print("sigma: ", pymc3.data.hpd(sigmas, alpha=0.2))
    print("alpha: ", hpd(alphas, alpha=0.2))
    print("beta: ", hpd(betas, alpha=0.2))
    print("sigma: ", hpd(sigmas, alpha=0.2))

    print()
    """ For comparison of the frequentist sigma value a point estimate of the
    sigma value is calculated. """
    print("Posterior mean of sigma ", np.mean(sigmas))

if __name__ == '__main__':
    main()
