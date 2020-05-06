class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, v1, v2):
        p1 = self.find(v1)
        p2 = self.find(v2)
        if p1 == p2:
            return
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1


class Solution:
    def minimumCost(self, N, connections):
        connections.sort(key=lambda x: x[2])
        weight = 0
        dsu = DSU(N)
        vert = N
        for s, e, w in connections:
            p1 = dsu.find(s)
            p2 = dsu.find(e)
            if p1 == p2:
                continue
            vert -= 1
            weight += w
            dsu.union(s, e)
        if vert == 1:
            return weight
        return -1


sol = Solution()
print(sol.minimumCost(4, [[1, 2, 1], [1, 3, 2], [3, 4, 4], [1, 4, 3]]))
print(sol.minimumCost(4, [[1, 2, 3], [3, 4, 4]]))
