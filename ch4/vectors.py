# vectors from chfpter-4

import math

def add(l1: list, l2: list) -> list:
    # (l1, l2 -> list) = vectors
    assert len(l1) == len(l2)
    return [x + y for x, y in zip(l1, l2)] # add([1,2,3],[4,5,6]) => return [1+4,2+5,6+3] => return [5,7,9] <- vector
assert add([1,2,3],[4,5,6]) == [5,7,9]

def substract(l1: list, l2: list) -> list:
    # (l1,l2 -> list) = vectors
    assert len(l1) == len(l2)
    return [x - y for x, y in zip(l1,l2)] # substract([4,5,6],[1,2,3]) => return [4-1,5-2,6-3] => return [3,3,3] <- vector
assert substract([4,5,6],[1,2,3]) == [3,3,3]

def vector_sum(l: list) -> list:
    # (l, list) = vectors
    assert l # if l is empty -> assert error | list not empty
    return [sum(v[i] for v in l) for i in range(len(l[0]))] # [[1,2],[3,4],[5,6]] -> [1+3+5,2+4+6] = [9,12]
assert vector_sum([[1,2],[3,4],[5,6]]) == [9,12]

def scalar_multiply(s: float = 1, l: list = [1,2,3]) -> list:
    # (list,list) = vectors
    #s - scalar
    # scalar_multiply(2,[1,2,3]) -> [2,4,6]
    # list is not empty
    return [s * v for v in l]
assert scalar_multiply() == [1,2,3] # [1*1,1*2,1*3] = [1,2,3]
assert scalar_multiply(2,[1,2,3]) == [2,4,6] # [2*1,2*2,2*3] = [2,4,6]

def vector_mean(l: list) -> list:
    # (l, list) = vectors
    # mean([1,2],[3,4],[5,6]) => return [3,4]
    assert l # list not empty
    return scalar_multiply(1 / len(l), vector_sum(l)) # vector_mean([1,2],[3,4],[5,6]) => len(l) = 3, vector_sum = [1+3+5,2+4+6] = [9,12] => [9,12] * 1/3 -> [9/3,12/3] = [3,4]
assert vector_mean([[1,2],[3,4],[5,6]]) == [3,4]

def dot(l1: list, l2: list) -> float:
    # (l1,l2) = vectors
    # float - result
    assert len(l1) == len(l2)
    return sum([x * y for x,y in zip(l1,l2)])
assert dot([1,2,3],[4,5,6]) == 32 # 1*4 + 2*5 + 6*3 = 4+10+18 = 28 + 4 = 32

def sum_of_squares(l: list) -> float:
    # l = vector
    # float = result dot(l,l)
    assert l
    return dot(l,l)
assert sum_of_squares([1,2,3]) == 14 # 1*1 + 2*2 + 3*3 = 1+ 4 + 9 = 13+1 = 14

def magnitude(l: list) -> float:
    assert l
    return math.sqrt(sum_of_squares(l))
assert magnitude([1,2,3]) == math.sqrt(14) # 1*1 + 2*2 + 3*3 = 14 | res = sqrt(14)

def squared_distance(l1: list, l2: list) -> float:
    assert len(l1) == len(l2) 
    return sum_of_squares(substract(l1,l2))
assert squared_distance([4,5,6],[1,2,3]) == 27 # 4-1, 5-2, 6-3 = [3,3,3] => 3*3+3*3+3*3 = 9 * 3 = 27

def distance(l1: list,l2: list) -> float:
    assert len(l1) == len(l2)
    return math.sqrt(squared_distance(l1,l2))
assert distance([4,5,6],[1,2,3]) == math.sqrt(27) 

def distance_from_magnitude(l1: list, l2: list) -> float:
    return magnitude(substract(l1,l2))
assert distance_from_magnitude([4,5,6],[1,2,3]) == math.sqrt(27) 
