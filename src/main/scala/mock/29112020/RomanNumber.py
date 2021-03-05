class Solution:
    def romanToInt(self, s):
        if not s:
            return None

        rom_to_num = {'I':1,'V': 5, 'X': 10,'L': 50,'C': 100,'D': 500,'M':1000}

        if len(s) == 1:
            return rom_to_num[s[0]]

        res = 0
        for i in range(1, len(s)):
            d1 = rom_to_num[i-1]
            d2 = rom_to_num[i]
            if d1 < d2:
                #there is one number
                res += d2 - d1
            else:
                res += d2
        return res

