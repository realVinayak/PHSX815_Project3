import matplotlib.pyplot as plt
import numpy as np
import math
from file_list_utils import read_list
from utils import get_meaned_interval, expectation_mid_prob, variance_mid_prob


def generate_plots():
    from driver import N_meas, X_MIN, X_MAX
    predicted_rates = read_list('./outputs/predicted_rate_parameters.txt')
    hist_prob, hist_bins = np.histogram(predicted_rates, range=(X_MIN, X_MAX),
                                        bins=300, density=True)
    x_bins = get_meaned_interval(hist_bins)
    expectation = expectation_mid_prob(x_bins, hist_prob)
    std_dev = round(math.sqrt(variance_mid_prob(x_bins, hist_prob)), 3)
    print('Expected Value of Rate Parameter: ', expectation)
    print('Standard Deviation: ', std_dev)
    plt.vlines(expectation, 0,
               max(hist_prob) * 1.2,
               color='black', linewidth=1)
    plt.plot(x_bins, hist_prob, 'r', linewidth=0.9,
             alpha=1)
    plt.xlabel('Maximum Likelihood Estimate \u03BB\u0302')
    plt.ylabel('P(\u03BB\u0302)')
    plt.legend([f'Expectation of \u03BB\u0302 = {round(expectation, 3)}'])
    plt.text(5, max(hist_prob), f'Standard Deviation: {std_dev}')
    plt.savefig(f'./outputs/predicted_rate_parameter_{N_meas}.png')
    plt.plot()
    plt.show()


if __name__ == '__main__':
    generate_plots()
