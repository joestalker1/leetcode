class Solution:
    def concatenatedBinary(self, n):
        mod = 10 ** 9 + 7
        res = 0
        for i in range(1, n + 1):
            a = i
            bits = 0
            while a:
                bits += 1
                a = a >> 1
            res = (res << bits) + i
        return res % mod


sol = Solution()
print(sol.concatenatedBinary(10000))
print(sol.concatenatedBinary(12))


