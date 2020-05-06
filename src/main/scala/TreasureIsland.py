class Solution:
    def findTreasure(self, grid):
        if not grid:
            return None
        n = len(grid)
        m = len(grid[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        q = [[0, 0, 0]]
        # path_len[0][0] = 0
        #treasure = [0, 0]
        while q:
            r, c, step = q.pop(0)
            if grid[r][c] == 'X':
                return step
            for r1, c1 in [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]:
                if 0 <= r1 < n and 0 <= c1 < m:
                    if grid[r1][c1] == 'D':
                        continue
                    if not visited[r1][c1]:
                        visited[r1][c1] = True
                        q.append([r1, c1, step + 1])
        return -1


sol = Solution()
print(sol.findTreasure([['O', 'O', 'O', 'O'],
                        ['D', 'O', 'D', 'O'],
                        ['O', 'O', 'O', 'O'],
                        ['X', 'D', 'D', 'O']]))
