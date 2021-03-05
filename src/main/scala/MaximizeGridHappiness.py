class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount, extrovertsCount):
        if m == 0 or n == 0 or (introvertsCount == 0 and extrovertsCount == 0):
            return 0

        # m is row number,n is column number

        def cost(i, j, mask_in, mask_ex, d):
            diff = 0
            up = (1 << n - 1)
            if j > 0 and (mask_in & 1):
                diff += (d - 30)
            if i > 0 and (mask_in & up):
                diff += (d - 30)
            if j > 0 and (mask_ex & 1):
                diff += (d + 20)

            if i > 0 and (mask_ex & up) == 1:
                diff += (d + 20)
            return diff

        def dfs(dp, p, intr, extr, mask_in, mask_ex):
            i = p // n
            j = p % n
            if i >= m:
                return 0
            if (p, intr, extr, mask_in, mask_ex) in dp:
                return dp[(p, intr, extr, mask_in, mask_ex)] - 1

            new_mask_in = (mask_in << 1) & 63
            new_mask_ex = (mask_ex << 1) & 63
            res = dfs(dp, p + 1, intr, extr, new_mask_in, new_mask_ex)
            if intr > 0:
                d = 120 + cost(i, j, mask_in, mask_ex, -30)
                res = max(res, d + dfs(dp, p + 1, intr - 1, extr, new_mask_in + 1, new_mask_ex))
            if extr > 0:
                d = 40 + cost(i, j, mask_in, mask_ex, 20)
                res = max(res, d + dfs(dp, p + 1, intr, extr - 1, new_mask_in, new_mask_ex + 1))
            dp[(p, intr, extr, mask_in, mask_ex)] = res + 1
            return res

        dp = {}
        return dfs(dp, 0, introvertsCount, extrovertsCount, 0, 0)


sol = Solution()
print(sol.getMaxGridHappiness(m=2, n=3, introvertsCount=1, extrovertsCount=2))  # 240
print(sol.getMaxGridHappiness(2, 2, introvertsCount=4, extrovertsCount=0))  # 240
print(sol.getMaxGridHappiness(3, 1, 2, 1))  # 260
