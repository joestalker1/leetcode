def is_valid(board):
    current_row, current_col = len(board) - 1, board[-1]
    for row, col in enumerate(board[:-1]):
        diff = abs(col - current_col)
        if diff == 0 or diff == abs(row - current_row):
            return False
    return True

def n_queens(n, board=[]):
    if n == len(board):
        return 1
    count = 0
    for col in range(n):
        board.append(col)
        if is_valid(board):
            count += n_queens(n, board)
        board.pop()
    return count

print(n_queens(9))