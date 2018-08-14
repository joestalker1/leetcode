class Solution:
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        return not(n * (n - 1))

sol = Solution()
print(sol.isPowerOfTwo(-16))
