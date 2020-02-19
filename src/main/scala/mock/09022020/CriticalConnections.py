from collections import defaultdict

class Solution:
    def criticalConnections(self, N, connections):
        if not connections or N == 0:
            return []
        adj_list = defaultdict(list)
        for s,e in connections:
            adj_list[s].append(e)
            adj_list[e].append(s)

        def is_critical(adj, s, forbid):
            q = [s]
            seen = set()
            k = set()
            while q:
                n = q.pop(0)
                k.add(n)
                for nei in adj[n]:
                    if nei in seen or (n,nei) in forbid:
                        continue
                    q.append(nei)
                    seen.add(nei)
            return len(k) < N
        res = []
        for s,e in connections:
            forbid = set()
            forbid.add((s,e))
            if is_critical(adj_list, s, forbid):
                res.append([s,e])
        return res


sol = Solution()
print(sol.criticalConnections(4,[[0,1],[1,2],[2,0],[1,3]]))






