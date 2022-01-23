class UnionFindDisjointSet:
    def __init__(self, size):
        self.parent = [i for i in range(size)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        p1 = self.find(x)
        p2 = self.find(y)
        self.parent[p1] = p2
        