# class UnionFind:
#     def __init__(self, equations):
#         self.parent = [-1] * len(equations)
#         self.rank = [0] * len(equations)
#         for i in range(len(self.parent)):
#             self.parent[i] = i
#
#     def find(self, i):
#         if self.parent[i] != i:
#             self.parent[i] = self.parent(self.parent[i])
#         return self.parent
#


class Solution:
    def path(self, adj, s, n, e, buf):
        buf.append(s)
        if s == e:
            return buf
        res = None
        for nodes in adj[s]:
            if nodes[0] == n:
                continue
            bufc = buf[:]
            resc = self.path(adj, nodes[0], s, e, bufc)
            if not res and resc:
                res = resc
            elif resc and len(resc) < len(res):
                res = resc
        return res

    def eval_weight(self, adj, nodes):
        w = 1
        for i in range(len(nodes) - 1):
            a = nodes[i]
            b = nodes[i + 1]
            for n in adj[a]:
                if n[0] == b:
                    w *= n[1]
                    break
        return w

    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        if not equations:
            return []
        adj = {}
        for i in range(len(equations)):
            pair = equations[i]
            if pair[0] not in adj.keys():
                adj[pair[0]] = [[pair[1], values[i]]]
            else:
                adj[pair[0]].append([pair[1], values[i]])
            if pair[1] not in adj.keys():
                adj[pair[1]] = [[pair[0], 1 / values[i]]]
            else:
                adj[pair[1]].append([pair[0], 1 / values[i]])
        res = []
        for query in queries:
            s = query[0]
            e = query[1]
            if s not in adj.keys() or e not in adj.keys():
                res.append(-1)
            elif s == e:
                res.append(1)
            else:
                nodes = self.path(adj, s,"", e, [])
                res.append(self.eval_weight(adj, nodes))
        return res

sol = Solution()

eq = [["a","e"],["b","e"]]
vl = [4.0,3.0]
qr = [["a","b"],["e","e"],["x","x"]]
print(sol.calcEquation(eq, vl, qr))


equestions = [["a", "b"], ["b", "c"]]
values=[2.0, 3.0]
queries1 = [ ["a","c"],["b","c"],["a","e"],["a","a"],["x","x"] ]
queries2 = [ ["a", "e"],["a", "c"], ["b", "a"], ["a", "a"], ["x", "x"] ]

print(sol.calcEquation(equestions, values, queries1))