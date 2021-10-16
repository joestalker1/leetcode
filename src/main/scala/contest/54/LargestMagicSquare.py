class Solution:
    def largestMagicSquare(self, grid):
        if not grid or len(grid[0]) == 0:
            return 0
        n = len(grid)
        m = len(grid[0])

        row_sum = [[0] * m for _ in range(n)]
        col_sum = [[0] * m for _ in range(n)]
        for i in range(n):
            row_sum[i][0] = grid[i][0]
            for j in range(1, m):
                row_sum[i][j] = row_sum[i][j - 1] + grid[i][j]
        for j in range(m):
            col_sum[0][j] = grid[0][j]
            for i in range(1, n):
                col_sum[i][j] = col_sum[i - 1][j] + grid[i][j]
        max_square = 1
        r = min(n, m)
        for i in range(n):
            for j in range(m):
                for l in range(2, r + 1):
                    i1 = i + l - 1
                    j1 = j + l - 1
                    if i1 >= n or j1 >= m:
                        break
                    cur_sum = 0
                    f = True
                    for k in range(i, i1 + 1):
                        if j > 0:
                            cand = row_sum[k][j1] - row_sum[k][j - 1]
                        else:
                            cand = row_sum[k][j1]
                        if k == i:
                            cur_sum = cand
                        else:
                            if cur_sum != cand:
                                f = False
                                break
                    if not f:
                        continue
                    for k in range(j, j1 + 1):
                        if i > 0:
                            cand = col_sum[i1][k] - col_sum[i - 1][k]
                        else:
                            cand = col_sum[i1][k]
                        if cand != cur_sum:
                            f = False
                            break
                    if f:
                        i2 = i
                        j2 = j
                        cand = 0
                        while i2 <= i1:
                            cand += grid[i2][j2]
                            i2 += 1
                            j2 += 1
                        if cand != cur_sum:
                            continue
                        cand = 0
                        i2 = i1
                        j2 = j
                        while i2 >= i:
                            cand += grid[i2][j2]
                            i2 -= 1
                            j2 += 1
                        if cand != cur_sum:
                            continue
                        max_square = max(max_square, l)
        return max_square


sol = Solution()
print(sol.largestMagicSquare([[1, 17, 15, 17, 5, 16, 8, 9], [1, 19, 11, 18, 8, 18, 3, 18], [6, 6, 5, 8, 3, 15, 6, 11],
                              [19, 5, 6, 11, 9, 2, 14, 13], [12, 16, 16, 15, 14, 18, 10, 7],
                              [3, 11, 15, 15, 7, 1, 9, 8], [15, 5, 11, 17, 18, 20, 14, 17],
                              [13, 17, 7, 20, 12, 2, 13, 19]]))#1
print(sol.largestMagicSquare([[5, 1, 3, 1], [9, 3, 3, 1], [1, 3, 3, 8]]))  # 2
print(sol.largestMagicSquare([[2, 2], [2, 2]]))  # 2
print(sol.largestMagicSquare([[7, 1, 4, 5, 6], [2, 5, 1, 6, 4], [1, 5, 4, 3, 2], [1, 2, 7, 3, 4]]))  # 3
