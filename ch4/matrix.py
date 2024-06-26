matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

def get_columns_and_rows(matrix: list) -> tuple:
    rows = len(matrix)
    columns = len(matrix[0])
    return (columns, rows)
assert get_columns_and_rows(matrix) == (3,3) # true

def get_row(matrix: list, row: int) -> list:
    return matrix[row]
assert get_row(matrix, 1) == [4,5,6]

def get_column(matrix: list, row: int) -> list:
    return [m[row] for m in matrix]
assert get_column(matrix, 1) == [2,5,8]

friend_matrix = [[0,1,1,0,0], # user-1
                 [1,0,0,1,0], # user-2
                 [0,0,0,0,0], # user-3
                 [1,1,1,0,0], # user-4
                 [1,0,0,0,0]] # user-5
#user-1 and user-2 friens? - Yes
assert friend_matrix[0][1] == 1 # not error, because user-1 and user-2 - friends
# user-3 and aser-5 frends? - No
assert friend_matrix[2][4] == 0 # not error, because user-3 and user-5 - not friends
