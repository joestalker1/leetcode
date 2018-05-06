class Solution:
    def isUgly(self, num):
        if num == 1:
            return True
        if num == 0:
            return False
        frac = [2,3,5]
        for k in frac:
            while num % k == 0:
                num = num // k
        return num == 1


sol = Solution()
print(sol.isUgly(14))