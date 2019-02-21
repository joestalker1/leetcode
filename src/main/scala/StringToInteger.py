class Solution:
    def is_digit(self, ch):
        return '0' <= ch <= '9'

    def myAtoi(self, str: 'str') -> 'int':
        if not str or len(str) == 0:
            return 0
        min_int = pow(-2, 31)
        max_int = pow(2, 31) - 1
        chars = []
        for ch in str:
            if ch == '+' or ch == '-':
                if len(chars) > 0:
                    break
                chars.append(ch)
            elif ch == ' ' and len(chars) == 0:
                continue
            elif self.is_digit(ch):
                chars.append(ch)
            else:
                break
        num = 0
        b = 1
        while len(chars) > 0:
            a = chars.pop()
            if a == '-':
                num *= -1
            elif self.is_digit(a):
                num += (ord(a) - ord('0')) * b
                b *= 10
        if num > max_int:
            return max_int
        if num < min_int:
            return min_int
        return num


sol = Solution()
print(sol.myAtoi("0-1")) #0
print(sol.myAtoi("+-2")) #0
print(sol.myAtoi("-5-"))
print(sol.myAtoi("-91283472332"))
print(sol.myAtoi("4193 with words"))
print(sol.myAtoi("42"))
