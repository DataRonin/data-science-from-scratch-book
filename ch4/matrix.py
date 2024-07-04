# matrix, chapter 4

matrix = [[1,2,3],
     [4,5,6],
     [7,8,9]]

def shape(m: list) -> tuple:
    # m = matrix
    rows = len(m)
    columns = len(m[0]) if m else 0
    return (rows, columns)
assert shape(matrix) == (3,3)
# matrix 3x3

def get_row(m: list, i: int) -> list:
    # m = matrix
    # i = index
    # list = vector
    return m[i-1]
assert get_row(matrix,3) == [7,8,9]

def get_column(m: list, i: int) -> list:
    # m = matrix
    # i = index
    # list = vector
    return [el[i-1] for el in m]
assert get_column(matrix,3) == [3,6,9] 

friend_matrix = [[0,1,1,0,0], # user-1
                 [1,0,0,1,0], # user-2
                 [0,0,0,0,0], # user-3
                 [1,1,1,0,0], # user-4
                 [1,0,0,0,0]] # user-5
#user-1 and user-2 friens? - Yes
assert friend_matrix[0][1] == 1 # not error, because user-1 and user-2 - friends
# user-3 and aser-5 frends? - No
assert friend_matrix[2][4] == 0 # not error, because user-3 and user-5 - not friends
