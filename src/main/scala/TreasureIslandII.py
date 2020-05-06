class Solution:
    def findTreasure(self, grid):
        if not grid:
            return None
        n = len(grid)
        m = len(grid[0])
        q = []
        path_len = [[float('inf') for _ in range(m)] for _ in range(n)]
        for i, r in enumerate(grid):
            for j, v in enumerate(r):
                if v == 'S':
                    path_len[i][j] = 0
                    q.append([i, j])

        treasure = []
        while q:
            r, c = q.pop(0)
            if grid[r][c] == 'X':
                treasure.append([r,c])
                continue
            for r1, c1 in [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]:
                if 0 <= r1 < n and 0 <= c1 < m:
                    if grid[r1][c1] == 'D':
                        continue
                    if path_len[r][c] + 1 < path_len[r1][c1]:
                        path_len[r1][c1] = path_len[r][c] + 1
                        q.append([r1,c1])

        return min([path_len[x[0]][x[1]] for x in treasure])


sol = Solution()
print(sol.findTreasure([['S', 'O', 'O', 'S', 'S'],
                        ['D', 'O', 'D', 'O', 'D'],
                        ['O', 'O', 'O', 'O', 'X'],
                        ['X', 'D', 'D', 'O', 'O'],
                        ['X', 'D', 'D', 'D', 'O']]))
