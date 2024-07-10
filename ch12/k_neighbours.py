# chapter 12 from book - k neighbours

from collections import Counter

def raw_majority_vote(labels: list) -> str:
    votes = Counter(labels)
    winner, _ = votes.most_common(1)[0]
    return winner
assert raw_majority_vote(['a','b','c','b']) == 'b' # {a:1, b:2, c:1}

def majority_vote(labels: list) -> str:
    vote_counts = Counter(labels)
    winner, winner_count = vote_counts.most_common(1)[0]
    num_winners = len([count for count in vote_counts.values() if count == winner_count])
    if num_winners == 1:
        return winner
    else:
        return majority_vote(labels[:-1])
assert majority_vote(['a','b','c','b','a']) == 'b' # {a:2, b:2, c:1}

from typing import NamedTuple
from linear_algebra_vectors import distance

class LabeledPoint(NamedTuple):
    point: list # vector
    label: str 

def knn_classify(k: int, labeled_points: list, new_point: list) -> str:
    by_distance = sorted(labeled_points, key = lambda lp: distance(lp.point, new_point))
    k_nearest_labels = [lp.label for lp in by_distance[:k]]
    return majority_vote(k_nearest_labels)

# iris
# file - iris.data | link - https://archive.ics.uci.edu/dataset/53/iris

from typing import Dict
import csv
from collections import defaultdict

def parse_iris_row(row: list) -> LabeledPoint:
    measurements = [float(value) for value in row[:-1]]
    label = row[-1].split('-')[-1]
    return LabeledPoint(measurements,label)

with open('iris.data') as f:
    reader = csv.reader(f)
    iris_data = [parse_iris_row(row) for row in reader if len(row)>0]

points_by_species: Dict[str,list] = defaultdict(list)

for iris in iris_data:
    points_by_species[iris.label].append(iris.point)

import random
import ml

random.seed(12)
iris_train, iris_test = ml.split_data(iris_data, 0.7)

assert len(iris_train) == 0.7 * 150
assert len(iris_test) == 0.3 * 150

from typing import Tuple

confusion_matrix: Dict[Tuple[str,str], int] = defaultdict(int)
num_correct = 0 

for iris in iris_data:

    predicted = knn_classify(5,iris_train,iris.point)
    actual = iris.label

    if predicted == actual:
        num_correct+=1

pct_correct = num_correct / len(iris_test)

print(pct_correct, confusion_matrix)
