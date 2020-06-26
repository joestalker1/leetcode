class Solution:
    def snakesAndLadders(self, board):
        if not board:
            return 0
        n = len(board)
        min_path = {1: 0}

        def get(s):
            quot, rem = divmod(s - 1, n)
            row = n - quot - 1
            col = rem if n % 2 != row % 2 else n - rem - 1
            return [row, col]

        q = [1]
        while q:
            s = q.pop(0)
            if s == n * n:
                return min_path[s]
            for s2 in range(s + 1, min(s + 6, n * n) + 1):
                r,c = get(s2)
                if board[r][c] != -1:
                    s2 = board[r][c]
                if s2 not in min_path:
                    min_path[s2] = min_path[s] + 1
                    q.append(s2)
        return -1


sol = Solution()
print(sol.snakesAndLadders([[-1, -1], [-1, 1]]))  # 1
print(sol.snakesAndLadders([[-1, -1], [-1, 3]]))  # 1
print(sol.snakesAndLadders([
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 35, -1, -1, 13, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 15, -1, -1, -1, -1]]))
