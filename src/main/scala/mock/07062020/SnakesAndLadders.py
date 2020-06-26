class Solution:
    def calc_rc(self, dest, n):
        r = dest // n
        if dest % n > 0:
            r += 1
        r = n - r
        c = dest % n
        if r % 2 == 0:
            c = n - c
        return [r, c - 1]

    def snakesAndLadders(self, board):
        if not board:
            return 0
        n = len(board)
        min_path = [[float('inf')] * n for _ in range(n)]
        min_path[n - 1][0] = 0
        q = [[n - 1, 0]]
        d1 = [-1, -2, -3, -4, -5, -6]  # 1
        d2 = [1, 2, 3, 4, 5, 6]  # 0
        while q:
            r, c = q.pop(0)
            if r == 0 and c == 0:
                break
            if c % 2 == 0:
                d = d2
            else:
                d = d1
            for r1, c1 in [[r, c + k] for k in range(1, min(6, n) + 1)]:
                if 0 <= c1 < n and 0 <= r1 < n:
                    x = abs(c1 - c)
                    if board[r1][c1] == -1:
                        if min_path[r][c] + x < min_path[r1][c1]:
                            q.append([r1, c1])
                            min_path[r1][c1] = min_path[r][c] + x
                    else:
                        dest = board[r1][c1]
                        r2, c2 = self.calc_rc(dest, n)
                        if min_path[r][c] + x < min_path[r1][c1]:
                            min_path[r1][c1] = min_path[r][c] + x
                            if min_path[r][c] + x < min_path[r2][c2]:
                                min_path[r2][c2] = min_path[r][c] + x
                            q.append([r2, c2])
        return min_path[0][0] if min_path[0][0] != float('inf') else -1


sol = Solution()
print(sol.snakesAndLadders([[-1, -1], [-1, 1]]))
print(sol.snakesAndLadders([[-1, -1], [-1, 3]]))
print(sol.snakesAndLadders([
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 35, -1, -1, 13, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 15, -1, -1, -1, -1]]))
