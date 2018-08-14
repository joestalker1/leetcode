class Solution:
    def findNthDigit(self, n):
        len = 1
        count = 9
        start = 1
        while n > len * count:
            n -= len * count
            len += 1
            count *= 10
            start *= 10
        start += (n - 1) // len
        s = str(start)
        return s[(n - 1) % len]



sol = Solution()
print(sol.findNthDigit(50))