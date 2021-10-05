## Sudoku project
## Josemaria Ezejelue
## 08/17/2021

board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]

    ]


def solve(bd):
    find = find_empty(bd)
    if not find:
        return True
    else:
        row, col = find

    for x in range(1, 10):
        if valid(bd, x, (row, col)):
            bd[row][col] = x

            if solve(bd):
                return True

            bd[row][col] = 0
    return False



def valid(bd, num, pos):
    # check  row
    for x in range(len(bd[0])):
        if bd[pos[0]][x] == num and pos[1] != x:
            return False
    # check column

    for x in range(len(bd)):
        if bd[x][pos[1]] == num and pos[0] != x:
            return False

    # check 3*3 box
    box_i = pos[1] // 3
    box_j = pos[0] // 3

    for x in range(box_j * 3, box_j * 3 + 3):
        for y in range(box_i * 3, box_i * 3 + 3):
            if bd[x][y] == num and (x, y) != pos:
                return False

    return True


def print_board(bd):
    for x in range(len(bd)):
        if x % 3 == 0 and x != 0:
            print("------------------------")

        for y in range(len(bd[0])):
            if y % 3 == 0 and y != 0:
                print(" | ", end="")

            if y == 8:
                print(bd[x][y])
            else:
                print(str(bd[x][y]) + "", end=" ")


def find_empty(bd):
    for x in range(len(bd)):
        for y in range(len(bd[0])):
            if bd[x][y] == 0:
                return (x, y)

    return None


print_board(board)
solve(board)
print("                 ")
print_board(board)


