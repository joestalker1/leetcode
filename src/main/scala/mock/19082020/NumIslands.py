from collections import defaultdict


class Solution:
    def code(self, m, x, y):
        return x * m + y

    def find(self, p, x):
        if p[x] != x:
            p[x] = self.find(p, p[x])
        return p[x]

    def union(self, p, x, y):
        p1 = self.find(p, x)
        p2 = self.find(p, y)
        if p1 == p2:
            return
        self.comp -= 1
        p[p1] = p2

    def numIslands(self, grid):
        n = len(grid)
        m = len(grid[0])
        p = defaultdict(int)
        self.comp = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    self.comp += 1
                    p[self.code(m, i, j)] = self.code(m, i, j)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                        i1 = i + dx
                        j1 = j + dy
                        if 0 <= i1 < n and 0 <= j1 < m and grid[i1][j1] == '1':
                            c1 = self.code(m, i, j)
                            c2 = self.code(m, i1, j1)
                            self.union(p, c1, c2)
        return self.comp


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
sol = Solution()
print(sol.numIslands(grid))
