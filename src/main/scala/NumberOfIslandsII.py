from collections import defaultdict


class UnionFind:
    def __init__(self):
        self.comp = 0
        self.parent = defaultdict(int)
        self.rank = defaultdict(int)

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
            return x
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
        self.comp += 1

    def has(self, x):
        return x in self.parent


class Solution:
    def numIslands2(self, m: int, n: int, positions):
        res = []
        uf = UnionFind()
        positions.sort(key=lambda x: [x[0], x[1]])
        for x, y in positions:
            for dx, dy in [[0, 1][0, -1], [1, 0], [-1, 0]]:
                x1 = x + dx
                y1 = y + dy
                c = x1 * n + y1
                if 0 <= x1 < m and 0 <= y1 < n and uf.has(c):
                    uf.union(x * n + y, c)
        return uf.comp
