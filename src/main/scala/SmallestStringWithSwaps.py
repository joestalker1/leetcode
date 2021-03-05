from collections import defaultdict


class Dsu:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x1, x2):
        p1 = self.find(x1)
        p2 = self.find(x2)
        if p2 == p1:
            return
        if self.rank[p1] > self.rank[p2]:
            self.p[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.p[p1] = p2
        else:
            self.p[p1] = p2
            self.rank[p2] += 1

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs):
        dsu = Dsu(len(pairs))
        for i,j in pairs:
            dsu.union(i, j)
        #component to its items
        m = defaultdict(list)
        for i in range(len(str)):
            p = dsu.find(i)
            m[p].append(i)
        #sort all items inside component
        for _,lst in m:
            lst.sort(key=lambda i:s[i])
        min_s = []
        #merge item one by one
        for i in range(len(s)):
            p = dsu.find(i)
            lst = m[p]
            #take minimal item
            min_s.append(lst.pop(0))
        return ''.join(min_s)






