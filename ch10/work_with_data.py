# using typed tuples
# chapter 10

import datetime as dt 
from collections import namedtuple
from typing import NamedTuple

prog = {'name': 'python', 'place': 2, 'using': 'DataScience'}
prog['placce'] = 3 # typo :(
print(f'Typo - {prog}\n---')

named_tuple_prog = namedtuple('prog', ['name','place','using'])
prog = named_tuple_prog('python',2,'DataScience')
assert prog.name == 'python'
assert prog.place == 2
assert prog.using == 'DataScience'
# The code editor helps you add and correct typos :)

del prog
class prog(NamedTuple):
    name: str
    place: int
    using: str

    def is_python(self):
        return self.name == 'python'

prog = prog('python',2,'DataScience')
assert prog.name == 'python'
assert prog.is_python
assert prog.place == 2
assert prog.using == 'DataScience'
# all good :)

# ---

# dataclasses

from dataclasses import dataclass

@dataclass
class prog2:
    name: str
    place: int
    using: str
    def is_python(self):
        return self.name == 'python'

prog = prog2('js',1,'web')
assert prog.name == 'js'
assert not prog.is_python()
assert prog.place == 1
assert prog.using == 'web'

# we can modify the values ​​of a data class instance

prog.place *= 2
assert prog.place == 2

# ---

# data management (some)

del prog, prog2

class prog(NamedTuple):
    name: str
    place: int
    using: str


data = [
        prog(name='js',place='1',using='web'),
        prog(name='python',place='2',using='data science'),
        prog(name='java',place='3',using='web'),
        prog(name='type script',place='3',using='web'),
        prog(name='c#',place='4',using='gamedev'),
        prog(name='c++',place='5',using='gamedev'),
        prog(name='python',place='2',using='ml'),
        prog(name='js',place='1',using='backend'),
        prog(name='js',place='1',using='frontend'),
        prog(name='python',place='2',using='ai')
        ]
using_py = [row.using for row in data if row.name == 'python']
print(f'using python: {using_py}\n---')

# ---

# scaling

'''

table: 10.1

face | height(inches) | height(cm) | weight(lbs)
1    | 63             | 160        | 150
2    | 67             | 170        | 160
3    | 70             | 177        | 171

'''

import linear_algebra_vectors 
a_to_b = linear_algebra_vectors.distance([63,150],[67,160])
b_to_c = linear_algebra_vectors.distance([67,160],[70,171])
a_to_c = linear_algebra_vectors.distance([63,150],[70,171])
print(a_to_b,b_to_c,a_to_c,sep='\n',end='\n\n')
# measured in inches - the nearest neighbor of b will be a

a_to_b= linear_algebra_vectors.distance([160,150],[170,160])
b_to_c= linear_algebra_vectors.distance([170,160],[177,171])
a_to_c= linear_algebra_vectors.distance([160,150],[177,171])
print(a_to_b,b_to_c,a_to_c,sep='\n')
# measure in centimeters the nearest neighbor b will be c
# ???

# using scaling

import statistics_from_book

def scale(data: list) -> tuple:
    dim = len(data[0])
    means = linear_algebra_vectors.vector_mean(data)
    stdevs = [statistics_from_book.standart_deviation([v[i] for v in data]) for i in range(dim)]
    return means, stdevs
vectors = [[-3,-1,1],[-1,0,1],[1,1,1]]
means, stdevs = scale(vectors)
assert means == [-1,0,1]
assert stdevs == [2,1,0]

def rescale(data: list) -> list:
    dim = len(data[0])
    means, stdevs = scale(data)
    rescaled = [v[:] for v in data]
    for v in rescaled:
        for i in range(dim):
            if stdevs[i] > 0:
                v[i] = (v[i] - means[i]) / stdevs[i]
    return rescaled
means, stdevs = scale(rescale(vectors))

assert means == [0,0,1]
assert stdevs == [1,1,0]
