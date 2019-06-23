class Solution:
    def mines(self, board, row, col):
        mines = 0
        if row - 1 >= 0 and board[row - 1][col] in 'MX':
            mines += 1
        if row + 1 < len(board) and board[row + 1][col] in 'MX':
            mines += 1
        if col - 1 >= 0 and board[row][col - 1] in 'MX':
            mines += 1
        if col + 1 < len(board[0]) and board[row][col + 1] in 'MX':
            mines += 1
        if row - 1 >= 0 and col - 1 >= 0 and board[row - 1][col - 1] in 'MX':
            mines += 1
        if row - 1 >= 0 and col + 1 < len(board[0]) and board[row - 1][col + 1] in 'MX':
            mines += 1
        if row + 1 < len(board) and col - 1 >= 0 and board[row+1][col-1] in 'MX':
            mines += 1
        if row + 1 < len(board) and col + 1 < len(board[0]) and board[row + 1][col + 1] in 'MX':
            mines += 1
        return mines

    def updateBoard(self, board, click):
        if not board or not click:
            return

        def reveal(board, row, col):
            if board[row][col] == 'M':
                board[row][col] = 'X'

            if board[row][col] == 'E':
                mines = self.mines(board, row, col)
                if mines > 0:
                    board[row][col] = chr(ord('0') + mines)
                else:
                    board[row][col] = 'B'

                if mines > 0:
                    return

                if row - 1 >= 0:
                    reveal(board, row - 1, col)

                if row + 1 < len(board):
                    reveal(board, row + 1, col)

                if col - 1 >= 0:
                    reveal(board, row, col - 1)

                if col + 1 < len(board[0]):
                    reveal(board, row, col + 1)

                if row - 1 >= 0 and col - 1 >= 0:
                    reveal(board, row - 1, col - 1)

                if row - 1 >= 0 and col + 1 < len(board[0]):
                    reveal(board, row - 1, col + 1)

                if row + 1 < len(board) and col - 1 >= 0:
                    reveal(board, row + 1, col - 1)

                if row + 1 < len(board) and col + 1 < len(board[0]):
                    reveal(board, row + 1, col + 1)

        reveal(board, click[0], click[1])
        return board





