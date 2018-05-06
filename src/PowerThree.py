class Solution:
    def isPowerOfThree(self, n):
        count = 0
        upper = 10
        w = 1
        for a in range(1, n + 1):
            if a == upper:
                upper *= 10
                w += 1

            count += w
            if count >= n:
                s = str(a)
                return int(s[w - 1 - count + n])







sol = Solution()
print(sol.isPowerOfThree(11))
