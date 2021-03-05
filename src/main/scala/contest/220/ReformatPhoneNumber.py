class Solution:
    def reformatNumber(self, number: str):
        if not number:
            return number
        digits = []
        for ch in number:
            if '0' <= ch <= '9':
                digits.append(ch)
        digits = ''.join(digits)

        def format_digit(s):
            if not s:
                return ''
            if len(s) <= 4:
                if len(s) == 3:
                    return s
                res = [s[0:2]]
                if len(s) > 2:
                    res.append('-')
                    res.append(s[2:])
                return ''.join(res)
            return s[0:3] + '-' + format_digit(s[3:])

        return format_digit(digits)


sol = Solution()
print(sol.reformatNumber("123 4-567"))
print(sol.reformatNumber("1-23-45 6"))



