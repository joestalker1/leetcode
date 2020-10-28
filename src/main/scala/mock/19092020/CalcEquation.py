from collections import defaultdict


class Solution:
    def calcEquation(self, equations, values, queries):
        adj_list = defaultdict(list)
        for i in range(len(equations)):
            a, b = equations[i]
            adj_list[a].append([values[i], b])
            adj_list[b].append([1 / values[i], a])
        res = []

        def find_path(adj_list, a, b, seen):
            for k,v in adj_list[a]:
                if v == b:
                    return k
                if v in seen:
                    continue
                seen.add(v)
                r = k * find_path(adj_list, v, b, seen)
                if r >= 0.0:
                    return r
            return -1.0

        for a, b in queries:
            # find path from a to b
            if a not in adj_list or b not in adj_list:
                res.append(-1.0)
                continue
            r = find_path(adj_list, a, b, set())
            if r < 0:
                res.append(-1.0)
            else:
                res.append(r)
        return res


sol = Solution()
print(sol.calcEquation([["a", "b"], ["b", "c"]], [2.0, 3.0], [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))
