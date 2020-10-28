class UnionFind:
    def __init__(self, grid):
        n = len(grid)
        m = len(grid[0])

        self.count = 0
        self.parent = [0 for i in range(m * n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    self.parent[i * m + j] = i * m + j
                    self.count += 1
        self.rank = [0 for _ in range(m * n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x1, x2):
        p1 = self.find(x1)
        p2 = self.find(x2)
        if p1 == p2:
            return
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1
        self.count -= 1


class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        n = len(grid)
        m = len(grid[0])
        uf = UnionFind(grid)

        def to_index(r, c):
            return r * m + c

        for r in range(n):
            for c in range(m):
                if grid[r][c] == '0':
                    continue
                if r - 1 >= 0 and grid[r - 1][c] == '1':
                    uf.union(to_index(r, c), to_index(r - 1, c))
                if r + 1 < n and grid[r + 1][c] == '1':
                    uf.union(to_index(r, c), to_index(r + 1, c))
                if c - 1 >= 0 and grid[r][c - 1] == '1':
                    uf.union(to_index(r, c), to_index(r, c - 1))
                if c + 1 < m and grid[r][c + 1] == '1':
                    uf.union(to_index(r, c), to_index(r, c + 1))
                grid[r][c] = '0'

        return uf.count


sol = Solution()
print(sol.numIslands([["1", "0", "1", "1", "1"], ["1", "0", "1", "0", "1"], ["1", "1", "1", "0", "1"]]))  # 1
print(sol.numIslands([["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]))

print(sol.numIslands([["1", "1"]]))
print(sol.numIslands(
    [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))
