import numpy as np
from file_list_utils import write_multi_list

def generate_data(n_meas, n_experiments):
    from driver import rate_parameter
    raw_data = np.random.exponential(rate_parameter, (n_experiments, n_meas))
    write_multi_list(raw_data, f'./outputs/raw_exponential.txt')


if __name__ == '__main__':
    from driver import N_experiments, N_meas
    generate_data(N_meas, N_experiments)
