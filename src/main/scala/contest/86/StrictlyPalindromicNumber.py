class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for base in range(2, n- 1):
            num = 0
            a = n
            while a:
                d = a % base
                num = num * base + d
                a = a // base
            if num != n:
                return False
        return True

sol = Solution()
print(sol.isStrictlyPalindromic(9))
