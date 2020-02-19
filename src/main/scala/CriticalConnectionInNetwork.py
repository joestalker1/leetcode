from collections import defaultdict

class Solution:
    def criticalConnections(self, n: int, connections):
        low = [-1] * n
        disc = [-1] * n
        time = 1
        adj_list = defaultdict(list)
        for s,e in connections:
            adj_list[s].append(e)
            adj_list[e].append(s)

        def dfs(u, low, disc, pre, res):
            nonlocal time
            low[u] = time
            disc[u] = time
            time += 1
            for v in adj_list[u]:
                if pre == v:
                    continue
                if disc[v] == -1:
                    dfs(v,low, disc, u, res)
                    low[u] = min(low[u], low[v])
                    if low[v] > disc[u]:
                        res.append([u,v])
                else:
                    low[u] = min(low[u], disc[v])
        res = []
        for i in range(n):
            if disc[i] == -1:
                dfs(i,low, disc,i,res)
        return res