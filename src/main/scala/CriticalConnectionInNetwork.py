from collections import defaultdict

class Solution:
    def criticalConnections(self, n: int, connections):
        low = [-1] * n # most earlier node we can reach from the current node
        disc = [-1] * n # time when we visit a node
        time = 1
        adj_list = defaultdict(list)#graph
        for s,e in connections:
            adj_list[s].append(e)
            adj_list[e].append(s)

        def dfs(p, low, disc, prev, res):
            nonlocal time
            low[p] = time#
            disc[p] = time
            time += 1
            for v in adj_list[p]:
                if prev == v:
                    continue # ignore cycle
                if disc[v] == -1: #when we visit node first time
                    dfs(v,low, disc, p, res) # go further
                    low[p] = min(low[p], low[v]) # update earlier time
                    if low[v] > disc[p]: # articulation point?
                        res.append([p,v])
                else:
                    low[p] = min(low[p], disc[v])
        res = []
        for i in range(n):
            if disc[i] == -1:
                dfs(i,low, disc,i,res)
        return res