from collections import Counter
def mean(l: list) -> float:
    return sum(l) / len(l)
assert mean([1,2,3,4,5]) == 3


def _median_odd(l: list) -> float:
    l = sorted(l)
    return l[len(l)//2]
def _median_even(l: list) -> list:
    l = sorted(l)
    mid = len(l) // 2
    return (l[mid-1]+l[mid])/2
def median(l: list) -> list:
    return _median_even(l) if len(l)%2 == 0 else _median_odd(l)
assert median([1,10,2,9,5]) == 5 
assert median([1,9,2,10]) == (2+9)/2


def quatile(l: list, p: float) -> float:
    l = sorted(l)
    index = int(len(l)*p)
    return l[index]
list_nums = [0,1,2,3,4,5,6,7,8,9,10]
assert quatile(list_nums, 0.1) == 1
assert quatile(list_nums,0.5) == 5
assert quatile(list_nums,0.7) == 7
assert quatile(list_nums,0.9) == 9

def mode(l: list) -> list:
    count = Counter(l)
    max_count = max(count.values())
    return [x_i for x_i, count in count.items() if count == max_count]
test_mode = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,8]
'''
1-1
2-2
3-3
4-4
5-5
6-6
7-7
8-8
9-9
8-8+1=9
8-9
mode(test_mode) = [8,9]
'''
assert mode(test_mode) == [8,9]
