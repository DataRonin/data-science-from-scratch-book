# chapter 11 - machine learning

import random

def split_data(data: list, prob: float) -> tuple: # data - list with 1000 elements
    data = data[:]
    random.shuffle(data)
    cut = int(len(data) * prob) # prob = 0.75 -> 1000 * 0.75 = 750
    return data[:cut], data[cut:] # len(data[:750]) = 750, len(data[750:]) = 250

data = [n for n in range(1000)]
train, test = split_data(data, 0.75)

assert len(train) == 750
assert len(test) == 250
assert sorted(train + test) == data
assert len(train + test) == len(data)

def train_test_split(xs: list, ys: list, test_pct: float) -> tuple:
    idxs = [i for i in range(len(xs))]
    train_idxs, test_idxs = split_data(idxs, 1 - test_pct)
    return (
        [xs[i] for i in train_idxs], # train x_train
        [xs[i] for i in test_idxs], # test x_test
        [ys[i] for i in train_idxs], # train y_train
        [ys[i] for i in test_idxs] # test t_test
    )

xs = [x for x in range(1000)]
ys = [2 * x for x in xs]
x_train, x_test, y_train, y_test = train_test_split(xs, ys, 0.25)

assert len(x_train) == 750
assert len(x_test) == 250
assert all(y == 2 * x for x, y in zip(x_train,y_train))
assert all(y == 2 * x for x, y in zip(x_test,y_test))

# ---

def accuracy(tp: int, fp: int, fn: int, tn: int) -> float:
    correct = tp + tn
    total = sum([tp,fp,fn,tn])
    return correct / total
assert accuracy(70,4930,13930,981070) == 0.98114
# this method is not suitable, although it shows impressive results, it is obviously unusable

def precision(tp:int, fp: int, fn: int, tn: int) -> float:
    return tp / (tp+fp)
assert precision(70,4930,13930,981070) == 0.014

def recall(tp: int, fp: int, fn: int, tn: int) -> float:
    return tp / (tp + fn)
assert recall(70,4930,13930,981070) == 0.005 

# the results are terrible - the model is terrible

def f1_score(tp: int,fp: int,fn: int,tn: int) -> float:
    p = precision(tp,fp,fn,tn)
    r = recall(tp,fp,fn,tn)

    return 2 * p * r / (p + r)
assert f1_score(70,4930,13930,981030) == 0.00736842105263158
