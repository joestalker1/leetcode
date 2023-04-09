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
    def friendRequests(self, n: int, restrictions, requests):
        friends = UnionFind(n)
        ans = [True] * len(requests)
        for i in range(len(requests)):
            a, b = requests[i]
            p1 = friends.find(a)
            p2 = friends.find(b)
            if p1 == p2:
                continue
            for x, y in restrictions:
                p11 = friends.find(x)
                p22 = friends.find(y)
                if p1 == p11 and p2 == p22 or p1 == p22 and p2 == p11:
                    ans[i] = False
                    break
            if ans[i]:
                friends.union(a, b)
        return ans