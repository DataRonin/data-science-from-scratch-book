import math

def logistic(x: float) -> float:
    return 1.0 / (1 + math.exp(-x))

def logistic_prime(x: float) -> float:
    return logistic(x) * (1 - logistic(x))

import linear_algebra_vectors
def _negative_log_likelihood(x: list, y: float, beta: list) -> float:
    if y==1:
        return -math.log(logistic(linear_algebra_vectors.dot(x, beta)))
    else:
        return -math.log(1.0 - logistic(linear_algebra_vectors.dot(x,beta)))

def negative_log_likelihood(xs: list, ys: list, beta: list) -> float:
    return sum(_negative_log_likelihood(x,y,beta) for x, y in zip(xs,ys))

def _negative_log_partial_j(x: list, y: float, beta: list, j: int) -> float:
    return -(y - logistic(linear_algebra_vectors.dot(x,beta))) * x[j]

def _negative_log_gradient(x: list, y: float, beta: list) -> list:
    return [_negative_log_partial_j(x,y,beta,j) for j in range(len(beta))]

def negative_log_gradient(xs: list, ys: list, beta:  list) -> list:
    return linear_algebra_vectors.vector_sum([_negative_log_gradient(x,y,beta) for x, y in zip(xs,ys)])
