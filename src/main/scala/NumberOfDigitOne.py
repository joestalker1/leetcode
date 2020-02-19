class Solution:
    def countDigitOne(self, n):
        if n <= 0:
            return 0
        i = 1
        count = 0
        while i <= n:
            divider = i * 10
            count += (n // divider) * i
            count += min(max(n % divider - i + 1, 0), i)
            i *= 10
        return count

sol = Solution()
print(sol.countDigitOne(13))
