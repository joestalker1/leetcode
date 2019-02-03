class Solution:
    def calculate_row(self, buf, board, i, k):
        for j in range(len(board[i])):
            dead = 0
            live = 0
            if i - 1 >= 0:
                if board[i - 1][j]:
                    live += 1
                else:
                    dead += 1
            if i + 1 < len(board):
                if board[i + 1][j]:
                    live += 1
                else:
                    dead += 1
            if j - 1 >= 0:
                if board[i][j - 1]:
                    live += 1
                else:
                    dead += 1
            if j + 1 < len(board[i]):
                if board[i][j + 1]:
                    live += 1
                else:
                    dead += 1
            if i - 1 >= 0 and j - 1 >= 0:
                if board[i - 1][j - 1]:
                    live += 1
                else:
                    dead += 1
            if i + 1 < len(board) and j + 1 < len(board[i]):
                if board[i + 1][j + 1]:
                    live += 1
                else:
                    dead += 1
            if i - 1 >= 0 and j + 1 < len(board[i]):
                if board[i - 1][j + 1]:
                    live += 1
                else:
                    dead += 1
            if i + 1 < len(board) and j - 1 >= 0:
                if board[i + 1][j - 1]:
                    live += 1
                else:
                    dead += 1
            if buf[k][j] == 1 and (live < 2 or live > 3):
                buf[k][j] = 0
            elif buf[k][j] == 1 and (live == 2 or live == 3):
                buf[k][j] = 1
            elif buf[k][j] == 0 and live == 3:
                buf[k][j] = 1

    def copy_back(self, buf, board, i, k):
        for j in range(len(board[i])):
            board[i][j] = buf[k][j]

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or len(board) == 0:
            return
        buf = list()
        i = 0
        while i < len(board):
            if len(buf) > 1:
                self.copy_back(buf, board, i - 2, 0)
                buf.pop(0)
            buf.append(board[i][:])
            self.calculate_row(buf, board, i, len(buf) - 1)
            i += 1

        i = len(board) - 1
        for j in range(len(buf) - 1, -1, -1):
            self.copy_back(buf, board, i, j)
            i -= 1


sol = Solution()
arr = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
]
sol.gameOfLife(arr)
print(arr)
