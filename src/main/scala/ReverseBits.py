class Solution:
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            res = res << 1
            res |= (n & 1)
            n = n >> 1
        return res

sol = Solution()
print(sol.reverseBits(43261596))
