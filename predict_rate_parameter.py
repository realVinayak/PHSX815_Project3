from scipy.optimize import minimize
from file_list_utils import read_multi_list, write_list
import numpy as np
import math


def generate_negative_log_likelihood_get(measured_data):
    def get_negative_log_likelihood(param):
        if param <= 0:
            return math.inf
        n = len(measured_data)
        x_sum = sum(measured_data)
        return -(n * math.log(param)) + (param * x_sum)

    return get_negative_log_likelihood


def generate_one_sigma_interval(max_likelihood_estimate, negative_ll_func):
    step_size = 0.01
    start_estimate = max_likelihood_estimate
    while negative_ll_func(start_estimate) - negative_ll_func(
            max_likelihood_estimate) < 0.5:
        start_estimate += step_size
    upper_bound = start_estimate
    start_estimate = max_likelihood_estimate
    while negative_ll_func(start_estimate) - negative_ll_func(
            max_likelihood_estimate) < 0.5:
        start_estimate -= step_size
    lower_bound = start_estimate
    return lower_bound, upper_bound


def predict_rate_parameter():
    raw_exponential_data = read_multi_list('./outputs/raw_exponential.txt')
    predicted_rate_parameters = []
    counter = 1
    for raw_exponential_measurements in raw_exponential_data:
        func_to_minimize = generate_negative_log_likelihood_get(
            raw_exponential_measurements)
        minimize_result = minimize(func_to_minimize,
                                   np.asarray(np.random.random() + 0.02))
        lower_b, upper_b = generate_one_sigma_interval(minimize_result.x[0],
                                                       func_to_minimize)
        predicted_rate_parameters.append(minimize_result.x[0])
        print(f'Results for Experiment #{counter}')
        print(f'Predicted Rate Parameter: {minimize_result.x[0]}')
        print(f'Lower Bound: {lower_b}')
        print(f'Upper Bound: {upper_b}')
        print('############################################\n\n')
        counter += 1

    write_list(predicted_rate_parameters,
               './outputs/predicted_rate_parameters.txt')


if __name__ == '__main__':
    predict_rate_parameter()
