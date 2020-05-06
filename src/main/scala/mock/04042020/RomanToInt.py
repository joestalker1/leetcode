class Solution:
    def romanToInt(self, s: str) -> int:
        if not s:
            return None
        roman_to_dec = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and roman_to_dec[s[i]] < roman_to_dec[s[i + 1]]:
                num += roman_to_dec[s[i + 1]] - roman_to_dec[s[i]]
                i += 2
            else:
                num += roman_to_dec[s[i]]
                i += 1
        return num
