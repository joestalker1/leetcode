class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        if p == 1:
            return 1
        MOD = 10 ** 9 + 7
        return (pow(2**p - 2,2 **(p-1) - 1, MOD) * (2 ** p-1)) % MOD
