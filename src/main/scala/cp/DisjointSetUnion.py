class UnionFindDisjointSet:

    def __init__(self, n):
        self.parent = list([i for i in range(n)])
        self.rank = [0] * n

    def findSet(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.findSet(self.parent[x])
        return self.parent[x]

    def unionSet(self, x, y):
        parent = self.findSet(x)
        rank1 = self.rank[parent]
        self.parent[y] = parent

    def isSameSet(self, x, y):
        return self.findSet(x) == self.findSet(y)

