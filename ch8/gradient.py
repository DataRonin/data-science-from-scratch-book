# chapter 8 book

import linear_algebra_vectors, random
from typing import List, TypeVar, Iterator

# using a gradient

def gradient_step(v: list, gradient: list, step_size: float) -> list:
    assert len(v) == len(gradient)
    step = linear_algebra_vectors.scalar_multiply(step_size, gradient)
    return linear_algebra_vectors.add(v, step)

def sum_of_squares_gradient(v: list) -> list:
    return [2 * i for i in v]

v = [random.uniform(-10,10) for i in range(3)]

for epoch in range(1001):
    grad = sum_of_squares_gradient(v)
    v = gradient_step(v, grad, -0.01)
    print(f'Epoch: {epoch} | Result - {v}')
assert linear_algebra_vectors.distance(v,[0,0,0]) < 0.001

print('---')

# using gradient descent to fit models

inputs = [(x, x * 20 + 5) for x in range(-50,50)]
def linear_gradient(x: float, y: float, theta: list) -> list:
    slope, intercept = theta
    predicted = slope * x + intercept
    error = predicted - y
    grad = [2*error * x, 2 * error]
    return grad

theta = [random.uniform(-1,1), random.uniform(-1,1)]
learning_rate = 0.001
for epoch in range(5001):
    grad = linear_algebra_vectors.vector_mean([linear_gradient(x,y,theta) for x, y in inputs])
    theta = gradient_step(theta,grad,-learning_rate)
    print(f'Epoch: {epoch} | Result - {theta}')
slope, intercept = theta
assert 19.9 < slope < 20.1
assert 4.9 < intercept < 5.1

print('---')

# minibatch gradient

T = TypeVar('T')
def minibatches(dataset: List[T], batch_size: int, shuffle: bool = True) -> Iterator[List[T]]:
    batch_starts = [start for start in range(0, len(dataset), batch_size)]
    if shuffle: random.shuffle(batch_starts)
    for start in batch_starts:
        end = start + batch_size
        yield dataset[start:end]
theta = [random.uniform(-1,1), random.uniform(-1,1)]
for epoch in range(1001):
    for batch in minibatches(inputs, batch_size=20):
        grad = linear_algebra_vectors.vector_mean([linear_gradient(x, y, theta) for x, y in batch])
        theta = gradient_step(theta, grad, -learning_rate)
    print(f'Epoch: {epoch} | Result - {theta}')
slope, intercept = theta
assert 19.9 < slope < 20.1
assert 4.9 < intercept < 5.1 

print('---')

# stochastic gradient

theta = [random.uniform(-1,1), random.uniform(-1,1)]

for epoch in range(101):
    for x, y in inputs:
        grad = linear_gradient(x, y, theta)
        theta = gradient_step(theta, grad, -learning_rate)
        print(f'Epoch: {epoch} | Result - {theta}')

slope, intercept = theta
assert 19.9 < slope < 20.1
assert 4.9 < intercept < 5.1
