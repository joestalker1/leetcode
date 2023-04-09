class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @lru_cache(None)
        def solve(l,r):
            if l >= r:
                return 0
            min_cost = math.inf
            for i in range(l, r + 1):
                cost_for_i = i + max(solve(l, i - 1), solve(i + 1, r))
                min_cost = min(min_cost, cost_for_i)
            return min_cost

        dp = [[0] * (n+1) for _ in range(n+1)]
        for i in range(1, n +1):
            for j in range(i):
                for k in range(j):

        return solve(1, n)