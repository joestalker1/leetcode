from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections):
        p = [i for i in range(n+1)]
        self.comp = n

        def parent(p, x):
            if x != p[x]:
                p[x] = parent(p[x], x)
            return p[x]

        def union(p, x1, x2):
            p1 = parent(p,x1)
            p2 = parent(p, x2)
            if p1 == p2:
                return
            self.comp -= 1
            p[p1] = p2
        adj_list = defaultdict(list)

        for x,y in connections:
            adj_list[x].append(y)

        def dfs(x, p, adj_list):
            for v in adj_list[x]:
                union(p,x,v)
                dfs(v, p, adj_list)

        for x in range(1, n + 1):
            dfs(x, p, adj_list)
        return self.comp



