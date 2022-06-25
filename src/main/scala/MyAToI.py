class Solution:

    def myAtoi(self, s: str) -> int:
        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1

        s = s.strip()
        if not s:
            return 0
        i = 0
        if s[i] in ['+', '-']:
            i += 1
        num = 0
        while i < len(s) and s[i].isdigit():
            d = int(s[i])
            if INT_MAX // 10 < num or num == INT_MAX // 10 and INT_MAX % 10 < d:
                return INT_MIN if s[0] == '-' else INT_MAX
            num = 10 * num + d
            i += 1
        return -num if s[0] == '-' else num