class Solution:
    def titleToNumber(self, s):
        a = 0
        b = 26 ** (len(s) - 1)
        for i in range(len(s)):
            a += b * (ord(s[i])- ord('A') + 1)
            b = b // 26
        return a


sol = Solution()
print(sol.titleToNumber('Z'))
print(sol.titleToNumber('AC'))
print(sol.titleToNumber('AZ'))
print(sol.titleToNumber('BA'))


