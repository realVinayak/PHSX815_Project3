from data_generator import generate_data
from predict_rate_parameter import predict_rate_parameter
from plot_pred_parameters import generate_plots

N_meas = 8
N_experiments = 1000
rate_parameter = 1 / 2.6
X_MIN = 0
X_MAX = 8


def main():
    generate_data(N_meas, N_experiments)
    predict_rate_parameter()
    generate_plots()


if __name__ == '__main__':
    main()
