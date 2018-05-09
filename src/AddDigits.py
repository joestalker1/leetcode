class Solution:
    def addDigits(self, num):
        return 1 + (num - 1) % 9

sol = Solution()
print(sol.addDigits(38))