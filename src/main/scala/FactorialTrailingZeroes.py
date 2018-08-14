class Solution:
    def trailingZeroes(self, n):
        a = 5
        count = 0
        while a <= n:
            count += (n // a)
            a = a * 5
        return count


sol = Solution()
print(sol.trailingZeroes(200))
