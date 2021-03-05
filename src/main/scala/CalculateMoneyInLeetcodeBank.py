class Solution:
    def totalMoney(self, n: int) -> int:
        w = n // 7
        res = 0
        if w > 0:
            res = 28 * w + 7 * (w - 1) * w // 2
        d = n % 7
        if w > 0:
            #first day at the rest week
            f = w + 1
            for _ in range(d):
                res += f
                f += 1
        return res

sol = Solution()
print(sol.totalMoney(20)) # 96