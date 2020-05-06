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
    def minimumCostToAllNodes(self, N, edges, newEdges):
        newEdges.sort(key=lambda x: x[2])
        weight = 0
        dsu = DSU(N)
        for s,e in edges:
            dsu.union(s, e)

        for s, e, w in newEdges:
            p1 = dsu.find(s)
            p2 = dsu.find(e)
            if p1 == p2:
                continue
            weight += w
            dsu.union(s, e)
        p = dsu.find(1)
        for n in range(2, N+1):
            if p != dsu.find(n):
                return -1
        return weight


sol = Solution()
print(sol.minimumCostToAllNodes(N = 6, edges = [[1, 4], [4, 5], [2, 3]], newEdges = [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]))