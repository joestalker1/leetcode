from collections import defaultdict


class Solution:
    def dfs(self, adj, s, e, r, seen):
        if s not in adj.keys() or s in seen:
            return -1
        seen.add(s)
        if s == e:
            return r
        for p in adj[s]:
            n, w = p
            r1 = self.dfs(adj, n, e, r * w, seen)
            if r1 != -1:
                return r1
        return r1

    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        if not equations:
            return []
        adj = defaultdict(list)
        for i in range(len(equations)):
            p0, p1 = equations[i]
            adj[p0].append([p1, values[i]])
            adj[p1].append([p0, 1 / values[i]])
        res = list()
        for query in queries:
            s, e = query
            res.append(self.dfs(adj, s, e, 1, set()))
        return res


sol = Solution()

# eq = [["a", "e"], ["b", "e"]]
# vl = [4.0, 3.0]
# qr = [["a", "b"], ["e", "e"], ["x", "x"]]
# print(sol.calcEquation(eq, vl, qr))

equestions = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries1 = [["a", "c"], ["b", "c"], ["a", "e"], ["a", "a"], ["x", "x"]]
queries2 = [["a", "e"], ["a", "c"], ["b", "a"], ["a", "a"], ["x", "x"]]

print(sol.calcEquation(equestions, values, queries1))
