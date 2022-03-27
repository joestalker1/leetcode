from functools import lru_cache

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def color(m, n, r, c, cur, prev):
            if r == m:
                return color(m, n, 0, c + 1, 0, cur)
            if c == n:
                return 1
            # if r == 0 and dp[c][prev] != -1:
            #     return dp[c][prev]
            cnt = 0
            #check if color is above
            up = (cur >> ((r-1)*2)) & 3 if r != 0 else 0
            #check a color is at the left of
            left = prev >> (r * 2) & 3
            for clr in range(1, 4):
                if clr != up and clr != left:
                    cnt  = (cnt + color(m, n, r + 1, c, cur + (clr << (r * 2)), prev)) % MOD
            # if r == 0:
            #     dp[c][prev] = cnt
            return cnt

       # dp = [[-1] * 1025 for _ in range(1002)]
        return color(m, n, 0, 0, 0, 0)


sol = Solution()
print(sol.colorTheGrid(5, 999))
print(sol.colorTheGrid(1,2))#6
