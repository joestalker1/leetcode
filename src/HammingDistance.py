class Solution:
    def hammingDistance(self, x, y):
        dist = 0
        while x > 0 or y > 0:
            if (x & 1) != (y & 1):
                dist += 1
            x >>= 1
            y >>= 1
        return dist

sol = Solution()
print(sol.hammingDistance(1, 4))
