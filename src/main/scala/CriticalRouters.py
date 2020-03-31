from collections import defaultdict

class Solution:
    def find_cut_points(self, numNodes, numEdges, edges):
        if not edges:
            return []
        adj = defaultdict(list)
        for s,d in edges:
            adj[s].append(d)
            adj[d].append(s)
        disc = [-1] * numNodes
        low = [-1] * numNodes
        visited = [False] * numNodes
        res = []
        timer = 0

        def dfs(u, p):
            nonlocal timer
            disc[u] = timer
            low[u] = timer
            timer += 1
            visited[u] = True
            children = 0
            for v in adj[u]:
                if v == p:
                    continue
                if visited[v]:
                    low[u] = min(low[u], disc[v])
                else:
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    if low[v] >= disc[u] and p != -1:
                        res.append(u)
                    children += 1
            if p == -1 and children > 1:
                res.append(u)

        for n in range(numNodes):
            if not visited[n]:
                dfs(n, -1)
        return res


sol = Solution()
print(sol.find_cut_points(numNodes = 7, numEdges = 7, edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]))

