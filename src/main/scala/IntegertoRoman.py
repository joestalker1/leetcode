class Solution:
    def find_greater_min(self, num):
        if 1 <= num < 4:
            return 1
        if 4 <= num < 5:
            return 4
        if 5 <= num < 9:
            return 5
        if 9 <= num < 10:
            return 9
        if 10 <= num < 40:
            return 10
        if 40 <= num < 50:
            return 40
        if 50 <= num < 90:
            return 50
        if 90 <= num < 100:
            return 90
        if 100 <= num < 400:
            return 100
        if 400 <= num < 500:
            return 400
        if 500 <= num < 900:
            return 500
        if 900 <= num < 1000:
            return 900
        return 1000

    def intToRoman(self, num):
        if num <= 0:
            return ''
        roman = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 500: 'D', 400: 'CD',
                 900: 'CM', 1000: 'M'}
        res = ''
        while num > 0:
            d = self.find_greater_min(num)
            res += roman[d]
            num -= d
        return res

sol = Solution()
print(sol.intToRoman(4))
print(sol.intToRoman(9))
print(sol.intToRoman(58))
print(sol.intToRoman(1994))
print(sol.intToRoman(3999))