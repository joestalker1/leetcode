class Solution:
    def concatenatedBinary(self, n):
        mod = 10 ** 9 + 7
        res = 0
        len = 0
        for i in range(1, n + 1):
            if i & (i - 1) == 0:
                len += 1
            res = (res << len) + i
            res = res % mod
        return res

sol = Solution()
print(sol.concatenatedBinary(3))
