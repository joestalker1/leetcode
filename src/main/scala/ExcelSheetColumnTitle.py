class Solution:
    def convertToTitle(self, n):
        res = ''
        n -= 1
        while n >= 0:
            code = n % 26
            res = res + chr(ord('A') + code)
            n = n // 26
            n -= 1
        return res[::-1]

sol = Solution()
print(sol.convertToTitle(26))
print(sol.convertToTitle(29))
print(sol.convertToTitle(52))
print(sol.convertToTitle(53))
print(sol.convertToTitle(54))