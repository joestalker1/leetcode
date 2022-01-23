from itertools import product


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return board

        def bfs(board, r, c):
            q = [[r, c]]
            while q:
                i, j = q.pop(0)
                if board[i][j] != 'O':
                    continue
                board[i][j] = 'E'
                if i + 1 < len(board):
                    q.append([i + 1, j])
                if i - 1 >= 0:
                    q.append([i - 1, j])
                if j - 1 >= 0:
                    q.append([i, j - 1])
                if j + 1 < len(board[0]):
                    q.append([i, j + 1])

        rows = len(board)
        cols = len(board[0])
        borders = list(product(range(rows), [0, cols - 1])) \
                  + list(product([0, rows - 1], range(cols)))
        for r, c in borders:
            bfs(board, r, c)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'E':
                    board[i][j] = 'O'
        return board

