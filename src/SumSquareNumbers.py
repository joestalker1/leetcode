import math

class Solution:
    def judgeSquareSum(self, c):
        if c < 0:
            return False
        i = 0
        while i*i <= c:
            b = math.sqrt(c - i*i)
            if b == int(b):
                return True
            i += 1
        return False


sol = Solution()
#print(sol.judgeSquareSum(4))
print(sol.judgeSquareSum(5))