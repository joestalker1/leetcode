class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        if p == 1:
            return 1
        if p % 2 == 0:
            pr = 1
            for num in range(1, 2**p):
                pr = pr * num
            return pr
        n = 2 ** p - 2
        return ((2**p - 2) ** (n //2)) * (2**p-1) % (10**9+7)

sol = Solution()
print(sol.minNonZeroProduct(3))#6