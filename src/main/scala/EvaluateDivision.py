from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):
        # assert self._calcEquation([['a','b']], [2.0], [['a', 'b']]) == [2.0], 'test1'
        # assert self._calcEquation([['a','b']], [2.0], [['b', 'a']]) == [0.5], 'test2'
        # assert self._calcEquation([['a','a']], [1.0], [['a', 'a']]) == [1.0], 'test3'
        return self._calcEquation(equations, values, queries)
        # a /b = 2, b /c = 3,-> a/c - ? a = 2*b, b = 3 * c, a/c = 2*b/b/3 = 6

    def _calcEquation(self, equations, values, queries):
        weight = {}

        def find(weight, node_id):
            if node_id not in weight:
                weight[node_id] = (node_id, 1.0)
            grp_id, w = weight[node_id]
            if grp_id != node_id:
                new_grp, new_w = find(weight, grp_id)
                weight[node_id] = (new_grp, new_w * w)
            return weight[node_id]

        def union(weight, dividend, divisor, val):
            div_id1, div_w1 = find(weight, dividend)
            div_id2, div_w2 = find(weight, divisor)
            if div_id1 != div_id2:
                weight[div_id1] = (div_id2, div_w2 * val / div_w1)

        for (d1, d2), val in zip(equations, values):
            union(weight, d1, d2, val)
        res = []

        for a, b in queries:
            if a not in weight or b not in weight:
                res.append(-1.0)
            else:
                div_id1, w1 = find(weight, a)
                div_id2, w2 = find(weight, b)
                if div_id1 != div_id2:
                    res.append(-1.0)
                else:
                    res.append(w1 / w2)
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
