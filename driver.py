import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from utils import get_containing_interval_index, get_meaned_interval

N_meas = 1
N_experiments = 30000
measured_mean_min = 0.5
measured_mean_max = 1.8
measured_mean_num = 3


def derive_neyman():
    x_data = []
    y_data = []
    for param in np.linspace(1, 1.5, 100):
        raw_values = np.random.exponential(param, size=(N_experiments, N_meas))
        values_per_experiment = np.sum(raw_values, 1) * (1 / N_meas)
        x_data = x_data + [param for _ in range(N_experiments)]
        y_data = y_data + list(values_per_experiment)

    packed_data = plt.hist2d(x_data, y_data, bins=100,
                             norm=mcolors.PowerNorm(0.4), density=True)
    hist2d_data = packed_data[0]
    xedges = packed_data[1]
    yedges = packed_data[2]
    for measured_mean in np.linspace(measured_mean_min, measured_mean_max,
                                     measured_mean_num):
        measured_mean_bin_index = get_containing_interval_index(yedges,
                                                                measured_mean)
        plt.clf()
        x_data_meaned = get_meaned_interval(xedges)
        y_plot_data = hist2d_data[measured_mean_bin_index]
        y_sum = sum(y_plot_data)
        plt.plot(x_data_meaned, y_plot_data/y_sum)
        plt.xlabel('true rate parameter')
        plt.savefig(f"./outputs/{measured_mean}-measured_mean-N-{N_meas}.png")
    plt.hist2d(x_data, y_data, bins=100, norm=mcolors.PowerNorm(0.4),
               density=True)
    plt.xlabel('true rate parameter')
    plt.ylabel('estimated mean')
    plt.savefig('neyman_construction.png')


if __name__ == '__main__':
    derive_neyman()
