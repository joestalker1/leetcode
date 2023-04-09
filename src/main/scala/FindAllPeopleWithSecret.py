class UnionFind:
    def __init__(self, n):
        self.rank = [1] * n
        self.par = [i for i in range(n)]

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x1, x2):
        p1 = self.find(x1)
        p2 = self.find(x2)
        if p1 == p2:
            return
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1

    def reset(self, x):
        self.par[x] = x
        self.rank[x] = 1

    def is_connected(self, x1, x2):
        return self.find(x1) == self.find(x2)


class Solution:
    def findAllPeople(self, n: int, meetings, firstPerson: int):
        if n == 0:
            return []
        sorted_meetings = sorted(meetings, key=lambda x: [x[2]])
        uf = UnionFind(n)
        uf.union(0, firstPerson)
        p = uf.find(0)
        while sorted_meetings:
            cur_time = sorted_meetings[0][2]
            vert = []
            while sorted_meetings and sorted_meetings[0][2] == cur_time:
                a, b, _ = sorted_meetings.pop(0)
                uf.union(a, b)
                vert.append(a)
                vert.append(b)
            for a in vert:
                if not uf.is_connected(a, 0):
                    uf.reset(a)
        p = uf.find(0)
        return [v for v in range(n) if uf.find(v) == p]