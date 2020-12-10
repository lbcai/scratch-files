# The problem: You have a 5x5 grid and each square can contain a diagonal going this way: /,
# or going this way: \, or the square can be empty. The diagonal lines cannot touch.
# How can you get 16 diagonals into the grid?

# -1 = cell undecided
# 0 = no line in cell
# 1 = /
# 2 = \

# 5x5 grid
n = 5
rows, cols = (n, n)
array = [[-1 for i in range(cols)] for j in range(rows)]
print(array)

def extend(array):
    if -1 not in array:
        print(array)
        exit()

    for item in [0, 1, 2]:
        for i in range(rows):
            for j in range(cols):
                array[i][j] = item
                if check_adjacent_cells(array[i][j], n):
                    extend(array)
                array[i][j] = -1


def check_adjacent_cells(array[i][j], n):
    if (i != 0 and i != n) and (j != 0 and j != n):
        # check all adjacent squares: [0][-1], [0][1], [-1][-1], [-1][0], [-1][1], [1][-1], [1][0], [1][1]
    elif i == 0:
        if j == 0:
            # in upper left corner. only check [0][1], [1][0], [1][1]
        elif j == n:
            # in upper right corner. only check [0][-1], [1][0], [1][-1]
        else:
            # anywhere in top row. only check [0][-1], [0][1], [1][0], [1][-1], [1][1]
    elif i == n:
        if j == 0:
            # in bottom left corner. only check [0][1], [-1][0], [-1][1]
        elif j == n:
            # in bottom right corner. only check [0][-1], [-1][0], [-1][-1]
        else:
            # anywhere in bottom row. only check [0][-1], [0][1], [-1][0], [-1][-1], [-1][1]
    elif j == 0:
        # anywhere in first column but not top or bottom rows. check [-1][0], [1][0], [-1][1], [1][1], [0][1]
    elif j == n:
        # anywhere in last column but not top or bottom rows. check [-1][0], [1][0], [0][-1], [-1][-1], [1][-1]
