# The problem: You have a 5x5 grid and each square can contain a diagonal going this way: /,
# or going this way: \, or the square can be empty. The diagonal lines cannot touch.
# How can you get 16 diagonals into the grid?

# -1 = cell undecided
# 0 = no line in cell
# 1 = /
# 2 = \

# 5x5 grid
n = 5
# Acceptable number of blank cells for a 5x5 is 25 - 16 = 9
zeros = 9
rows, cols = (n, n)
# Makes an array (list of lists) full of -1s of n x n size
array = [[-1 for i in range(cols)] for j in range(rows)]
zero_count = 0
z = (n ** 2) - 1

def extend(array, z, n):
    global zero_count

    # Using 24 / 5 + rounding to nearest int = 4 to get rows...see 1 / 5 = 0, 0 / 5 = 0
    # and 24 modulo 5 = 4 to get columns...see 1 modulo 5 = 1, 0 modulo 5 = 0
    i = int(z / n)
    j = z % n

    # Once the last item is passed, end the program
    if z == -1:
        print(array)
        print('Total zeros:', zero_count)
        exit()

    # Make sure to increase the count every time a zero is placed and decrease it every time a zero
    # is removed (placed after the recursive call)
    # Take one off the counter in the recursive call (z) every time in order to track which cell you
    # are on in the array. Neighbor checking has to pass and total zeros cannot exceed allotment in
    # order to proceed. Check 0 last in [1, 2, 0] since it's basically a free pass and we'd
    # prefer to backtrack less if possible by placing fewer early zeros
    for item in [1, 2, 0]:
        if item == 0:
            zero_count += 1
        array[i][j] = item
        print(array)
        if check_adjacent_cells(array, i, j, n - 1) and zero_count <= zeros:
            extend(array, z - 1, n)

        if item == 0:
            zero_count -= 1


# Neighbor checking
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


extend(array, z, n)
