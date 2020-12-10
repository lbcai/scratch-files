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

def extend(array):
    if not any(-1 in list for list in array):
            print(array)
            exit()

    for i in range(0, rows):
        for j in range(0, cols):
            if array[i][j] == -1:
                for item in [1, 2, 0]:
                    array[i][j] = item
                    print(array)
                    if check_adjacent_cells(array, i, j, n-1):
                        extend(array)
                    else:
                        array[i][j] = -1


def check_adjacent_cells(array, i, j, n):
    zero_count = 0
    for x in range(0, rows):
        for y in range(0, cols):
            if array[x][y] == 0:
                zero_count += 1

    if zero_count <= 9:
        if (i != 0 and i != n) and (j != 0 and j != n):
            # check all adjacent squares: [0][-1], [0][1], [-1][-1], [-1][0], [-1][1], [1][-1], [1][0], [1][1]
            if array[i][j] == 0:
                return True
            elif array[i][j] == 1:  # /
                if array[i + 1][j - 1] == 1 or array[i - 1][j + 1] == 1:
                    return False
                elif array[i + 0][j - 1] == 2 or array[i + 0][j + 1] == 2 or array[i + 1][j + 0] == 2 or array[i - 1][
                    j + 0] == 2:
                    return False
                else:
                    return True
            elif array[i][j] == 2:  # \
                if array[i - 1][j - 1] == 2 or array[i + 1][j + 1] == 2:
                    return False
                elif array[i + 0][j - 1] == 1 or array[i + 0][j + 1] == 1 or array[i + 1][j + 0] == 1 or array[i - 1][
                    j + 0] == 1:
                    return False
                else:
                    return True
            else:
                print("validation failed, seems to be checking -1")
                return False
        elif i == 0:
            if j == 0:
                # in upper left corner. only check [0][1], [1][0], [1][1]
                if array[i][j] == 0:
                    return True
                elif array[i][j] == 1:  # /
                    if array[i + 0][j + 1] == 2 or array[i + 1][j + 0] == 2:
                        return False
                    else:
                        return True
                elif array[i][j] == 2:  # \
                    if array[i + 1][j + 1] == 2:
                        return False
                    elif array[i + 0][j + 1] == 1 or array[i + 1][j + 0] == 1:
                        return False
                    else:
                        return True
                else:
                    print("validation failed, seems to be checking -1")
                    return False
            elif j == n:
                # in upper right corner. only check [0][-1], [1][0], [1][-1]
                if array[i][j] == 0:
                    return True
                elif array[i][j] == 1:  # /
                    if array[i + 1][j - 1] == 1:
                        return False
                    elif array[i + 0][j - 1] == 2 or array[i + 1][j + 0] == 2:
                        return False
                    else:
                        return True
                elif array[i][j] == 2:  # \
                    if array[i + 0][j - 1] == 1 or array[i + 1][j + 0] == 1:
                        return False
                    else:
                        return True
                else:
                    print("validation failed, seems to be checking -1")
                    return False
            else:
                # anywhere in top row. only check [0][-1], [0][1], [1][0], [1][-1], [1][1]
                if array[i][j] == 0:
                    return True
                elif array[i][j] == 1:  # /
                    if array[i + 1][j - 1] == 1:
                        return False
                    elif array[i + 0][j - 1] == 2 or array[i + 0][j + 1] == 2 or array[i + 1][j + 0] == 2:
                        return False
                    else:
                        return True
                elif array[i][j] == 2:  # \
                    if array[i + 1][j + 1] == 2:
                        return False
                    elif array[i + 0][j - 1] == 1 or array[i + 0][j + 1] == 1 or array[i + 1][j + 0] == 1:
                        return False
                    else:
                        return True
                else:
                    print("validation failed, seems to be checking -1")
                    return False
        elif i == n:
            if j == 0:
                # in bottom left corner. only check [0][1], [-1][0], [-1][1]
                if array[i][j] == 0:
                    return True
                elif array[i][j] == 1:  # /
                    if array[i - 1][j + 1] == 1:
                        return False
                    elif array[i + 0][j + 1] == 2 or array[i - 1][j + 0] == 2:
                        return False
                    else:
                        return True
                elif array[i][j] == 2:  # \
                    if array[i + 0][j + 1] == 1 or array[i - 1][j + 0] == 1:
                        return False
                    else:
                        return True
                else:
                    print("validation failed, seems to be checking -1")
                    return False
            elif j == n:
                # in bottom right corner. only check [0][-1], [-1][0], [-1][-1]
                if array[i][j] == 0:
                    return True
                elif array[i][j] == 1:  # /
                    if array[i + 0][j - 1] == 2 or array[i - 1][j + 0] == 2:
                        return False
                    else:
                        return True
                elif array[i][j] == 2:  # \
                    if array[i - 1][j - 1] == 2:
                        return False
                    elif array[i + 0][j - 1] == 1 or array[i - 1][j + 0] == 1:
                        return False
                    else:
                        return True
                else:
                    print("validation failed, seems to be checking -1")
                    return False
            else:
                # anywhere in bottom row. only check [0][-1], [0][1], [-1][0], [-1][-1], [-1][1]
                if array[i][j] == 0:
                    return True
                elif array[i][j] == 1:  # /
                    if array[i - 1][j + 1] == 1:
                        return False
                    elif array[i + 0][j - 1] == 2 or array[i + 0][j + 1] == 2 or array[i - 1][j + 0] == 2:
                        return False
                    else:
                        return True
                elif array[i][j] == 2:  # \
                    if array[i - 1][j - 1] == 2:
                        return False
                    elif array[i + 0][j - 1] == 1 or array[i + 0][j + 1] == 1 or array[i - 1][j + 0] == 1:
                        return False
                    else:
                        return True
                else:
                    print("validation failed, seems to be checking -1")
                    return False
        elif j == 0:
            # anywhere in first column but not top or bottom rows. check [-1][0], [1][0], [-1][1], [1][1], [0][1]
            if array[i][j] == 0:
                return True
            elif array[i][j] == 1: # /
                if array[i - 1][j + 1] == 1:
                    return False
                elif array[i + 0][j + 1] == 2 or array[i + 1][j + 0] == 2 or array[i - 1][j + 0] == 2:
                    return False
                else:
                    return True
            elif array [i][j] == 2: # \
                if array[i + 1][j + 1] == 2:
                    return False
                elif array[i + 0][j + 1] == 1 or array[i + 1][j + 0] == 1 or array[i - 1][j + 0] == 1:
                    return False
                else:
                    return True
            else:
                print("validation failed, seems to be checking -1")
                return False
        elif j == n:
            # anywhere in last column but not top or bottom rows. check [-1][0], [1][0], [0][-1], [-1][-1], [1][-1]
            if array[i][j] == 0:
                return True
            elif array[i][j] == 1:  # /
                if array[i + 1][j - 1] == 1:
                    return False
                elif array[i + 0][j - 1] == 2 or array[i + 1][j + 0] == 2 or array[i - 1][j + 0] == 2:
                    return False
                else:
                    return True
            elif array[i][j] == 2:  # \
                if array[i - 1][j - 1] == 2:
                    return False
                elif array[i + 0][j - 1] == 1 or array[i + 1][j + 0] == 1 or array[i - 1][j + 0] == 1:
                    return False
                else:
                    return True
            else:
                print("validation failed, seems to be checking -1")
                return False
    elif zero_count > 9:
        return False


extend(array)
