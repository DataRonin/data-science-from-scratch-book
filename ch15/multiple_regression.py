import linear_algebra_vectors

def predict(x: list, beta: list) -> float:
    return linear_algebra_vectors.dot(x,beta)

def error(x: list, y: list, beta: list) -> float:
    return predict(x,beta) - y

def squared_error(x: list, y: list, beta: list) -> float:
    return error(x,y,beta) ** 2

x = [1,2,3]
y = 30
beta = [4,4,4]

assert predict(x,beta) == 24 # 1 * 4 + 2 * 4 + 3 * 4 = 4 + 8 + 12 = 24
assert error(x,y,beta) == -6 # 24 - 30 = -6
assert squared_error(x,y,beta) == 36 # 6 * 6 = 36

def sqerror_gradient(x: list, y: list, beta: list) -> list:
    err = error(x,y,beta)
    return [2 * err * x_i for x_i in x]

assert sqerror_gradient(x,y,beta) == [-12, -24, -36] # err = -6 | 2 * -6 * x_i for x_i in x | [-12 * 1, -12 * 2, -12 * 3] = [-12,-24,-36]

import random, tqdm, gradient_descent

def least_squares_fit(xs: list, ys: list, learning_rate: float = 0.001, num_steps: int = 1000, batch_size: int = 1) -> list:
    guess = [random.random() for _ in xs[0]]
    for _ in tqdm.trange(num_steps, desc='least squares fir'):
        for start in range(0,len(xs),batch_size):
            batch_xs = xs[start:start+batch_size]
            batch_ys = ys[start:start+batch_size]

            gradient = linear_algebra_vectors.vector_mean([sqerror_gradient(x,y,guess) for x,y in zip(batch_xs,batch_ys)])
            guess = gradient_descent.gradient_step(guess,gradient,-learning_rate)
    return guess

from simple_linear_regression import total_sum_of_squares

def multiple_r_squared(xs: list, ys: list, beta: list) -> float:
    sum_of_squared_errors = sum(error(x,y,beta) ** 2 for x,y in zip(xs, ys))
    return 1.0 - sum_of_squared_errors / total_sum_of_squares(ys)

def bootstrap_sample(data: list) -> list:
    return [random.choice(data) for _ in data]

def bootstrap_statistic(data: list, stats_fn, num_samples: int) -> list:
    return [stats_fn(bootstrap_sample(data)) for _ in range(num_samples)] 

close_to_100 = [99.5 + random.random() for _ in range(101)]
far_from_100 = ([99.5 + random.random()] + [random.random() for _ in range(50)] + [200 + random.random() for _ in range(50)])
from statistics_from_book import median, standart_deviation

medians_close = bootstrap_statistic(close_to_100, median, 100)
medians_far = bootstrap_statistic(far_from_100, median, 100)

assert standart_deviation(medians_close) < 1
assert standart_deviation(medians_far) > 90

import datetime

def estimate_sample_beta(pairs: list):
    x_sample = [x for x, _ in pairs]
    y_sample = [y for _, y in pairs]
    beta = least_squares_fit(x_sample,y_sample, 0.001, 5000,25)
    print(beta)
    return beta

def ridge_penalty(beta: list, alpha: float) -> float:
    return alpha * linear_algebra_vectors.dot(beta[1:],beta[1:])

def squared_error_ridge(x: list, y: list, beta: list, alpha: list) -> float:
    return error(x,y,beta) ** 2  + ridge_penalty(beta,alpha)

def ridge_penalty_gradient(beta: list, alpha: float) -> list:
    return [0.] + [2 * alpha * beta_j for beta_j in beta[1:]]

def sqerror_ridge_gradient(x: list, y: float, beta: float, alpha: float) -> list:
    return linear_algebra_vectors.add(sqerror_gradient(x,y,beta), ridge_penalty_gradient(beta,alpha))

def lasso_penalty(beta, alpha):
    return alpha * sum(abs(beta_i) for beta_i in beta[1:])
