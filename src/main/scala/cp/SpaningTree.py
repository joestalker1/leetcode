class UnionFind:
    def __init__(self, n):
        self.link = [0] * n
        self.size = [1] * n
        for i in range(len(self.link)):
            self.link[i] = i

    def find(self, x):
        if x != self.link[x]:
            p = self.find(self.link[x])
            self.link[x] = p
        return x

    def unite(self, a, b):
        p1 = self.find(a)
        p2 = self.find(b)
        if self.size[a] < self.size[b]:
            a, b = b, a
            self.size[a] += self.size[b]
        self.link[b] = a

    def same(self, a, b):
        return self.find(a) == self.find(b)


def kruskal(edges):
    edges = sorted(edges, key = lambda x: x[2])
    uf = UnionFind(len(edges) * 2)
    for edge in edges:
        n1, n2, w = edge
        if not uf.same(n1, n2):
            uf.unite(n1, n2)



edges = [(1, 3, 2), (1, 5, 5), (2, 5, 3), (2, 6, 5), (3, 9, 4), (3, 3, 6), (4, 7, 6), (5, 2, 6)]
kruskal(edges)