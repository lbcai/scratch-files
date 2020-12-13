# The problem: You have a 5x5 grid and each square can contain a diagonal going this way: /,
# or going this way: \, or the square can be empty. The diagonal lines cannot touch.
# How can you get 16 diagonals into the grid?

# -1 = cell undecided
# 0 = no line in cell
# 1 = /
# 2 = \

# 5x5 grid
n = 5
# acceptable number of blank cells for a 5x5 is 25 - 16 = 9
zeros = 9
rows, cols = (n, n)
array = [[-1 for i in range(cols)] for j in range(rows)]
print(array)
zero_count = 0


def extend(array):
    global zero_count
    global zeros
    if not any(-1 in list for list in array):
            print(array)
            print(zero_count)
            exit()

    break_count = 0
    for i in range(0, rows):
        for j in range(0, cols):
            if array[i][j] == -1:
                break_count = 1
                break
        if break_count == 1:
            break

    for item in [1, 2, 0]:
        if item == 0:
            zero_count += 1
        array[i][j] = item
        print(array)
        if check_adjacent_cells(array, i, j, n-1) and zero_count <= zeros:
            extend(array)
        else:
            if item == 0:
                zero_count -= 1
            array[i][j] = -1


def check_adjacent_cells(array, i, j, n):
    if array[i][j] == 0:
        return True
    elif array[i][j] == 1:  # /
        if j != 0:
            if array[i][j - 1] == 2: # [0][-1] direct left
                return False
        if j != n:
            if array[i][j + 1] == 2: # [0][1] direct right
                return False
        if i != 0:
            if array[i - 1][j] == 2: # [-1][0] direct above
                return False
            if j != n:
                if array[i - 1][j + 1] == 1: # [-1][1] upper right corner
                    return False
        if i != n:
            if array[i + 1][j] == 2: # [1][0] direct below
                return False
            if j != 0:
                if array[i + 1][j - 1] == 1: # [1][-1] bottom left corner
                    return False
        return True
    elif array[i][j] == 2:  # \
        if j != 0:
            if array[i][j - 1] == 1: # [0][-1] direct left
                return False
            if i != 0:
                if array[i - 1][j - 1] == 2: # [-1][-1] upper left corner
                    return False
        if j != n:
            if array[i][j + 1] == 1: # [0][1] direct right
                return False
        if i != 0:
            if array[i - 1][j] == 1: # [-1][0] direct above
                return False
        if i != n:
            if array[i + 1][j] == 1: # [1][0] direct below
                return False
            if j != n:
                if array[i + 1][j + 1] == 2: # [1][1] bottom right corner
                    return False
        return True


extend(array)
print(zero_count)
