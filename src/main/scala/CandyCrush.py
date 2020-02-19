class Solution:
    def candyCrush(self, board):
        if not board:
            return board
        rows = len(board)
        cols = len(board[0])
        changes = 0
        for j in range(cols):
            for i in range(rows):
                a = abs(board[i][j])
                if a == 0:
                    continue
                if j + 2 < cols:
                    if abs(board[i][j + 1]) == a and abs(board[i][j + 2]) == a:
                        board[i][j + 1] = -abs(board[i][j + 1])
                        board[i][j + 2] = -abs(board[i][j + 2])
                        changes += 1
                        if board[i][j] > 0:
                            board[i][j] = -board[i][j]
                if i + 2 < rows:
                    if abs(board[i + 1][j]) == a and abs(board[i + 2][j]) == a:
                        changes += 1
                        board[i + 1][j] = -abs(board[i + 1][j])
                        board[i + 2][j] = -abs(board[i + 2][j])
                        if board[i][j] > 0:
                            board[i][j] = -board[i][j]
        if changes == 0:
            return board
        for j in range(cols):
            l = rows - 1
            i = rows - 1
            while i >= 0:
                while l >= 0 and board[l][j] < 0:
                    l -= 1
                if l >= 0:
                    board[i][j] = board[l][j]
                    l -= 1
                else:
                    board[i][j] = 0
                i -= 1
        return self.candyCrush(board)


sol = Solution()
print(sol.candyCrush(
    [[110, 5, 112, 113, 114], [210, 211, 5, 213, 214], [310, 311, 3, 313, 314], [410, 411, 412, 5, 414],
     [5, 1, 512, 3, 3], [610, 4, 1, 613, 614], [710, 1, 2, 713, 714], [810, 1, 2, 1, 1], [1, 1, 2, 2, 2],
     [4, 1, 4, 4, 1014]]))
