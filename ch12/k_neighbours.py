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
# I'll add the code tomorrow
