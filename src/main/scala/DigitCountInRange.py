class Solution:
    def count_digit(self, d, n):
        if n < 0 and n < d:
            return 0
        count = 0
        i = 1
        while i <= n:
            divider = i * 10
            count += (n // divider) * i
            if d > 0:
                count += min(max(n % divider - d * i + 1, 0), i)
            else:
                if n // divider > 0:
                    if i > 1:
                        count -= i
                        count += min(n % divider + 1, i)
            i *= 10
        return count

    def digitsCount(self, d, low, high):
        return self.count_digit(d, high) - self.count_digit(d, low - 1)


sol = Solution()
print(sol.digitsCount(0,1080,2160))#339
print(sol.digitsCount(1, 1, 20))
print(sol.digitsCount(1, 1, 99))
