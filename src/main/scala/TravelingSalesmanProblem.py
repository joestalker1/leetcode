class Solution:
    def travel(self, c):
        n = len(c)
        mem = [[-1] * (1 << n) for _ in range(n)]

        def tsp(i, s):
            if s == (1 << n) - 1:
                return c[i][0]
            if mem[i][s] != -1:
                return mem[i][s]
            res = 10000000000
            for j in range(n):
                if s & (1 << j):
                    continue
                res = min(res, c[i][j] + tsp(j, s | (1 << j)))
            mem[i][s] = res
            return res
        return tsp(0, 1 << 0)

