class Solution(object):
    def hammingWeight(self, n):
        bits = 0
        while n:
            n = n & (n - 1)
            bits += 1
        return bits

sol = Solution()
print(sol.hammingWeight(8))