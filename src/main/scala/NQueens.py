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

def is_valid(board):
    current_queen_row = len(board) - 1
    # set up last col
    current_queen_col = board[-1]
    # Iterate over all already-placed queens and check if any of them can attack
    # each other.
    # take all except last item
    for row, col in enumerate(board[:-1]):
        # if col == current_queen_col it will be breach
        # or current_col - col == current_row - row the queen is atacked by other one.
        diff = abs(current_queen_col - col)
        if diff == 0 or diff == current_queen_row - row:
            return False
    return True


print(n_queens(5))