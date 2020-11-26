class Solution:
    def tilingRectangle(self, n, m):
        n1 = max(n, m)
        mem = [[-1] * n1 for _ in range(n1)]
        return self.solve(min(n, m), max(n, m), mem)

    def solve(self, n, m, mem):
        if mem[n - 1][m - 1] != -1:
            return mem[n - 1][m - 1]

        if n == m:
            return 1
        if n == 0 or m == 0:
            return 0
        if n == 1:
            return m
        # find min square
        nextn = min(n, m)
        # find second square
        nextm = max(n, m) - nextn
        # first square is min(n,m) x min(n,m), let solve the rest
        # solve for the rest rects
        res = self.solve(min(nextm, nextn), max(nextm, nextn), mem) + 1
        s = nextn - 1
        while s > 0:
            a = max(abs(m - s), abs(n - s))
            b = min(abs(m - s), abs(n - s))
            k = b
            while k <= a and k <= n:
                # max, min a-k,b-k
                x = min(abs(a - k), abs(b - k))
                y = max(abs(a - k), abs(b - k))
                # solve for existant rectange
                rect1 = self.solve(min(b, abs(m - k)), max(b, abs(m - k)), mem)
                rect2 = self.solve(x, y, mem)
                rect3 = self.solve(min(a, abs(n - k)), max(a, abs(n - k)), mem)
                res = min(res, rect1 + rect2 + rect3 + 2)
                k += 1
            s -= 1
        mem[n - 1][m - 1] = res
        return mem[n - 1][m - 1]


sol = Solution()
print(sol.tilingRectangle(5, 8))
print(sol.tilingRectangle(2, 3))
