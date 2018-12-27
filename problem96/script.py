# Algorithm is taken from https://medium.com/@george.seif94/solving-sudoku-using-a-simple-search-algorithm-3ac44857fee8
import numpy as np
import re

file = open("p096_sudoku.txt").read()
master_arr = re.sub(r'Grid \d+', "~", file)
master_arr = master_arr.replace("~\n", "~")
master_arr = master_arr.replace("\n~", "~")
master_arr = master_arr.replace("\n", ",")
master_arr = master_arr.split('~')
del master_arr[0]
for ind, val in enumerate(master_arr):
    master_arr[ind] = val.split(',')
    for index, numbers in enumerate(master_arr[ind]):
        master_arr[ind][index] = list(numbers)
        for idx, string in enumerate(master_arr[ind][index]):
            master_arr[ind][index][idx] = int(string)

# For testing a single array
# arr = [[0, 0, 3, 0, 2, 0, 6, 0, 0],
#         [9, 0, 0, 3, 0, 5, 0, 0, 1],
#         [0, 0, 1, 8, 0, 6, 4, 0, 0],
#         [0, 0, 8, 1, 0, 2, 9, 0, 0],
#         [7, 0, 0, 0, 0, 0, 0, 0, 8],
#         [0, 0, 6, 7, 0, 8, 2, 0, 0],
#         [0, 0, 2, 6, 0, 9, 5, 0, 0],
#         [8, 0, 0, 2, 0, 3, 0, 0, 9],
#         [0, 0, 5, 0, 1, 0, 3, 0, 0]]
#
# arr = np.array(arr)


def print_grid(grid):
    for i in range(9):
        print(grid[i])


def used_in_column(num, col):
    if num in arr[:, col]:
        return True
    else:
        return False


def used_in_row(num, row):
    if num in arr[row]:
        return True
    else:
        return False


def get_start_end(index):
    start_index = 0
    end_index = 3

    if 3 <= index < 6:
        start_index = 3
        end_index = 6
    elif 6 <= index < 9:
        start_index = 6
        end_index = 9

    return [start_index, end_index]


def used_in_cell(num, row, col):
    col_ind = get_start_end(col)
    row_ind = get_start_end(row)

    box = arr[row_ind[0]:row_ind[1], col_ind[0]:col_ind[1]]

    if num in box:
        return True
    else:
        return False


def get_blank_location():
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:
                return [i, j]

    return [9, 9]


def is_safe(number, row, col):
    return not used_in_row(number, row) and \
                not used_in_column(number, col) and \
                not used_in_cell(number, row, col)


def solve():
    locations = get_blank_location()
    if locations == [9, 9]:
        return True

    row = locations[0]
    col = locations[1]

    for number in range(1, 10):
        if is_safe(number, row, col):
            arr[row][col] = number
            if solve():
                return True
            arr[row][col] = 0
    return False


final_sum = 0
for puzzle in master_arr:
    arr = np.array(puzzle)
    solve()
    final_sum += int(''.join(map(str, arr[0, 0:3])))
    print_grid(arr)
    print(final_sum)
print(final_sum)
