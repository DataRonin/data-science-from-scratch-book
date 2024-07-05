# 5 chapter of the book

from random import shuffle
from collections import Counter
import linear_algebra_vectors
import math 

l = list(range(101))
shuffle(l)

# not sorted list in range 0-100

def mean(l: list) -> float:
    return sum(l)/len(l)
assert mean(l) == 50

def _median_odd(l: list) -> float:
    return sorted(l)[len(l) // 2]
def _median_even(l: list) -> float:
    mid = len(l) // 2
    sorted_list = sorted(l)
    return (sorted_list[mid-1] + sorted_list[mid]) / 2
def median(l: list) -> float:
    return _median_odd(l) if len(l)%2==1 else _median_even(l)
assert median(l) == 50
assert median([1,2,3,4,5,6]) == 3.5 # l[3] = 4 | l[2] = 3 | 3 + 4 = 7 | 7 / 2 = 3.5

def quantile(l: list, q: float) -> float:
    index = int(len(l) * q)
    return sorted(l)[index]
assert quantile(l, 0.5) == 50
assert quantile(l, 0.45) == 45

def mode(l: list) -> list:
    counts = Counter(l)
    max_count = max(counts.values())
    return [x for x, count in counts.items() if count == max_count]
assert set(mode([1,1,1,1,1,4,4,4,4,4,5,3,2,7,8,9])) == {1,4}

def data_range(l: list) -> float:
    return max(l) - min(l)
assert data_range(l) == 100 # 100 - 0 = 100 

def de_mean(l: list) -> list:
    mid = mean(l)
    return [x-mid for x in l]
assert de_mean([1,2,3,4,5]) == [-2,-1,0,1,2]

def variance(l: list) -> float:
    assert len(l) >= 2
    n = len(l)
    deviations = de_mean(l)
    return linear_algebra_vectors.sum_of_squares(deviations) / (n - 1)
assert variance([1,2,3,4,5]) == 10/4 # deviations = [-2,-1,0,1,2] -> 4+1+0+1+4 = 8+2= 10 / 4
assert variance(l) == 858.5

def standart_deviation(l: list) -> float:
    return math.sqrt(variance(l))
assert standart_deviation([1,2,3,4,5]) == math.sqrt(10/4)
assert standart_deviation(l) == math.sqrt(858.5)

def interquartile_range(l: list) -> float:
    return quantile(l, 0.75) - quantile(l, 0.25)
assert interquartile_range(l) == 50 # 75 - 25 = 50

def covariance(l1: list, l2: list) -> float:
    assert len(l1) == len(l2)
    return linear_algebra_vectors.dot(de_mean(l1),de_mean(l2)) / (len(l1) - 1) # len(l1) == len(l2)
assert covariance([1,2,3,4,5],[1,2,3,4,5]) == 10/4 # [-2,-1,0,1,2] = 4 + 4 + 2 = 10 / 4

def correlation(l1: list, l2: list) -> float:
    stdev_l1 = standart_deviation(l1)
    stdev_l2 = standart_deviation(l2)
    if stdev_l1 > 0 and stdev_l2 > 0:
        return covariance(l1,l2) / stdev_l1 / stdev_l2
    else: 
        return 0 # if variation = 0 => correlation = 0
assert correlation([1,2,3,4,5],[1,2,3,4,5]) == (10/4) / math.sqrt(10 / 4) / math.sqrt(10 / 4) # stdevs = sqrt(10/4) | (10/4)/sqrt(10/4)/sqrt(10/4)
