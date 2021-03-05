class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x1, x2):
        p1 = self.find(x1)
        p2 = self.find(x2)
        self.parent[p1] = p2

class Solution:
    def findRedundantConnection(self, edges):
        if not edges:
            return []
        dsu = DSU(len(edges) * 2 + 1)
        for x,y in edges:
            if dsu.find(x) == dsu.find(y):
                return [x,y]
            dsu.union(x, y)
        return []


sol = Solution()
print(sol.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]))
