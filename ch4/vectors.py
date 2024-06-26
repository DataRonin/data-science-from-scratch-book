from math import sqrt

def add(v: list, w: list) -> list:
    assert len(v) == len(w)
    return [v_i + w_i for v_i, w_i in zip(v,w)]
assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]

def substract(v: list, w: list) -> list:
    assert len(v) == len(w)
    return [v_i - w_i for v_i, w_i in zip(v,w)]
assert substract([5,6,7],[1,2,3]) == [4,4,4]

def vector_sum(v: list) -> list:
    assert v

    num_elements = len(v[0])
    assert all(len(v) == num_elements for v in v)

    return [sum(v[i] for v in v) for i in range(num_elements)]
assert vector_sum([[1,2],[4,5],[6,7],[8,9]]) == [19,23]

def scalar_multiply(c: float, v: list) -> list:
    return [c*v for v in v]
assert scalar_multiply(5,[5,3,1]) == [25,15,5]

def vector_mean(v: list) -> list:
    n = len(v)
    return scalar_multiply(1/n,vector_sum(v))
assert vector_mean([[1,2],[3,4],[5,6]]) == [3,4]

def dot(v: list, w:list) -> float:
    assert len(v) == len(w)
    return sum(v_i * w_i for v_i,w_i in zip(v,w))
assert dot([1,3,5],[4,6,7]) ==  57 #1*4 + 3*6 + 5*7 = 4+18+35=22+35=37+20=57

def sum_of_squares(v: list) -> float:
    return dot(v,v)
assert sum_of_squares([1,2,3]) == 14 #1*1+2*2+3*3 = 1+4+9=13+1=14

def magnitude(v: list) -> float:
    return sqrt(sum_of_squares(v))
assert magnitude([3,4]) == 5 #3*3+4*4=9+16=25 / sqrt(25) = 5 !!!!!!!!!!!!!!!1

def square_distance(v: list, w: list) -> list:
    return sum_of_squares(substract(v,w))
assert square_distance([5,4],[2,1]) == 18 #sqrt(18)^2=18

def distance(v: list, w: list) -> list:
    return sqrt(square_distance(v,w))
assert distance([5,4],[2,1]) == sqrt(18)

def distance_upgrade(v: list,w: list) -> list:
    return magnitude(substract(v,w))
assert distance_upgrade([5,4],[2,1]) == sqrt(18) #5-2=3 / 4-1=3 -> sqrt(3*3+3*3=9+9=18) = sqrt(18) 
