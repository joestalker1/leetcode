class Solution:
    def nthmember(self, a1,a2, n):
        r = a2/a1
        return a1 * (r ** (n - 1))


sol = Solution()
print(sol.nthmember(1,2,4))