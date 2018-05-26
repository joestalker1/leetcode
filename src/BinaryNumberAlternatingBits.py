class Solution:
    def hasAlternatingBits(self, n):
        if not n:
            return False
        while n > 0:
            a = n & 3
            if a == 0 or a == 3:
                return False
            n = n >> 1
        return True

sol = Solution()
print(sol.hasAlternatingBits(5))
print(sol.hasAlternatingBits(7))
print(sol.hasAlternatingBits(11))
print(sol.hasAlternatingBits(10))
