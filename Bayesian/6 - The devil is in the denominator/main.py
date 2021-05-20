import pandas as pd
from negative_binomial_model import compute_likelihood
from helper_functions import plotter
import numpy as np
from Bayesian import DATA_DIR
import os

def loadData(data_path):

    data_frame = pd.read_csv(data_path)

    return data_frame


def reshape_data(data_column):

    data_values = data_column.values.reshape(-1)

    return data_values

def convert_str_to_int(string_list):

    int_list = [ int(x) for x in string_list ]

    return int_list


def main():
    """ Load and pre-process data. """
    data_path = os.path.join(DATA_DIR,"denominator_NBCoins.csv")
    data_path = (data_path)
    crime_dataframe = loadData(data_path)

    failuers_before_five_successes =  convert_str_to_int(reshape_data(crime_dataframe["No failuers before 5 successes"]))

    theta1_range = np.arange(0.001, 0.999, 0.01)
    theta2_range = np.arange(0.001, 0.999, 0.01)

    """ Compute the likelihood over the theta_1 and theta_2 ranges. """
    likelihoods = compute_likelihood(failuers_before_five_successes, theta1_range, theta2_range)

    """ Create a contour plot over the rwo theta values."""
    plotter(theta1_range, theta2_range, likelihoods, r'The posterior shape over $\theta_1$ and $\theta_2$ for the Negative Binomial likelihood', r"$\theta_1$", r"$\theta_2$")


if __name__ == '__main__':
    main()
