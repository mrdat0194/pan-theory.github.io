from helper_functions import plotter, plotter_discrete, plotter_histogram, loadData, get_column
from Epilepsy_model import *
import matplotlib.pyplot as plt
from Bayesian import DATA_DIR
import os


def main():
    data_path = os.path.join(DATA_DIR,"conjugate_epil.csv")
    data_path = (data_path)

    epilepsy_data = loadData(data_path)

    epilepsy_counts = get_column(epilepsy_data["x"])
    # print(epilepsy_counts)
    a = 4
    b = 0.25

    eilepsy_model = Epilepsy_model(a, b)

    """ Q 9.2.3 The Gamma Posterior """
    posterior, theta_range = eilepsy_model.posterior_gamma(epilepsy_counts)

    plotter(theta_range, posterior, "Gamma(a + " +r'$\sum^n_{i=1}(x_i)$'+", b + n) posterior over " + r'$\theta$', r'$\theta$', "pdf")


    """ Q 9.2.5 The Gamma Posterior Predictive distribution """
    posterior_NB, theta_range = eilepsy_model.posterior_predictive_gamma(epilepsy_counts)

    plotter(theta_range, posterior_NB, "Gamma(a + " +r'$\sum^n_{i=1}(x_i)$'+", b + n) posterior over " + r'$\theta$', r'$\theta$', "pdf")

if __name__ == '__main__':
    main()
