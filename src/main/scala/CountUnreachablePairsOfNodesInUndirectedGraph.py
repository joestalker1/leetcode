from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        p1 = self.find(x)
        p2 = self.find(y)
        if p1 == p2:
            return
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1


class Solution:

    def countPairs(self, n: int, edges) -> int:
        uf = UnionFind(n)
        for a, b in edges:
            uf.union(a, b)

        set_num = defaultdict(int)
        for i in range(n):
            p = uf.find(i)
            set_num[p] += 1
        pair = n * (n - 1) // 2
        # subtract number of existing pairs and it gets the number of unreachable pairs
        for p in set_num:
            pair -= set_num[p] * (set_num[p] - 1) // 2
        return pair


sol = Solution()
print(sol.countPairs(5,[[1,0],[3,1],[0,4],[2,1]]))#0
print(sol.countPairs(7,[[0,2],[0,5],[2,4],[1,6],[5,4]]))#14
