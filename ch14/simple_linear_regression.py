def predict(alpha: float, beta: float, x_i: float) -> float:
    return beta * x_i + alpha

def error(alpha: float, beta: float, x_i: float, y_i: float) -> float:
    return predict(alpha,beta,x_i) - y_i

def sum_of_sqerrors(alpha: float, beta: float, x: list, y: list) -> float:
    return sum(error(alpha,beta,x_i,y_i) ** 2 for x_i, y_i in zip(x,y))

from statistics_from_book import correlation, standart_deviation, mean, de_mean

def least_squares_fit(x: list, y: list) -> tuple:
    beta = correlation(x,y) * standart_deviation(y) / standart_deviation(x)
    alpha = mean(y) - beta * mean(x)
    return alpha, beta

x = [i for i in range(-100,110,10)]
y = [x_i * 3 - 5 for x_i in x]

assert least_squares_fit(x,y) == (-5,3)

def total_sum_of_squares(y: list) -> float:
    return sum(y_i ** 2 for y_i in y)

def r_squared(alpha: float, beta: float, x: list, y: list) -> float:
    return 1.0 - (sum_of_sqerrors(alpha,beta,x,y) / total_sum_of_squares(y))
