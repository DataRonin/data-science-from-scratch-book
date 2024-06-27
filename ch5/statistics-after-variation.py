import statistics_book, vectors # past chapters
import math
def data_range(l: list) -> float:
    return (max(l) - min(l))
assert data_range([1,2,3,4,5]) == 4 # 5-1 =4

def de_mean(l: list) -> list:
    x_mid = statistics_book.mean(l)
    return [x - x_mid for x in l]
assert de_mean([1,2,3,4,5]) == [-2,-1,0,1,2]
def variance(l: list) -> float:
    n = len(l) - 1
    deviations = de_mean(l)
    return vectors.sum_of_squares(deviations) / n # n = len(l) - 1
assert variance([1,2,3,4,5]) == 10/4 # n = 5 - 1 = 4 | deviations = [-2,-1,0,1,2] | sum_of_sq(deviations) = -2*-2 + -1*-1 + 0*0 + 1*1 + 2*2 = 4 + 1 + 0 + 1 + 4 = 5 + 5 = 10 | 10 / n = 10/4

def standart_deviation(l: list) -> float:
    return math.sqrt(variance(l))
assert standart_deviation([1,2,3,4,5]) == math.sqrt(10/4)

def interquatile_range(l: list) -> float:
    return (statistics_book.quatile(l, 0.75) - statistics_book.quatile(l, 0.25))
assert interquatile_range(range(0,101)) == 50 # list = [1,2,3,4,5 .... 99,100] -> 0.75 = 75, 0.25 = 25 -> 75 - 25 = 50

#----

#correlation
def covariance(l: list, l1: list) -> float:
    assert len(l) == len(l1)
    return vectors.dot(de_mean(l),de_mean(l1))/(len(l)-1)
assert covariance([1,2,3],[4,5,6]) == 1 # de_mean(l)=[-1,0,1] de_mean(l1)=[-1,0,1] = -1*-1, 0*0, 1*1 = 1+0+1=2 | 2/2 (len([1,2,3]) = 3 | 3-1=2)

def correlation(l: list, l1: list) -> float:
    st_x = standart_deviation(l)
    st_y = standart_deviation(l1)
    return covariance(l,l1) if (st_x > 0 and st_y > 0) else 0
assert correlation([1,2,3],[4,5,6]) ==  1 # l=[-1,0,1] | l1=[-1,0,1] | 1+0+1 = 2 / 2
