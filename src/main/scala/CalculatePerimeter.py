def get_num_neighbours(board, r, c):
    num = 0
    if r > 0:
        num += board[r - 1][c] == 1

    if r < len(board) - 1:
        num += board[r + 1][c] == 1

    if c > 0:
        num += board[r][c - 1] == 1

    if c < len(board[0]) - 1:
        num += board[r][c + 1] == 1

    return num


def island_perimeter(board):
    perimeter = 0
    for r, row in enumerate(board):
        for c, val in enumerate(row):
            if val == 1:
                perimeter += 4 - get_num_neighbours(board, r, c)
    return perimeter


print(island_perimeter([[0, 1, 1, 0],
                        [1, 1, 1, 0],
                        [0, 1, 1, 0],
                        [0, 0, 1, 0]]))
