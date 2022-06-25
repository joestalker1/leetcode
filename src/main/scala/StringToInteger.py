class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        num = 0
        i = 0
        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        if i < len(s) and s[i] == '-':
            sign = -1
            i += 1
        elif i < len(s) and s[i] == '+':
            sign = 1
            i += 1
        while i < len(s) and s[i].isdigit():
            d = int(s[i])
            if num > INT_MAX // 10 or num == INT_MAX // 10 and INT_MAX % 10 < d:
                return INT_MAX if sign == 1 else INT_MIN
            num = num * 10 + d
            i += 1
        return num * sign


sol = Solution()
print(sol.myAtoi("0-1")) #0
print(sol.myAtoi("+-2")) #0
print(sol.myAtoi("-5-"))
print(sol.myAtoi("-91283472332"))
print(sol.myAtoi("4193 with words"))
print(sol.myAtoi("42"))
